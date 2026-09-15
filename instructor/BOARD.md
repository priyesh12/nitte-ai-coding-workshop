# What goes on the whiteboard — no printing needed

You have no printer. Everything students need is either on the board (below),
on the projector (the `handouts/` files — open them in your editor and zoom),
or in the repo they just downloaded.

---

## BOARD 1 — up before anyone sits down. Leave it all day.

```
   github.com/<you>/nitte-ai-coding-workshop

   git clone <that URL>
   cd nitte-ai-coding-workshop
   python3 check_setup.py
   python3 run_tests.py bugs

   Expect:  18 passing, 16 failing
   The failures ARE the workshop.

   No git?  Green "Code" button -> Download ZIP
   Stuck 3 min?  Hand up, pair with a neighbour.
```

> Optional, 1 minute, free: make a `tinyurl.com` short link. Nobody types a
> long GitHub URL correctly at 09:31.

---

## BOARD 2 — the loop. This stays up for all three days.

```
   1. REPRODUCE    make it fail on demand
   2. HYPOTHESISE  write it down  <-- ON PAPER
   3. ISOLATE      prove which line
   4. FIX          smallest possible change
   5. VERIFY       green, nothing else broken

   AI allowed from step 3. NOT before.
```

---

## BOARD 3 — the hypothesis format (students copy onto their own paper)

No printed sheet needed. Tell them: *"Fold a page in half, copy these five
lines, one bug per half-page."*

```
   BUG # ____

   1. Expected:
   2. Actually got:
   3. My hypothesis:        <-- BEFORE any AI
   4. Fix (lines changed: __):
   5. Was I right?  Y / partly / N
```

---

## BOARD 4 — scoring. Write this BEFORE the 15:30 practical.

```
   Tests green ................ 4
   Hypothesis was correct ..... 3
   Fix was minimal ............ 2
   Explained it out loud ...... 1
                                --
                                10

   You can score 6/10 without fixing anything.
```

> Say it out loud: **interviewers hire the reasoning, not the keystrokes.**

---

## BOARD 5 — traceback anatomy. Draw at 11:30.

```
   Traceback (most recent call last):
     File "run_tests.py", line 42        <- 3. how you got here
     File "bug_02.py", line 12           <- 2. WHERE
       return total / len(cgpa)
   TypeError: object of type 'float' has no len()
                                         <- 1. WHAT  ** START HERE **

   READ IT BOTTOM-UP.
```

Then the three print tricks:
```
   print(f"{cgpa=}")     name AND value
   print(repr(cgpa))     the TRUTH (7.300000000000001)
   breakpoint()          stop here; n / c / q
```

---

## BOARD 6 — 13:45, the AI rules.

```
   ALLOWED                      BANNED
   "explain this traceback"     "fix it"
   "what does this line do"     "write this for me"
   "what does this error mean"
   "give me 3 edge cases"
```

---

## BOARD 7 — 16:55, homework. Everyone does it in the room.

```
   https://aistudio.google.com/apikey

   1. Sign in with any Google account
   2. Create API key -> Copy
   3. Mac/Linux:  echo 'export GEMINI_API_KEY="KEY"' >> ~/.zshrc
      Windows:    setx GEMINI_API_KEY "KEY"   (then reopen terminal)
   4. Check:  echo $GEMINI_API_KEY

   Day 2 does not work without this.
```

Full instructions with troubleshooting are in their repo at
`harnesses/GET-YOUR-KEY.md` — tell them that, and project it while they work.

---

## Project, don't print

**Open `slides/index.html`** — it lists every deck. One deck per 90-minute
session, so Day 1 is `day1-s1` through `day1-s4`. Press `F` for fullscreen,
arrows or space to advance. No internet, no install.

| Session | Deck | Slides |
|---|---|---|
| 09:30–11:00 | `day1-s1.html` | 29 |
| 11:30–13:00 | `day1-s2.html` | 24 |
| 13:45–15:15 | `day1-s3.html` | 15 |
| 15:30–17:00 | `day1-s4.html` | 15 |

| Instead of printing | Do this |
|---|---|
| Traceback handout | `day1-s2.html`, or `handouts/reading-a-traceback.md` on screen |
| Hypothesis sheet | Board 3 above — they copy it onto their own paper |
| Scoring | `day1-s4.html` |
| Key setup | end of `day1-s4.html`, or `harnesses/GET-YOUR-KEY.md` |

They all have the repo. Anything you'd have printed, they can already read.
