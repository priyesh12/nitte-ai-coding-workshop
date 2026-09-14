from bug_03_eligible import is_eligible, shortlist


def test_clearly_above_the_bar():
    assert is_eligible(8.5, 0) is True


def test_clearly_below_the_bar():
    assert is_eligible(6.2, 0) is False


def test_too_many_backlogs():
    assert is_eligible(9.0, 3) is False


def test_exactly_on_the_cgpa_boundary():
    # "7.0 or above" includes 7.0 itself.
    assert is_eligible(7.0, 0) is True, "a student with exactly 7.0 CGPA IS eligible"


def test_exactly_on_the_backlog_boundary():
    assert is_eligible(8.0, 1) is True


def test_shortlist_includes_boundary_student():
    students = [("Asha", 7.0, 0), ("Bhavya", 6.9, 0), ("Chetan", 8.0, 1)]
    assert shortlist(students) == ["Asha", "Chetan"]
