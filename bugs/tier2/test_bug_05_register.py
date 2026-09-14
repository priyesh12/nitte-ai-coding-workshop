from bug_05_register import register


def test_first_company_drive():
    assert register("Asha") == ["Asha"]


def test_second_company_starts_empty():
    # A brand new drive must not remember the previous one.
    assert register("Bhavya") == ["Bhavya"], "this drive should start empty!"


def test_explicit_drive_still_works():
    existing = ["Asha"]
    assert register("Bhavya", existing) == ["Asha", "Bhavya"]
