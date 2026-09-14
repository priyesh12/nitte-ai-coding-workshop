from bug_04_toppers import drop_unplaced, names_of


def s(name, placed):
    return {"name": name, "placed": placed}


def test_drops_the_single_unplaced_student():
    out = drop_unplaced([s("Asha", True), s("Bhavya", False)])
    assert names_of(out) == ["Asha"]


def test_drops_two_unplaced_in_a_row():
    # Two unplaced students side by side is where this falls apart.
    out = drop_unplaced([s("Asha", True), s("Bhavya", False), s("Chetan", False)])
    assert names_of(out) == ["Asha"], f"expected only Asha, got {names_of(out)}"


def test_everyone_unplaced():
    out = drop_unplaced([s("Asha", False), s("Bhavya", False)])
    assert names_of(out) == [], f"expected nobody, got {names_of(out)}"
