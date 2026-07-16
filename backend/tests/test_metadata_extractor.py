from io import BytesIO

import fitz
from docx import Document

from app.services.metadata_extractor import MetadataExtractor


def test_extract_text_metadata() -> None:
    metadata = MetadataExtractor.extract(
        filename="policy.txt",
        contents=b"Information Security Policy",
        extracted_text="Information Security Policy",
    )

    assert metadata.page_count is None
    assert metadata.word_count == 3
    assert metadata.character_count == 27
    assert metadata.author is None


def test_extract_pdf_metadata() -> None:
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Business continuity plan")

    contents = document.tobytes()
    document.close()

    metadata = MetadataExtractor.extract(
        filename="plan.pdf",
        contents=contents,
        extracted_text="Business continuity plan",
    )

    assert metadata.page_count == 1
    assert metadata.word_count == 3
    assert metadata.character_count == 24


def test_extract_docx_metadata() -> None:
    document = Document()
    document.add_paragraph("Access control policy")
    document.core_properties.author = "AuditPilot"

    buffer = BytesIO()
    document.save(buffer)

    metadata = MetadataExtractor.extract(
        filename="policy.docx",
        contents=buffer.getvalue(),
        extracted_text="Access control policy",
    )

    assert metadata.page_count is None
    assert metadata.word_count == 3
    assert metadata.character_count == 21
    assert metadata.author == "AuditPilot"