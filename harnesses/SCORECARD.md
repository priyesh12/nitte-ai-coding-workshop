# Harness Rotation Scorecard

**Name(s):** ______________________  **Date:** __________

You will attempt the **same task** at four stations, 20 minutes each. Fill this in
as you go — not afterwards from memory.

> **The task** (same at every station):
> In `placement_tracker`, add a function `students_at_risk(students)` that returns
> every student with `cgpa < 6.0` **or** `backlogs > 0`, sorted by CGPA ascending.
> Then make `tests/visible/test_at_risk.py` pass.

---

## Station scoring

Rate 1–5. Be honest — the bake-off later depends on this being real.

| | Station 1<br>Gemini CLI | Station 2<br>OpenCode | Station 3<br>Aider | Station 4<br>Browser AI |
|---|---|---|---|---|
| Minutes to first working setup | | | | |
| Did it find the right file itself? (Y/N) | | | | |
| Did it run the tests itself? (Y/N) | | | | |
| Could you see the diff before it applied? (Y/N) | | | | |
| Did it respect `AGENTS.md`? (Y/N) | | | | |
| How easy was it to undo a bad edit? (1–5) | | | | |
| Did it work first try? (Y/N) | | | | |
| **Would you use this in an assessment?** (1–5) | | | | |

---

## The seven invariants — find each one

For **each** station, write down where you saw the invariant. If a station
doesn't have one, write "none" — that is a real and interesting answer.

| Invariant | Gemini CLI | OpenCode | Aider | Browser AI |
|---|---|---|---|---|
| 1. Context file | | | | |
| 2. Agent loop visible? | | | | |
| 3. Permission / approval | | | | |
| 4. Diff review | | | | |
| 5. Session state / undo | | | | |
| 6. Provider choice | | | | |
| 7. Extensions (MCP etc.) | | | | |

---

## Debrief questions

**1.** Which station was *fastest*? ______________________

**2.** Which station did you *trust most*, and why? (These are usually different
tools — that gap is the lesson.)

<br><br>

**3.** Station 4 had no file access — you had to paste context by hand. What did
you have to tell it that the others figured out on their own?

<br><br>

**4.** Same model behind stations 1–3. Same task. Different results. **Why?**

<br><br>

**5.** If your placement assessment banned AI tomorrow, which skill from today
would still be worth something?

<br><br>
