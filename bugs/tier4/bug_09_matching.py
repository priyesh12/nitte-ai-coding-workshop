"""BUG 09 - Tier 4 - target time: 30 minutes

Match students to companies by required skills.

It is CORRECT. Every test passes on small input. Then the real placement
season arrives with 2000 students and 200 companies, the assessment
platform kills your submission, and you get "Time Limit Exceeded".

Nothing here crashes. Nothing here is logically wrong.
Count the operations. How many times does the inner line run?
"""


def find_matches(students, companies):
    """Return {company_name: [student names who have every required skill]}."""
    matches = {}
    for company in companies:
        matched = []
        for student in students:
            has_all = True
            for required in company["skills"]:
                found = False
                for skill in student["skills"]:
                    if skill.lower() == required.lower():
                        found = True
                if not found:
                    has_all = False
            if has_all:
                matched.append(student["name"])
        matches[company["name"]] = matched
    return matches
