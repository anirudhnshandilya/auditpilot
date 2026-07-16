import pandas as pd

from app.validators.models import Finding
from app.validators.rules.base import ValidationRule
from app.validators.severity import Severity


class MissingDescriptionRule(ValidationRule):
    name = "missing-description"
    description = "Detect risks without a description."

    def validate(self, df: pd.DataFrame) -> list[Finding]:
        if "Description" not in df.columns:
            return []

        findings: list[Finding] = []
        missing = df["Description"].isna() | (
            df["Description"].astype(str).str.strip() == ""
        )

        for index in df.index[missing]:
            findings.append(
                Finding(
                    severity=Severity.MEDIUM,
                    row=int(index) + 2,
                    column="Description",
                    message="Risk has no description.",
                    recommendation="Provide a clear risk description.",
                )
            )

        return findings