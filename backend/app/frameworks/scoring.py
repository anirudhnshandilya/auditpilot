from dataclasses import dataclass


@dataclass(frozen=True)
class ComplianceScore:
    score: int
    rating: str
    covered_controls: int
    uncovered_controls: int
    coverage_percentage: float