# AI-Enabled Coding & Debugging — 18-Hour Curriculum

> Redesign of the source POA into a hands-on, zero-cost, tool-agnostic workshop.
> Audience: CS students preparing for campus placements.

## Design principles

1. **One codebase, three days.** Students live inside `placement_tracker` for all
   18 hours. Day 3 is not a cold start.
2. **Hypothesis before prompt.** The house rule for all three days. You may use AI
   at any time — but you must write down what you think is wrong *first*.
3. **Tool-agnostic.** We teach the seven invariants every AI harness shares, not
   one vendor's UI. Students should be able to pick up harness #151 from its README.
4. **Zero cost.** Every exercise has a free path. No credit card, ever.
5. **You own every line.** Nothing gets submitted that the student cannot explain
   out loud. This is graded on Day 3.

## The house rule

```
   ┌──────────────────────────────────────────────┐
   │  1. Reproduce   — make it fail on demand     │
   │  2. Hypothesize — write it down, on paper    │
   │  3. Isolate     — prove which line           │
   │  4. Fix         — smallest possible change   │
   │  5. Verify      — tests green, nothing broke │
   └──────────────────────────────────────────────┘
        AI is allowed at any step — AFTER step 2.
```

Step 2 is the whole workshop. An engineer who prompts before thinking gets a
plausible answer to the wrong question, and cannot defend it in a viva.

---

## Day 1 — UNDERSTAND

**Goal:** Fix broken code systematically. AI is a tutor, not a mechanic.

| Time | Module | What actually happens |
| --- | --- | --- |
| 09:30–11:00 | Code Execution & Common Bugs | Live Bug Hunt #1. The debugging loop. Tier 0–1 bugs, no AI — these must be reflex, because most placement OAs ban AI. Pairs, rotating driver. |
| 11:30–13:00 | Stack Traces & Print Logging | Anatomy of a traceback (read it bottom-up). `print` → `repr` → `breakpoint()`. Live Bug Hunt #2. Tier 2 bugs. |
| 13:45–15:15 | **AI as Explainer** | First AI contact. Allowed prompts: *explain this traceback*, *what does this line do*, *what does this error mean*. Banned: *fix it*. Students discover AI is a better teacher than it is a mechanic. |
| 15:30–17:00 | Hands-on Debugging Practical | Timed, graded. 4 broken programs. Hypothesis written **before** any AI use. Scored on hypothesis accuracy AND fix minimality, not just green tests. |

**Why AI enters at 13:45 and not 09:30:** students need to fail at reading a
traceback *once* before they will respect the skill. Then AI becomes the thing
that explains what they just struggled with — which is when it actually teaches.

## Day 2 — DELEGATE

**Goal:** Drive any AI harness competently, and distrust its output on reflex.

| Time | Module | What actually happens |
| --- | --- | --- |
| 09:30–11:00 | The Seven Invariants + `AGENTS.md` | Every harness is the same seven primitives. Write ONE `AGENTS.md`, then watch three different tools obey it. Provider vs harness — one free key, many tools. |
| 11:30–13:00 | **Harness Rotation** | 4 stations, *identical* task, 20 min each, pairs rotate, scorecard filled in. Comparing, not learning four things. |
| 13:45–15:15 | **The Sabotage Drill** | Students are given AI output that is clean, commented, idiomatic — and subtly wrong. Nobody finds it by reading. They find it by testing. Then: using AI to generate test cases instead of solutions. |
| 15:30–17:00 | Cold Start + Bake-Off | Unknown harness, README only, 15 minutes. Then: same bug, four harnesses, race. The winner is always the best decomposer, not the best tool. |

### The seven invariants

| # | Invariant | Seen as |
| --- | --- | --- |
| 1 | Context file | `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `copilot-instructions.md` |
| 2 | The agent loop | prompt → plan → read/edit/bash → test → iterate |
| 3 | Permission model | what runs without asking you |
| 4 | Diff review | the only real quality gate |
| 5 | Session state | resume, fork, checkpoint — and `git` as universal undo |
| 6 | Provider routing | BYO key; one key unlocks many harnesses |
| 7 | Extension surface | MCP, custom commands, subagents |

Know these seven and any new harness is a ten-minute README read. That is the
placement-proof skill, and a strong interview answer.

## Day 3 — DELIVER

**Goal:** Ship end-to-end under time pressure, then defend every line.

| Time | Module | What actually happens |
| --- | --- | --- |
| 09:30–11:00 | Clean Code & the Dev Loop | Naming, modular functions, when a comment is a code smell. Write → Test → Refactor-with-AI → Verify. Refactor a Day 1 fix and keep tests green. |
| 11:30–13:00 | Git as the AI Safety Net | Commit before you let an agent touch anything. `git diff` as the review surface. `git reset --hard` as the undo. AI traps: bloat, invented APIs, over-engineering. |
| 13:45–15:15 | **Mock Assessment** | Timed, end-to-end: one feature + three bugs in `placement_tracker`, hidden tests, auto-graded. Any tool allowed. |
| 15:30–17:00 | **Code Defense / Viva** | Students present. Line-by-line justification, complexity, edge cases, "why this approach". Scored on the rubric. Any line they cannot explain is struck. |

---

## Rituals

### Bug Hunt (3× per day, 20 min, on the projector)

1. Push the bug live — nobody has seen it
2. **90 seconds silent reading.** No running code. Everyone writes one hypothesis
3. **Collect three *wrong* hypotheses first** — this kills the fear of being wrong
   in a room, which is the #1 reason students freeze in interviews
4. A student drives. Reproduce → isolate → fix
5. Post-mortem: *What was the smallest fix?* *How could you have caught this in 10s?*

Step 5 matters more than the fix. Placement tests reward exact minimal fixes;
students reflexively rewrite whole functions.

### Scoreboard

`python -m pytest` points, running across all three days. Hidden tests are run by
the instructor at the end of each practical. Bonus points for a correct hypothesis
recorded *before* the fix.

---

## Bug difficulty ladder

| Tier | Time | Examples |
| --- | --- | --- |
| 0 — warm-up | 2–3 min | `IndentationError`, `str + int`, typo'd name |
| 1 — classic | 5–8 min | boundary `>` vs `>=`, mutable default arg, mutating a list while iterating, `/` vs `//` |
| 2 — sneaky | 10–15 min | `is` vs `==`, float equality, shallow copy, late-binding closure, silent `.get()` default |
| 3 — multi-hop | 15–25 min | state corrupted two functions upstream, bare `except` swallowing the real error, wrong `sort(key=)`, recursion base case |
| 4 — boss | 25–40 min | fails only a hidden test; an O(n²) that times out; and **one where the test itself is wrong** |

That last one is deliberate. A student who says *"the spec is ambiguous, here's my
reading and why"* has just won an interview.
