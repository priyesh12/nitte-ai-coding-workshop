"""BUG 04 - Tier 1 - target time: 8 minutes

Remove students who are not placed, so we can email the rest.

This one is nasty: it does not crash. It just silently keeps the wrong
people. Run it and compare what you got against what you expected.
"""


def drop_unplaced(students):
    """students is a list of dicts with 'name' and 'placed' keys."""
    for student in students:
        if not student["placed"]:
            students.remove(student)
    return students


def names_of(students):
    return [s["name"] for s in students]
