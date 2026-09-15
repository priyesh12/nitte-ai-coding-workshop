# Day 3 run sheet — DELIVER

**Goal:** ship end-to-end under time pressure, then defend every line.

> **Say this at 09:30, before anything else:**
> *"This afternoon you will be called at random to explain your own code line
> by line. Any line you cannot explain is struck from your submission — it
> scores zero even if the tests pass."*
>
> Announcing it now is the entire point. It changes how they code all day.


## Slide decks

One deck per session. Open `slides/index.html`, or go straight to:

| Session | Deck | Slides |
|---|---|---|
| 09:30–11:00 | [`day3-s1.html`](../../slides/day3-s1.html) | 15 |
| 11:30–13:00 | [`day3-s2.html`](../../slides/day3-s2.html) | 14 |
| 13:45–15:15 | [`day3-s3.html`](../../slides/day3-s3.html) | 15 |
| 15:30–17:00 | [`day3-s4.html`](../../slides/day3-s4.html) | 17 |

Press `F` for fullscreen. Arrows or space to advance. Works offline.

---

## 09:30–11:00 — Clean Code & the Developer Loop

### 09:30 (10 min) — The announcement above. Then the day's shape.
```
  09:30  clean code      11:30  git safety net
  13:45  MOCK ASSESSMENT (90 min, graded)
  15:30  VIVA (random, 30 marks)
```

### 09:40 (30 min) — What "readable" actually means
Not style rules. Three things only:

1. **Names that say what, not how.** `s` → `student`. `tmp2` → `eligible`.
2. **A function does one thing.** If the name needs "and", split it.
3. **Comments say WHY.** A comment restating the line below is noise.

Live demo: take `bugs/tier3/bug_07_shortlist.py` — which they debugged on
Day 1 — and rename everything properly. Same logic, suddenly obvious.

> **The Day 1 callback lands hard here:** half those bugs were only hard to
> find because the code was unclear. Clean code is not decoration, it is
> *bug prevention*.

### 10:10 (25 min) — The loop
```
   WRITE  ->  TEST  ->  REFACTOR WITH AI  ->  VERIFY
                              ^                  |
                              +---- commit ------+
```
The critical rule: **refactor only when tests are green.** Otherwise you cannot
tell whether AI broke it or it was already broken.

### 10:35 (25 min) — Pairs: refactor a Day 1 fix, keep tests green
Any tier 1–2 bug they already fixed. Rule: **tests must be green before AND
after.** Run them before you touch anything.

---

## 11:30–13:00 — Git as the AI Safety Net

### 11:30 (25 min) — The four commands that matter today
```bash
git status                 # what have I changed?
git add -A && git commit -m "working: eligibility fixed"
git diff                   # what did the AI just do?
git reset --hard HEAD      # undo ALL uncommitted changes
```
> **`git diff` is invariant #4.** It is the same review surface no matter which
> harness made the change. This is why you commit *before* you prompt.

### 11:55 (25 min) — Live demo: let an AI wreck the repo, then undo it
Do this for real on the projector:
1. `git commit` a working state
2. Prompt an agent to "improve" `placement_tracker/eligibility.py` — invite
   over-engineering, ask it to "make it more extensible"
3. `git diff` — watch the bloat arrive
4. Run tests — often still green, which is the scary part
5. `git reset --hard HEAD`

> **Green tests do not mean it was a good change.** That is the lesson of the
> whole morning.

### 12:20 (25 min) — The AI trap list
Build it on the board from **their own** examples across three days:

| Trap | Looks like |
|---|---|
| Bloat | 40 lines where 6 would do |
| Invented APIs | a method that does not exist |
| Wrong defaults | `.get(key, 0)` when `None` was meant |
| Over-abstraction | a class hierarchy for one function |
| Confident wrongness | a docstring that contradicts the code (Day 2!) |
| Silent scope creep | you asked for a fix, it rewrote the file |

### 12:45 (15 min) — Everyone commits a clean working state before lunch
They will refactor after lunch. This is the safety net. Check hands.

---

## 13:45–15:15 — MOCK ASSESSMENT (90 min, graded)

### Setup, 5 minutes
- Brief: `day3/mock/BRIEF.md` — project it AND tell them it is in the repo
- **Any AI tool allowed**
- Announce: *"there are hidden tests you cannot see. Re-read the brief —
  every rule in it is tested."*

### Then: silence. Do not help.
Walk the room. Note who reaches for AI before reading the brief — that is your
best viva material at 15:30.

| Time | Call out |
|---|---|
| 13:50 | Start |
| 14:20 | "30 minutes gone. Part A should be done." |
| 14:50 | "40 left. If Part B isn't started, start now." |
| 15:05 | "10 minutes. **Commit what works.**" |
| 15:15 | Stop. Hard stop. |

### Grading
```bash
python3 instructor/grade.py <their>/drive.py
```
Auto-grades 55 marks (visible 35 + hidden 20). You award clean code (10),
git (5) and viva (30) by hand.

> Grade a few during the break so you have real numbers for the debrief.

---

## 15:30–17:00 — Code Defense / Viva

Full format, scoring and question bank: **`instructor/VIVA-RUBRIC.md`**

Two things to get right:

1. **Random selection, announced in the morning.** That is what makes all 60
   students prepare, not just the 15 you call.
2. **Mark honesty UP.** *"The AI wrote this and I don't fully understand it"*
   scores more than a confident bluff. Say so before you begin.

### 16:45 — Debrief, then close
Read out the three best answers you heard and why they were good.

> "Three days ago you could fix a bug if you could see it. Now you can find it,
> explain it, and defend the fix — with or without AI. That last part is what
> gets you hired. The tools will all be different in a year. The method won't."

---

## If you are running behind

| Cut this | Not this |
|---|---|
| The 10:35 refactor pairs | The mock assessment |
| Half the AI trap list | The viva |
| The 11:55 live demo | The 09:30 announcement |

The mock and the viva are the assessment. Everything else is warm-up.
