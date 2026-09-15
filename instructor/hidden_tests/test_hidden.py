"""HIDDEN tests for the Day 3 mock — do NOT give these to students.

Every one of these checks something the BRIEF states but the visible tests
do not cover. Students who re-read the brief will pass them.

    python3 instructor/grade.py <student-dir>
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

from placement_tracker.models import Criteria, Student  # noqa: E402

TARGET = None  # injected by grade.py


def crit(**kw):
    base = {"company": "Infosys", "min_cgpa": 7.0, "max_backlogs": 1}
    base.update(kw)
    return Criteria(**base)


def batch():
    return [
        Student("R1", "Asha", "CSE", 9.0, 0),
        Student("R2", "Bhavya", "CSE", 7.0, 0),
        Student("R3", "Chetan", "ECE", 8.5, 0),
        Student("R4", "Divya", "CSE", 6.0, 0),
        Student("R5", "Esha", "CSE", 8.0, 3),
    ]


# --- brief: "Empty student list -> rate is 0.0, not a crash" -----------------

def test_empty_student_list_does_not_crash():
    r = TARGET.generate_drive_report([], crit())
    assert r["eligibility_rate"] == 0.0
    assert r["eligible"] == []
    assert r["eligible_count"] == 0


# --- brief: "The input list must not be modified" ---------------------------

def test_input_list_is_not_modified():
    students = batch()
    TARGET.generate_drive_report(students, crit(allowed_branches=["CSE"]))
    assert len(students) == 5, "the input list was modified"
    assert students[0].name == "Asha", "the input list was reordered"


# --- brief: "reason is the FIRST criterion the student fails" ----------------

def test_reason_is_the_first_failure_not_any_failure():
    # Fails CGPA *and* backlogs. CGPA is checked first, so CGPA must be cited.
    s = Student("R9", "Farah", "CSE", 5.0, 9)
    r = TARGET.generate_drive_report([s], crit(allowed_branches=["CSE"]))
    reason = r["rejected"][0]["reason"]
    assert "CGPA" in reason, f"expected the CGPA reason first, got: {reason}"


# --- brief: "best first = CGPA, then fewest backlogs, then roll number" ------

def test_tie_broken_by_backlogs_then_roll_number():
    tied = [
        Student("R3", "Chetan", "CSE", 8.0, 1),
        Student("R1", "Asha", "CSE", 8.0, 0),   # same CGPA, fewer backlogs
        Student("R2", "Bhavya", "CSE", 8.0, 1),  # ties Chetan, lower roll no
    ]
    r = TARGET.generate_drive_report(tied, crit(allowed_branches=["CSE"]))
    assert r["eligible"] == ["Asha", "Bhavya", "Chetan"], (
        f"tie-break order wrong: {r['eligible']}"
    )


# --- brief: empty allowed_branches means all branches ------------------------

def test_no_branch_restriction_admits_everyone():
    r = TARGET.generate_drive_report(batch(), crit(allowed_branches=[]))
    assert "Chetan" in r["eligible"], "ECE should be eligible with no restriction"


# --- brief: rate rounded to 2 decimals --------------------------------------

def test_rate_is_rounded_to_two_decimals():
    three = [
        Student("R1", "Asha", "CSE", 9.0, 0),
        Student("R2", "Bhavya", "CSE", 5.0, 0),
        Student("R3", "Chetan", "CSE", 5.0, 0),
    ]
    r = TARGET.generate_drive_report(three, crit(allowed_branches=["CSE"]))
    assert r["eligibility_rate"] == 33.33, f"got {r['eligibility_rate']}"


# --- boundary, again --------------------------------------------------------

def test_student_exactly_on_the_cgpa_bar_is_eligible():
    r = TARGET.generate_drive_report(batch(), crit(allowed_branches=["CSE"]))
    assert "Bhavya" in r["eligible"], "7.0 meets a 7.0 minimum"


def test_student_exactly_on_the_backlog_limit_is_eligible():
    s = Student("R1", "Asha", "CSE", 8.0, 1)
    r = TARGET.generate_drive_report([s], crit(max_backlogs=1, allowed_branches=["CSE"]))
    assert r["eligible"] == ["Asha"], "exactly 1 backlog is within a limit of 1"
