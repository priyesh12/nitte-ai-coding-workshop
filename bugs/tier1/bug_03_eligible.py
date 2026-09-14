"""BUG 03 - Tier 1 - target time: 6 minutes

Shortlist students for a company. The rule from the company is:

    "We need CGPA of 7.0 or above, and at most 1 backlog."

Most students come out right. One does not. Which one, and why?
"""


def is_eligible(cgpa, backlogs):
    if cgpa > 7.0 and backlogs <= 1:
        return True
    return False


def shortlist(students):
    """students is a list of (name, cgpa, backlogs) tuples."""
    return [name for name, cgpa, backlogs in students if is_eligible(cgpa, backlogs)]
