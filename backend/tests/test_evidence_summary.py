from io import BytesIO

from fastapi.testclient import TestClient

from app.main import app
from app.services.evidence_service import evidence_repository

client = TestClient(app)


def setup_function() -> None:
    evidence_repository._documents.clear()


def test_empty_summary() -> None:
    response = client.get("/evidence/summary")

    assert response.status_code == 200

    body = response.json()

    assert body["total_documents"] == 0
    assert body["sufficient_documents"] == 0
    assert body["review_required_documents"] == 0
    assert body["invalid_documents"] == 0
    assert body["document_types"] == {}
    assert body["common_issues"] == []


def test_summary_after_uploads() -> None:
    client.post(
        "/evidence/upload",
        files={
            "file": (
                "policy.txt",
                BytesIO(
                    b"Information Security Policy Version 1.0 Approved by CISO"
                ),
                "text/plain",
            )
        },
    )

    client.post(
        "/evidence/upload",
        files={
            "file": (
                "draft-policy.txt",
                BytesIO(
                    b"Information Security Policy Draft"
                ),
                "text/plain",
            )
        },
    )

    response = client.get("/evidence/summary")

    assert response.status_code == 200

    body = response.json()

    assert body["total_documents"] == 2
    assert body["sufficient_documents"] == 1
    assert body["review_required_documents"] == 1
    assert body["invalid_documents"] == 0

    assert body["document_types"]["Policy"] == 2