from bug_08_parse import parse_students

GOOD = "Asha,9.0,0\nBhavya,7.5,1\nChetan,6.5,0"

def test_parses_clean_data():
    assert len(parse_students(GOOD)) == 3

def test_whitespace_around_numbers_is_fine():
    # " 8.0 " is perfectly valid input - float() handles the spaces.
    out = parse_students("Asha, 8.0 , 0 ")
    assert len(out) == 1, "a row with spaces around the numbers is still valid"
    assert out[0]["cgpa"] == 8.0

def test_genuinely_bad_row_is_skipped():
    out = parse_students("Asha,9.0,0\nBROKEN ROW\nChetan,6.5,0")
    assert [s["name"] for s in out] == ["Asha", "Chetan"]

def test_extra_column_is_reported_not_swallowed():
    # A row with too many columns is a DATA problem. It must not be
    # silently dropped - the caller has to find out.
    try:
        parse_students("Asha,9.0,0,extra")
    except ValueError:
        return  # good: the problem surfaced
    raise AssertionError("a malformed row was silently swallowed")
