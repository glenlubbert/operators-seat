#!/usr/bin/env python3
# Copyright (c) 2026 Glen Lubbert. MIT License.
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
# to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
"""
Knowledge Index builder (Operator's Seat, Level 2).

Regenerates knowledge/INDEX.md as a per-note index (one line per note) from
YAML frontmatter, following the router/index/nodes/edges/state pattern.

Usage:
    python3 build_index.py            # rebuild knowledge/INDEX.md
    python3 build_index.py --dry-run  # print, don't write

Finds knowledge/ by walking up from this script's folder until it sees one
containing agents.md, so it works from "Level 2 - Operator Layer/scripts/",
from a root "scripts/" folder, or anywhere else inside the vault. It does not
depend on the current working directory.

Frontmatter format this script reads (a documented subset of YAML):
    key: value                      one key per line
    key: [a, b, c]                  inline list
    key:                            block list (each item on its own "- " line)
      - a
      - b
    key: "quoted value"             quotes stripped
Anything else (nested maps, multi-line strings, anchors) is reported as
unsupported for that file and the file is indexed with whatever parsed.

Skips:
    - INDEX.md, agents.md
    - Loop files (knowledge.md / hypotheses.md / rules.md) at any depth, listed
      as a single "Loop files" line per domain
    - Any file whose frontmatter has status: example
    - Any file under digests/ or feed-output/ (summarized as one line)
    - Operational logs: any file ending in -log.md or named audit-log.md

Links are path-qualified ([[domain/sub/slug|slug]]) so same-named notes in
different folders never collide. Writes are atomic: the new index is written
to a temp file in the same folder and renamed over INDEX.md, so a crash never
leaves a half-written index. Files that fail to decode as UTF-8 are reported
and skipped, never silently ignored.

Standard library only. Safe to run nightly. Idempotent.
"""
import os, re, sys, tempfile
from pathlib import Path
from datetime import date

SKIP_NAMES = {"INDEX.md", "agents.md"}
LOOP = {"knowledge.md", "hypotheses.md", "rules.md"}
SKIP_DIRS = {"digests", "feed-output"}
SUMMARY_MAXLEN = 110

def find_kb(start):
    for folder in [start] + list(start.parents):
        cand = folder / "knowledge"
        if cand.is_dir() and (cand / "agents.md").exists():
            return cand
    return None

def is_log(name):
    return name.endswith("-log.md") or name == "audit-log.md"

def parse_frontmatter(text):
    """Return (fields, body, unsupported_lines). Handles the documented subset."""
    fm, unsupported = {}, []
    if not text.startswith("---"):
        return fm, text, unsupported
    end = text.find("\n---", 3)
    if end == -1:
        return fm, text, unsupported
    block = text[3:end].strip("\n").splitlines()
    i, current_list_key = 0, None
    while i < len(block):
        line = block[i]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            i += 1; continue
        if stripped.startswith("- ") and current_list_key is not None and line.startswith((" ", "\t", "-")):
            fm[current_list_key].append(stripped[2:].strip().strip('"').strip("'"))
            i += 1; continue
        current_list_key = None
        if ":" not in line or line.startswith((" ", "\t")):
            unsupported.append(line); i += 1; continue
        k, _, v = line.partition(":")
        k, v = k.strip(), v.strip()
        if v == "":
            # block list follows, or an empty value
            fm[k] = []
            current_list_key = k
        elif v.startswith("[") and v.endswith("]"):
            fm[k] = [x.strip().strip('"').strip("'") for x in v[1:-1].split(",") if x.strip()]
        elif v.startswith(("{", "&", "*", "|", ">")):
            unsupported.append(line); fm[k] = v
        else:
            fm[k] = v.strip('"').strip("'")
        i += 1
    # normalize empty block lists to empty string for display
    for k, v in list(fm.items()):
        if isinstance(v, list):
            fm[k] = ", ".join(v)
    return fm, text[end+4:], unsupported

def first_summary(body):
    for line in body.splitlines():
        s = line.strip()
        if not s or s.startswith(("#", "---", "|", "![]", "**Filed", "**Domain", "**Type", "**Status", "*")):
            continue
        s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
        s = re.sub(r"\[\[([^\]|]+)(\|[^\]]+)?\]\]", r"\1", s)
        s = re.sub(r"`([^`]+)`", r"\1", s)
        s = s.lstrip("-•*> ").strip()
        if len(s) > SUMMARY_MAXLEN:
            s = s[:SUMMARY_MAXLEN].rsplit(" ", 1)[0] + "…"
        return s
    return ""

def wikilink(link, slug):
    return f"[[{link}]]" if link == slug else f"[[{link}|{slug}]]"

KB = find_kb(Path(__file__).resolve().parent)
if KB is None:
    sys.exit("knowledge/ folder (with agents.md inside) not found above this script")

notes, loops, skipped_dirs, problems = [], {}, {}, []
for p in sorted(KB.rglob("*.md")):
    rel = p.relative_to(KB)
    if p.name in SKIP_NAMES or is_log(p.name):
        continue
    domain = rel.parts[0] if len(rel.parts) > 1 else "(root)"
    if any(part in SKIP_DIRS for part in rel.parts):
        skipped_dirs[domain] = skipped_dirs.get(domain, 0) + 1
        continue
    try:
        text = p.read_text(encoding="utf-8")
    except UnicodeDecodeError as e:
        problems.append(f"{rel.as_posix()}: not UTF-8 ({e.reason}); skipped")
        continue
    except OSError as e:
        problems.append(f"{rel.as_posix()}: could not read ({e.strerror}); skipped")
        continue
    fm, body, unsupported = parse_frontmatter(text)
    if unsupported:
        problems.append(f"{rel.as_posix()}: unsupported frontmatter line(s): " + "; ".join(u.strip() for u in unsupported[:3]))
    if str(fm.get("status", "")).lower() == "example":
        continue
    link = rel.with_suffix("").as_posix()
    updated = fm.get("reviewed") or fm.get("updated") or fm.get("date") or fm.get("added") or fm.get("created") or ""
    if p.name in LOOP:
        loops.setdefault(domain, []).append((link, p.stem, updated))
        continue
    notes.append(dict(
        domain=domain, slug=p.stem, link=link, type=fm.get("type", ""),
        status=fm.get("status", ""), tags=fm.get("tags", ""),
        related=fm.get("related", ""), updated=updated, summary=first_summary(body),
    ))

by_domain = {}
for n in notes:
    by_domain.setdefault(n["domain"], []).append(n)
all_domains = sorted(set(by_domain) | set(loops))  # folders holding only excluded files get no heading

seen = {}
for n in notes:
    seen.setdefault(n["slug"], []).append(n["link"])
dupes = {s: l for s, l in seen.items() if len(l) > 1}

out = [
    "# Knowledge Index",
    "",
    f"*Regenerated {date.today().isoformat()} by `build_index.py`. One line per note. Score relevance here before opening any file.*",
    "",
    "> **Operating instructions:** see [[agents]]. Each domain's `knowledge.md` / `hypotheses.md` / `rules.md` hold that domain's compounding loop and are listed as *Loop files* under each heading.",
    "",
    f"**Totals:** {len(notes)} atomic notes across {len(by_domain)} domains · {sum(len(v) for v in loops.values())} loop files · {sum(skipped_dirs.values())} files in digests/ or feed-output/ (excluded)",
    "",
    "Line format: `[[path|slug]] · type · reviewed-or-updated · tags · related · summary`. Links are path-qualified so same-named notes in different folders never collide. Example notes and operational logs are not indexed.",
    "",
]
if dupes:
    out.append("> **Duplicate filenames** (use the path-qualified link, not the bare slug, in `related:` fields): "
               + "; ".join(f"`{s}` → " + ", ".join(l) for s, l in sorted(dupes.items())))
    out.append("")
if problems:
    out.append("> **Files needing attention** (indexed as far as possible): " + " · ".join(problems))
    out.append("")

for domain in all_domains:
    items = sorted(by_domain.get(domain, []), key=lambda n: n["updated"] or "0000", reverse=True)
    out.append(f"## {'knowledge' if domain == '(root)' else domain} ({len(items)} note{'' if len(items) == 1 else 's'})")
    if domain in loops:
        out.append("*Loop files:* " + ", ".join(
            wikilink(link, stem) + (f" ({upd})" if upd else "")
            for link, stem, upd in sorted(loops[domain])))
    if domain in skipped_dirs:
        out.append(f"*Excluded:* {skipped_dirs[domain]} file(s) in digests/ or feed-output/ under `{domain}`")
    if not items:
        out.append("*(no atomic notes yet)*")
    out.append("")
    for n in items:
        parts = [wikilink(n["link"], n["slug"])]
        if n["type"]:    parts.append(n["type"])
        if n["status"] and n["status"] not in ("active", ""): parts.append(n["status"])
        if n["updated"]: parts.append(n["updated"])
        if n["tags"]:    parts.append(f"tags: {n['tags']}")
        if n["related"]: parts.append(f"related: {n['related']}")
        line = " · ".join(parts)
        if n["summary"]:
            line += f" · {n['summary']}"
        out.append(f"- {line}")
    out.append("")

content = "\n".join(out).rstrip() + "\n"
if "--dry-run" in sys.argv:
    print(content)
    if problems:
        print("\n".join("PROBLEM: " + p for p in problems), file=sys.stderr)
else:
    target = KB / "INDEX.md"
    fd, tmp = tempfile.mkstemp(prefix=".INDEX.", suffix=".tmp", dir=str(KB))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(content)
        os.replace(tmp, target)
    except Exception:
        try: os.unlink(tmp)
        except OSError: pass
        raise
    print(f"INDEX.md rebuilt: {len(notes)} notes, {len(by_domain)} domains with notes, "
          f"{sum(skipped_dirs.values())} excluded, {len(dupes)} duplicate slugs flagged, "
          f"{len(problems)} files needing attention, {len(content.splitlines())} lines, ~{len(content)//4} tokens")
    if problems:
        print("\n".join("PROBLEM: " + p for p in problems), file=sys.stderr)
