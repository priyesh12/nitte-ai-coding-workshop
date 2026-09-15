"""INSTRUCTOR reference solution for the Day 3 mock.

Part A fixes:
  meets_cgpa    ->  >=  not  >
  meets_branch  ->  empty allowed_branches means all branches

Part B: generate_drive_report below.
"""


def meets_cgpa(student, criteria):
    return student.cgpa >= criteria.min_cgpa


def meets_branch(student, criteria):
    if not criteria.allowed_branches:
        return True
    return student.branch in criteria.allowed_branches


def generate_drive_report(students, criteria):
    eligible, rejected = [], []
    for student in students:
        reason = rejection_reason(student, criteria)
        if reason is None:
            eligible.append(student)
        else:
            rejected.append({"name": student.name, "reason": reason})

    eligible.sort(key=lambda s: (-s.cgpa, s.backlogs, s.roll_no))
    rate = round(len(eligible) / len(students) * 100, 2) if students else 0.0

    return {
        "company": criteria.company,
        "eligible": [s.name for s in eligible],
        "rejected": rejected,
        "eligible_count": len(eligible),
        "eligibility_rate": rate,
    }
