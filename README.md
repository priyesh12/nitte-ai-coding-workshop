# AI-Enabled Coding and Debugging for Corporate Placement

An 18-hour (3 × 6h) workshop for CS students preparing for campus placements.
**Day 1 needs nothing but Python 3.10+ — no pip, no accounts, no internet.**

## Start here

```bash
python3 check_setup.py            # 10 seconds, tells you what's missing
python3 run_tests.py bugs/tier0   # your first broken programs
```

You should see failing tests. **The failures are the workshop.**

## The house rule

```
1. Reproduce   2. Hypothesise   3. Isolate   4. Fix   5. Verify
              ^ ON PAPER, BEFORE YOU ASK AI
```

You may use AI at any step — **after step 2**. Prompting before you think gets a
confident answer to the wrong question, and you won't be able to defend it.

## Layout

| Path | What's in it |
| --- | --- |
| [CURRICULUM.md](CURRICULUM.md) | The full 18-hour plan, all three days |
| [bugs/](bugs/) | 10 broken programs, tier 0 (2 min) → tier 4 (40 min) |
| [placement_tracker/](placement_tracker/) | The spine codebase — Days 2 & 3 live here |
| [day2/sabotage/](day2/sabotage/) | AI output that looks perfect and isn't |
| [day3/mock/](day3/mock/) | The timed mock assessment + brief |
| [handouts/](handouts/) | Traceback anatomy, prompt templates, AI traps, hypothesis sheet |
| [harnesses/](harnesses/) | The zero-cost AI tool lab and rotation scorecard |
| [slides/](slides/) | 12 decks — one per 90-min session, 211 slides. Open `slides/index.html`. Works offline. |
| [AGENTS.md](AGENTS.md) | Rules for any AI agent in this repo (invariant #1) |
| [run_tests.py](run_tests.py) | Tiny stdlib test runner. No pytest needed. |

> `instructor/` — run sheets, answer keys, hidden tests and the grader — is
> deliberately **not** in this repo. Students clone this.

## The three days

| Day | Theme | Goal |
| --- | --- | --- |
| 1 | **UNDERSTAND** | Debug systematically. AI as a tutor, not a mechanic. |
| 2 | **DELEGATE** | Drive any AI harness, and distrust its output on reflex. |
| 3 | **DELIVER** | Ship end-to-end under time pressure, then defend every line. |

Sessions run 09:30–11:00, 11:30–13:00, 13:45–15:15, 15:30–17:00.

Source plan: [`18-Hour Workshop POA - AI-Enabled Coding & Debugging.pdf`](./18-Hour%20Workshop%20POA%20-%20AI-Enabled%20Coding%20%26%20Debugging.pdf)

## Running things

```bash
python3 run_tests.py                        # everything
python3 run_tests.py bugs/tier1             # one tier
python3 run_tests.py bugs/tier0/test_bug_01_greeting.py   # one file
```

## For Day 2 (not needed tomorrow)

**One free Google AI Studio key** unlocks most open-source harnesses — that is
the only thing you need. Step-by-step: [harnesses/GET-YOUR-KEY.md](harnesses/GET-YOUR-KEY.md).
Do it on Day 1 evening; Day 2 depends on it.
