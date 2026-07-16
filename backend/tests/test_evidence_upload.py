from io import BytesIO

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_upload_text_document() -> None:
    response = client.post(
        "/evidence/upload",
        files={
            "file": (
                "policy.txt",
                BytesIO(b"Information Security Policy"),
                "text/plain",
            )
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["filename"] == "policy.txt"
    assert body["processing_status"] == "Processed"
    assert body["evidence_status"] == "Present"
    assert body["extracted_text_length"] > 0


def test_reject_empty_file() -> None:
    response = client.post(
        "/evidence/upload",
        files={
            "file": (
                "policy.txt",
                BytesIO(b""),
                "text/plain",
            )
        },
    )

    assert response.status_code == 400


def test_reject_unsupported_extension() -> None:
    response = client.post(
        "/evidence/upload",
        files={
            "file": (
                "virus.exe",
                BytesIO(b"abc"),
                "application/octet-stream",
            )
        },
    )

    assert response.status_code == 400