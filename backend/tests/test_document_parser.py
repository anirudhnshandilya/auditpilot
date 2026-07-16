from io import BytesIO

import fitz
import pandas as pd
from docx import Document

from app.services.document_parser import DocumentParser


def test_parse_txt() -> None:
    contents = b"Information security policy"

    result = DocumentParser.parse("policy.txt", contents)

    assert result == "Information security policy"


def test_parse_csv() -> None:
    contents = b"Risk ID,Title\nR001,Weak Passwords\n"

    result = DocumentParser.parse("risks.csv", contents)

    assert "Risk ID,Title" in result
    assert "R001,Weak Passwords" in result


def test_parse_xlsx() -> None:
    dataframe = pd.DataFrame(
        {
            "Risk ID": ["R001"],
            "Title": ["Weak Passwords"],
        }
    )

    buffer = BytesIO()
    dataframe.to_excel(buffer, index=False)

    result = DocumentParser.parse("risks.xlsx", buffer.getvalue())

    assert "Risk ID,Title" in result
    assert "R001,Weak Passwords" in result


def test_parse_docx() -> None:
    document = Document()
    document.add_paragraph("Access control policy")

    buffer = BytesIO()
    document.save(buffer)

    result = DocumentParser.parse("policy.docx", buffer.getvalue())

    assert result == "Access control policy"


def test_parse_pdf() -> None:
    document = fitz.open()
    page = document.new_page()
    page.insert_text((72, 72), "Business continuity plan")
    contents = document.tobytes()
    document.close()

    result = DocumentParser.parse("plan.pdf", contents)

    assert "Business continuity plan" in result


def test_reject_unsupported_document_type() -> None:
    try:
        DocumentParser.parse("malware.exe", b"unsupported")
    except ValueError as exc:
        assert str(exc) == "Unsupported document type: .exe"
    else:
        raise AssertionError("Expected ValueError")