"""BUG 01 - Tier 0 - target time: 2 minutes

A company wants a welcome line for each shortlisted student.
This file does not even load. Fix it.
"""


def greet(name, company)
    return f"Hello {name}, welcome to your {company} interview!"


def greet_all(names, company):
    return [greet(n, company) for n in names]
