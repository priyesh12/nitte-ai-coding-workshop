# The Sabotage Drill — Day 2, 13:45

Below are four functions **an AI actually produced**, in response to reasonable
prompts. They are clean, commented, idiomatic and well-named.

**Every single one has a bug.**

## Rules

1. **20 minutes, reading only.** No running the code. No AI. Just read.
   Write down every bug you think you've found.
2. Then run `python3 ../../run_tests.py .` and see how you did.
3. Count how many you found by reading versus by testing.

The number is usually humbling. That is the lesson.

## Why this matters for your placement

You will be tempted to paste AI output straight into an assessment. It will
look right. It will pass the sample case they gave you. It will fail the hidden
tests, and you will have no idea why — because you never understood the code.

## The rule that saves you

> **You may not submit a line you cannot explain out loud.**

You are graded on this in the Day 3 viva. Any line you cannot explain is struck
from your submission.

## Debrief questions

1. Which bug was hardest to spot by reading? Why?
2. Every one of these reads *beautifully*. Why does good style make bugs harder
   to see, not easier?
3. What would you have asked the AI to do differently up front?
4. Which of these would have passed a sample test case and failed hidden tests?
