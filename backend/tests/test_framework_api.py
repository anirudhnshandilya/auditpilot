from fastapi.testclient import TestClient

from app.main import app

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