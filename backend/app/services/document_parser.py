from io import BytesIO
from pathlib import Path

import fitz  # type: ignore[import-untyped]
import pandas as pd
from docx import Document


class DocumentParser:
    @staticmethod
    def parse(filename: str, contents: bytes) -> str:
        extension = Path(filename).suffix.lower()

        if extension == ".pdf":
            return DocumentParser._parse_pdf(contents)

        if extension == ".docx":
            return DocumentParser._parse_docx(contents)

        if extension == ".txt":
            return contents.decode("utf-8")

        if extension == ".csv":
            dataframe = pd.read_csv(BytesIO(contents))
            return dataframe.to_csv(index=False)

        if extension == ".xlsx":
            dataframe = pd.read_excel(BytesIO(contents))
            return dataframe.to_csv(index=False)

        raise ValueError(f"Unsupported document type: {extension}")

    @staticmethod
    def _parse_pdf(contents: bytes) -> str:
        text_parts: list[str] = []

        with fitz.open(stream=contents, filetype="pdf") as document:
            for page in document:
                text_parts.append(page.get_text())

        return "\n".join(text_parts).strip()

    @staticmethod
    def _parse_docx(contents: bytes) -> str:
        document = Document(BytesIO(contents))

        return "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
            if paragraph.text.strip()
        )