from app.frameworks.gap_service import GapService
from app.remediation.models import (
    ActionStatus,
    Priority,
    RemediationAction,
)
from app.services.evidence_models import EvidenceDocument


class RemediationService:
    @staticmethod
    def generate(
        documents: list[EvidenceDocument],
    ) -> list[RemediationAction]:
        gaps = GapService.detect(documents)

        actions: list[RemediationAction] = []

        for gap in gaps:
            if gap.severity == "High":
                priority = Priority.HIGH
            elif gap.severity == "Medium":
                priority = Priority.MEDIUM
            else:
                priority = Priority.LOW

            actions.append(
                RemediationAction(
                    control_id=gap.control_id,
                    control_title=gap.control_title,
                    priority=priority,
                    recommendation=gap.recommendation,
                    expected_evidence=gap.expected_evidence,
                    status=ActionStatus.OPEN,
                )
            )

        return actions