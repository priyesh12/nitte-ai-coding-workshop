"""Ranking and selecting top candidates."""

from .models import Student


def rank_by_cgpa(students: list[Student]) -> list[Student]:
    """Return students sorted best-first: CGPA desc, then fewest backlogs,
    then roll number for a stable, predictable tie-break.
    """
    return sorted(students, key=lambda s: (-s.cgpa, s.backlogs, s.roll_no))


def top_n(students: list[Student], n: int) -> list[Student]:
    """Return the best ``n`` students.

    Ties at the cut-off are broken by the ``rank_by_cgpa`` ordering, so this
    returns exactly ``n`` students (or all of them, if fewer exist).
    """
    if n <= 0:
        return []
    return rank_by_cgpa(students)[:n]
