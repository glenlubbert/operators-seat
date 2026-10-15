# scripts/

Small, boring automation that keeps the vault current. Each script is safe to run repeatedly.

## build_index.py

Rebuilds `knowledge/INDEX.md` as a one-line-per-note index from each note's YAML frontmatter. The agent scans the index, ranks the two or three notes most likely to matter, and opens only those. Without an index, the agent reads whole folders to find one fact; past a hundred notes that stops working.

Why it helps: finding the right note is the expensive part. Without an index, the AI has to open folders and files to discover what's there, which uses time and fills its working memory with material it doesn't need. A one-line summary per note, with type, date, tags, and links, lets it pick the two or three notes worth opening first. About 60 tokens per note, so a 100-note vault costs about 6k tokens to scan.

It finds `knowledge/` by walking up from the script's own location, so the folder you run it from doesn't matter. The path to the script does: use its full path (the relative form below only works when your current folder is OS_ROOT):

```
python3 "/full/path/to/OS_ROOT/Level 2 - Operator Layer/scripts/build_index.py"            # rebuild knowledge/INDEX.md
python3 "/full/path/to/OS_ROOT/Level 2 - Operator Layer/scripts/build_index.py" --dry-run  # print, don't write

cd "/full/path/to/OS_ROOT" && python3 "Level 2 - Operator Layer/scripts/build_index.py"   # same thing, from OS_ROOT
```

It reads every `.md` under `knowledge/`, skips `INDEX.md`, `agents.md`, any note with `status: example`, operational logs (`*-log.md`, `audit-log.md`), and anything under `digests/` or `feed-output/`. Loop files are listed as one line per domain. Duplicate filenames and files it couldn't fully read are flagged at the top of the index and on stderr, never silently dropped. The index is written to a temp file and renamed into place, so a crash never leaves a half-written `INDEX.md`. Works with a flat `knowledge/` or one subfolder per domain, from any working directory.

For it to be useful, each note needs frontmatter in the subset of YAML the script reads: one `key: value` per line; lists either inline (`tags: [a, b]`) or as a block of `- item` lines under the key; quoted values are fine. Nested maps, multi-line strings, and anchors are reported as unsupported and the note is indexed with whatever parsed. The minimum:

```yaml
---
title: One-line title
type: fact | decision | pattern | risk | reference | person | rule
status: active | superseded | parked | example
added: YYYY-MM-DD
reviewed: YYYY-MM-DD
source: where it came from
related: [other-note-slug, another-slug]
tags: [tag1, tag2]
---
```

A filled-in example is `_example-atomic-note.md` in this folder: a real decision note, written the way yours should be. It carries `status: example`, so the index skips it even if you copy it into `knowledge/`. The first non-heading line of the body becomes the summary, so make it a real sentence. The date shown in the index is `reviewed`, falling back to `updated`, `date`, `added`, then `created`.

### Run it nightly

In the Claude desktop app (Scheduled, in the sidebar), create a task with this prompt, adjusting the path:

> Run `python3 "<full path to OS_ROOT>/Level 2 - Operator Layer/scripts/build_index.py"` and report the one-line output. If the script errors, report the error verbatim and do not edit INDEX.md by hand. Append one line to `<full path to OS_ROOT>/knowledge/index-rebuild-log.md` in the form `YYYY-MM-DD HH:MM · <script output or error>`.

Schedule it 30 minutes before your nightly git commit so the committed index is current. Without the Claude app's scheduler, the same command goes in a launchd plist or a cron entry.

## Adding scripts

Single file, standard library only, idempotent, finds its inputs by walking up from its own location, writes atomically, reports what it couldn't process. Document each one here with what it reads, what it writes, and the task prompt that runs it. Tools with outside dependencies (like the PDF builder) live in `../publishing/`, not here.
