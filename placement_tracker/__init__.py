"""placement_tracker — the workshop spine codebase.

A small student-placement system: load records, check eligibility against
company criteria, rank candidates, and report on outcomes.

Day 1 you debug it. Day 2 you extend it with AI. Day 3 you ship a feature
in it under time pressure and defend the code.
"""

from .models import Student, Criteria

__all__ = ["Student", "Criteria"]
