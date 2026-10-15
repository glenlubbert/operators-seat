# Goals: what you're aiming for this quarter, and how it's going

*Optional, and worth it. The AI checks your progress against your own goals, using the work in your folders as evidence. Pattern adapted from Katie Parrott's writing at Every on using AI as a career coach (every.to); the specific piece isn't yet confirmed.*

## Setting your goals

Say:

> Set my goals for this quarter.

The AI asks for three to five goals, and for each one, how you'd know you got there. It pushes back, gently, on anything too vague to check: "grow the business" can't be checked; "10 new clients by the end of June" can. Life goals work the same way: "run three times a week" beats "get fit." It saves them as `Q[N]-[YYYY].md` in this folder after you approve.

## The audit prompt

> Act as my evidence-based coach. Read this quarter's goals file in [GOALS] (named Q{quarter}-{year}.md) and [OS_ROOT]/seat/role.md. Compare each goal to the work in my folders, using the project notes in [PROJECTS], [KNOWLEDGE]/knowledge.md, and these named sources only: [list connected tools by name, or "none"]. If a named source is unavailable, say so and don't substitute another. For each goal, show: confirmed progress with citations; valuable work that's currently uncounted; missing evidence, especially around impact; places where the goal no longer fits the work; the single next action most likely to improve the outcome. Then name the larger pattern in my role. Separate confirmed evidence from interpretation and from questions only I can answer. When the record can answer, don't rely on my self-assessment. Write the result to [GOALS]/review-YYYY-MM.md and edit nothing else.

*The names in capitals come from `seat/paths.md`; the AI fills them in when it runs or schedules this.*

Expect surprises in both directions the first time.

## When to run it

End of each month for a gut check; two weeks before quarter-end to correct course; first week of the new quarter as the basis for the next set. Fifteen minutes a run.

## The second prompt

> Given my goals, what I've shipped, and what you know about my role, where am I creating leverage and where noise? What should I do less of? What should I propose for next quarter that I haven't dared to ask for?

## Automate it

This is feed 4 in `seat/feeds.md`. Ask the AI to schedule it for the first Friday of the month, and the check happens whether you remember or not.
