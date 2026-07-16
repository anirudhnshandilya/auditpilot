import pandas as pd

from app.validators.models import Finding
from app.validators.rules.base import ValidationRule
from app.validators.severity import Severity


class MissingReviewDateRule(ValidationRule):
    name = "missing-review-date"
    description = "Detect risks without a review date."

    def validate(self, df: pd.DataFrame) -> list[Finding]:
        if "Review Date" not in df.columns:
            return []

        findings: list[Finding] = []
        missing = df["Review Date"].isna() | (
            df["Review Date"].astype(str).str.strip() == ""
        )

        for index in df.index[missing]:
            findings.append(
                Finding(
                    severity=Severity.MEDIUM,
                    row=int(index) + 2,
                    column="Review Date",
                    message="Risk has no review date.",
                    recommendation="Assign a review date.",
                )
            )

        return findings