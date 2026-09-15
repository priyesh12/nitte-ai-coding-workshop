# Day 1 answer key — INSTRUCTOR ONLY

> Do not commit this to the branch students clone, or do — it is more useful
> that they *can* peek and choose not to. Your call.

---

## bug_01 — greeting (Tier 0, ~2 min)
**Root cause:** missing `:` at the end of `def greet(name, company)`
**Minimal fix:** add one colon.
**Teaching point:** `SyntaxError` means the file never ran *at all*. The caret
`^` points at where the parser gave up — which is often one character *after*
the real mistake.

## bug_02 — average (Tier 0, ~3 min)
**Root cause:** `len(cgpa)` uses the loop variable instead of the list `cgpas`.
**Minimal fix:** `len(cgpas)`.
**Teaching point:** `TypeError: object of type 'float' has no len()` names the
*type* — a float where a list was expected. Reading the type tells you the fix.
**Follow-up to ask:** "what does `average_cgpa([])` do?" → `ZeroDivisionError`.
Nobody guards it. Bridge to edge cases.

## bug_03 — eligible (Tier 1, ~6 min) ★ highest value
**Root cause:** `cgpa > 7.0` should be `cgpa >= 7.0`. The spec says
"7.0 **or above**".
**Minimal fix:** one character.
**Teaching point:** the code reads correctly in English; only a **boundary test**
catches it. Draw the number line, open vs closed circle at 7.0.
**Say out loud:** boundary/off-by-one is the most common cause of hidden-test
failures in screening assessments.

## bug_04 — toppers (Tier 1, ~8 min)
**Root cause:** `students.remove(student)` mutates the list *while iterating it*.
The iterator advances by index, so the element after each removal is skipped.
**Minimal fix:** build a new list —
`return [s for s in students if s["placed"]]`
**Teaching point:** passes the 1-unplaced test, fails on two adjacent unplaced.
**This is your visible-vs-hidden-test lesson.** One green test proves nothing.
**Demo:** add `print(student["name"])` inside the loop — Chetan is never visited.

## bug_05 — register (Tier 2, ~12 min)
**Root cause:** mutable default argument. `drive=[]` is evaluated **once**, at
function definition, so every call shares one list.
**Minimal fix:**
```python
def register(name, drive=None):
    if drive is None:
        drive = []
```
**Teaching point:** state leaking between calls that look independent. Classic
Python interview question — worth memorising as a pattern.
**Demo:** `print(register.__defaults__)` between calls. It visibly grows.

## bug_06 — cutoff (Tier 2, ~15 min)
**Root cause:** `==` on floats. `6.9 + 0.4` is `7.300000000000001`.
**Minimal fix:** `abs(cgpa - 7.3) < 1e-9`
**Better fix:** don't use floats for marks at all — integers, or `Decimal`.
**Teaching point:** `print(x)` shows `7.3`; `print(repr(x))` shows the truth.
Make the room see those two lines differ.
**Note:** 7.5 is exactly representable in binary and would NOT have broken —
the cut-off being 7.3 is deliberate. Mention it if a sharp student asks.
**Interview-grade question:** *"tolerance, or never use floats for marks?"*
Both defensible. Say so — real engineering has more than one right answer.

---

## Reading the room

| Signal | Meaning | Action |
|---|---|---|
| Fixed in 30s, can't explain why | Pattern-matched, didn't reason | Make them explain. No credit without it. |
| Rewrote the whole function | Avoiding the diagnosis | "Revert. Now fix it in one line." |
| Stuck >10 min on tier 0/1 | Reading tracebacks, not parsing them | Sit with them. Read it bottom-up, out loud, together. |
| Silent pair | One person has the keyboard | Enforce the 10-minute driver swap. |
