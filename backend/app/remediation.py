from dataclasses import dataclass


@dataclass(frozen=True)
class RemediationAction:
    control_id: str
    title: str
    description: str
    priority: str
    recommendation: str
    expected_evidence: list[str]