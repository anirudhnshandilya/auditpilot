import pandas as pd

from app.validators.models import Finding
from app.validators.rules.base import ValidationRule
from app.validators.severity import Severity


class InvalidImpactRule(ValidationRule):
    name = "invalid-impact"
    description = "Detect impact values outside the accepted range of 1 to 5."

    def validate(self, df: pd.DataFrame) -> list[Finding]:
        if "Impact" not in df.columns:
            return []

        findings: list[Finding] = []
        impact = pd.to_numeric(df["Impact"], errors="coerce")
        invalid_mask = impact.isna() | ~impact.between(1, 5)

        for index in df.index[invalid_mask]:
            findings.append(
                Finding(
                    severity=Severity.HIGH,
                    row=int(index) + 2,
                    column="Impact",
                    message=f"Invalid impact value: {df.at[index, 'Impact']}",
                    recommendation="Use a numeric impact value between 1 and 5.",
                )
            )

        return findings