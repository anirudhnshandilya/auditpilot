from io import BytesIO
from pathlib import Path

import pandas as pd
from fastapi import APIRouter, File, HTTPException, UploadFile

from app.validators.engine import ValidationEngine

router = APIRouter(prefix="/upload", tags=["Upload"])

ALLOWED_EXTENSIONS = {".csv", ".xlsx"}
MAX_FILE_SIZE_BYTES = 5 * 1024 * 1024


@router.post("/risk-register")
async def upload_risk_register(
    file: UploadFile = File(...),
) -> dict[str, object]:
    filename = file.filename or ""
    extension = Path(filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only CSV and XLSX files are supported.",
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
            detail="File exceeds the 5 MB size limit.",
        )

    try:
        if extension == ".csv":
            dataframe = pd.read_csv(BytesIO(contents))
        else:
            dataframe = pd.read_excel(BytesIO(contents))
    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail="The uploaded file could not be parsed.",
        ) from exc

    validation_engine = ValidationEngine()
    validation_result = validation_engine.validate(dataframe)

    return {
        "filename": filename,
        "status": "validated",
        "rows": len(dataframe),
        "columns": len(dataframe.columns),
        "column_names": dataframe.columns.astype(str).tolist(),
        "score": validation_result.score,
        "audit_readiness": validation_result.audit_readiness,
        "findings": [
            {
                "severity": finding.severity,
                "row": finding.row,
                "column": finding.column,
                "message": finding.message,
                "recommendation": finding.recommendation,
            }
            for finding in validation_result.findings
        ],
    }