# Viva rubric — Day 3, 15:30–17:00

**30 of 100 marks.** Students present their mock assessment code and defend it.

> Announce the format on Day 3 morning, not at 15:30. They should write code
> all day knowing they will have to explain it.

## Format

- **5 minutes per student.** With 60 students you cannot do all of them —
  call **12–15 at random**, and tell them at 09:30 that it will be random.
  Random selection makes the whole room prepare.
- Student shares their screen (or you open their file on the projector).
- You pick **one function** and ask them to walk it line by line.
- Then 2–3 questions from the bank below.

## Scoring — 30 marks

| Dimension | Marks | What full marks looks like |
|---|---|---|
| **Line-by-line walkthrough** | 10 | Explains what each line does *and why it is there*. No "the AI wrote that". |
| **Complexity** | 5 | States time and space complexity and justifies it by pointing at the loops. |
| **Edge cases** | 5 | Names the cases they handled and, honestly, the ones they did not. |
| **Design justification** | 5 | Explains why this approach over an alternative they can actually name. |
| **Honesty about AI use** | 5 | Says clearly what AI wrote, what they changed and why. |

### The strike rule

> **Any line a student cannot explain is struck from their submission** and
> scores zero in Parts A/B, even if the tests pass.

Announce this at 09:30. Enforce it once, early, visibly — the room will
recalibrate instantly.

### Marking honesty *up*, not down

A student who says *"the AI wrote this line and I don't fully understand it"*
scores **more** on Honesty than one who bluffs. Say this out loud before you
start. You are training a habit that keeps them employed, not punishing AI use.

---

## Question bank

### Walkthrough openers
- Walk me through `generate_drive_report`, line by line.
- Why a `list` here and not a `dict`?
- What happens on the very first iteration of that loop?
- What is the value of `reason` when the student *is* eligible?

### Complexity
- What is the time complexity? Point at the line that dominates.
- You sort inside the function — what does that cost?
- 5000 students instead of 5 — what breaks first?
- Could you do this in one pass instead of two? Would you want to?

### Edge cases
- What happens with an empty student list? Show me.
- A student exactly on the CGPA bar — eligible or not? Where is that decided?
- Two students with identical CGPA and backlogs — what decides the order?
- What if `allowed_branches` is empty?
- What if two students have the same roll number?

### Design
- Why did you reuse `rejection_reason` instead of writing the checks inline?
- You return a dict. Why not a class?
- Someone asks for the *rejected* list sorted too. What changes?
- What would you name this differently if you wrote it again?

### AI use — ask everyone at least one
- Which parts did AI write? Which did you change?
- Did AI suggest anything you rejected? Why did you reject it?
- How did you check the AI was right?
- Show me a line you rewrote after AI produced it. Why?
- What would you have done if you had no AI today?

### For the strong ones
- Your sort key is `(-s.cgpa, s.backlogs, s.roll_no)`. Why negate CGPA instead
  of `reverse=True`?
- Is your sort stable? Does it matter here?
- If `eligibility_rate` had to be exact rather than rounded, what changes?
- How would you test this if you could not see the implementation?

---

## Running it with 60 students and 90 minutes

| Time | What |
|---|---|
| 15:30 | Explain format + strike rule. 5 min. |
| 15:35 | 12–15 vivas, 5 min each, called at random. |
| 16:45 | **Group debrief** — the three best answers you heard, and why. |
| 16:55 | Close the workshop. |

> Do the debrief even if you run late. The students who *watched* 14 vivas
> learn nearly as much as the ones who gave them.

## Closing the workshop

> "Three days ago you could fix a bug if you could see it. Now you can find it,
> explain it, and defend the fix — with or without AI. That last part is what
> gets you hired. The tools will all be different in a year. The method won't."
