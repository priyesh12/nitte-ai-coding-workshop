"""BUG 07 - Tier 3 - target time: 18 minutes

The placement cell runs two company drives off the same student list.

Infosys runs first and shortlists correctly. Then TCS runs and gets far
fewer students than it should - even though TCS has LOWER requirements.

Nothing crashes. The bug is not in the function that looks wrong.
Trace what happens to `students` between the two calls.
"""


def shortlist(students, min_cgpa):
    """Return the students meeting min_cgpa."""
    for student in students:
        if student["cgpa"] < min_cgpa:
            students.remove(student)
    return students


def run_drive(students, company, min_cgpa):
    selected = shortlist(students, min_cgpa)
    return {"company": company, "selected": [s["name"] for s in selected]}
