# Backup with history (git)

*For when Dropbox's version history and Time Machine aren't enough: you want every change on record, with a save point every night. This uses git and a few Terminal commands. If you use Claude Code, you can ask it to do all of this.*

## One-time setup

First, the exclusions. Make sure your top folder (VAULT_ROOT) has a `.gitignore` before anything is staged: if it doesn't, copy the Starter's; if it does, add any of the Starter's lines it's missing. Then, in VAULT_ROOT:

```
cd "/path/to/VAULT_ROOT"
git init
git add -A
git commit -m "Initial vault"
```

The `.gitignore` in the Starter excludes editor state, `.DS_Store`, `.env`, `.secrets/`, `REVIEW.md`, and `knowledge/feed-output/`. Before the first commit, search your folders for anything that looks like a key or password. Once committed, it's in the history for good, and the fix is changing the password, not deleting the file.

## A nightly save point

As a scheduled task (ask the AI, or use Scheduled in the Claude sidebar):

> In "/path/to/VAULT_ROOT", run `git add -A && git commit -m "Nightly $(date +%F)"`. Report the commit hash, or "nothing to commit." If git returns an error, report it word for word and do not retry. Do not push unless a remote is configured and this prompt says to.

Or a cron line: `0 23 * * * cd "/path/to/VAULT_ROOT" && git add -A && git commit -qm "Nightly $(date +\%F)"`.

## What this gives you, honestly

A daily recovery point, if the commit ran and succeeded. If the task didn't fire, the app was closed, or git errored, there's no save point for that day. So:

- **Check it monthly.** `git log --oneline | head -5` should show recent nightly commits. If there are gaps, find out why before you need the backup.
- **Practice a restore once.** Pick any note, run `git log --oneline -- "path/to/note.md"` to see its history, then `git show <hash>:"path/to/note.md"` to read an old version, or `git checkout <hash> -- "path/to/note.md"` to bring it back. Ten minutes, and you'll know the backup is real.

A private remote (GitHub) is optional and gives you a copy off your machine. The password warning matters more once your folders are on someone else's server. Plenty of people run local git plus Dropbox and never add a remote.
