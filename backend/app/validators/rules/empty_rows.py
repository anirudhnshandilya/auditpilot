import pandas as pd

from app.validators.models import Finding
from app.validators.rules.base import ValidationRule
from app.validators.severity import Severity


class EmptyRowsRule(ValidationRule):
    name = "empty-rows"

    description = "Detect completely empty rows."

    def validate(self, df: pd.DataFrame) -> list[Finding]:
        findings = []

        empty = df.isna().all(axis=1)

        for index in df.index[empty]:
            findings.append(
                Finding(
                    severity=Severity.LOW,
                    row=int(index) + 2,
                    column="Row",
                    message="Empty row detected.",
                    recommendation="Remove empty rows.",
                )
            )

        return findings