# AI Harnesses — the zero-cost lab

> **Nobody pays for anything in this workshop.** Every station below is free.
> No credit card is required at any point.

## The one idea that makes this free

Most AI coding tools are **harnesses**, not models. The harness is the program on
your machine — it reads files, runs commands, applies edits. The **provider** is
the API it talks to. They are separate, and almost every open-source harness lets
you bring your own.

```
   ┌─────────────┐        ┌──────────────────────┐
   │  HARNESS    │ ─────▶ │  PROVIDER (the model) │
   │  OpenCode   │        │  Google AI Studio     │
   │  Aider      │        │  (free tier, no card) │
   │  Gemini CLI │        │                       │
   └─────────────┘        └──────────────────────┘
        ^ different UIs          ^ ONE free key
```

**So: get one free Google AI Studio API key, and it unlocks three of the four
stations.** That is invariant #6 from the curriculum, and you are about to learn
it by needing it.

## Before Day 2 — one thing only

**A free Google AI Studio API key.** Step-by-step: [`GET-YOUR-KEY.md`](GET-YOUR-KEY.md)

That's it. No other accounts, no card, nothing to install in advance.

## The four rotation stations

| # | Harness | What makes it different | How it's free |
| --- | --- | --- | --- |
| 1 | **Gemini CLI** | Google's own terminal agent. Best free tier of anything, works with just a Google login. **The universal baseline — if all else fails, this works.** | Free tier, no card |
| 2 | **OpenCode** | Open source, provider-agnostic (75+ providers), full TUI. The "you're not locked in" lesson. | Free tool + your free key |
| 3 | **Aider** | Architecturally *different* — patch/diff-centric and git-native rather than an agent TUI. Auto-commits every change. | Free tool + your free key |
| 4 | **Browser AI** (ChatGPT / Gemini / Claude free tiers) | No install, no key, works on a locked-down lab machine. Teaches copy-paste discipline and context-by-hand. | Free, always |

### Backup stations (if the lab network blocks something)

| Harness | Note |
| --- | --- |
| **Ollama + OpenCode** | Fully local, fully offline, zero account. Needs ~8GB RAM and a small model. The nuclear fallback — works with *no internet at all*. |
| **Pair up** | Two students, one key. Costs nothing and the driver/navigator split is good practice anyway. |

> **GitHub Copilot is deliberately not a station.** It needs the Student
> Developer Pack, which takes days to approve — and our three days are
> consecutive. Worth applying for your own sake; not something this workshop
> can depend on.

## The demo zoo (15 min, watch only — do not install)

So students know these categories exist and can name them in an interview:

- **Pi / oh-my-pi** — minimal, adaptable harness; session fork/branch is first-class
- **Goose**, **Crush**, **Plandex**, **Continue CLI** — other open-source takes
- **Claude Code**, **Codex CLI**, **Cursor** — the platform agents
- **Orchestrators** — Claude Squad, vibe-kanban, cmux: running *fleets* of agents in parallel
- **Agent infrastructure** — context compression, memory, security guards

The point of the zoo is not the tools. It is: *there are 150+ of these, they ship
weekly, and they are all the same seven primitives.* Do not memorise tools.
Learn the primitives.

## The Cold Start exercise

Late on Day 2 you will be handed a harness **nobody taught you**, with nothing but
its README, and 15 minutes to install it, point it at a provider, and complete a
task.

This is the actual skill. You cannot be taught 150 tools. You can be taught to
onboard yourself onto any of them — and that is a genuinely great answer to
*"how do you pick up new technology?"* in an interview.
