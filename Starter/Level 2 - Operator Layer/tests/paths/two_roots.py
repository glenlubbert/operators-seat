#!/usr/bin/env python3
# Copyright (c) 2026 Glen Lubbert. MIT License (see REUSE.md).
"""
Two-computer path test for seat/paths.md.

Copies the Starter into a temporary folder twice, under two different full
paths and with nonstandard folder names, then follows the runbook's path rules:
relative folders inside the vault, one full path per computer, a real existence
check, and a list of scheduled prompts that need updating when the vault moves.
It also expands Feed 1 for each computer and runs the index builder from "/".

This checks the procedure's logic with a script. It is not a test of a real AI
following the runbook. Standard library only. Nothing outside the temp folder
is touched.

Usage:  python3 two_roots.py
"""
import os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
STARTER = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
assert os.path.isfile(os.path.join(STARTER, "seat", "paths.md")), "run from inside the Starter"

REL = {"OS_ROOT": ".", "KNOWLEDGE": "knowledge", "INBOX": "_Inbox", "PROJECTS": "10 Active",
       "AREAS": "2. Areas", "PEOPLE": "2. Areas/people", "GOALS": "2. Areas/goals",
       "RESOURCES": "3. Resources", "ARCHIVE": "4. Archive",
       "SAVED": "3. Resources/Saved conversations", "SHARED": "3. Resources/Shared"}

results = []
def check(name, ok): results.append((name, bool(ok)))

def fill(vault, computer):
    p = os.path.join(vault, "seat", "paths.md"); t = open(p).read()
    for k, v in REL.items():
        t = re.sub(rf"(\| {k} \|[^|]*\| )\[relative path\]", rf"\g<1>{v}", t)
    t = t.replace("**Status: not filled in**", "**Status: checked 2026-10-15**")
    t = t.replace("| [name] | [full path] | [date] |", f"| {computer} | {vault} | 2026-10-15 |")
    t = t.replace("| [none yet] | | |", f"| Feed 1: Stale check | Claude Scheduled | {computer} |")
    open(p, "w").write(t)

def startup_check(vault, computer):
    """The runbook's session-start check, as a script."""
    p = os.path.join(vault, "seat", "paths.md"); t = open(p).read()
    rel = dict(re.findall(r"^\| ([A-Z_]+) \| [^|]*\| ([^|\n]+?) \|$", t, re.M))
    recorded = {c.strip(): r.strip() for c, r, _ in re.findall(r"^\| ([^|]+?) \| (/[^|]+?) \| ([^|]+?) \|$", t, re.M)}
    added = False
    if recorded.get(computer) != vault:
        t = t.replace("| Computer | VAULT_ROOT (full path) | Last checked |\n|----------|------------------------|--------------|\n",
                      f"| Computer | VAULT_ROOT (full path) | Last checked |\n|----------|------------------------|--------------|\n| {computer} | {vault} | 2026-10-15 |\n", 1)
        open(p, "w").write(t); added = True
    missing = [k for k, v in rel.items() if not os.path.isdir(os.path.normpath(os.path.join(vault, v)))]
    feeds = re.findall(r"^\| (Feed[^|]+?) \| [^|]+? \| ([^|]+?) \|$", t, re.M)
    stale = [f.strip() for f, c in feeds if c.strip() != computer]
    return rel, missing, added, stale

def expand_feed1(vault, rel):
    f = open(os.path.join(vault, "seat", "feeds.md")).read()
    pre = re.search(r"## The preamble every feed starts with.*?\n> (.*?)\n", f, re.S).group(1)
    s = f.index("## Feed 1:"); e = f.index("## Feed 2:")
    prompt = "\n".join(l for l in f[s:e].splitlines() if l.startswith(">")).replace("> [preamble]", "> " + pre)
    full = {k: os.path.normpath(os.path.join(vault, v)) for k, v in rel.items()}; full["VAULT_ROOT"] = vault
    for k, v in full.items(): prompt = prompt.replace(f"[{k}]", v)
    return prompt

tmp = tempfile.mkdtemp(prefix="opseat-paths-")
try:
    A = os.path.join(tmp, "laptopA", "Glen Vault")
    B = os.path.join(tmp, "laptopB", "Users", "other", "Dropbox", "Glen Vault")
    shutil.copytree(STARTER, A, ignore=shutil.ignore_patterns(".DS_Store", "tests"))
    os.rename(os.path.join(A, "1. Projects"), os.path.join(A, "10 Active"))
    os.rename(os.path.join(A, "0. Inbox"), os.path.join(A, "_Inbox"))
    os.makedirs(os.path.join(A, "3. Resources", "Saved conversations"), exist_ok=True)
    os.makedirs(os.path.join(A, "3. Resources", "Shared"), exist_ok=True)
    fill(A, "Laptop A")
    shutil.copytree(A, B)   # same vault, opened on a second computer at a different path

    relA, missA, addedA, staleA = startup_check(A, "Laptop A")
    check("Laptop A: every folder resolves and exists", not missA and len(relA) == len(REL))
    check("Laptop A: no new computer line needed", not addedA)
    check("Laptop A: no scheduled prompts flagged", not staleA)

    relB, missB, addedB, staleB = startup_check(B, "Laptop B")
    check("Laptop B: same relative folders resolve under the new root", not missB and relB == relA)
    check("Laptop B: its own computer line is added", addedB)
    check("Laptop B: the Laptop A scheduled prompt is flagged for updating", staleB == ["Feed 1: Stale check"])
    check("Laptop B: inbox resolves to its own copy", os.path.isdir(os.path.join(B, relB["INBOX"])))

    pA, pB = expand_feed1(A, relA), expand_feed1(B, relB)
    check("Feed 1 expands with no unresolved path names (A)", not re.findall(r"\[([A-Z_]+)\]", pA))
    check("Feed 1 expands with no unresolved path names (B)", not re.findall(r"\[([A-Z_]+)\]", pB))
    check("Laptop B's prompt contains no Laptop A paths", "laptopA" not in pB)

    for name, v in (("A", A), ("B", B)):
        r = subprocess.run([sys.executable, os.path.join(v, "Level 2 - Operator Layer", "scripts", "build_index.py")],
                           cwd="/", capture_output=True, text=True)
        check(f"Index builds from '/' on Laptop {name}", r.returncode == 0 and os.path.isfile(os.path.join(v, "knowledge", "INDEX.md")))
finally:
    shutil.rmtree(tmp, ignore_errors=True)

for n, ok in results: print(("PASS" if ok else "FAIL") + "  " + n)
passed = sum(ok for _, ok in results); print(f"\n{passed}/{len(results)} passed")
sys.exit(0 if passed == len(results) else 1)
