from io import BytesIO

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_upload_valid_csv() -> None:
    csv_content = (
        b"Risk ID,Title,Owner,Likelihood,Impact\n"
        b"R001,Weak Password Policy,IT Manager,4,5\n"
        b"R002,Missing MFA,Security Team,5,5\n"
    )

    response = client.post(
        "/upload/risk-register",
        files={
            "file": (
                "risk-register.csv",
                BytesIO(csv_content),
                "text/csv",
            )
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "filename": "risk-register.csv",
        "status": "uploaded",
        "rows": 2,
        "columns": 5,
        "column_names": [
            "Risk ID",
            "Title",
            "Owner",
            "Likelihood",
            "Impact",
        ],
    }


def test_reject_unsupported_file_type() -> None:
    response = client.post(
        "/upload/risk-register",
        files={
            "file": (
                "risk-register.txt",
                BytesIO(b"unsupported"),
                "text/plain",
            )
        },
    )

    assert response.status_code == 400


def test_reject_empty_file() -> None:
    response = client.post(
        "/upload/risk-register",
        files={
            "file": (
                "risk-register.csv",
                BytesIO(b""),
                "text/csv",
            )
        },
    )

    assert response.status_code == 400