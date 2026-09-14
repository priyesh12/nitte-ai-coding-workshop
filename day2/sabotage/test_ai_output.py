"""Tests the AI did NOT write. This is the whole point of the drill."""

from ai_output import calculate_percentage, get_cgpa, merge_skill_lists, paginate


# --- calculate_percentage ---------------------------------------------------

def test_percentage_normal_case():
    assert calculate_percentage(50, 200) == 25.0


def test_percentage_empty_batch():
    assert calculate_percentage(0, 0) == 0.0


def test_percentage_rejects_impossible_input():
    # More students placed than exist. Real data has typos in it.
    # Returning 250.0% is not "handling" it - it is hiding it.
    try:
        calculate_percentage(500, 200)
    except ValueError:
        return
    raise AssertionError(
        "placed > total is impossible data and was silently accepted"
    )


# --- paginate ---------------------------------------------------------------

STUDENTS = [f"student_{i}" for i in range(25)]


def test_page_one_returns_the_first_ten():
    # The docstring says pages are 1-indexed.
    assert paginate(STUDENTS, 1) == STUDENTS[0:10], (
        "page 1 must return the FIRST ten students"
    )


def test_page_two_returns_the_second_ten():
    assert paginate(STUDENTS, 2) == STUDENTS[10:20]


def test_last_partial_page():
    assert paginate(STUDENTS, 3) == STUDENTS[20:25]


# --- get_cgpa ---------------------------------------------------------------

def test_cgpa_present():
    assert get_cgpa({"cgpa": 8.5}) == 8.5


def test_cgpa_missing_key():
    assert get_cgpa({}) == 0.0


def test_cgpa_explicitly_none():
    # A student whose CGPA has not been entered yet has cgpa=None in the
    # database. The key EXISTS, so .get()'s default never fires.
    assert get_cgpa({"cgpa": None}) == 0.0, (
        "a record with cgpa=None should read as 0.0, not crash"
    )


# --- merge_skill_lists ------------------------------------------------------

def test_merge_removes_duplicates_and_sorts():
    assert merge_skill_lists(["Python"], ["SQL", "Python"]) == ["Python", "SQL"]


def test_merge_does_not_damage_the_original_list():
    original = ["Python"]
    merge_skill_lists(original, ["SQL"])
    assert original == ["Python"], (
        f"the caller's list was modified - it is now {original}"
    )
