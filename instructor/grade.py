#!/usr/bin/env python3
"""Grade a Day 3 mock submission. Stdlib only.

    python3 instructor/grade.py path/to/student/drive.py
    python3 instructor/grade.py day3/mock/drive.py

Runs the visible tests and the hidden tests, prints a mark out of 70.
The remaining 30 (viva) you award by hand - see instructor/VIVA-RUBRIC.md
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys
import traceback

ROOT = pathlib.Path(__file__).resolve().parents[1]


def load(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def run_suite(mod, label: str) -> tuple[int, int, list[str]]:
    names = sorted(n for n in dir(mod) if n.startswith("test_"))
    passed, failed, notes = 0, 0, []
    for n in names:
        try:
            getattr(mod, n)()
        except Exception as exc:
            failed += 1
            notes.append(f"    FAIL {n[5:].replace('_', ' ')}: {exc}"[:150])
        else:
            passed += 1
    return passed, failed, notes


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    target_path = pathlib.Path(sys.argv[1]).resolve()
    if not target_path.exists():
        print(f"No such file: {target_path}")
        return 2

    sys.path.insert(0, str(ROOT))
    sys.path.insert(0, str(target_path.parent))

    print("=" * 56)
    print(f"  GRADING  {target_path.name}")
    print("=" * 56)

    try:
        student = load(target_path, "drive")
    except Exception:
        print("\n  Submission does not even import:\n")
        traceback.print_exc(file=sys.stdout)
        print("\n  Score: 0 / 70")
        return 1

    # Part A + B visible
    vis_p = vis_f = 0
    vis_notes: list[str] = []
    visible_path = target_path.parent / "test_drive.py"
    if visible_path.exists():
        try:
            vis = load(visible_path, "test_drive_vis")
            vis_p, vis_f, vis_notes = run_suite(vis, "visible")
        except Exception as exc:
            vis_notes = [f"    visible suite failed to load: {exc}"]

    # Hidden
    hid_p = hid_f = 0
    hid_notes: list[str] = []
    if not hasattr(student, "generate_drive_report"):
        hid_notes = ["    generate_drive_report not implemented"]
        hid_f = 8
    else:
        hidden = load(ROOT / "instructor/hidden_tests/test_hidden.py", "test_hidden")
        hidden.TARGET = student
        hid_p, hid_f, hid_notes = run_suite(hidden, "hidden")

    vis_total = vis_p + vis_f or 1
    hid_total = hid_p + hid_f or 1
    part_ab = round(35 * vis_p / vis_total)
    hidden_marks = round(20 * hid_p / hid_total)

    print(f"\n  VISIBLE tests   {vis_p}/{vis_total}")
    for n in vis_notes:
        print(n)
    print(f"\n  HIDDEN tests    {hid_p}/{hid_total}")
    for n in hid_notes:
        print(n)

    print("\n" + "-" * 56)
    print(f"  Part A + B (visible)      {part_ab:>3} / 35")
    print(f"  Hidden tests              {hidden_marks:>3} / 20")
    print(f"  Clean code                  ? / 10   (by hand)")
    print(f"  Git hygiene                 ? /  5   (by hand)")
    print(f"  Viva                        ? / 30   (VIVA-RUBRIC.md)")
    print("-" * 56)
    print(f"  AUTO-GRADED SUBTOTAL      {part_ab + hidden_marks:>3} / 55")
    print("=" * 56)
    return 0


if __name__ == "__main__":
    sys.exit(main())
