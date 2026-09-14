from bug_06_cutoff import count_qualifiers, qualifies_for_bonus


def test_cgpa_typed_in_directly():
    assert qualifies_for_bonus(7.3) is True


def test_clearly_below_cutoff():
    assert qualifies_for_bonus(6.0) is False


def test_clearly_above_cutoff():
    assert qualifies_for_bonus(9.1) is False, "9.1 is not the cut-off, 7.3 is"


def test_chetans_revalued_cgpa():
    revalued = 6.9 + 0.4
    assert qualifies_for_bonus(revalued) is True, (
        f"Chetan's CGPA is {revalued!r} - the computer does not think that is 7.3"
    )


def test_counting_a_mixed_batch():
    batch = [7.3, 6.9 + 0.4, 6.0, 9.1]
    assert count_qualifiers(batch) == 2, "only the two 7.3 students qualify"
