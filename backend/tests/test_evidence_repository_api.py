from io import BytesIO

from fastapi.testclient import TestClient

from app.main import app
from app.services.evidence_service import evidence_repository

client = TestClient(app)


def setup_function() -> None:
    evidence_repository._documents.clear()


def test_upload_and_list_evidence() -> None:
    upload_response = client.post(
        "/evidence/upload",
        files={
            "file": (
                "policy.txt",
                BytesIO(b"Information Security Policy"),
                "text/plain",
            )
        },
    )

    assert upload_response.status_code == 200
    document_id = upload_response.json()["id"]

    list_response = client.get("/evidence")

    assert list_response.status_code == 200
    body = list_response.json()

    assert len(body) == 1
    assert body[0]["id"] == document_id
    assert body[0]["filename"] == "policy.txt"


def test_get_evidence_by_id() -> None:
    upload_response = client.post(
        "/evidence/upload",
        files={
            "file": (
                "policy.txt",
                BytesIO(b"Information Security Policy"),
                "text/plain",
            )
        },
    )

    document_id = upload_response.json()["id"]

    response = client.get(f"/evidence/{document_id}")

    assert response.status_code == 200
    assert response.json()["id"] == document_id
    assert response.json()["filename"] == "policy.txt"


def test_delete_evidence() -> None:
    upload_response = client.post(
        "/evidence/upload",
        files={
            "file": (
                "policy.txt",
                BytesIO(b"Information Security Policy"),
                "text/plain",
            )
        },
    )

    document_id = upload_response.json()["id"]

    delete_response = client.delete(f"/evidence/{document_id}")

    assert delete_response.status_code == 200
    assert delete_response.json() == {"status": "deleted"}

    get_response = client.get(f"/evidence/{document_id}")

    assert get_response.status_code == 404


def test_get_unknown_evidence_returns_404() -> None:
    response = client.get(
        "/evidence/00000000-0000-0000-0000-000000000000"
    )

    assert response.status_code == 404