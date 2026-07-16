import pandas as pd

from app.validators.models import Finding
from app.validators.rules.base import ValidationRule
from app.validators.severity import Severity


class RequiredColumnsRule(ValidationRule):

    REQUIRED_COLUMNS = [
        "Risk ID",
        "Title",
        "Description",
        "Owner",
        "Treatment",
        "Likelihood",
        "Impact",
        "Review Date",
    ]

    def validate(self, df: pd.DataFrame) -> list[Finding]:
        findings = []

        for column in self.REQUIRED_COLUMNS:
            if column not in df.columns:
                findings.append(
                    Finding(
                        severity=Severity.CRITICAL,
                        row=0,
                        column=column,
                        message=f"Missing required column: {column}",
                        recommendation=f"Add column '{column}'.",
                    )
                )

        return findings