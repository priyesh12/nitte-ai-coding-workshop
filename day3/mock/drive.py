"""Company drive reporting.

Part A: two bugs live in this file.
Part B: add generate_drive_report() below.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

from placement_tracker.models import Criteria, Student  # noqa: E402


def meets_cgpa(student: Student, criteria: Criteria) -> bool:
    """True if the student meets the minimum CGPA.

    The bar is inclusive: exactly min_cgpa is a pass.
    """
    return student.cgpa > criteria.min_cgpa


def meets_backlogs(student: Student, criteria: Criteria) -> bool:
    """True if the student is within the backlog limit (inclusive)."""
    return student.backlogs <= criteria.max_backlogs


def meets_branch(student: Student, criteria: Criteria) -> bool:
    """True if the student's branch is allowed.

    An empty allowed_branches list means "all branches welcome".
    """
    return student.branch in criteria.allowed_branches


def is_eligible(student: Student, criteria: Criteria) -> bool:
    """True if the student passes every check."""
    return (
        meets_cgpa(student, criteria)
        and meets_backlogs(student, criteria)
        and meets_branch(student, criteria)
    )


def rejection_reason(student: Student, criteria: Criteria) -> str | None:
    """The first criterion the student fails, or None if eligible."""
    if not meets_cgpa(student, criteria):
        return f"CGPA {student.cgpa} below minimum {criteria.min_cgpa}"
    if not meets_backlogs(student, criteria):
        return f"{student.backlogs} backlogs exceeds limit {criteria.max_backlogs}"
    if not meets_branch(student, criteria):
        return f"branch {student.branch} not eligible"
    return None


# --- Part B: write generate_drive_report() here -----------------------------
