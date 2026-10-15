# Run It on Your Own Machine

*The open-source path: the same folders, read by an AI running on your own laptop.*

*What's been tested: the author has run this kit's files against open-source AI through Ollama on a MacBook Pro M1 with 16 GB, reading the seat and knowledge files and answering from them. What hasn't: the full seven steps end to end (the interview, a saved correction, retrieval in a fresh conversation, a scheduled feed) in any local setup below. Until that pilot is done, treat this page as a path to try, not a supported setup.*

---

## Why this matters

The case for open-source AI in a business comes down to three claims: your data can stay on your machine, the cost is hardware instead of a per-seat subscription, and nobody can change the terms on you. All three depend on where the context lives, not which AI reads it. A business running a local AI with no memory is re-explaining itself to a free chatbot. With a seat, a memory, and a loop, you can swap a hosted AI for a local one and keep working.

## What a local setup has to provide

Three things. A chat window alone gives you only the first:

1. **An AI that runs locally.** Ollama or LM Studio supply this.
2. **A host that can open your folder and edit files with your review.** Without this, the interview can't save the seat, and "file this" means you paste it yourself. This is the piece most "just run AI locally" advice skips.
3. **A scheduler**, for step 7. Neither Ollama nor LM Studio ships one.

The AI also has to be able to use tools (read a file, write a file) reliably. Many small open-source models can chat but can't do that well, and an agent host will either hide them or use them badly.

## Setups to try

**Obsidian + Copilot for Obsidian (Agent Mode, with the opencode agent) + Ollama.** Copilot for Obsidian 4.0 rewrote its agent features around real agents running inside Obsidian: Claude Code, Codex, and opencode. Of the three, opencode is the one you point at a local provider such as Ollama or LM Studio; Claude Code and Codex use hosted models. Agent Mode is desktop-only, and it's the mode that can read and edit your notes; the plain "Quick Chat" can answer questions but can't save anything, so the seven steps won't work there. The plugin's own docs for configuring opencode with a local provider are the current reference; settings move between versions.

**Cline (in VS Code) with Ollama as the provider.** Reads files, edits files, and runs the runbook as written. Closer to a developer tool; less friendly to look at.

**Model size.** On 16 GB of RAM, 7B to 8B models are the practical size (`qwen2.5:7b`, `llama3.1:8b`, `mistral`; the number is the AI's size). Pick one that's listed as supporting tool use. On 32 GB or more, 14B models follow the runbook noticeably better. Below 16 GB, expect to repeat yourself.

### Setup, in order

1. Install Ollama (ollama.com) and pull an AI that supports tool use: `ollama pull qwen2.5:7b`.
2. Install Obsidian and open your folder as a vault.
3. Install the Copilot community plugin, turn on Agent Mode, and configure the opencode agent with Ollama as its provider at `http://localhost:11434`, following the plugin's docs.
4. If the plugin can't reach Ollama, Ollama needs to allow Obsidian's origin. Set `OLLAMA_ORIGINS` to Obsidian's app origin (`app://obsidian.md`), not `*`; a wildcard lets any web page on your machine talk to your AI. On a Mac: `launchctl setenv OLLAMA_ORIGINS "app://obsidian.md"`, then quit and reopen Ollama. Cline doesn't need this.
5. Run the pilot before trusting it: "Read AGENTS.md, then interview me," approve, save; in a new conversation, correct one thing and confirm it saved; in a third, ask something only the seat knows; then run the first feed once.

### If the pilot fails

Work through it in this order:

- **The AI can't use tools well.** It talks about saving but nothing lands, or it invents file contents. Try a larger or tool-capable model before anything else.
- **The host isn't in agent mode.** Plain chat can't write files. Check you're in Agent Mode (Copilot) or that Cline has file access.
- **Permissions.** The host needs read and write access to your folder, and Ollama has to accept the host's connection (step 4).
- **Context is too small.** If it forgets the runbook halfway, start each conversation with "Read AGENTS.md first" and keep questions narrow.

## What changes in the seven steps

Nothing in the files. The differences are in the agent:

- **Every conversation:** a local AI usually doesn't open the seat on its own. Start with "Read AGENTS.md first," or set it as the agent's standing instructions if the host allows.
- **Steps 3 to 5:** filing and rules work only in a host that can write files. Small AIs pay most attention to the start of what they read, so the rules and the no-list come first.
- **Step 6 (Friday audit):** works, slower. Expect to prompt each part rather than saying "run the audit."
- **Step 7 (feeds):** you need a scheduler. The plain version is a cron job running a script that calls Ollama's API with the expanded feed prompt and writes the result where the feed says. Or run the feed by hand on Fridays until it earns automation.

## Two different promises: "stays in this folder" and "stays on this machine"

The kit's private-folder rule ("nothing leaves this folder") is about where the AI may copy things *within* your files. It says nothing about whether the text travels over the internet. A hosted AI (Claude, ChatGPT) reading a private folder sends that folder's contents to its servers, even if it never copies them anywhere else in your vault.

So if you want some material never to leave your machine, keep it where hosted AIs can't see it:

- **Separate roots.** Keep private material in a folder outside the one you attach to Claude or ChatGPT, and attach that private folder only to your local AI. Each app sees only the folder it's given.
- **Or separate access.** If your tools allow it, exclude the private subfolders from the hosted app's access. Check that the exclusion really works before relying on it.

Pointing a hosted AI and a local AI at the same folder does not make any of it private.

## When "nothing leaves the machine" is actually true

Only when all of these hold:

- **Inference and embeddings are local.** Search inside Copilot can use a cloud embedding service; point it at a local embedding model through Ollama instead.
- **Cloud features in the plugin or host are off,** including any hosted plan.
- **The folder isn't synced to a cloud service,** or the private parts are excluded from sync.
- **No hosted AI has access to that folder** (see above).

If any one of these is off, some of your text leaves the machine.

## What's slower or worse

Retrieval across many notes. A small AI with a short context can't hold the whole index plus three notes plus your question, so the Level 2 index earns its place sooner. Long drafts in your voice are rougher. The double-check before anything leaves under your name matters more, because small AIs are more confident when wrong.

What isn't worse: the memory. Your facts, decisions, rules, and people notes are the same quality whichever AI reads them.

## The mixed setup most people end up with

A hosted AI for drafting, long reasoning, and anything that uses connected tools, attached to your main folder. A local AI for private material, attached only to the private folder, and for working offline. Two roots, two access profiles, one way of working.

## For a business

A shared folder on a machine in the office, a mid-size open-source AI on that machine, each seat's feeds running on a schedule, and customer, pricing, and payroll material kept where no hosted service can read it. That's the version the open-source conversation is reaching for, and the memory is the part it usually skips.

---

*References: Copilot for Obsidian 4.0.0 release notes (agents inside Obsidian; opencode for local providers; Agent Mode desktop-only), github.com/logancyang/obsidian-copilot/releases/tag/4.0.0; Cline docs on running models locally; Ollama FAQ on allowed origins. Read October 2026. Tested on: MacBook Pro M1, 16 GB, Ollama with mistral and qwen2.5:7b, reading and answering from the files. Full seven-step local pilot: owed.*
