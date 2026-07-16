from datetime import UTC, datetime

from app.frameworks.scoring_service import ScoringService
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


def test_no_documents_scores_poor() -> None:
    score = ScoringService.calculate([])

    assert score.score == 0
    assert score.rating == "Poor"


def test_partial_coverage_scores_needs_improvement() -> None:
    document = make_document(
        "Information Security Policy Version 1.0 "
        "Approved by the CISO after policy review."
    )

    score = ScoringService.calculate([document])

    assert score.score == 50
    assert score.rating == "Needs Improvement"


def test_full_coverage_scores_excellent() -> None:
    policy = make_document(
        "Information Security Policy Version 1.0 "
        "Approved by the CISO after policy review."
    )

    roles = make_document(
        "This RACI matrix defines information security "
        "roles and responsibilities and accountability."
    )

    score = ScoringService.calculate([policy, roles])

    assert score.score == 100
    assert score.rating == "Excellent"