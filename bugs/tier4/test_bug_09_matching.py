import time
from bug_09_matching import find_matches


def test_small_case_is_correct():
    students = [
        {"name": "Asha", "skills": ["Python", "SQL"]},
        {"name": "Bhavya", "skills": ["Java"]},
    ]
    companies = [{"name": "Infosys", "skills": ["python"]}]
    assert find_matches(students, companies) == {"Infosys": ["Asha"]}


def test_company_needing_two_skills():
    students = [
        {"name": "Asha", "skills": ["Python", "SQL"]},
        {"name": "Bhavya", "skills": ["Python"]},
    ]
    companies = [{"name": "TCS", "skills": ["Python", "SQL"]}]
    assert find_matches(students, companies) == {"TCS": ["Asha"]}


def test_finishes_at_placement_season_scale():
    # 5000 students, 500 companies. This is a REAL assessment input size.
    skills = ["Python", "SQL", "Java", "C++", "Go", "Rust", "C", "JS"]
    students = [{"name": f"S{i}", "skills": skills} for i in range(5000)]
    companies = [
        {"name": f"C{j}", "skills": ["python", "sql"]} for j in range(500)
    ]
    start = time.time()
    find_matches(students, companies)
    elapsed = time.time() - start
    assert elapsed < 1.5, (
        f"took {elapsed:.1f}s - an assessment platform would have killed this "
        f"with Time Limit Exceeded. Count how many times the innermost "
        f"comparison runs."
    )
