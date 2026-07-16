from app.services.evidence_models import (
    DocumentType,
    EvidenceStatus,
    ProcessingStatus,
)
from app.services.evidence_service import EvidenceService


def test_process_valid_text_document() -> None:
    evidence = EvidenceService.process(
        filename="policy.txt",
        contents=b"Information Security Policy",
        mime_type="text/plain",
        document_type=DocumentType.POLICY,
    )

    assert evidence.filename == "policy.txt"
    assert evidence.document_type == DocumentType.POLICY
    assert evidence.processing_status == ProcessingStatus.PROCESSED
    assert evidence.evidence_status == EvidenceStatus.PRESENT
    assert evidence.extracted_text == "Information Security Policy"
    assert len(evidence.checksum) == 64


def test_process_invalid_document() -> None:
    evidence = EvidenceService.process(
        filename="virus.exe",
        contents=b"malware",
        mime_type="application/octet-stream",
    )

    assert evidence.processing_status == ProcessingStatus.FAILED
    assert evidence.evidence_status == EvidenceStatus.INVALID
    assert evidence.extracted_text == ""