# Day 1 run sheet — UNDERSTAND

**Assume students arrive with nothing.** No setup done, no accounts, no keys.
Day 1 is deliberately designed to need **only Python 3.10+ and this repo**.
No pip, no pytest, no internet, no AI accounts until 13:45.


## Slide decks

One deck per session. Open `slides/index.html`, or go straight to:

| Session | Deck | Slides |
|---|---|---|
| 09:30–11:00 | [`day1-s1.html`](../../slides/day1-s1.html) | 29 |
| 11:30–13:00 | [`day1-s2.html`](../../slides/day1-s2.html) | 24 |
| 13:45–15:15 | [`day1-s3.html`](../../slides/day1-s3.html) | 15 |
| 15:30–17:00 | [`day1-s4.html`](../../slides/day1-s4.html) | 15 |

Press `F` for fullscreen. Arrows or space to advance. Works offline.

---

## 09:15 — before you start

Write on the board and leave it there all day:

```
1. Reproduce   2. Hypothesise   3. Isolate   4. Fix   5. Verify
              ^ ON PAPER, BEFORE YOU ASK AI
```

Have the repo URL on the board too. See `instructor/BOARD.md` for everything
that goes on the whiteboard — **nothing needs printing.**

If the network fails: `python3 serve.py` on your laptop hands the repo out over
the room's wifi with no internet at all.

---

## 09:30–11:00 — Code Execution & Common Bugs

### 09:30 (10 min) — Setup, and no further
Everyone runs:
```bash
git clone <REPO-URL>
cd nitte-ai-coding-workshop
python3 check_setup.py
```
> **Timebox this hard.** At 09:40 anyone still broken pairs up with a working
> neighbour. Do not debug 60 laptops. Pairs are the plan anyway.

### 09:40 (10 min) — The framing
Say this plainly, it sets up the whole workshop:

> "Most placement tests ban AI. So today you learn to do it without. Tomorrow
> you learn to do it with. The people who get placed can do both — and the tell
> is whether you can explain your own fix."

### 09:50 (20 min) — **Bug Hunt #1** — `bugs/tier0/bug_01_greeting.py`
Run it on the projector. Let the traceback fill the screen.

1. **90 seconds, silent.** No typing. Everyone writes one hypothesis on paper.
2. **Collect three WRONG hypotheses first.** Thank each one. This is the single
   most important thing you do today — it makes being wrong safe in a room,
   and that is exactly what students freeze on in interviews.
3. Then take a correct one. A student drives at the keyboard.
4. **Post-mortem:** *"What was the smallest possible fix?"* (one colon)
   *"How could you have caught that in 10 seconds?"* (read the caret)

### 10:10 (25 min) — Pairs on `tier0` and `tier1`
```bash
python3 run_tests.py bugs/tier0
```
Rotating driver, swap every 10 minutes. Enforce the swap.

> **Expected sticking points**
> - `bug_02`: they fix `len(cgpa)` → `len(cgpas)` fast. Ask them what happens
>   on an empty list — nobody handles it. That is your bridge to edge cases.
> - `bug_03`: **most of the room will not find this.** It reads correctly in
>   English. Push them to the boundary test, not the code.

### 10:35 (20 min) — Debrief `bug_03` (boundary) as a group
This is the highest-value bug of the morning. `>` vs `>=`. Draw the number line
on the board and mark 7.0 with an open vs closed circle.

> Off-by-one and boundary errors are the **most common single cause** of hidden
> test failures in screening assessments. Say that out loud.

### 10:55 — Close: "write down the bug class you got fooled by"

---

## 11:30–13:00 — Stack Traces & Print Logging

### 11:30 (20 min) — Traceback anatomy
**Project** `handouts/reading-a-traceback.md` (it's in their repo too) and draw
BOARD 5 from `instructor/BOARD.md`. Teach **bottom-up reading**:
- last line = *what* went wrong
- the line above = *where*
- the frames above that = *how you got there*

Demo live on `bug_02`.

### 11:50 (20 min) — **Bug Hunt #2** — `bugs/tier1/bug_04_toppers.py`
Same 5-step ritual. This one **does not crash** — it silently keeps the wrong
students. The lesson: *no traceback does not mean no bug.*

Show the giveaway: it passes the first test and fails the second. Ask why.
(Mutating a list while iterating it — the iterator skips.)

### 12:10 (35 min) — Pairs on `tier2` + print debugging
Teach three things and make them use all three:
```python
print(f"{cgpa=}")              # prints both name and value
print(repr(cgpa))              # shows you 7.300000000000001, not 7.3
breakpoint()                   # stops here; type n, c, q
```
> `repr()` is the punchline for `bug_06`. Do not give it away — let them find
> it, then make the room notice that `print(7.3)` and `print(repr(7.3))` differ.

### 12:45 (15 min) — Debrief `bug_05` (mutable default) and `bug_06` (float)
`bug_06` post-mortem question: *"Is the fix to compare with a tolerance, or to
never use floats for money and marks?"* Both are right. That ambiguity is a
real interview answer.

---

## 13:45–15:15 — AI as Explainer  ← first AI contact

### 13:45 (10 min) — The rules, on the board
```
ALLOWED   "explain this traceback"
          "what does this line do"
          "what does this error mean"
          "give me 3 edge cases for this function"

BANNED    "fix it"
          "write this for me"
```

> **Zero setup needed.** Any free browser AI works — ChatGPT, Gemini, Claude.
> Phone is fine. Nobody installs anything. If the lab blocks all of them, run
> this session as a projector demo and it still works.

### 13:55 (30 min) — Explain-the-bug drill
Pairs take a bug they **already fixed** this morning and ask AI to explain the
original error. They compare the explanation against what they actually found.

The discovery you are steering toward: *AI explains the general class well, and
is often wrong or generic about this specific code.* Let them find that.

### 14:25 (30 min) — The paste-context lesson
Ask AI about `bug_04` **without** pasting the test. Then **with** the test.
Night and day. This is invariant #1 (context) arriving early — tomorrow it has
a name.

### 14:55 (20 min) — Group: where did AI help, where did it mislead?
Collect real examples on the board. Keep the photo — you will reuse it on Day 2
for the sabotage drill.

---

## 15:30–17:00 — Hands-on Debugging Practical (graded)

### The format
- 4 bugs, unseen, 60 minutes, pairs
- **Hypothesis sheet handed in** — their own paper, format copied from BOARD 3.
  Written before any AI use.
- AI allowed — but only after the hypothesis is on paper

### Scoring (out of 10) — read this out before you start
| | |
|---|---|
| Tests green | 4 |
| **Hypothesis was correct** | 3 |
| **Fix was minimal** (no rewrites) | 2 |
| Explained it out loud | 1 |

> Say clearly: **you can score 6/10 without fixing anything, if your hypothesis
> and reasoning are right.** That is the message of the whole day. Placement
> interviewers hire the reasoning, not the keystrokes.

### 16:30 (30 min) — Live solve of the two nobody got
You drive. Think aloud. **Get stuck on purpose and recover** — they need to see
an experienced person not knowing something and working it out calmly.

### 16:55 — Close
> "Tomorrow: the same skill, with AI in the loop. The hypothesis rule does not
> go away — it is the only thing that makes AI safe."

### Homework — DO THIS IN THE ROOM, do not just announce it
Days are consecutive, so this is the only window. **Day 2 does not work without it.**

Project `harnesses/GET-YOUR-KEY.md` — it's already in their repo. Put BOARD 7
on the board:

```
        https://aistudio.google.com/apikey
```

Give it **5 minutes now, on their phones or laptops, while you watch.** Ask for
hands when `echo $GEMINI_API_KEY` prints something. Whoever fails, note their
name — you'll pair them on Day 2 morning.

> **Do not set homework you cannot verify.** If you only announce it, expect
> a third of the room to arrive without a key and lose your 09:30 session.

> GitHub Student Pack is **not** on the critical path — approval takes days and
> Day 2 is tomorrow. Mention it as a "do this for yourself later" aside only.

---

## If things go wrong

| Problem | Do this |
|---|---|
| No Python on lab machines | Windows: Microsoft Store → Python 3.12, no admin needed. Or any online Python runner — the bugs are single-file. |
| No internet at all | Day 1 needs none. Only the 13:45 AI session does — run it as a projector demo. |
| Room is way ahead | Send fast pairs to `bugs/tier2` early, then have them write a *new* bug for another pair. Writing bugs teaches more than fixing them. |
| Room is way behind | Drop `tier2` entirely. Do `bug_03` and `bug_04` properly as a group instead. Depth beats coverage. |
| Someone rewrites the whole function | Ask: *"revert it — now fix it in one line."* Minimal-fix discipline is the point. |
