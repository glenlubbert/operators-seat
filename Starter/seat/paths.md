# Paths: where your folders actually are

*The AI fills this in the first time it works in your folders, or during an install inside folders you already have, and checks it at the start of every session. Every instruction and scheduled feed looks folder locations up here instead of guessing. You never edit it by hand; if you rename or move a folder, tell the AI and it updates this file.*

## Inside the vault (the same on every computer)

Each folder is written relative to the top folder (VAULT_ROOT), so moving the whole vault or opening it on another computer doesn't break anything.

**Status: not filled in**
*(The AI sets this to `checked {date}` after it has confirmed every folder below exists by actually opening it.)*

| Name | What it is | Path inside the vault |
|------|------------|-----------------------|
| OS_ROOT | The folder holding `seat/`, `knowledge/`, and Level 2 (`.` on a standard install) | [relative path] |
| KNOWLEDGE | `knowledge/` inside OS_ROOT | [relative path] |
| INBOX | Where you drop files to be sorted | [relative path] |
| PROJECTS | Things with a finish line | [relative path] |
| AREAS | Ongoing parts of your work and life | [relative path] |
| PEOPLE | One note per person (inside AREAS) | [relative path] |
| GOALS | Quarterly goals (inside AREAS) | [relative path] |
| RESOURCES | Reference and library | [relative path] |
| ARCHIVE | Finished things; not read by default | [relative path] |
| SAVED | Where "Save this" puts conversations (inside RESOURCES) | [relative path] |
| SHARED | Where "Pass it on" puts shareable copies (inside RESOURCES) | [relative path] |

## This computer

The full path to the top folder differs from computer to computer. One line per computer the vault has been opened on.

| Computer | VAULT_ROOT (full path) | Last checked |
|----------|------------------------|--------------|
| [name] | [full path] | [date] |

## Scheduled prompts that contain full paths

A scheduled feed has full paths written into it. If VAULT_ROOT changes on a computer, these need their prompts updated; the AI lists them for you.

| Feed | Where it's scheduled | Computer it was written for |
|------|----------------------|-----------------------------|
| [none yet] | | |
