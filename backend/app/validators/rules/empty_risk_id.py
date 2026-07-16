import pandas as pd

from app.validators.models import Finding
from app.validators.rules.base import ValidationRule
from app.validators.severity import Severity

class EmptyRiskIdRule(ValidationRule):
    name = "empty-risk-id"
    description = "Detect empty Risk IDs."

    def validate(self, df: pd.DataFrame) -> list[Finding]:
        if "Risk ID" not in df.columns:
            return []

        findings: list[Finding] = []

        missing = df["Risk ID"].isna() | (
            df["Risk ID"].astype(str).str.strip() == ""
        )

        for index in df.index[missing]:
            findings.append(
                Finding(
                    severity=Severity.CRITICAL,
                    row=int(index) + 2,
                    column="Risk ID",
                    message="Risk ID is missing.",
                    recommendation="Every risk must have a unique Risk ID.",
                )
            )

        return findings