from io import BytesIO

from fastapi.testclient import TestClient

from app.main import app
from app.services.evidence_service import evidence_repository

client = TestClient(app)


def setup_function() -> None:
    evidence_repository._documents.clear()


def test_no_evidence_returns_two_actions() -> None:
    response = client.get("/remediation/actions")

    assert response.status_code == 200

    body = response.json()

    assert len(body) == 2
    assert body[0]["control_id"] == "A.5.1"
    assert body[1]["control_id"] == "A.5.2"


def test_policy_upload_returns_single_action() -> None:
    upload_response = client.post(
        "/evidence/upload",
        files={
            "file": (
                "policy.txt",
                BytesIO(
                    b"Information Security Policy Version 1.0 "
                    b"Approved by the CISO after policy review."
                ),
                "text/plain",
            )
        },
    )

    assert upload_response.status_code == 200

    response = client.get("/remediation/actions")

    assert response.status_code == 200

    body = response.json()

    assert len(body) == 1
    assert body[0]["control_id"] == "A.5.2"
    assert body[0]["priority"] == "Medium"
    assert body[0]["status"] == "Open"