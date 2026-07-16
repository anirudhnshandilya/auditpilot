from dataclasses import dataclass
from enum import StrEnum


class Priority(StrEnum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class ActionStatus(StrEnum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


@dataclass(frozen=True)
class RemediationAction:
    control_id: str
    control_title: str
    priority: Priority
    recommendation: str
    expected_evidence: list[str]
    status: ActionStatus = ActionStatus.OPEN