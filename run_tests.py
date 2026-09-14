#!/usr/bin/env python3
"""Tiny test runner. Stdlib only - no pytest, no pip, no internet.

    python3 run_tests.py                  # everything
    python3 run_tests.py bugs/tier0       # one tier
    python3 run_tests.py bugs/tier0/bug_01_greeting.py
"""
from __future__ import annotations  # keeps this file runnable on Python 3.8

import importlib.util
import pathlib
import sys
import traceback

GREEN, RED, DIM, BOLD, RESET = "\033[32m", "\033[31m", "\033[2m", "\033[1m", "\033[0m"
if not sys.stdout.isatty():
    GREEN = RED = DIM = BOLD = RESET = ""


def load(path: pathlib.Path):
    # Put the file's own folder first so a test can import the buggy module
    # sitting next to it.
    folder = str(path.parent.resolve())
    if folder not in sys.path:
        sys.path.insert(0, folder)
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[path.stem] = module
    spec.loader.exec_module(module)
    return module


def run_file(path: pathlib.Path) -> tuple[int, int]:
    """Run every test_* function in a file. Returns (passed, failed)."""
    try:
        rel = path.resolve().relative_to(pathlib.Path.cwd())
    except ValueError:
        rel = path  # outside the current folder - just show it as given
    print(f"\n{BOLD}{rel}{RESET}")
    try:
        module = load(path)
    except Exception:
        # An import-time crash IS the bug in tier 0. Show it properly.
        print(f"  {RED}CRASHED ON IMPORT{RESET} - the file cannot even load.\n")
        traceback.print_exc(file=sys.stdout)
        return 0, 1

    tests = sorted(n for n in dir(module) if n.startswith("test_"))
    if not tests:
        print(f"  {DIM}(no tests here){RESET}")
        return 0, 0

    passed = failed = 0
    for name in tests:
        label = name[5:].replace("_", " ")
        try:
            getattr(module, name)()
        except AssertionError as exc:
            failed += 1
            print(f"  {RED}FAIL{RESET} {label}")
            if str(exc):
                print(f"       {exc}")
        except Exception as exc:
            failed += 1
            print(f"  {RED}ERROR{RESET} {label}")
            print(f"       {type(exc).__name__}: {exc}")
            tb = traceback.extract_tb(sys.exc_info()[2])
            if len(tb) > 1:
                f = tb[-1]
                print(f"       {DIM}at {pathlib.Path(f.filename).name}:{f.lineno}"
                      f"  {f.line}{RESET}")
        else:
            passed += 1
            print(f"  {GREEN}PASS{RESET} {label}")
    return passed, failed


def main() -> int:
    target = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    if not target.exists():
        print(f"{RED}No such path: {target}{RESET}")
        return 2

    files = [target] if target.is_file() else sorted(
        p for p in target.rglob("test_*.py") if "__pycache__" not in p.parts
    )
    if not files:
        print(f"{RED}No test files under {target}{RESET}")
        return 2

    total_p = total_f = 0
    for f in files:
        p, fl = run_file(f)
        total_p += p
        total_f += fl

    print("\n" + "=" * 46)
    if total_f == 0:
        print(f"  {GREEN}{BOLD}ALL {total_p} TESTS PASSING{RESET}")
    else:
        print(f"  {GREEN}{total_p} passing{RESET}   {RED}{BOLD}{total_f} failing{RESET}")
        print(f"\n  {DIM}Remember: hypothesis on paper BEFORE you ask AI.{RESET}")
    print("=" * 46)
    return 1 if total_f else 0


if __name__ == "__main__":
    sys.exit(main())
