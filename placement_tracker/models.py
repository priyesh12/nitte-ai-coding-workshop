"""Core data types for the placement tracker."""

from dataclasses import dataclass, field


@dataclass
class Student:
    """One student's placement record."""

    roll_no: str
    name: str
    branch: str
    cgpa: float
    backlogs: int
    skills: list[str] = field(default_factory=list)
    placed: bool = False

    def has_skill(self, skill: str) -> bool:
        """Case-insensitive skill check."""
        return skill.casefold() in {s.casefold() for s in self.skills}


@dataclass
class Criteria:
    """A company's shortlisting criteria.

    Both bounds are inclusive: a student on exactly ``min_cgpa`` is eligible,
    and a student with exactly ``max_backlogs`` is eligible.
    """

    company: str
    min_cgpa: float = 0.0
    max_backlogs: int = 0
    allowed_branches: list[str] = field(default_factory=list)
    required_skills: list[str] = field(default_factory=list)
