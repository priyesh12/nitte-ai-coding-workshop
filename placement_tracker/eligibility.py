"""Shortlisting students against company criteria."""

from .models import Criteria, Student


def is_eligible(student: Student, criteria: Criteria) -> bool:
    """Return True if ``student`` meets every one of ``criteria``.

    Bounds are inclusive. An empty ``allowed_branches`` or ``required_skills``
    means "no restriction", not "nothing qualifies".
    """
    if student.cgpa < criteria.min_cgpa:
        return False
    if student.backlogs > criteria.max_backlogs:
        return False
    if criteria.allowed_branches and student.branch not in criteria.allowed_branches:
        return False
    for skill in criteria.required_skills:
        if not student.has_skill(skill):
            return False
    return True


def shortlist(students: list[Student], criteria: Criteria) -> list[Student]:
    """Return a new list of the students who meet ``criteria``.

    The input list is never modified.
    """
    return [s for s in students if is_eligible(s, criteria)]


def rejection_reason(student: Student, criteria: Criteria) -> str | None:
    """Explain the first criterion ``student`` fails, or None if eligible."""
    if student.cgpa < criteria.min_cgpa:
        return f"CGPA {student.cgpa} below minimum {criteria.min_cgpa}"
    if student.backlogs > criteria.max_backlogs:
        return f"{student.backlogs} backlogs exceeds limit {criteria.max_backlogs}"
    if criteria.allowed_branches and student.branch not in criteria.allowed_branches:
        return f"branch {student.branch} not in {criteria.allowed_branches}"
    for skill in criteria.required_skills:
        if not student.has_skill(skill):
            return f"missing required skill: {skill}"
    return None
