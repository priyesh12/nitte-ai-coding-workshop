"""BUG 10 - Tier 4 - target time: 25 minutes  ** READ THIS ONE CAREFULLY **

The placement cell wants the toppers list for a company visit.

One test fails. Before you change any code, read the docstring of
`top_students` and read the failing test. They do not agree with each other.

Your job is NOT simply to make the test green.
Your job is to work out WHICH ONE IS WRONG, and be able to defend it.

This happens constantly in real assessments and real jobs: the spec and
the test disagree, and the engineer who notices is the one who gets hired.
"""


def top_students(students, n):
    """Return the top n students by CGPA, highest first.

    If several students are tied at the cut-off, INCLUDE ALL OF THEM -
    the placement cell will not drop one student and keep another on the
    same CGPA. This means the result can be longer than n.
    """
    ranked = sorted(students, key=lambda s: -s["cgpa"])
    return ranked[:n]
