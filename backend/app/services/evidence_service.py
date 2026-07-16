import hashlib
from datetime import UTC, datetime

from app.services.document_classifier import DocumentClassifier
from app.services.document_parser import DocumentParser
from app.services.evidence_models import (
    DocumentType,
    EvidenceDocument,
    EvidenceStatus,
    ProcessingStatus,
)
from app.services.evidence_repository import EvidenceRepository
from app.services.metadata_extractor import MetadataExtractor
from app.services.evidence_status_engine import EvidenceStatusEngine

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

            if document_type == DocumentType.UNKNOWN:
                document_type = DocumentClassifier.classify(
                    filename=filename,
                    extracted_text=extracted_text,
                )

            metadata = MetadataExtractor.extract(
                filename=filename,
                contents=contents,
                extracted_text=extracted_text,
            )

            processing_status = ProcessingStatus.PROCESSED
            status_result = EvidenceStatusEngine.evaluate(extracted_text)
            evidence_status = status_result.status

        except (ValueError, UnicodeDecodeError):
            extracted_text = ""
            metadata = MetadataExtractor.extract(
                filename="unknown.txt",
                contents=b"",
                extracted_text="",
            )
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
            page_count=metadata.page_count,
            word_count=metadata.word_count,
            character_count=metadata.character_count,
            author=metadata.author,
            document_created_at=metadata.created_at,
            document_modified_at=metadata.modified_at,
        )


evidence_repository = EvidenceRepository()