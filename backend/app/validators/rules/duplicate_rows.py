import pandas as pd

from app.validators.models import Finding
from app.validators.rules.base import ValidationRule
from app.validators.severity import Severity

class DuplicateRowsRule(ValidationRule):
    name = "duplicate-rows"
    description = "Detect duplicate rows."

    def validate(self, df: pd.DataFrame) -> list[Finding]:
        findings = []

        duplicates = df.duplicated(keep=False)

        for index in df.index[duplicates]:
            findings.append(
                Finding(
                    severity=Severity.MEDIUM,
                    row=int(index) + 2,
                    column="Row",
                    message="Duplicate row detected.",
                    recommendation="Remove duplicate records.",
                )
            )

        return findings