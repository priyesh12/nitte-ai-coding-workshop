from bug_07_shortlist import run_drive

def batch():
    return [
        {"name": "Asha", "cgpa": 9.0},
        {"name": "Bhavya", "cgpa": 7.5},
        {"name": "Chetan", "cgpa": 6.5},
        {"name": "Divya", "cgpa": 5.5},
    ]

def test_first_drive_is_correct():
    assert run_drive(batch(), "Infosys", 7.0)["selected"] == ["Asha", "Bhavya"]

def test_second_drive_sees_the_full_batch():
    students = batch()
    run_drive(students, "Infosys", 7.0)
    # TCS asks for LESS, so it must get MORE students - not fewer.
    tcs = run_drive(students, "TCS", 6.0)
    assert tcs["selected"] == ["Asha", "Bhavya", "Chetan"], (
        f"TCS should see the whole batch again, got {tcs['selected']}"
    )

def test_original_list_is_not_damaged():
    students = batch()
    run_drive(students, "Infosys", 7.0)
    assert len(students) == 4, (
        f"the batch had 4 students before the drive, now it has {len(students)}"
    )
