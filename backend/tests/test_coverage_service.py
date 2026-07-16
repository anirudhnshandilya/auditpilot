from app.frameworks.coverage_service import CoverageService
from app.services.evidence_models import (
    DocumentType,
    EvidenceDocument,
    EvidenceStatus,
    ProcessingStatus,
)
from datetime import UTC, datetime


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


def test_no_documents_gives_zero_coverage() -> None:
    result = CoverageService.analyse([])

    assert result.total_controls == 2
    assert result.covered_controls == 0
    assert result.uncovered_controls == 2
    assert result.coverage_percentage == 0.0
    assert result.covered_control_ids == []
    assert result.uncovered_control_ids == ["A.5.1", "A.5.2"]


def test_policy_document_covers_a_5_1() -> None:
    document = make_document(
        "Information Security Policy Version 1.0 "
        "Approved by the CISO after policy review."
    )

    result = CoverageService.analyse([document])

    assert result.covered_controls == 1
    assert result.coverage_percentage == 50.0
    assert result.covered_control_ids == ["A.5.1"]
    assert result.uncovered_control_ids == ["A.5.2"]


def test_documents_can_cover_all_controls() -> None:
    policy = make_document(
        "Information Security Policy Version 1.0 "
        "Approved by the CISO after policy review."
    )
    roles = make_document(
        "This RACI matrix defines information security roles "
        "and responsibilities and accountability."
    )

    result = CoverageService.analyse([policy, roles])

    assert result.covered_controls == 2
    assert result.uncovered_controls == 0
    assert result.coverage_percentage == 100.0
    assert result.covered_control_ids == ["A.5.1", "A.5.2"]