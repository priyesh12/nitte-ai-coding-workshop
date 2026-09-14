# The AI trap checklist

Every trap here came out of this workshop, from real AI output.

## The rule

> **You may not submit a line you cannot explain out loud.**
>
> Graded in the Day 3 viva. Any line you cannot explain is struck from your
> submission — it scores zero even if the tests pass.

---

## The six traps

### 1. Bloat
40 lines where 6 would do. Helper functions called once. Config for a thing
with one setting.
**Catch it:** *"could I write this in half the lines?"* Usually yes.

### 2. Invented APIs
A method that does not exist, on a class that does, with a plausible name.
**Catch it:** run it. Hallucinated APIs fail instantly — this is the *easiest*
trap to catch and the one people worry about most.

### 3. Wrong defaults
```python
student.get("cgpa", 0.0)   # returns None if the key EXISTS as None
```
**Catch it:** test with `None`, `0`, `""`, and `[]` — not just a missing key.

### 4. Over-abstraction
A base class and two subclasses for something used once.
**Catch it:** *"how many places call this?"* If the answer is one, delete the
abstraction.

### 5. Confident wrongness ← the dangerous one
A perfect docstring above code that does something else.
```python
def paginate(students, page, per_page=10):
    """Pages are 1-indexed, so page 1 returns the first per_page students."""
    start = page * per_page      # page 1 starts at index 10. It lied.
```
**Catch it:** read the docstring, then read the code, then ask whether they
actually agree. They often do not.

### 6. Silent scope creep
You asked it to fix one function. It reformatted the file, renamed three
variables and "improved" an unrelated method.
**Catch it:** `git diff`. Always. Before you accept anything.

---

## Why good style makes bugs harder to see

Every trap above arrived with a clean name, a full docstring and tidy
formatting. **Beautiful code lowers your guard.**

You skim clean code. You scrutinise ugly code. AI output is *always* clean —
so your guard is *always* down. That is the whole risk in one sentence.

---

## Your 60-second review

Before accepting any AI-generated code:

- [ ] **Read every line.** Every one.
- [ ] **Does the docstring match the code?**
- [ ] **`git diff`** — did it touch anything I didn't ask about?
- [ ] **Run the tests.** Not just the happy path.
- [ ] **Test the boundary.** Exactly-at-the-limit values.
- [ ] **Test empty.** `[]`, `""`, `None`, `0`.
- [ ] **Could this be shorter?**
- [ ] **Can I explain every line out loud?** ← if no, you cannot submit it

## The safety net

```bash
git add -A && git commit -m "working: tests green"   # BEFORE you prompt
git diff                                             # review what it did
git reset --hard HEAD                                # undo everything
```

**Commit before you prompt.** Then any AI change is one command away from gone.
