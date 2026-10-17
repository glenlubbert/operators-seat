# Playbooks: Occasional Tasks

*The runbook (`knowledge/agents.md`) is read at the start of every conversation and kept short. This file holds the tasks that come up now and then. Open only the section the person's request calls for; you don't need to read the rest. Everything in the runbook still applies here, especially section 7 (protected content) and the folder map in `seat/paths.md`.*

---

## The first interview

**When to run it.** `seat/seat.md` has a line near the top: `Onboarding: not started | partial | complete`. Run the interview when it says `not started`, when the person says "interview me" (including "Read AGENTS.md, then interview me"), or when it says `partial` and they agree to finish. Never restart it because a file contains an `[example]`; example text is inactive. The person never edits the seat by hand; you do, after they approve.

**How to run it**

- Open with this, in your own words but no longer: "I'll ask about a dozen short questions, one at a time, then set up your folders. Rough answers are fine, and you can say skip. About twenty-five minutes."
- One question at a time. Wait for the answer. Don't list the questions up front.
- One plain sentence per question. No field names. Say "what have you already decided," not "the Settled block."
- Follow up once if an answer is vague ("Can you give me an example?"), then move on. It's a conversation, not a form.
- Short answers are fine and so is "skip." Never push for completeness; a rough first pass is the goal and the files fill in as you work together. A skipped question doesn't make onboarding `partial`; leave that section's example lines out and pick it up when it comes up naturally later.
- After the last question (or whenever they want to stop), draft every file you're about to change, show each draft in the chat, and ask "Anything wrong or missing?" Edit until they say it's right. Then save. Never save before they've approved, including a partial save.
- After saving, read the files back (open them and confirm the content matches the approved draft) and tell them what was saved where. If a save failed, say so and keep the approved draft in the chat.
- Close with the handoff to step 2, in one or two sentences: "That's step 1. When you're ready, start a new conversation in this project and ask: 'What should I be careful about this week?'"
- Set `Onboarding:` to `complete` once they've been through all fourteen; a skipped question counts as done. Use `partial` only if they stopped before the end, with a line listing which questions are left.
- Questions 1 to 8 are the seat; 9 to 12 are the role; 13 and 14 set up their folders. If they stop after 8, save, mark `partial`, and offer to do the role later; when they come back, ask only the questions that are left.

**The questions, in order**

*The seat (`seat/seat.md`)*
1. What's your name, and what do you do, in a sentence or two?
2. What's this folder for: a company, a project, or your life and work in general? And who does it serve?
3. What are your best hopes for this week? The two or three things that would make it a good week. (Follow up: "And what's already going well that should keep going?")
4. What have you already decided that you don't want re-argued? Prices, a word you never use, a thing you've said no to. (Follow up: "Anything you keep having to tell an AI not to do?")
5. What are you still figuring out? (Follow up, if they're stuck on one: "Suppose it were sorted out. What would you notice first?")
6. Who are the two or three people I should know about, and what should I know?
7. Any words or terms specific to your work that I should use correctly?
8. How do you like to be talked to? Short or thorough, blunt or careful, anything that annoys you.

*The role (`seat/role.md`)*
9. What outcomes are you responsible for? Not tasks; the results that are yours to deliver. (Three to six.)
10. Which decisions are yours alone, where I should prepare and you decide? (At work: pricing, hiring, what to publish, spending over some amount. In life: where you travel, what you say yes to, big purchases.)
11. What work lands on you that belongs to someone else, or to nobody yet? (So I route it instead of bringing it to you.) Skip this one if they've said they work alone or the folder is for their personal life; count it as done.
12. Most weeks, what would you look at to know it went well? Numbers if you have them, things you'd notice if you don't.

*Your folders (`1. Projects/`, `2. Areas/`)*
13. What projects are you working on right now? Just the names, anything with a finish line. (If they list ongoing things with no end, like "my health" or "marketing," say those are areas and hold them for the next question.)
14. Then propose a starting set of areas based on Q2, as a short list they can edit, and ask "Which of these fit, and what's missing?"
    - Business: Sales, Marketing, Finance, Operations, Product development, Clients, Team.
    - Personal life: Health, Career, Money, Family, Relationships, Friends and community, Personal growth, Spirituality, Fun and recreation, Home. Say most people keep five or six.
    - Both: a short mix of the two, led by whichever they said matters most.
    Add anything from Q13 that turned out to be an area. `people/`, `brand/`, and `goals/` already exist; don't propose them again.

**What goes where**

Q1 and Q2: *Me* and *What this folder is for*. Q3: *Now* (best hopes, active threads, already working). Q4: *Settled*, and the "said no to" items also go to `seat/role.md` under "What I've said no to." Q5: *Open*. Q6: *Key People*. Q7: *Key Terms*. Q8: *How to talk to me* in the seat, and item by item to `knowledge/rules.md` under Always or Never, marked STABLE, because the person said it directly. Q9: `role.md` "What I own." Q10: "Decisions that are mine." Q11: "Not my seat." Q12: "Measures of a good week" (the Friday audit and the morning feed read these). Q13: one folder per project under `1. Projects/`, each copied from `_Example Project/` with `project.md` holding only the name and "Details to fill in"; step 4 fills one in properly. Q14: one folder per area under `2. Areas/`, each with a one-line `README.md` saying what it covers. Show the list of folders you'll create in the same approval as the seat drafts; create them only on the yes.

Leave the company-vault pointer blank unless they mention a shared company folder. Replace example lines in each file with the real ones; delete examples that have no real counterpart.

---

## Projects

- **"I want to add a project"** (or "add a project to [folder name]," "set up a project," "I want to add something I'm working on"): ask what it is, what done looks like, the deadline, and who's involved. Duplicate `1. Projects/_Example Project/` under the project's name (all three files: `project.md`, `CLAUDE.md`, `AGENTS.md`), fill in `project.md` from the answers, leave the two pointer files as they are, and confirm.
- **"Let's fill in [project]"** (or "tell me about [project]"): for a project folder created in the interview, ask what done looks like, the deadline, and who's involved, then fill in its `project.md`. If it has files, read them first and say what you found.
- **"Read what's in there and tell me what matters"** (about a project or area folder): read its files, then give a short summary of what it is, where it stands, the next deadline, and who's involved. Offer to put that into the folder's notes and any lasting facts into `knowledge/knowledge.md`; save on a yes.
- **"This project is done":** move the project's folder to `4. Archive/` with the end month in front (`2026-03 - Name`), following "Moving files" below. Then ask whether anything learned is worth keeping and file it in `knowledge/knowledge.md` on a yes. Never delete.

---

## Sorting and moving files

**Moving files.** Some apps let you write files but not move them. If you can't move files directly but your app can control the computer (clicking and dragging in Finder or File Explorer), offer that, with their yes, before falling back to a list. The first time, their computer will ask them to allow it (on a Mac, Accessibility and Screen Recording); tell them in one line that this is expected and they can turn it off afterward. If you can't move files either way, don't fake it by copying a file to its new place and leaving the original, which makes duplicates. Do all the thinking, then give a short numbered move list they can follow ("Drag `Q3 plan.pdf` from `0. Inbox` into `1. Projects/Website relaunch`"). Write any new notes yourself, since you can create files. When they say they're done, check each file is where the list said and tell them anything that's out of place. This applies everywhere a task says "move."

**"Sort my inbox."** Read each file in `0. Inbox/`. For each, say in one line what it is and propose a home: `1. Projects/[name]/` (has a finish line), `2. Areas/` (ongoing responsibility), `3. Resources/` (reference), or `4. Archive/` (done, keep for the record). List any facts, decisions, or people worth keeping, as drafts for `knowledge/knowledge.md`, `seat/seat.md`, or `2. Areas/people/`. Show the whole plan, then move and save only what they approve; read back what you saved. If there are more than about twenty files, sort the first twenty and ask before continuing. Before opening anything that looks like health, money, legal, or client records, ask; those get their own protected folder under `2. Areas/` (runbook section 7), and nothing from them is copied anywhere else except under section 7's one exception. Never delete a file; "done" goes to `4. Archive/`. Files you can't read (some images, locked PDFs): say so and leave them in the inbox.

**"I have a lot of existing files"** (folders that aren't organized as Projects / Areas / Resources / Archive): don't offer to reorganize everything. Offer three choices and recommend the first for the first week. (1) Start fresh: leave the old folders where they are; when something matters, drag it into `0. Inbox` and say "Sort my inbox." (2) Archive it, PARA-style: they move the old top folder into `4. Archive/` as "Old files (YYYY-MM)"; you search it when a question needs it and move things into Projects or Areas only when they're in use. (3) Sort one folder they care about: "Sort [folder] into PARA" works like the inbox, 20 files at a time, moving only on approval. Never offer option 3 for a whole drive. Moving their files is something they do or approve per batch, never something you do on your own.

---

## Areas, people, voice, goals

- **"I want to add an area for [X]":** ask what keeping it up well looks like and anything you should know, create `2. Areas/[X]/` with a short `README.md` holding the answers. If they say it's private, put a one-paragraph confidentiality note at the top of that README (runbook section 7 applies).
- **"Add [name] to my people":** ask who they are, how they know them, and what matters for working with them; copy `2. Areas/people/_Example Person.md` to `2. Areas/people/[First Last].md`, fill it in, set `status: active` and today's `last_contact`. Never record another person's health, money, or private life, even if told.
- **"I talked to [name] today"** (or "met with," "heard from"): add a dated entry under "Recent conversations" in their note and update `last_contact`. If there's no note yet, offer to create one.
- **"Here's something I wrote. Learn my voice from it"** (pasted, or files in the inbox): draft `2. Areas/brand/voice.md` from the samples, show it, save on approval. When they later say a draft doesn't sound like them, propose the specific edit to that file.
- **"Set my goals for this quarter":** ask for three to five goals and how they'd know each was reached; push back once, kindly, on anything too vague to check; save as `2. Areas/goals/Q[N]-[YYYY].md` on approval.

---

## Installing inside existing folders

**"Install Operator's Seat inside my folders"** (when they already have their own Projects / Areas / Resources / Archive folders): follow "Setting it up inside folders you already have" in the kit's `Starter/README.md`, one step at a time. Fill in and check `seat/paths.md` (folders as paths inside their top folder, plus this computer's full path to it) before anything else, and use it for every later step. For existing projects, follow that README's two cases exactly: existing notes stay canonical, or a new `project.md` is created, never both, and never a pointer to a file that doesn't exist. Show each change before saving. Never move, rename, or overwrite their existing files; when a `CLAUDE.md`, `AGENTS.md`, or `.gitignore` you'd create already exists, keep its content and add your lines to it. Finish with the step 9 test, then offer to start the interview.

---

## Save this and pass it on

Both follow the protected-content rule in runbook section 7. More detail in `seat/feeds.md`, under "On request."

- **"Save this"** saves the conversation to SAVED (`3. Resources/Saved conversations/`) as `YYYY-MM-DD - [topic].md`. Save what you actually have: if your app gives you the real transcript, save it under the heading "Transcript"; if it doesn't, write a careful record under the heading "Summary (full transcript not available)." Never call a reconstruction word for word. "Save this with a summary" puts a short summary (what was decided, what's next) above either one. If the conversation touched a protected folder, save it inside that folder instead, or, if they'd rather have it in SAVED, replace those parts with "[private: see {folder name}]." Ask which when it isn't obvious.
- **"Pass this on to [person]"** prepares a copy for someone else. Before opening any note it links to, check that note's folder: skip protected ones and list them at the end as "not included (private)." Leave out money, health, and anything about people other than the recipient. Show the finished copy, then put it in SHARED (`3. Resources/Shared/`), or a company folder if one is named, only on their yes. Putting it in a shared folder is disclosure even though nothing is sent. You never send it.

---

## Double-check

**"Double-check [a draft or file]"** (often said to a second AI about something another AI wrote): read it fresh against `knowledge/rules.md`, the seat, and the facts in `knowledge/`, as if you hadn't written it. List what's wrong, missing, unsupported, or off-voice, each with where you found the problem. Don't rewrite or save anything unless they ask; the point is a second opinion, not a second draft.

---

## Feeds and scheduling

- **"Run the first feed":** feed 1 in `seat/feeds.md`. Fill in the real paths for `[VAULT_ROOT]` and `[OS_ROOT]` and paste in the preamble (its "For the AI" section says how), run it once now, and show the results.
- **Scheduling it.** If your app lets you create the scheduled task yourself, do it and show what you set up. If it doesn't (in the Claude desktop app, people create scheduled tasks themselves, from Scheduled in the sidebar), give them the finished prompt with no `[brackets]` left, plus the exact clicks. Either way, ask them to tell you after the first run whether it could open their folder; scheduled tasks may run in the cloud, and some need the app open on their computer to reach local files. Add every feed you help schedule to the "Scheduled prompts" table in `seat/paths.md`. If their app has no scheduling at all, offer the by-hand version: they say "Run the first feed" each Friday.
- **Step 6's calendar event.** If a calendar is connected, create the Friday event. If not, say so in one line and they'll make it.

---

## The Friday audit

Once a week (default Friday afternoon, or when the person asks):

1. Read the Now block in `seat/seat.md` and ask the seat's questions, in this order: best hopes for next week; what's already working that should keep going; on a 0 to 10 for the week, where are they and what would one point higher look like; the smallest next step. Write the answers into Now.
2. Read the measures in `seat/role.md` and report the week against them, from the record.
3. Read the latest `knowledge/feed-output/stale-*.md` (or `tidy-*.md`) if one exists; otherwise do that sweep yourself, using the review scope in `seat/feeds.md`. Stale means an entry's `reviewed` date is more than 30 days old; it doesn't mean the fact is false. Entries with no date at all are a separate list, "missing dates": ask "still true?" and add today's date on a yes. For each stale entry, ask "still true?" On a yes, set `reviewed` to today. On a no, mark it `superseded` with a one-line note. On "promote," move it to `rules.md` (proposed, then saved on their yes).
4. Suggest rule promotions or demotions from the week's conversations.
5. Report what's missing: things they keep repeating that a file should hold.
6. Save every approved change, read the changed files back, and append one line to `knowledge/audit-log.md`: date, what was refreshed, confirmed, superseded, or promoted, and the measures reported.

Under 15 minutes. The system rots if the audit becomes a chore.
