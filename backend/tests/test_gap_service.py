from datetime import UTC, datetime

from app.frameworks.gap_service import GapService
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


def test_no_evidence_creates_gaps_for_all_controls() -> None:
    gaps = GapService.detect([])

    assert len(gaps) == 2
    assert [gap.control_id for gap in gaps] == ["A.5.1", "A.5.2"]


def test_policy_evidence_leaves_a_5_2_gap() -> None:
    document = make_document(
        "Information Security Policy Version 1.0 "
        "Approved by the CISO after policy review."
    )

    gaps = GapService.detect([document])

    assert len(gaps) == 1
    assert gaps[0].control_id == "A.5.2"
    assert gaps[0].control_title == (
        "Information security roles and responsibilities"
    )
    assert "RACI matrix" in gaps[0].expected_evidence


def test_full_coverage_creates_no_gaps() -> None:
    policy = make_document(
        "Information Security Policy Version 1.0 "
        "Approved by the CISO after policy review."
    )
    roles = make_document(
        "This RACI matrix defines information security "
        "roles and responsibilities and accountability."
    )

    gaps = GapService.detect([policy, roles])

    assert gaps == []