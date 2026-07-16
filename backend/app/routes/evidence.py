from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.evidence_models import DocumentType
from app.services.evidence_service import EvidenceService

router = APIRouter(prefix="/evidence", tags=["Evidence"])

ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt", ".csv", ".xlsx"}
MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024


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

    return {
        "filename": evidence.filename,
        "document_type": evidence.document_type,
        "mime_type": evidence.mime_type,
        "size_bytes": evidence.size_bytes,
        "checksum": evidence.checksum,
        "uploaded_at": evidence.uploaded_at.isoformat(),
        "processing_status": evidence.processing_status,
        "evidence_status": evidence.evidence_status,
        "extracted_text_length": len(evidence.extracted_text),
    }