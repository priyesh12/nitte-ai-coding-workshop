from bug_02_average import average_cgpa


def test_averages_three_students():
    assert average_cgpa([8.0, 7.0, 9.0]) == 8.0


def test_single_student():
    assert average_cgpa([6.5]) == 6.5
