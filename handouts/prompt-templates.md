# Prompt templates

Works in any harness — CLI, IDE, or a browser chat. **The template is the
skill; the tool is not.**

## The rule

> **Hypothesis first.** Never prompt before you can say what you think is wrong.
> Otherwise you get a confident answer to the wrong question — and you cannot
> defend it in a viva.

---

## 1. Explain an error *(Day 1 — your safest AI use)*

```
Here is a Python traceback:

<paste the WHOLE traceback>

And here is the function it points at:

<paste the function>

Explain what this error means and what usually causes it.
Do NOT fix it — I want to find the bug myself.
```

`Do NOT fix it` matters. Without it you get a rewrite and learn nothing.

## 2. Understand unfamiliar code

```
Explain what this function does, step by step, for someone who has
never seen this codebase.

<paste the function>

Then tell me: what input would make it behave unexpectedly?
```

The second question is the valuable one.

## 3. Ask for a function *(be this specific)*

```
Write a Python function with this exact signature:

    def students_at_risk(students: list[Student]) -> list[Student]:

Behaviour:
- return students with cgpa < 6.0 OR backlogs > 0
- sort by cgpa ascending (worst first)
- do NOT modify the input list
- empty input returns []

Constraints:
- standard library only, no pip packages
- Python 3.10+
- the Student dataclass already exists - do not redefine it

Example:
  input:  [Student("1","Asha","CSE",9.0,0), Student("2","Bee","CSE",5.5,0)]
  output: [Student("2","Bee","CSE",5.5,0)]
```

**Why this works:** exact signature, explicit edge cases, stated constraints,
and a worked example. That is four separate ways of stopping it inventing things.

## 4. Generate tests — the highest-value prompt you know

```
Write edge-case tests for this function. Do NOT change the implementation.

<paste the function>

Cover: empty input, single element, boundary values, duplicates,
and anything that would break it.
Use plain asserts - no pytest, no imports beyond the standard library.
```

> Tests are **cheap to verify** and expensive to write. Code is the opposite.
> This is the best trade you can make with an AI.

## 5. Review before you trust

```
Review this function against its docstring.
List anything where the behaviour and the docstring disagree.
Do not rewrite it - just list the discrepancies.
```

This one catches Day 2's `paginate` bug. The docstring lied.

## 6. Complexity — rehearsal for your viva

```
What is the time and space complexity of this function?
Point at the specific line that dominates.
What breaks first if the input is 5000 items instead of 5?
```

---

## Prompts that get you into trouble

| Don't say | Because |
|---|---|
| "fix this" | You get a rewrite and learn nothing |
| "make it better" | It over-engineers — "better" is undefined |
| "write a function to process students" | Vague in, hallucinated out |
| "is this correct?" | It will usually just agree with you |
| "optimise this" | You get cleverness you cannot explain in a viva |

## The checklist

Before you send it:

- [ ] Did I write my hypothesis first?
- [ ] Did I give the exact function signature?
- [ ] Did I state the edge cases?
- [ ] Did I say what NOT to do (no pip, don't rewrite)?
- [ ] Did I include a worked example?

After you get it back:

- [ ] Did I read every line?
- [ ] Can I explain every line **out loud**?
- [ ] Did I run the tests?
- [ ] Did I test the edge cases myself, not just the happy path?
