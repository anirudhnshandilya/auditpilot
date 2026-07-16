from app.services.evidence_models import EvidenceStatus
from app.services.evidence_status_engine import EvidenceStatusEngine


def test_draft_requires_human_review() -> None:
    result = EvidenceStatusEngine.evaluate(
        "Information Security Policy Draft v1.0"
    )

    assert result.status == EvidenceStatus.HUMAN_REVIEW_REQUIRED
    assert "Document appears to be a draft." in result.reasons


def test_missing_approval_requires_human_review() -> None:
    result = EvidenceStatusEngine.evaluate(
        "Information Security Policy Version 1.0"
    )

    assert result.status == EvidenceStatus.HUMAN_REVIEW_REQUIRED
    assert "Approval information was not detected." in result.reasons


def test_missing_version_requires_human_review() -> None:
    result = EvidenceStatusEngine.evaluate(
        "Information Security Policy Approved by CISO"
    )

    assert result.status == EvidenceStatus.HUMAN_REVIEW_REQUIRED
    assert "Version information was not detected." in result.reasons


def test_approved_versioned_document_is_sufficient() -> None:
    result = EvidenceStatusEngine.evaluate(
        "Information Security Policy Version 1.0 Approved by CISO"
    )

    assert result.status == EvidenceStatus.SUFFICIENT
    assert result.reasons == []