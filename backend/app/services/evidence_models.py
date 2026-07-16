from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


class EvidenceStatus(StrEnum):
    PRESENT = "Present"
    MISSING = "Missing"
    OUTDATED = "Outdated"
    INVALID = "Invalid"
    PARTIALLY_SUFFICIENT = "Partially sufficient"
    SUFFICIENT = "Sufficient"
    HUMAN_REVIEW_REQUIRED = "Human review required"


class ProcessingStatus(StrEnum):
    PENDING = "Pending"
    PROCESSING = "Processing"
    PROCESSED = "Processed"
    FAILED = "Failed"


class DocumentType(StrEnum):
    UNKNOWN = "Unknown"
    RISK_REGISTER = "Risk Register"
    ASSET_REGISTER = "Asset Register"
    POLICY = "Policy"
    PROCEDURE = "Procedure"
    INCIDENT_REGISTER = "Incident Register"
    AUDIT_REPORT = "Audit Report"
    TRAINING_RECORD = "Training Record"
    EVIDENCE = "Evidence"


@dataclass
class EvidenceDocument:
    filename: str
    document_type: DocumentType
    mime_type: str
    size_bytes: int
    checksum: str
    uploaded_at: datetime
    processing_status: ProcessingStatus
    evidence_status: EvidenceStatus
    extracted_text: str = ""
    page_count: int | None = None
    word_count: int = 0
    character_count: int = 0
    author: str | None = None
    document_created_at: str | None = None
    document_modified_at: str | None = None