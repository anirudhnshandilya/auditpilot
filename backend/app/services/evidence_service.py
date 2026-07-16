import hashlib
from datetime import UTC, datetime
from app.services.evidence_repository import EvidenceRepository

from app.services.document_parser import DocumentParser
from app.services.evidence_models import (
    DocumentType,
    EvidenceDocument,
    EvidenceStatus,
    ProcessingStatus,
)


class EvidenceService:
    @staticmethod
    def process(
        filename: str,
        contents: bytes,
        mime_type: str,
        document_type: DocumentType = DocumentType.UNKNOWN,
    ) -> EvidenceDocument:
        checksum = hashlib.sha256(contents).hexdigest()

        try:
            extracted_text = DocumentParser.parse(filename, contents)
            processing_status = ProcessingStatus.PROCESSED
            evidence_status = EvidenceStatus.PRESENT
        except (ValueError, UnicodeDecodeError):
            extracted_text = ""
            processing_status = ProcessingStatus.FAILED
            evidence_status = EvidenceStatus.INVALID

        return EvidenceDocument(
            filename=filename,
            document_type=document_type,
            mime_type=mime_type,
            size_bytes=len(contents),
            checksum=checksum,
            uploaded_at=datetime.now(UTC),
            processing_status=processing_status,
            evidence_status=evidence_status,
            extracted_text=extracted_text,
        )

evidence_repository = EvidenceRepository()