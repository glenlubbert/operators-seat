# Feeds: what the AI checks on a schedule

*You don't need to read this file; the AI does. Step 7 uses the first feed. The rest are here for when you want them.*

A feed is something the AI checks on its own, on a schedule. Each one does only what it was set up to do. Most just write a report for you; the meeting-notes feed also adds entries to people notes. None of them sends, deletes, or decides anything.

**Scheduled feeds**

1. **Stale check** (weekly, Friday): lists what in your memory hasn't been confirmed in a month, so your Friday audit starts with a list. *This is step 7.*
2. **Morning briefing** (weekday mornings): the five things most worth your attention today, tied to your measures and deadlines. Works from your folders alone; better with email or meeting notes connected.
3. **Meeting notes to people files** (daily): adds what was discussed to each person's note. *Needs a connected meeting-notes tool (Granola, Otter, or similar).*
4. **Monthly goals check** (first Friday of the month): how you're doing against your goals.
5. **Tidy up** (weekly): the stale check plus duplicates, broken links, and overdue projects. The bigger version of feed 1, for when you're ready; it replaces feed 1 rather than running alongside it.

**On request (just say it, any day)**

- **"Save this"**: saves the conversation to your Saved conversations folder: the transcript if your AI app provides one, otherwise a careful summary, clearly labeled. Private material stays in its own folder.
- **"Pass this on to [person]"**: makes a cleaned-up copy safe to share and shows it to you before putting it in your Shared folder. Nothing is sent; you send it.

To add a feed, tell the AI what you want checked and how often.

---
---

# For the AI

*Each feed is a prompt for a scheduled task (in Claude: the person creates it from Scheduled in the sidebar and pastes the prompt you give them; in ChatGPT Work: scheduled tasks against the local project). Every run starts fresh with no memory of conversations, so each prompt names the files it reads and starts with the same preamble. Feeds only write what their prompt names; anything else is reported, not done.*

*Before running or scheduling any feed: replace every path name in capitals (`[VAULT_ROOT]`, `[OS_ROOT]`, `[KNOWLEDGE]`, `[PROJECTS]`, `[AREAS]`, `[PEOPLE]`, `[GOALS]`, `[INBOX]`) with its full path on this computer: this computer's VAULT_ROOT from `seat/paths.md`, joined to the folder's path inside the vault. Never work a path out from where this file happens to sit; if `paths.md` isn't `checked` or has no line for this computer, check it first (the runbook says how). After scheduling, add the feed to the "Scheduled prompts" table in `paths.md` so it can be updated if the vault moves. Replace any other square-bracket fill-in (like a source `[NAME]`), and paste the preamble in place of `> [preamble]`. Words in curly braces, like `{meeting ID}`, are different: the feed fills those in each time it runs, so leave them. Show the person the finished prompt before you schedule it. A scheduled prompt that still contains a square bracket is broken.*

## What the review feeds read (Feeds 1 and 5)

Both feeds use the same scope, so they never disagree about what counts:

- **Read:** `[KNOWLEDGE]/knowledge.md`, `[KNOWLEDGE]/hypotheses.md`, any other note in `[KNOWLEDGE]` and its subfolders (atomic notes), and the person notes in `[PEOPLE]`.
- **Skip these files entirely:** `agents.md`, `playbooks.md`, `rules.md`, `INDEX.md`, `audit-log.md`, any file ending in `-log.md`, anything under `feed-output/` or `digests/`, any file whose frontmatter says `status: example` or `status: superseded`, and in `[PEOPLE]`, `README.md` and any file starting with `_`.
- **Inside the files you read, skip entries** marked `status: example` or `status: superseded`, and anything under a "Disproven" heading in hypotheses.md.
- **Dates:** never guess one. An entry with no `reviewed` date (or a person with no `last_contact`) goes in a separate "missing dates" list, not the stale list.


## The preamble every feed starts with

Paste this at the top of every feed prompt. It makes a scheduled run follow the same rules as a live conversation.

> Work only inside the vault at "[VAULT_ROOT]" (the operating system files are at "[OS_ROOT]"; on a standalone install these are the same folder; the full folder map is in [OS_ROOT]/seat/paths.md). Before anything else, read [OS_ROOT]/knowledge/agents.md, [OS_ROOT]/knowledge/rules.md, [OS_ROOT]/seat/rules.md, [OS_ROOT]/seat/role.md, and, if it exists, "[OS_ROOT]/Level 2 - Operator Layer/CONNECTORS.md". Honor every confidentiality boundary named in any project.md, CLAUDE.md, or README you encounter. Use only the sources this prompt names; if one is unavailable or not connected, say so in the output and do not substitute another source. Do not read the archive folder named in paths.md, or any folder marked private or confidential. Write only to the files this prompt names. Nothing leaves the vault.

---

## Feed 1: Stale check (weekly; step 7)

**Reads:** the review scope above
**Rule:** active entries whose `reviewed` date is over 30 days old; active hypotheses past their check-back date; active people whose `last_contact` is over 30 days old; and, separately, anything with no date at all
**Lands in:** `[KNOWLEDGE]/feed-output/stale-YYYY-MM-DD.md` (overwritten each run), which the Friday audit reads
**Writes:** only that output file

> [preamble]
> Read what the "What the review feeds read" section of [OS_ROOT]/seat/feeds.md lists, and follow its skip rules exactly. Today's date is the run date. List: (1) active knowledge entries and atomic notes whose `reviewed` date is more than 30 days old; (2) active hypotheses whose check-back date has passed; (3) active people whose `last_contact` is more than 30 days ago. Then, as a separate list headed "Missing dates," anything in scope with no `reviewed`, check-back, or `last_contact` date; never guess a date. For each line: what it is, the date in question (or "no date"), and the question to ask ("still true?", "promote or kill?", "ping or let go?"). Stale means needs review, not false. Write the result to [KNOWLEDGE]/feed-output/stale-YYYY-MM-DD.md, overwriting any file from today. Do not edit any other file.

Schedule: Friday, an hour before your audit.

## Feed 2: Morning briefing (weekday mornings; email and meeting notes optional)

**Reads:** `seat/seat.md` (Now), `seat/role.md` (measures, no-list), every project's notes (Now and Open), plus, only if named below, yesterday's meeting notes and the inbox
**Rule:** rank by this week's measures first, deadlines second, open questions third; never surface anything on the no-list
**Lands in:** `[VAULT_ROOT]/REVIEW.md`, overwritten daily; you answer in it
**Sources you must authorize by name:** meeting-notes connector [name it or write "none"], email connector [name it or "none"]

> [preamble]
> Read [OS_ROOT]/seat/seat.md and [OS_ROOT]/seat/role.md, and the notes of each project in "[PROJECTS]" except _Example Project, found by the project-notes rule in [OS_ROOT]/knowledge/agents.md (project.md if it exists, otherwise whichever of CLAUDE.md or AGENTS.md holds more than a one-line pointer). If this prompt names a meeting-notes source ([NAME or none]), read yesterday's meetings from it; if it names an email source ([NAME or none]), scan that inbox for anything unanswered over 48 hours. If a named source is unavailable, write "source unavailable: {source name}" in the output and continue. Write to [VAULT_ROOT]/REVIEW.md: today's date; the five things most worth attention today, each with one line of reason tied to a measure in role.md, a deadline, or an open question, and one bounded first step the AI could take if told yes; then a "waiting on you" list of anything promised and not done, each with its source. Nothing from the no-list. Overwrite the file. Take none of the steps.

## Feed 3: Meeting notes to people files (daily; needs a connected meeting-notes tool)

**Reads:** your named meeting-notes source only (Granola, Otter, Read; name one); the state file; the people notes
**Rule:** for each matched participant, add one dated entry per meeting version, with a marker that's checked before every write; for new participants, propose a note, don't create one
**Writes:** people notes (an entry under "Recent conversations," plus the `last_contact` field), and four working files in `[KNOWLEDGE]/feed-output/`: `meetings-lock.md` (stops two runs overlapping), `meetings-state.md` and `meetings-state.prev.md` (what has been fully processed, and the copy before the last update), and `meetings-attempts.md` (every run, including failures)

**Needs from the source:** a stable meeting ID and an edit or last-modified time for each meeting. Without a stable ID the feed won't run; it says so and stops. Without edit times it processes each meeting once and doesn't track later amendments; the attempts log says that every run.

**How it stays safe to retry.** Only one run at a time: a lock file stops a second run from starting while one is working. Every entry it adds to a person's note carries a marker with the meeting ID and edit time, and it checks for that marker before writing, so a rerun after an interruption skips anyone already done. The state file is updated by writing a complete new copy, keeping the previous one, so an interrupted save can be recovered. And "last successful run" only moves forward when every query, including every page of results, came back complete. Failures go in the attempts log, never in the state file. Tested in simulation only; see "Tested how" below.

> [preamble]
> The meeting-notes source for this feed is [NAME]; use no other source. This feed may write only: entries under "Recent conversations" and the `last_contact` field in notes in "[PEOPLE]", and these files in [KNOWLEDGE]/feed-output/: meetings-lock.md, meetings-state.md, meetings-state.prev.md, meetings-state.new.md, meetings-attempts.md.
>
> 1. **Lock.** Read meetings-lock.md. If it says "held" with a time less than 2 hours ago, another run is working: append "skipped: run in progress" to meetings-attempts.md and stop. If it says "held" with an older time, the last run died: note "stale lock taken over" in the attempts log and continue. Write "held {now}" to meetings-lock.md. Append "{now} started" to meetings-attempts.md.
> 2. **Load state.** Read meetings-state.md. A complete state file ends with the line `END OF STATE`. If it doesn't (an interrupted save), use meetings-state.prev.md instead and note "state recovered from previous copy." If meetings-state.new.md exists and ends with `END OF STATE`, it's the newest complete copy: use it. The state holds `last_successful_run:` and one line per meeting: ID, edit time processed (or "none"), date, title, participants matched, people completed, status (`complete`, `partial`, or `waiting for transcript`), and a two-line summary of what was recorded.
> 3. **Check the source can do this.** If the source gives no stable meeting ID, write "cannot run: source has no stable meeting IDs" to the attempts log, release the lock, and stop. If it gives no edit or modified time, use "none" as the edit time, skip all amendment checks this run, and note "no edit times: amendments not tracked" in the attempts log. Never make up an ID or a time.
> 4. **Fetch, completely.** Run three queries, following every page of each to the end: (a) meetings that started after `last_successful_run` minus 24 hours (the last 24 hours if there's no state); (b) the reconciliation sweep: every meeting from the last 14 days, so meetings whose transcripts arrived late, or that an earlier run missed, are found even if they're older than 24 hours; (c) every state line that's `partial` or `waiting for transcript`, whatever its date. If any query or page fails, mark this run "retrieval incomplete," process only what was fully fetched, and don't advance `last_successful_run` at the end. If the source is unavailable altogether, log "source unavailable: [NAME]," release the lock, and stop without touching the state. A query that completes and returns nothing is a successful empty result, not a failure.
> 5. **Decide what needs work.** For each fetched meeting: new ID, process it. Known ID with a newer edit time than the state, process it as an amendment. Status `partial`, finish it. No transcript yet, record or keep it as `waiting for transcript` (it'll be found again by the sweep for 14 days, then logged as given up). Otherwise skip.
> 6. **Match people.** Match participants against the notes in "[PEOPLE]" (skip README.md and files starting with "_"; match on the `name` field, not the filename alone; if two notes could match, don't write and flag it).
> 7. **Write each person's entry.** Open their note and look for `<!-- meeting:{meeting ID} edited:{edit time} -->`. If that exact marker is there, they're done for this version: skip. For a new meeting, add under "Recent conversations": the date, the title, the source and meeting ID as a citation, two to four lines on what was discussed and decided, and the marker. For an amendment, compare the new transcript with the summary and participant list in the state and add "Amended: {meeting title}" with the new marker, saying only what changed. For anyone matched in the previous version but not in this one, add "Amended: {meeting title}: the updated record no longer lists you; the earlier entry may not apply," with the new marker; never delete the earlier entry. Set `last_contact` to the meeting date if it's later than the current value. Read the note back and confirm the marker is there.
> 8. **Save state safely.** After each meeting, build the full new state: that meeting's line with the edit time, participants, people completed, status (`complete` if every matched person is confirmed, otherwise `partial`), and the two-line summary. Write it to meetings-state.new.md ending with `END OF STATE`, read it back, copy the current meetings-state.md to meetings-state.prev.md, then write the new content to meetings-state.md and read it back. If a write fails partway, the next run recovers using step 2.
> 9. **Finish.** If every query was complete and every meeting is `complete` or `waiting for transcript`, set `last_successful_run` to this run's start time (saved the same way as step 8). Otherwise leave it unchanged. Append the result to meetings-attempts.md: "ok," "ok, nothing new," "partial," or "retrieval incomplete," with counts and any errors word for word. Write "free" to meetings-lock.md. In your reply, list what you added, any unmatched participants with a one-line proposed note each, and anything you flagged.

Schedule: daily, early. If your scheduler lets you prevent overlapping runs, turn that on too; the lock is the backstop.

**What the safeguards do and don't promise.** The marker check stops a rerun from adding the same meeting version to the same person's note twice. The lock stops two runs from both checking before either writes. Both depend on the AI following these steps exactly; nothing at the file level enforces them.

**Tested how:** simulation only. A Python model of these steps and its fake meeting source and sample people notes are kept in `Level 2 - Operator Layer/tests/feed3/`; running `sim.py --write-results` writes `results.md` beside it. Last run October 14, 2026, on the author's Mac: 17 of 17 checks passed. It covers: a repeat run, an interruption after the first person's note, the retry, an amended older transcript, a removed participant, a delayed transcript outside the 24-hour window, a failed page of results, an empty successful fetch, missing edit times, missing IDs, an overlapping run, an interrupted state save, and an unavailable source. The simulation checks the procedure's logic, not how a real AI or a real connector behaves. It has not been run against a real meeting-notes connector.

## Feed 4: Monthly goals audit (monthly)

The prompt is in the goals README (`[GOALS]/README.md`). Add the preamble, fill in its paths and its named sources, and schedule it for the first Friday of the month. It writes only `[GOALS]/review-YYYY-MM.md`.

## Feed 5: Tidy up (weekly; the bigger version of feed 1)

*Credit: Nick Milo's "janitor" skill. Ours runs the Friday audit's sweep as a feed so the audit starts done instead of blank.*

**Reads:** the review scope above, plus `seat/seat.md`, `seat/role.md`, and every project's notes
**Rule:** everything Feed 1 reports, plus overdue projects, the same fact stated two ways, broken links, and leftover placeholders after onboarding
**Lands in:** `[KNOWLEDGE]/feed-output/tidy-YYYY-MM-DD.md`; nothing is changed without your yes

> [preamble]
> Part A, using the review scope: read what the "What the review feeds read" section of [OS_ROOT]/seat/feeds.md lists, following its skip rules exactly, plus [OS_ROOT]/seat/seat.md and the notes of each project in "[PROJECTS]" except _Example Project, found by the project-notes rule in [OS_ROOT]/knowledge/agents.md. Report: (1) everything Feed 1 would report, including the separate "Missing dates" list (never guess a date); (2) projects whose deadline has passed with no Now update since; (3) the same fact stated in two places with different wording; (4) links or paths to files that don't exist.
> Part B, a separate check that deliberately looks at examples: only if [OS_ROOT]/seat/seat.md says "Onboarding: complete," scan seat.md, role.md, [KNOWLEDGE]/knowledge.md, [KNOWLEDGE]/hypotheses.md, and each project's notes for leftover `status: example` entries and unfilled placeholders in square brackets. Ignore the rules file's single "Example (inactive)" rule, which is meant to stay, and the `_Example Project` and `_Example Person` templates.
> For each finding, one line and a proposed fix. Write the report to [KNOWLEDGE]/feed-output/tidy-YYYY-MM-DD.md. Do not edit any other file.

Schedule: Friday morning, before the audit. When you're ready for it, ask the AI to swap feed 1 for this one; don't run both.

## On request

*These aren't scheduled; the person asks for them, and `knowledge/playbooks.md` runs them. Details here for reference.*

### Save this

*Credit: Nick Milo's "chronicler" skill in his AI OS. Same idea, our name.*

**Reads:** the current conversation
**Rule:** save what's actually available: the real transcript if the app provides one, labeled "Transcript," otherwise a careful record labeled "Summary (full transcript not available)." "Save this with a summary" adds what was decided and what's next on top. Private material stays in its own folder (runbook section 7).
**Lands in:** `[SAVED]/YYYY-MM-DD - {topic}.md`, or inside the protected folder the conversation was about

Nothing to schedule; the runbook handles it. A good conversation with an AI is gone the moment you close it unless someone writes it down, and that someone shouldn't be you.

### Pass it on

*Credit: Nick Milo's "courier" skill. This is the seed of the company version: how a note leaves a personal seat for a shared one.*

**Reads:** the note you name, and the notes it links to, checking each one's folder first
**Rule:** when you say "pass this on to [person or the team]," the AI makes a copy without private material (protected folders, money, health, people other than the recipient), adds one-line summaries of linked notes that aren't private, lists any it left out as "not included (private)," and shows you the copy
**Lands in:** `[SHARED]` on a personal seat, or the company folder's inbox once one exists, only after you say yes. Putting it there is sharing it.

Nothing is sent. "Pass it on" prepares; you send.

---

## Company feeds

When a seat belongs to a company vault, its feeds run against the company vault only: `[VAULT_ROOT]` and `[OS_ROOT]` both point at the shared vault, the preamble reads the company's runbook and rules, and the personal vault is never on the path. A company feed that needs something from a person's own files gets it through "pass it on," not by reading the personal folder.

## Adding a feed

Name it, say what it reads (by name, one source per kind), write the rule for what counts, say where it lands and what it may write, paste the preamble, then the prompt. Add the row to `Level 2 - Operator Layer/CONNECTORS.md` if it touches a system outside the vault. Feeds that write to anything outside the vault need your explicit approval in the prompt, per item.
