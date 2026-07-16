import pandas as pd

from app.validators.models import Finding
from app.validators.rules.base import ValidationRule
from app.validators.severity import Severity


class InvalidReviewDateRule(ValidationRule):
    name = "invalid-review-date"
    description = "Detect invalid review dates."

    def validate(self, df: pd.DataFrame) -> list[Finding]:
        if "Review Date" not in df.columns:
            return []

        findings: list[Finding] = []

        review_date = df["Review Date"].astype(str).str.strip()
        dates = pd.to_datetime(review_date, errors="coerce")

        invalid = (
            dates.isna()
            & review_date.ne("")
            & df["Review Date"].notna()
        )

        for index in df.index[invalid]:
            findings.append(
                Finding(
                    severity=Severity.MEDIUM,
                    row=int(index) + 2,
                    column="Review Date",
                    message="Invalid review date.",
                    recommendation="Use a valid date format (YYYY-MM-DD).",
                )
            )

        return findings