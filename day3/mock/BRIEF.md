# Mock Assessment — 90 minutes

> Modelled on an entry-level corporate technical round. Read the whole brief
> before you write anything. **You have 90 minutes.**

## The scenario

The placement cell needs a **company eligibility report**. You are extending
`placement_tracker`, which you already know from Days 1 and 2.

## Part A — Fix 2 bugs (30 min)

`python3 run_tests.py day3/mock` fails. Two of those failures are pre-existing
bugs in `day3/mock/drive.py`. Find and fix them.

**Minimal fixes.** Do not rewrite functions.

## Part B — Build the feature (45 min)

Add `generate_drive_report(students, criteria)` to `day3/mock/drive.py`.

```
generate_drive_report(students, criteria) -> dict
```

Return a dict with exactly these keys:

| Key | Type | Meaning |
|---|---|---|
| `company` | `str` | from `criteria.company` |
| `eligible` | `list[str]` | names of eligible students, **best first** |
| `rejected` | `list[dict]` | `{"name": str, "reason": str}` for each rejected student |
| `eligible_count` | `int` | how many are eligible |
| `eligibility_rate` | `float` | percent eligible, rounded to 2 decimals |

**Rules**
- "Best first" = highest CGPA, then fewest backlogs, then roll number
- `reason` is the **first** criterion the student fails
- Empty student list → rate is `0.0`, not a crash
- The input list must **not** be modified

You may use anything already in `placement_tracker/`. Reuse beats rewriting.

## Part C — Commit your work (15 min)

```bash
git add -A
git commit -m "Add drive report and fix eligibility bugs"
```

Commit **before** you let any AI refactor. That is your undo button.

## Rules

- **Any AI tool allowed.** Use everything you learned yesterday.
- **You must be able to explain every line.** You will be asked, this afternoon,
  in front of the room. Any line you cannot explain is **struck from your
  submission** — it scores zero even if the tests pass.

## How you are graded

| | Marks |
|---|---|
| Part A — both bugs fixed, minimally | 15 |
| Part B — visible tests pass | 20 |
| Part B — **hidden tests** pass | 20 |
| Clean code — naming, no dead code, no bloat | 10 |
| Git — committed working state before refactoring | 5 |
| **Viva — explaining your own code** | **30** |
| | **100** |

> **30 marks are for explaining it.** That is not padding. In a real interview
> it is closer to 100%.

## Hidden tests

There are hidden tests you cannot see — exactly like a real assessment. They
check the things the brief mentions but the visible tests do not.

Re-read the brief. Every rule above is tested.
