from io import BytesIO
from pathlib import Path

import pandas as pd
from fastapi import APIRouter, File, HTTPException, UploadFile

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

    return {
        "filename": filename,
        "status": "uploaded",
        "rows": len(dataframe),
        "columns": len(dataframe.columns),
        "column_names": dataframe.columns.astype(str).tolist(),
    }