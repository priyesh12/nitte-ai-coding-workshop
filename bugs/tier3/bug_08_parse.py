"""BUG 08 - Tier 3 - target time: 20 minutes

Load student records from CSV text. One row is malformed.

The team added a try/except so "one bad row doesn't kill the import".
Now imports never crash - and silently lose good data. Worse, when you
ask WHY a row was skipped, nobody can tell you.

What is the except actually catching?
"""


def parse_students(text):
    students = []
    for line in text.strip().split("\n"):
        try:
            name, cgpa, backlogs = line.split(",")
            students.append({
                "name": name.strip(),
                "cgpa": float(cgpa),
                "backlogs": int(backlogs),
            })
        except:
            continue
    return students
