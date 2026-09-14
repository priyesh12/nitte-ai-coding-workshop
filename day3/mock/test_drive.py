"""VISIBLE tests. There are hidden ones too - re-read the brief."""

from drive import is_eligible, meets_branch, meets_cgpa
from placement_tracker.models import Criteria, Student


def crit(**kw):
    base = {"company": "Infosys", "min_cgpa": 7.0, "max_backlogs": 1}
    base.update(kw)
    return Criteria(**base)


def stu(name="Asha", branch="CSE", cgpa=8.0, backlogs=0):
    return Student("R1", name, branch, cgpa, backlogs)


# --- Part A: these two are broken -------------------------------------------

def test_cgpa_bar_is_inclusive():
    assert meets_cgpa(stu(cgpa=7.0), crit()) is True, (
        "the docstring says exactly min_cgpa is a PASS"
    )


def test_empty_branch_list_means_all_branches():
    c = crit(allowed_branches=[])
    assert meets_branch(stu(branch="ECE"), c) is True, (
        "an empty allowed_branches means all branches are welcome"
    )


# --- these already pass ------------------------------------------------------

def test_cgpa_below_bar_fails():
    assert meets_cgpa(stu(cgpa=6.5), crit()) is False


def test_branch_restriction_works():
    c = crit(allowed_branches=["CSE"])
    assert meets_branch(stu(branch="ECE"), c) is False
    assert meets_branch(stu(branch="CSE"), c) is True


def test_eligible_student_passes_everything():
    assert is_eligible(stu(), crit(allowed_branches=["CSE"])) is True


# --- Part B: the feature -----------------------------------------------------

BATCH = [
    Student("R1", "Asha", "CSE", 9.0, 0),
    Student("R2", "Bhavya", "CSE", 7.0, 0),
    Student("R3", "Chetan", "ECE", 8.5, 0),
    Student("R4", "Divya", "CSE", 6.0, 0),
    Student("R5", "Esha", "CSE", 8.0, 3),
]


def report():
    from drive import generate_drive_report
    return generate_drive_report(BATCH, crit(allowed_branches=["CSE"]))


def test_report_has_every_required_key():
    r = report()
    assert set(r) == {
        "company", "eligible", "rejected", "eligible_count", "eligibility_rate"
    }


def test_eligible_students_best_first():
    assert report()["eligible"] == ["Asha", "Bhavya"]


def test_eligibility_rate():
    assert report()["eligibility_rate"] == 40.0


def test_every_rejected_student_has_a_reason():
    rejected = report()["rejected"]
    assert len(rejected) == 3
    assert all(r["reason"] for r in rejected)
