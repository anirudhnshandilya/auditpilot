from dataclasses import dataclass


@dataclass(frozen=True)
class CoverageResult:
    total_controls: int
    covered_controls: int
    uncovered_controls: int
    coverage_percentage: float
    covered_control_ids: list[str]
    uncovered_control_ids: list[str]