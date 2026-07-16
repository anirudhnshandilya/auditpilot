import pandas as pd

from app.validators.models import Finding
from app.validators.severity import Severity


def validate_risk_register(df: pd.DataFrame) -> list[Finding]:
    findings: list[Finding] = []

    required_columns = [
        "Risk ID",
        "Title",
        "Owner",
        "Likelihood",
        "Impact",
    ]

    for column in required_columns:
        if column not in df.columns:
            findings.append(
                Finding(
                    severity=Severity.CRITICAL,
                    row=0,
                    column=column,
                    message=f"Missing required column: {column}",
                    recommendation=f"Add the '{column}' column.",
                )
            )

    return findings