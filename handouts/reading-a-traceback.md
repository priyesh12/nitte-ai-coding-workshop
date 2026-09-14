# Reading a traceback

## Read it BOTTOM-UP

```
Traceback (most recent call last):          <- ignore this line
  File "run_tests.py", line 42, in main     <-  3. how you got there
  File "bug_02_average.py", line 12         <-  2. WHERE it broke
    return total / len(cgpa)                <-     the actual line
TypeError: object of type 'float' has no len()
   ^^^^^^^^^                                 <-  1. WHAT went wrong  ← START HERE
```

1. **Last line = what.** The error type and message.
2. **Line above = where.** File and line number. Click it.
3. **Frames above = how.** The call chain that got you there.

> Students read tracebacks top-down, panic at the wall of text, and paste the
> whole thing into AI. Read the last line first. Usually that is enough.

## What the common ones actually mean

| Error | Plain English | Look for |
|---|---|---|
| `SyntaxError` | Python couldn't even read your file | Missing `:` `)` `"`. Check the line **above** the caret too. |
| `IndentationError` | Spacing is inconsistent | Mixed tabs and spaces |
| `NameError` | You used a name that doesn't exist | Typo, or used before defined |
| `TypeError` | Wrong kind of thing | `str + int`, calling a non-function, `len()` of a number |
| `AttributeError` | That object has no such `.thing` | Typo in method name, or it's `None` |
| `IndexError` | List index past the end | Off-by-one, `range(len(x)+1)` |
| `KeyError` | Dict has no such key | Use `.get()` — but mind the default |
| `ZeroDivisionError` | Divided by zero | Empty list, unguarded `len()` |
| `ValueError` | Right type, impossible value | `int("abc")` |

## The caret lies (a little)

```python
def greet(name, company)
                        ^
SyntaxError: expected ':'
```
The caret shows where the parser **gave up**, not always where you went wrong.
For `SyntaxError`, always check the line **above** as well.

## Three print techniques

```python
print(f"{cgpa=}")     # prints:  cgpa=7.3       (name AND value - use this one)
print(repr(cgpa))     # prints:  7.300000000000001   (the TRUTH)
breakpoint()          # stops here. type: n (next) c (continue) q (quit)
```

**`repr()` is the one that finds bugs `print()` hides.** `print(7.300000000000001)`
shows you `7.3`. It is lying to you to be helpful.

## No traceback does NOT mean no bug

The worst bugs don't crash. They quietly produce the wrong answer — the wrong
students shortlisted, the wrong average. **A green test proves the test passed,
not that the code is right.**

Always ask: *what input would break this?*
- empty list
- exactly on the boundary
- duplicates
- negative numbers
- one element

## The loop

```
1. Reproduce   - make it fail on demand
2. Hypothesise - WRITE IT DOWN, on paper
3. Isolate     - prove which line
4. Fix         - smallest possible change
5. Verify      - green, and nothing else broke
```

AI is allowed at any step — **after step 2**. Prompting before you think gets
you a confident answer to the wrong question, and you will not be able to
defend it when someone asks why.
