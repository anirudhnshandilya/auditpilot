from dataclasses import dataclass


@dataclass(frozen=True)
class ComplianceGap:
    control_id: str
    control_title: str
    expected_evidence: list[str]
    severity: str
    recommendation: str