from dataclasses import dataclass
from io import BytesIO
from pathlib import Path

import fitz  # type: ignore[import-untyped]
from docx import Document


@dataclass
class DocumentMetadata:
    page_count: int | None
    word_count: int
    character_count: int
    author: str | None
    created_at: str | None
    modified_at: str | None


class MetadataExtractor:
    @staticmethod
    def extract(
        filename: str,
        contents: bytes,
        extracted_text: str,
    ) -> DocumentMetadata:
        extension = Path(filename).suffix.lower()

        page_count: int | None = None
        author: str | None = None
        created_at: str | None = None
        modified_at: str | None = None

        if extension == ".pdf":
            with fitz.open(stream=contents, filetype="pdf") as document:
                page_count = document.page_count
                metadata = document.metadata or {}
                author = metadata.get("author") or None
                created_at = metadata.get("creationDate") or None
                modified_at = metadata.get("modDate") or None

        elif extension == ".docx":
            document = Document(BytesIO(contents))
            properties = document.core_properties

            author = properties.author or None
            created_at = (
                properties.created.isoformat()
                if properties.created is not None
                else None
            )
            modified_at = (
                properties.modified.isoformat()
                if properties.modified is not None
                else None
            )

        words = extracted_text.split()

        return DocumentMetadata(
            page_count=page_count,
            word_count=len(words),
            character_count=len(extracted_text),
            author=author,
            created_at=created_at,
            modified_at=modified_at,
        )