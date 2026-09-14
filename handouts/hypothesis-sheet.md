# Hypothesis sheet

**Name(s):** ________________________________  **Pair #:** ______

> Fill in **1–3 before you run anything and before you ask any AI.**
> You score more for a correct hypothesis than for a green test. That is not a
> typo — it's the point of the day.

---

## Bug ____________________

**1. What I expected to happen**

<br><br>

**2. What actually happened** *(copy the last line of the traceback, or the wrong output)*

<br><br>

**3. My hypothesis — what I think is broken and why** ← WRITE THIS BEFORE AI

<br><br><br>

**4. How I proved it** *(the print / breakpoint / test that confirmed it)*

<br><br>

**5. The fix** *(how many lines did you change? fewer is better)*

Lines changed: ______

<br><br>

**6. Was my hypothesis right?**   ☐ Yes   ☐ Partly   ☐ No — it was actually:

<br><br>

**7. How could I have caught this in 10 seconds?**

<br><br>

---

## Scoring (out of 10)

| | Marks | Yours |
|---|---|---|
| Tests green | 4 | |
| **Hypothesis was correct** | 3 | |
| **Fix was minimal** (no rewrites) | 2 | |
| Explained it out loud | 1 | |
| | **/10** | |

> **You can score 6/10 without fixing anything**, if your reasoning is right.
> Interviewers hire the reasoning, not the keystrokes.

---

## The loop

```
1. Reproduce   - make it fail on demand
2. Hypothesise - WRITE IT DOWN  <- you are here
3. Isolate     - prove which line
4. Fix         - smallest possible change
5. Verify      - green, and nothing else broke
```

**AI is allowed from step 3 onward.** Not before.
