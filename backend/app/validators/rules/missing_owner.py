import pandas as pd

from app.validators.models import Finding
from app.validators.rules.base import ValidationRule
from app.validators.severity import Severity


class MissingOwnerRule(ValidationRule):
    name = "missing-owner"
    description = "Detect risks without an assigned owner."

    def validate(self, df: pd.DataFrame) -> list[Finding]:
        if "Owner" not in df.columns:
            return []

        findings: list[Finding] = []
        missing_owner_mask = df["Owner"].isna() | (
            df["Owner"].astype(str).str.strip() == ""
        )

        for index in df.index[missing_owner_mask]:
            findings.append(
                Finding(
                    severity=Severity.HIGH,
                    row=int(index) + 2,
                    column="Owner",
                    message="Risk has no assigned owner.",
                    recommendation="Assign an accountable owner to the risk.",
                )
            )

        return findings