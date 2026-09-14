from bug_10_toppers_list import top_students

BATCH = [
    {"name": "Asha", "cgpa": 9.5},
    {"name": "Bhavya", "cgpa": 8.8},
    {"name": "Chetan", "cgpa": 8.2},
    {"name": "Divya", "cgpa": 8.2},   # tied with Chetan, right at the cut-off
    {"name": "Esha", "cgpa": 7.1},
]


def test_no_ties_involved():
    assert [s["name"] for s in top_students(BATCH, 2)] == ["Asha", "Bhavya"]


def test_n_larger_than_the_batch():
    assert len(top_students(BATCH, 99)) == 5


def test_tie_at_the_cutoff_strict():
    """Whoever wrote this assumed top_students(n) returns exactly n."""
    names = [s["name"] for s in top_students(BATCH, 3)]
    assert names == ["Asha", "Bhavya", "Chetan"], f"got {names}"


def test_tie_at_the_cutoff_inclusive():
    """This one follows the docstring: ties at the cut-off are all included.

    Chetan and Divya are both on 8.2. The placement cell will not take one
    and drop the other.
    """
    names = [s["name"] for s in top_students(BATCH, 3)]
    assert sorted(names) == ["Asha", "Bhavya", "Chetan", "Divya"], (
        f"got {names} - the docstring says ties at the cut-off are included"
    )
