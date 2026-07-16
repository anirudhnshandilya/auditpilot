import pandas as pd

from app.validators.models import Finding
from app.validators.rules.base import ValidationRule
from app.validators.severity import Severity


class DuplicateRiskIdRule(ValidationRule):
    name = "duplicate-risk-id"
    description = "Detect duplicate values in the Risk ID column."

    def validate(self, df: pd.DataFrame) -> list[Finding]:
        if "Risk ID" not in df.columns:
            return []

        findings: list[Finding] = []
        duplicate_mask = df["Risk ID"].duplicated(keep=False)

        for index in df.index[duplicate_mask]:
            findings.append(
                Finding(
                    severity=Severity.HIGH,
                    row=int(index) + 2,
                    column="Risk ID",
                    message=f"Duplicate Risk ID: {df.at[index, 'Risk ID']}",
                    recommendation="Ensure every risk has a unique Risk ID.",
                )
            )

        return findings