# Level 2: The Operator Layer

*You don't need this folder on day one, or in week one. Open it when one of three things happens.*

**The agent can't find a note you know is there.** Your `knowledge/` has passed a dozen notes. Add frontmatter to your notes (see `scripts/README.md`), run `scripts/build_index.py`, and schedule it nightly. The runbook already tells the agent to scan `INDEX.md` before opening files.

**The agent guesses which tool to use, or you catch it about to send something.** Fill in `CONNECTORS.md`: every external system, what truth lives there, how the agent reaches it, read or write, and where the credential lives (never the value). Do the first pass as an audit; expect to find a key in two places.

**You can't remember why the system is shaped the way it is.** Start `BUILD_LOG.md`. One entry per change: what, why, shareable or not. The agent appends; you correct the why.

## What's here

- `CONNECTORS.md`: the tool map and the six standing rules (read-only by default, reversibility is the line, money is human-only, secrets never in the vault).
- `BUILD_LOG.md`: the design record.
- `scripts/build_index.py` and `scripts/README.md`: the index builder and the nightly task prompt.
- `Run it on your own machine.md`: installing an open-source AI on your laptop, and what a fully local setup takes if you want nothing to leave the machine. Same folders, same opening line.
- `Backup with history.md`: git, a nightly save point, and how to check and restore it.

## Rules that must never be broken

Rules in `knowledge/rules.md` are instructions, and an AI can miss one. For the few that must never break (compliance language, legal phrasing, anything about secrets), set them up as a hook in your AI tool's settings so the action is blocked before it happens, not just discouraged. Claude Code and most developer tools support this.

## Two files that live at the vault root instead

`AGENTS.md` (a one-line pointer for agents that look for that name) and `.gitignore` (keeps editor state and local secrets out of git) have to be at the root to work. They're tiny; ignore them until you need git or a second agent.

## The business version

When this seat joins a company vault, the operator layer is where the company's memory keeps its tool map and its build log, shared across seats. The personal vault keeps its own copies for personal tools. Nothing here crosses between them except by a pointer.
