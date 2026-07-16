from pathlib import Path
from uuid import UUID

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.evidence_models import DocumentType, EvidenceDocument
from app.services.evidence_service import EvidenceService, evidence_repository
from app.services.evidence_summary import EvidenceSummaryService
from app.frameworks.mapper import ControlMapper

router = APIRouter(prefix="/evidence", tags=["Evidence"])

ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt", ".csv", ".xlsx"}
MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024


def serialize_evidence(
    document_id: UUID,
    evidence: EvidenceDocument,
) -> dict[str, object]:
   control_mappings = ControlMapper.map_text(
        evidence.extracted_text
    )
   
   return {

        "id": str(document_id),
        "filename": evidence.filename,
        "document_type": evidence.document_type,
        "mime_type": evidence.mime_type,
        "size_bytes": evidence.size_bytes,
        "checksum": evidence.checksum,
        "uploaded_at": evidence.uploaded_at.isoformat(),
        "processing_status": evidence.processing_status,
        "evidence_status": evidence.evidence_status,
        "extracted_text_length": len(evidence.extracted_text),
        "page_count": evidence.page_count,
        "word_count": evidence.word_count,
        "character_count": evidence.character_count,
        "author": evidence.author,
        "document_created_at": evidence.document_created_at,
        "document_modified_at": evidence.document_modified_at,
        "control_mappings": [
            {
                "control_id": mapping.control_id,
                "confidence": mapping.confidence,
                "matched_keywords": mapping.matched_keywords,
            }
            for mapping in control_mappings
        ],
    }


@router.post("/upload")
async def upload_evidence(
    file: UploadFile = File(...),
    document_type: DocumentType = DocumentType.UNKNOWN,
) -> dict[str, object]:
    filename = file.filename or ""
    extension = Path(filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOCX, TXT, CSV, and XLSX files are supported.",
        )

    contents = await file.read()

    if not contents:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty.",
        )

    if len(contents) > MAX_FILE_SIZE_BYTES:
        raise HTTPException(
            status_code=413,
            detail="File exceeds the 10 MB size limit.",
        )

    evidence = EvidenceService.process(
        filename=filename,
        contents=contents,
        mime_type=file.content_type or "application/octet-stream",
        document_type=document_type,
    )

    if evidence.processing_status.value == "Failed":
        raise HTTPException(
            status_code=400,
            detail="The uploaded document could not be processed.",
        )

    document_id = evidence_repository.add(evidence)

    return serialize_evidence(document_id, evidence)


@router.get("")
def list_evidence() -> list[dict[str, object]]:
    return [
        serialize_evidence(document_id, evidence)
        for document_id, evidence in evidence_repository.list()
    ]

@router.get("/summary")
def get_evidence_summary() -> dict[str, object]:
    documents = [
        evidence
        for _, evidence in evidence_repository.list()
    ]

    summary = EvidenceSummaryService.summarize(documents)

    return {
        "total_documents": summary.total_documents,
        "sufficient_documents": summary.sufficient_documents,
        "review_required_documents": summary.review_required_documents,
        "invalid_documents": summary.invalid_documents,
        "document_types": summary.document_types,
        "common_issues": summary.common_issues,
    }

@router.get("/{document_id}")
def get_evidence(document_id: UUID) -> dict[str, object]:
    evidence = evidence_repository.get(document_id)

    if evidence is None:
        raise HTTPException(
            status_code=404,
            detail="Evidence document not found.",
        )

    return serialize_evidence(document_id, evidence)


@router.delete("/{document_id}")
def delete_evidence(document_id: UUID) -> dict[str, str]:
    deleted = evidence_repository.delete(document_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Evidence document not found.",
        )

    return {"status": "deleted"}