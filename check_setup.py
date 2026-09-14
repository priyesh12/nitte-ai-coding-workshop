#!/usr/bin/env python3
"""Workshop setup check. Stdlib only - no pip, no internet needed.

    python3 check_setup.py
"""
import sys
import pathlib

def main() -> int:
    print("=" * 46)
    print("  AI Coding & Debugging Workshop - setup check")
    print("=" * 46)
    ok = True

    v = sys.version_info
    old_python = v < (3, 10)
    if v >= (3, 10):
        print(f"  [PASS] Python {v.major}.{v.minor}.{v.micro}")
    elif v >= (3, 8):
        print(f"  [WARN] Python {v.major}.{v.minor} - fine for Day 1.")
        print("         Upgrade to 3.10+ before Day 2.")
    else:
        print(f"  [FAIL] Python {v.major}.{v.minor} - too old, need 3.8+")
        print("         Windows: install 'Python 3.12' from the Microsoft Store")
        print("         Others:  https://www.python.org/downloads/")
        ok = False

    root = pathlib.Path(__file__).parent
    if (root / "bugs").is_dir():
        n = len(list((root / "bugs").glob("tier*/bug_*.py")))
        print(f"  [PASS] Workshop files found ({n} exercises)")
    else:
        print("  [FAIL] Run this from inside the workshop folder")
        ok = False

    try:
        from placement_tracker import Student  # noqa: F401
        print("  [PASS] placement_tracker imports")
    except Exception as exc:
        if old_python:
            # Day 2/3 code only. Day 1 does not touch it.
            print("  [WARN] placement_tracker needs Python 3.10+ (Day 2 only)")
        else:
            print(f"  [FAIL] placement_tracker broken: {exc}")
            ok = False

    print("-" * 46)
    if ok:
        print("  ALL CHECKS PASSED - you are ready.")
        print("  Next:  python3 run_tests.py bugs/tier0")
    else:
        print("  Something needs fixing. Show this screen to an instructor.")
    print("=" * 46)
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
