# Day 2 run sheet — DELEGATE

**Goal:** drive any AI harness competently, and distrust its output on reflex.

> **09:30 reality check.** Some students will not have a key despite last
> night's homework. Do not spend the morning fixing that — **pair them
> immediately** with someone who has one. One key per pair is plenty, and
> driver/navigator is better practice anyway.


## Slide decks

One deck per session. Open `slides/index.html`, or go straight to:

| Session | Deck | Slides |
|---|---|---|
| 09:30–11:00 | [`day2-s1.html`](../../slides/day2-s1.html) | 19 |
| 11:30–13:00 | [`day2-s2.html`](../../slides/day2-s2.html) | 14 |
| 13:45–15:15 | [`day2-s3.html`](../../slides/day2-s3.html) | 20 |
| 15:30–17:00 | [`day2-s4.html`](../../slides/day2-s4.html) | 14 |

Press `F` for fullscreen. Arrows or space to advance. Works offline.

---

## 09:30–11:00 — The Seven Invariants + AGENTS.md

### 09:30 (10 min) — Key check
"Hands up if `echo $GEMINI_API_KEY` prints something." Pair the rest **now**.
Write pairs on the board so nobody drifts.

### 09:40 (25 min) — There are 150+ of these tools
Project `harnesses/README.md`. Name them: OpenCode, Aider, Pi, oh-my-pi, Goose,
Crush, Plandex, Codex CLI, Gemini CLI, Cline, Continue, Cursor, Claude Code —
plus orchestrators that run *fleets* of them.

> **The point is not the tools.** It is: there are 150+, they ship weekly, and
> they are all the same seven primitives. **Do not memorise tools. Learn the
> primitives.** Say this twice.

Then teach the seven (slide 5–6):
context file · agent loop · permissions · diff review · session state ·
provider routing · extensions

### 10:05 (20 min) — Harness vs provider
Draw it on the board:
```
   HARNESS (on your laptop)  ---->  PROVIDER (the model)
   OpenCode / Aider / Gemini CLI    Google AI Studio (free)
```
> **This is why today is free.** One key, many tools. Invariant #6 is not
> theory — it is the reason you can afford to be here.

### 10:25 (30 min) — The AGENTS.md demo ★ the money moment
1. Open `AGENTS.md` on the projector. Read rule 2 aloud: *standard library only*.
2. Ask a harness: *"add a function to reports.py that reads a CSV of students"*
3. Watch it **not** reach for pandas.
4. Now edit `AGENTS.md`, delete that rule, ask again. It reaches for pandas.
5. Point at `CLAUDE.md` — same content, different filename, because the
   ecosystem hasn't converged.

> One file changed the behaviour of a tool you did not configure. **That is
> invariant #1**, and it is the highest-leverage thing you will learn today.

---

## 11:30–13:00 — Harness Rotation

### The setup
Four stations, **identical task**, 20 minutes each, pairs rotate.
Task and scorecard: `harnesses/SCORECARD.md`. Target: `tests/visible/test_at_risk.py`.

| Station | Harness |
|---|---|
| 1 | Gemini CLI |
| 2 | OpenCode |
| 3 | Aider |
| 4 | Browser AI (paste by hand) |

> **Ring a bell every 20 minutes.** Hard rotation. Unfinished is fine — the
> comparison is the deliverable, not the working function.

### What you are steering toward
- Station 4 has no file access, so they must paste context **by hand**. They
  feel invariant #1 physically.
- Stations 1–3 can use the **same model**. Different results anyway. Why?
  Because the harness — how it gathers context, when it runs tests, what it
  shows you — matters as much as the model.

### 12:50 (10 min) — Fill in the debrief questions properly
Question 4 is the one that matters: *same model, same task, different results —
why?*

---

## 13:45–15:15 — The Sabotage Drill ★ the best session of the workshop

### 13:45 (20 min) — Reading only
Open `day2/sabotage/ai_output.py`. Tell them honestly: **an AI wrote this, and
every function has a bug.** 20 minutes, **no running the code, no AI**. Write
down every bug you find.

> Do not tell them how many bugs there are. Four functions, four bugs.

### 14:05 (10 min) — Collect findings on the board
Most rooms find **one**, usually the mutation. Let that land before moving on.

### 14:15 (15 min) — Now run the tests
```bash
python3 run_tests.py day2/sabotage
```
Six failures, four bugs:

| Function | Bug |
|---|---|
| `calculate_percentage` | accepts `placed > total` — 250% is not "handled" |
| `paginate` | 0-indexed despite a docstring promising 1-indexed |
| `get_cgpa` | `.get("cgpa", 0.0)` never fires when the key exists as `None` |
| `merge_skill_lists` | `.extend()` mutates the caller's list |

### 14:30 (20 min) — Why good style hides bugs
This is the real content. Every one of these has a clean name, a full docstring,
and type-appropriate logic. **The docstring on `paginate` is a lie**, and the
lie is what makes you skip reading the code.

> Beautiful code lowers your guard. That is exactly what makes AI output
> dangerous — it is *always* beautiful.

### 14:50 (25 min) — Use AI to generate tests, not solutions
Flip it. Ask a harness: *"write edge-case tests for this function"* — do not
let it touch the implementation.

> This is the single highest-value AI habit for placements. **Tests are cheap
> to verify and expensive to write.** Code is the opposite.

---

## 15:30–17:00 — Cold Start + Bake-Off

### 15:30 (35 min) — Cold Start ★
Hand them a harness **nobody taught them** — Goose, Crush, or Plandex. README
only. 15 minutes to install, point it at their free key, and complete a small task.

> **This is the actual skill.** You cannot be taught 150 tools. You can learn to
> onboard yourself onto any of them. That is also a genuinely great answer to
> *"how do you pick up new technology?"* — and you will be asked.

Expect maybe half to succeed. That is a fine outcome. Debrief what blocked them:
it is almost always provider config, i.e. invariant #6.

### 16:05 (35 min) — The Bake-Off
Same bug (use a tier 3 bug they have not seen), four harnesses, pairs race.
Board: harness, time, and **did it work first try**.

### 16:40 (20 min) — The reveal
Correlate the winners against the harness they used. **There is no correlation.**
The winners are the pairs who decomposed the problem before prompting.

> **The tool is not the skill. You are the skill.**

### 16:55 — Close
> "Tomorrow you build something end-to-end and defend every line of it. Any
> line you cannot explain gets struck from your submission. Bring your Day 1
> hypothesis sheets."

**Homework:** none. They will be tired. Tomorrow is the heavy day.
