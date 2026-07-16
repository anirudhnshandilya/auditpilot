from fastapi import APIRouter

from app.remediation.service import RemediationService
from app.services.evidence_service import evidence_repository

router = APIRouter(
    prefix="/remediation",
    tags=["Remediation"],
)


@router.get("/actions")
def get_remediation_actions() -> list[dict[str, object]]:
    documents = [
        evidence
        for _, evidence in evidence_repository.list()
    ]

    actions = RemediationService.generate(documents)

    return [
        {
            "control_id": action.control_id,
            "control_title": action.control_title,
            "priority": action.priority,
            "recommendation": action.recommendation,
            "expected_evidence": action.expected_evidence,
            "status": action.status,
        }
        for action in actions
    ]