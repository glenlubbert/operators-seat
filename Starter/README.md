# Starter: the folder you copy

*This is the operating system. Copy it, rename it, and follow `START HERE.md` in the kit you were sent. This page covers what's inside, how to set it up inside folders you already have, and how to keep it backed up.*

---

## What's in this folder

```
Starter/
├── CLAUDE.md                      ← one line: read seat/seat.md first
├── AGENTS.md                      ← the same line, for AIs that look for this name
├── seat/
│   ├── seat.md                    ← who you are, Now / Settled / Open, the questions it runs on (step 1)
│   ├── paths.md                   ← where your folders really are; the AI fills it in
│   ├── role.md                    ← what you own, decide, and have said no to (step 1)
│   ├── rules.md                   ← rules for this role only (usually short)
│   └── feeds.md                   ← what the AI checks on a schedule (step 7)
├── knowledge/
│   ├── agents.md                  ← the runbook; every AI reads it first (kept short)
│   ├── playbooks.md               ← occasional tasks; opened only when needed
│   ├── knowledge.md               ← confirmed facts (step 3)
│   ├── hypotheses.md              ← things you're testing
│   └── rules.md                   ← rules that apply everywhere (step 5)
├── 0. Inbox/                      ← drop files here; say "Sort my inbox" (step 3, and any day)
├── 1. Projects/                   ← anything with a finish line; each gets a folder with project.md (step 4)
├── 2. Areas/                      ← ongoing: people, voice, goals, health, home
├── 3. Resources/                  ← reference and library
├── 4. Archive/                    ← finished; not read by default
├── Level 2 - Operator Layer/      ← open later: index, tool map, build log, own-machine setup, backup with history
└── .gitignore                     ← only matters if you use git
```

Three parts. **The seat** (`seat/`) says who you are and what you own. **The memory** (`knowledge/` and the four numbered folders) holds what's true. **The loop** (filing as you go, the Friday audit, feeds) keeps it current and brings decisions back to you.

## Reader, AI, sync

- **Reader:** any app that opens text files. Obsidian (free, obsidian.md) is a good one, with search and links between notes, and a phone app.
- **AI:** the Claude desktop app or ChatGPT desktop in Work mode, attached to this folder as a project. Developer tools (Claude Code, Cursor, Codex) and an AI on your own laptop work too; see `Why it works.md`.
- **Sync:** Dropbox or iCloud. One sync service per folder, never two.

## Backup

Sync is not backup: a bad edit syncs everywhere in seconds. Two simple protections cover most people:

- **Dropbox keeps earlier versions of every file.** On dropbox.com, open the file's menu and choose Version history to bring back an earlier copy. How far back depends on your plan.
- **Time Machine** (on a Mac, with an external drive) keeps hourly snapshots of everything, including this folder. Windows has File History.

If a file ever goes wrong, tell the AI what happened; it can't restore old versions itself, but it can tell you which file to restore and what should be in it.

Want full history of every change, with a nightly save point? That's git, and the setup is in `Level 2 - Operator Layer/Backup with history.md`.

## Already have lots of files?

If your files aren't organized as Projects, Areas, Resources, and Archive, use the standard setup anyway, and don't try to sort everything first. In a conversation, say "I have a lot of existing files," and the AI will offer three choices:

1. **Start fresh** (best for the first week). Your old folders stay where they are. When something matters, drag it into `0. Inbox` and say "Sort my inbox."
2. **Archive it.** Move your old top folder into `4. Archive` as "Old files" with today's month. The AI can search it when a question needs it, and moves things into Projects or Areas only when they're in use. This is the way Tiago Forte recommends switching to PARA.
3. **Sort one folder.** For a single folder you care about, say "Sort [folder] into PARA." It works like the inbox: a batch at a time, moving only what you approve.

Nothing of yours gets moved without your say-so.

## Setting it up inside folders you already have

If you already organize your files in Projects, Areas, Resources, and Archive (in Obsidian or anywhere), you don't need a second set of those folders. The operating system goes inside yours, as a Resource. Attach your existing top folder to your AI as a project, put the unzipped kit somewhere inside that folder (your inbox is fine) so the AI can see it, then say:

> Read the Starter README in the Operator's Seat kit and install it inside my folders.

The AI follows the steps below, shows you each change before saving, and never moves or renames your existing files. Then say "Interview me" and carry on with START HERE.

**The steps, for reference.** Two names show up here and in the feeds:

- **VAULT_ROOT**: your top folder, the one your AI is attached to.
- **OS_ROOT**: where the operating system's files live: `[VAULT_ROOT]/3. Resources/[Your Name] OS/`.

1. Create OS_ROOT.
2. Copy into OS_ROOT: `seat/`, `knowledge/`, `Level 2 - Operator Layer/`. Don't copy the numbered folders; you have them.
3. Fill in `seat/paths.md` in OS_ROOT: each of your real folders as a path inside your top folder, whatever it's called (your Projects folder might be "Projects" or "10 Active"; your inbox might be "_Inbox"), plus this computer's full path to the top folder. Open each folder to confirm it exists. If one doesn't, create it only on your yes. Every later step and every feed looks folders up here.
4. Copy `_Example Project/` (the whole folder) into your PROJECTS folder; creating a new project copies it. Then, for each project you already have, one of two cases, never both:
   - **It already has notes** in a `CLAUDE.md` or `AGENTS.md`. Those stay the project's notes; don't create `project.md`. If the other entry file is missing, create it with one line pointing to the file that has the notes. If the other one exists, keep its content and add that pointer line at the top.
   - **It has no notes yet.** Create `project.md` filled in from what's in the folder, then create or update both `CLAUDE.md` and `AGENTS.md` with a pointer line to `project.md`, keeping anything already in them.
   Never write a pointer to a file that doesn't exist. Every session and feed finds project notes the same way (the project-notes rule in `knowledge/agents.md`).
5. Inbox: if you already have an inbox folder, it's the INBOX in `paths.md`. If not, copy `0. Inbox/` and record it.
6. Copy `_Example Person.md` into your PEOPLE folder and `brand/voice.md` into your AREAS, if you want them.
7. At your top folder: if `CLAUDE.md` or `AGENTS.md` already exist, add this line at the top of each without removing anything: `Read "[OS_ROOT]/seat/paths.md", "[OS_ROOT]/seat/seat.md", and "[OS_ROOT]/knowledge/agents.md" first.` (with OS_ROOT written relative to the top folder). If they don't exist, create each with that one line.
8. If your top folder has a `.gitignore`, add the lines from this Starter's `.gitignore` that aren't there; if it doesn't, copy this one. Do this before any backup setup, so nothing private is ever staged.
9. Test: new conversation, "What do you understand about me?" Before the interview it should say it hasn't met you yet and offer to start; after, it should answer from the seat. Then ask "Where's my inbox?" and check it names your real folder.

This has been done on one real set of folders (the author's). Run step 9 before relying on yours.

## The business version

A company runs the same three parts, with several seats sharing one memory in a shared folder. Each person's own folders stay private and point to their seat in the shared one; nothing else crosses between them.

## Questions

Reply to whoever sent you this. Everyone's version ends up different, and the differences are the interesting part.
