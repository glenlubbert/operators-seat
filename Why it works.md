# Why It Works

*An AI chief of staff for you and your business, built for privacy and portability.*

*The reasoning behind Operator's Seat. Read it when you're curious, not before you start; `START HERE.md` is the start. About ten minutes.*

---

## The problem

Most AI apps now remember some things about you on their own. But that memory lives inside one app, you can't easily see what it holds or correct it, it keeps what it decides is important rather than what you decided, and none of it comes with you when you switch. So you still spend the first five minutes of too many conversations explaining who you are and what you're working on. The AI is brilliant at the task in front of it and patchy about the work you did yesterday.

The fix is to write the context down in files you own and can read, which the agent reads at the start of each conversation, and update the files as decisions change. That's the whole idea. Everything else is structure that keeps it from rotting.

## Three parts

**The seat** defines the role: what you're working on now, what's settled, what's open, what you own, what you've said no to. The no-list does more work than the yes-list; it's what stops the agent from re-proposing things you've already decided against. On a personal OS the seat is you. In a company, there are several seats sharing one memory.

**The memory** supplies the context: confirmed facts, decisions and the reasoning behind them, rules, the people and projects around you. Plain markdown files in a folder you already keep, organized by how actionable they are (PARA: Projects, Areas, Resources, Archive). Any agent can read it. Any editor can open it.

**The loop** moves the work and brings decisions back to you. The agent files decisions at checkpoints so the memory stays current. You run a fifteen-minute Friday audit so stale things get pruned and earned things get promoted. Later, feeds: things the agent checks on a schedule and returns to you for judgment.

One sentence: the seat defines the role, the memory supplies the context, the loop moves the work and brings decisions back.

## Why plain files

The folder works with the Claude desktop app and ChatGPT Work (same opening line in both), with Codex, Cursor, and Gemini, with an open-source AI running on your own laptop, and with whatever ships next. Write the context once, then use the right tool for each task. When a better AI arrives, you point it at the same folder and it picks up where the last one left off. If a vendor changes pricing or restricts features, you switch; the context goes with you.

AI that runs on your own machine matters more than people expect. An open-source AI running locally (through Ollama or LM Studio) costs nothing per token, works offline, and, set up carefully, keeps your context off anyone else's server: that takes local search as well as local chat, cloud features turned off, sync settled, and no hosted AI attached to the same private folder. The author has run this kit's files that way for reading and answering; the full seven steps haven't been piloted locally yet. `Starter/Level 2 - Operator Layer/Run it on your own machine.md` is the path.

The folder is the asset. The agent is interchangeable.

## Why it uses fewer tokens

Every AI plan has limits, measured in tokens: roughly, how much text the AI reads and writes. Three things in this kit keep your token use down.

**Fresh chats that already know you.** A long conversation gets more expensive with every message, because the AI rereads the whole history each time it answers. Here, anything that matters gets saved to the files, so you can start a new chat for each task and lose nothing. You also stop pasting the same background and re-uploading the same documents every time.

**A map instead of the whole library.** Knowledge is kept as small notes, one idea per file, with a plain name. Once you have more than a dozen, a short script (in Level 2) builds an index: one line per note. The AI reads that one page, picks the two or three notes that matter, and opens only those. Topic folders carry a short summary so the AI can get its bearings without opening everything. So the cost of a question depends on the question, not on how much you've saved. Five years of notes cost about the same to search as five weeks.

**Short standing instructions.** The instructions every conversation reads are kept to about 2,400 words. The procedures you only need now and then (the first interview, sorting files, the Friday audit, setting up feeds) sit in a separate file the AI opens only when that task comes up.

There's a small fixed cost: each new conversation starts by reading a few short files. That's the trade, and it's much less than re-explaining yourself. No savings figure is claimed here, because it depends on how you work; the mechanics above are what make it smaller.

## You think. It types.

Nick Milo has a name for the failure mode this kit is built to avoid: cognitive surrender, handing your thinking to an AI because you're tired, and getting short-term relief at the cost of your own judgment. It's a fair worry about any system where the AI does the writing.

The line this kit holds is between effort that carries judgment and effort that's clerical. You answer the interview in your own words. You decide what's settled and what you've said no to. You approve the interview's drafts before they're saved, and any rule the AI proposes on its own; routine filing of what you've told it happens without a prompt, and it tells you what it filed. You run the Friday audit and decide what gets promoted and what gets cut. The AI asks the questions, takes the notes, files the decisions, and brings things back to you. Nick calls the first kind good friction and the second kind bad friction; the kit keeps the good kind and removes the bad.

The test, if you ever wonder which side of the line you're on: could you explain, without opening the folder, what your AI believes about your work and why? If yes, the thinking is still yours.

## Why the loop is the part people miss

A folder of context gets bigger. A folder with a loop gets smarter. Three sub-files inside `knowledge/` do it: `hypotheses.md` for what you're testing, `knowledge.md` for what's confirmed, `rules.md` for what the agent applies by default. Hypotheses get promoted when they survive a test. Knowledge gets promoted to rules when you find yourself applying it every time. Rules you stop following get demoted. The vault becomes a record of what you've learned, not just what you've read, and the agent gets cautious on purpose: signal earns its way up.

The two habits that keep it alive are the agent filing at checkpoints (the runbook tells it to; you confirm) and the Friday audit. Skip them and the system rots in six weeks. Keep them and it compounds for years.

## Why a seat and not just a profile

A profile says who you are. A seat says what you own, what you decide, and what you've refused. That's what an agent needs to answer "what should I work on next" without being told, and it's what lets a company run several seats on one memory without the agent bringing the sales rep the operator's decisions. It's also what makes the system outlive a person: the seat stays when someone leaves.

The seat also carries the questions it runs on. They come from the Solution-Focused approach to coaching, which starts from what you want and what's already working rather than from what's wrong: best hopes for the week, what's already working and should keep going, suppose it went just right and what you'd notice first, where you are on a 0 to 10 and what one point higher would look like, the smallest next step. The AI asks them in the first-run interview and every Friday. It doesn't answer them for you. Most AI setups ask "what's the problem"; this one asks "what's working," and the difference shows up in what the AI brings you.

## One rule for approvals

Reversible work runs unattended: drafting, filing, research, preparing. Irreversible work asks: anything the outside world sees, anything that moves money, anything you can't undo. Money systems are human-only. Stated once, pointed at from everywhere. Most agent accidents come from having three different approval rules in three files.

## Where it came from

It started with Andrej Karpathy. In April 2026 he posted about building personal knowledge bases with AI: raw material goes into a folder, the AI compiles it into a wiki of markdown files and keeps it current, Obsidian is the window onto it, and whatever you produce gets filed back so the next question starts smarter. He closed by saying there was room for "an incredible new product instead of a hacky collection of scripts." This kit is one answer to that: the same idea, with a seat on top, an interview instead of scripts, and a weekly loop to keep it honest.

The pattern has been converging since. Tiago Forte built PARA, which turns out to be near-perfect scaffolding for an AI a decade after it was designed for people, and calls the person who designs these folders a context architect. Pawel Huryn wrote the compounding loop. AGENTS.md became the shared convention for telling an AI where to start. Katie Parrott at Every has written about using AI as a career coach working from her own record. Several operator teams arrived at the seat / memory / loop split independently in 2026. Different domains, same shape: markdown files, any AI, in your folder. That's the tell that it's a real pattern and not a trend.

## Which agents read it on their own

| Agent | Reads at the start of a conversation | What you do |
|---|---|---|
| Claude desktop app (make the folder a Project) and Claude Code | `CLAUDE.md` in the folder, plus any `CLAUDE.md` in a subfolder it's working in (each project has one, pointing to its `project.md`) | Nothing. The runbook tells it what to read next. |
| Cursor, Cline, Codex | Their own instruction file (`.cursor/rules`, `AGENTS.md`), not `CLAUDE.md` | The Starter ships `AGENTS.md` as a pointer. |
| An AI on your own machine (Ollama, LM Studio) | Nothing | Point a reader at the folder (Obsidian with a local-AI plugin, or Cline) and say "Read AGENTS.md first." Setup in `Level 2 - Operator Layer/Run it on your own machine.md`. |
| ChatGPT desktop app in Work mode | Nothing on its own, but it can read the folder once you open it | Say "Read AGENTS.md first." The runbook offers to put that line in the project's instructions so you stop typing it. ChatGPT on the web and phone runs in the cloud and can't open folders on your computer. |
| Gemini, any web chat | Nothing from your disk | Paste `seat/seat.md` and `seat/role.md` into the project instructions once, or attach the files, or connect your cloud folder through the tool's connector. Refresh the paste at the Friday audit. |

Three practical setups: the Claude desktop app (Projects, +, Use an existing folder; no terminal); Claude Code inside Obsidian (install Claude Code, add Obsidian's Terminal community plugin, type `claude` in the panel); Cursor or Cline with an AI provider of your choice, which is also the own-machine path when paired with Ollama. Whichever you pick, expect a short training period. In practice the corrections taper off over the first couple of weeks as the files fill in; they never reach zero, which is what the Friday audit is for.

## What comes after the seven steps

The operator layer, in `Starter/Level 2 - Operator Layer/`: a per-note index so the agent scans one line per note instead of reading folders; a connectors map so it knows every outside tool, what it may do there, and where the credential lives; a build log so you remember why the system is shaped the way it is. Each one earns its place when a specific problem shows up, and the Level 2 README names the problem.

Then the business version: several seats, one shared memory, each seat with its own feeds. Same kit, one more dimension.

## Build this weekend

Pick one project. Make the folder. Fill the seat. Have one conversation. File one note. Everything else is a layer you add later.

The first version will be wrong. The third will be useful. The tenth will quietly change how you work.

---

## Version, reuse, sources

**Version:** Operator's Seat v0.9, October 13, 2026. "0.9" because the seven steps haven't yet been run end to end by an outside user. The author ran them as a new user on October 15, 2026: a separate computer, a fresh Claude desktop install on a different account, the kit downloaded from its public page, and a real business's old files sorted through the inbox. Everything tested worked. The author's own system, which this kit is cut down from, runs daily on the Claude desktop app. The ChatGPT Work and own-machine paths are written from vendor documentation and partial testing. 1.0 follows the first outside pilots.

**Reuse:** free to share, adapt, and use commercially, including charging to set it up for others, as long as you credit Glen Lubbert. The writing and folders are under CC BY 4.0 (creativecommons.org/licenses/by/4.0/); the four scripts are under the MIT License. Details in `REUSE.md`.

**Sources named above:**
- Andrej Karpathy, "LLM Knowledge Bases," his post on X (@karpathy), early April 2026, and the follow-up "idea file" gist describing the architecture. Content confirmed from the author's saved notes on the thread and independent coverage; direct links to be added.
- Tiago Forte, PARA: "The PARA Method," fortelabs.com/blog/para/ (verified October 2026). The "context architect" framing is from his 2026 writing and talks; specific link not yet confirmed.
- AGENTS.md, the open format the Starter's pointer file follows: agents.md (verified October 2026). Matt Wolfe's coverage of it: not yet linked.
- Nick Milo, cognitive surrender and good vs bad friction: his AI OS material at Linking Your Thinking (linkingyourthinking.com) and podcast, 2026; specific episode not yet linked.
- Katie Parrott at Every: her writing on AI as a career coach, for example "I Hired ChatGPT as My Career Coach," every.to/working-overtime/i-hired-chatgpt-as-my-career-coach. The evidence rules in the runbook are adapted from her later work; that specific piece is not yet confirmed.
- Pawel Huryn, the compounding knowledge loop: attributed to his newsletter, 2026; not yet confirmed with a link.
- Solution-Focused questions: the approach developed by Steve de Shazer and Insoo Kim Berg; the five questions here are the operator's distillation.

Where a source says "not yet confirmed," treat the attribution as the author's recollection until a link is added.
