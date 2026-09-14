"""BUG 06 - Tier 2 - target time: 15 minutes

A company's bonus round has a cut-off CGPA of exactly 7.3.

One student, Chetan, had a CGPA of 6.9 and won a 0.4 bump on revaluation.
6.9 + 0.4 = 7.3, so he qualifies. The system says he does not.

Before you change anything, open a Python shell and type these. Write down
what you expect BEFORE you press enter:

    >>> 6.9 + 0.4
    >>> 6.9 + 0.4 == 7.3
    >>> 0.1 + 0.2
"""


def qualifies_for_bonus(cgpa):
    return cgpa == 7.3


def count_qualifiers(cgpas):
    return sum(1 for c in cgpas if qualifies_for_bonus(c))
