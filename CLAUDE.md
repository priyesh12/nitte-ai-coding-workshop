# CLAUDE.md

Identical to [AGENTS.md](AGENTS.md) — deliberately.

Claude Code reads `CLAUDE.md`; OpenCode, Codex CLI, Pi and others read
`AGENTS.md`. Same content, two filenames, because the ecosystem has not fully
converged yet.

**Day 2 demo:** change one rule below, then run the same prompt through two
different harnesses and watch both obey it. That is invariant #1 in action.

## What this project is

A teaching repo for an 18-hour workshop on debugging and AI-assisted coding.
`bugs/` contains **deliberately broken** programs. `placement_tracker/` is the
working spine codebase.

## Rules

1. **Never "fix" anything under `bugs/`.** Those files are broken on purpose.
   If asked about one, explain the bug — do not rewrite the file.
2. **Standard library only.** No pip, no external packages. Lab machines block
   installs, so a dependency breaks the workshop for everyone.
3. **Tests run with `python3 run_tests.py`**, not pytest.
4. **Smallest possible change.** Do not refactor surrounding code, do not
   rename things, do not add abstraction that was not asked for.
5. **Show the diff before applying it.** Always.
6. **Do not touch `instructor/`.** Answer keys live there.

## Style

- Python 3.10+, type hints on public functions
- Docstrings say *why*, not *what*
- No comment that restates the line below it

## Verify before you claim done

```bash
python3 run_tests.py
```

State the actual pass/fail numbers. Never report success without running it.
