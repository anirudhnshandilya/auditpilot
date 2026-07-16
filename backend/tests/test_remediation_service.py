from datetime import UTC, datetime

from app.remediation.models import Priority
from app.remediation.service import RemediationService
from app.services.evidence_models import (
    DocumentType,
    EvidenceDocument,
    EvidenceStatus,
    ProcessingStatus,
)


def make_document(text: str) -> EvidenceDocument:
    return EvidenceDocument(
        filename="evidence.txt",
        document_type=DocumentType.POLICY,
        mime_type="text/plain",
        size_bytes=len(text.encode()),
        checksum="a" * 64,
        uploaded_at=datetime.now(UTC),
        processing_status=ProcessingStatus.PROCESSED,
        evidence_status=EvidenceStatus.SUFFICIENT,
        extracted_text=text,
    )


def test_no_evidence_generates_actions() -> None:
    actions = RemediationService.generate([])

    assert len(actions) == 2
    assert actions[0].priority == Priority.MEDIUM


def test_policy_document_generates_single_action() -> None:
    document = make_document(
        "Information Security Policy Version 1.0 "
        "Approved by the CISO after policy review."
    )

    actions = RemediationService.generate([document])

    assert len(actions) == 1
    assert actions[0].control_id == "A.5.2"
    assert actions[0].priority == Priority.MEDIUM


def test_full_coverage_generates_no_actions() -> None:
    policy = make_document(
        "Information Security Policy Version 1.0 "
        "Approved by the CISO after policy review."
    )

    roles = make_document(
        "This RACI matrix defines information security "
        "roles and responsibilities and accountability."
    )

    actions = RemediationService.generate([policy, roles])

    assert actions == []