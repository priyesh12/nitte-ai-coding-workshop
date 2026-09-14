"""Summary reporting over a set of students."""

from .models import Student


def placement_percentage(students: list[Student]) -> float:
    """Percentage of students placed, rounded to 2dp. Empty input -> 0.0."""
    if not students:
        return 0.0
    placed = sum(1 for s in students if s.placed)
    return round(placed / len(students) * 100, 2)


def branch_summary(students: list[Student]) -> dict[str, dict[str, float]]:
    """Per-branch totals, placed counts and placement percentage."""
    summary: dict[str, dict[str, float]] = {}
    for student in students:
        row = summary.setdefault(
            student.branch, {"total": 0, "placed": 0, "percentage": 0.0}
        )
        row["total"] += 1
        if student.placed:
            row["placed"] += 1
    for row in summary.values():
        row["percentage"] = round(row["placed"] / row["total"] * 100, 2)
    return summary


def format_report(students: list[Student]) -> str:
    """Human-readable placement report."""
    lines = [
        "PLACEMENT REPORT",
        "=" * 40,
        f"Total students: {len(students)}",
        f"Placed: {sum(1 for s in students if s.placed)}",
        f"Placement rate: {placement_percentage(students)}%",
        "",
        "By branch:",
    ]
    for branch, row in sorted(branch_summary(students).items()):
        lines.append(
            f"  {branch:<6} {int(row['placed']):>3}/{int(row['total']):<3} "
            f"({row['percentage']}%)"
        )
    return "\n".join(lines)
