from fastapi.testclient import TestClient

from app.main import app
from io import BytesIO

from app.services.evidence_service import evidence_repository


client = TestClient(app)


def test_list_iso27001_controls() -> None:
    response = client.get("/frameworks/iso27001")

    assert response.status_code == 200

    body = response.json()

    assert len(body) == 2
    assert body[0]["id"] == "A.5.1"
    assert body[1]["id"] == "A.5.2"


def test_get_iso27001_control() -> None:
    response = client.get("/frameworks/iso27001/A.5.1")

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == "A.5.1"
    assert body["title"] == "Policies for information security"
    assert "Information Security Policy" in body["expected_evidence"]


def test_get_unknown_control_returns_404() -> None:
    response = client.get("/frameworks/iso27001/A.99.99")

    assert response.status_code == 404
    assert response.json() == {"detail": "Control not found."}

def setup_function() -> None:
    evidence_repository._documents.clear()


def test_iso27001_coverage_with_no_evidence() -> None:
    response = client.get("/frameworks/iso27001/coverage")

    assert response.status_code == 200

    body = response.json()

    assert body["total_controls"] == 2
    assert body["covered_controls"] == 0
    assert body["uncovered_controls"] == 2
    assert body["coverage_percentage"] == 0.0
    assert body["covered_control_ids"] == []
    assert body["uncovered_control_ids"] == ["A.5.1", "A.5.2"]


def test_iso27001_coverage_after_policy_upload() -> None:
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

    response = client.get("/frameworks/iso27001/coverage")

    assert response.status_code == 200

    body = response.json()

    assert body["covered_controls"] == 1
    assert body["coverage_percentage"] == 50.0
    assert body["covered_control_ids"] == ["A.5.1"]
    assert body["uncovered_control_ids"] == ["A.5.2"]

def test_iso27001_gaps_with_no_evidence() -> None:
    response = client.get("/frameworks/iso27001/gaps")

    assert response.status_code == 200

    body = response.json()

    assert len(body) == 2
    assert body[0]["control_id"] == "A.5.1"
    assert body[1]["control_id"] == "A.5.2"


def test_iso27001_gaps_after_policy_upload() -> None:
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

    response = client.get("/frameworks/iso27001/gaps")

    assert response.status_code == 200

    body = response.json()

    assert len(body) == 1
    assert body[0]["control_id"] == "A.5.2"
    assert (
        body[0]["control_title"]
        == "Information security roles and responsibilities"
    )

def test_iso27001_score_with_no_evidence() -> None:
    response = client.get("/frameworks/iso27001/score")

    assert response.status_code == 200

    body = response.json()

    assert body["score"] == 0
    assert body["rating"] == "Poor"
    assert body["covered_controls"] == 0
    assert body["uncovered_controls"] == 2
    assert body["coverage_percentage"] == 0.0


def test_iso27001_score_after_policy_upload() -> None:
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

    response = client.get("/frameworks/iso27001/score")

    assert response.status_code == 200

    body = response.json()

    assert body["score"] == 50
    assert body["rating"] == "Needs Improvement"
    assert body["covered_controls"] == 1
    assert body["uncovered_controls"] == 1
    assert body["coverage_percentage"] == 50.0