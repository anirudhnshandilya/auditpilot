import pandas as pd

from app.validators.models import Finding
from app.validators.rules.base import ValidationRule
from app.validators.severity import Severity


class MissingTreatmentRule(ValidationRule):
    name = "missing-treatment"
    description = "Detect risks without a treatment plan."

    def validate(self, df: pd.DataFrame) -> list[Finding]:
        if "Treatment" not in df.columns:
            return []

        findings: list[Finding] = []
        missing = df["Treatment"].isna() | (
            df["Treatment"].astype(str).str.strip() == ""
        )

        for index in df.index[missing]:
            findings.append(
                Finding(
                    severity=Severity.HIGH,
                    row=int(index) + 2,
                    column="Treatment",
                    message="Risk has no treatment plan.",
                    recommendation="Document a treatment plan for the risk.",
                )
            )

        return findings