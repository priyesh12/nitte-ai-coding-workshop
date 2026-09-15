# The 09:30 cold start — highest-risk 10 minutes of the workshop

You cannot contact students beforehand. They arrive with nothing. This page is
the plan for getting 60 cold machines to `18 passing, 16 failing` by 09:40.

---

## Do tonight (10 minutes, non-negotiable)

- [ ] **Push everything and make the repo PUBLIC.** Then check the URL loads in
      a private/incognito window with no login. This is the one thing that
      would sink 09:30 — verify it, don't assume it.
- [ ] **Optional, free, 1 min:** a `tinyurl.com` short link. Nobody types a long
      GitHub URL correctly at 09:31.
- [ ] **Test `python3 serve.py` once** on your laptop so you know it runs. That
      is your no-internet fallback and it needs no USB stick.
- [ ] **Read `instructor/BOARD.md`.** No printing needed — everything students
      need is on the board or in the repo they just downloaded.

> **Nothing to print, nothing to buy.** Public repo + your laptop covers it.

---

## On the board before anyone sits down

```
   tinyurl.com/YOUR-LINK

   git clone <that URL>
   cd nitte-ai-coding-workshop
   python3 check_setup.py

   Stuck 3 min? Raise your hand and pair with a neighbour.
```

That last line is the most important thing on the board. Say it out loud too.

---

## The 09:30 triage

**Your goal is not 60 working laptops. It is 30 working pairs.** Pairing is the
pedagogy anyway — rotating driver/navigator — so a broken laptop costs nothing.

1. **09:30** — everyone starts. You do not help anyone yet. Watch the room.
2. **09:33** — "hands up if `check_setup.py` printed ALL CHECKS PASSED."
   Those students are now your assistants. Send them to raised hands.
3. **09:36** — anyone still stuck **pairs up now**. Not later. Move them
   physically next to a working machine.
4. **09:40** — **start teaching regardless of how many laptops work.**

> Do not debug laptops past 09:40. A student watching their partner drive learns
> more this morning than a student alone with a broken Python install.

---

## No Python — fastest path per OS

| OS | Fastest | Notes |
|---|---|---|
| **Windows** | Microsoft Store → search "Python 3.12" → Install | **No admin rights needed.** This is the fastest path on a locked lab machine, by a distance. |
| **Windows (no Store)** | python.org/downloads | ⚠️ **Tick "Add python.exe to PATH"** on the first screen. Miss it and nothing works. |
| **macOS** | Usually preinstalled. Else `brew install python3` | If `python3` fails, Xcode CLT prompt will offer to install. |
| **Linux** | `sudo apt install python3` | Usually already there. |

**Check:** `python3 --version` (Windows may need `py --version` or `python --version`).

> If a machine has `python` but not `python3`, tell them to use `python` in every
> command today. Write that on the board — it will happen to somebody.

---

## Failure ladder — go down only as far as you must

| Level | Situation | Response |
|---|---|---|
| 1 | Normal | `git clone` from the (public) URL |
| 2 | Git missing | GitHub → green **Code** button → **Download ZIP**. **Git is not needed on Day 1.** |
| 3 | GitHub blocked / no internet | **`python3 serve.py` on your laptop.** It prints an address like `http://192.168.1.7:8000` — write that on the board. Students open it in a browser and download. Same wifi is all it needs; no internet, no USB. |
| 4 | Campus wifi isolates devices | Some networks block laptop-to-laptop. Test `serve.py` from your phone's browser in the room first. If blocked, phone hotspot works for ~8 at a time — enough to seed a few students who then AirDrop/share onward. |
| 5 | No Python, no admin | Windows: **Microsoft Store → Python 3.12**, no admin needed. Or use any online Python runner — the bugs are single-file. |
| 6 | Total disaster, one machine | Project `bug_01` (8 lines) and have them **type it**. Typing it is not wasted time. Then pair. |

---

## Things that will actually happen

| | |
|---|---|
| Someone types the URL wrong 4 times | Short URL. Check their spelling yourself, don't ask. |
| `python3` not found on Windows | Try `py` then `python`. PATH wasn't ticked. |
| Corporate wifi blocks GitHub | `python3 serve.py`. This is why you tested it last night. |
| A student has no laptop at all | Pair them. Say nothing about it. |
| Someone already finished all 6 bugs | Send them to `bugs/tier2`, then have them **write a new bug** for another pair. Writing bugs teaches more than fixing them. |
| Wrong Python — 3.8 on an old lab image | f-strings with `=` need 3.8+, the `list[str]` type hints need 3.10. Bugs 1–6 run on 3.8; only `placement_tracker` needs 3.10. Day 1 is safe either way. |

---

## What "ready" looks like

```
  18 passing   16 failing
```

That is the correct output. Say it before they run it, or twenty hands go up to
report the failures as a problem. **The failures are the workshop.**
