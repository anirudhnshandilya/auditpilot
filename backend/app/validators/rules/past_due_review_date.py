import pandas as pd

from app.validators.models import Finding
from app.validators.rules.base import ValidationRule
from app.validators.severity import Severity


class PastDueReviewDateRule(ValidationRule):
    name = "past-due-review-date"
    description = "Detect review dates that are in the past."

    def validate(self, df: pd.DataFrame) -> list[Finding]:
        if "Review Date" not in df.columns:
            return []

        findings: list[Finding] = []

        dates = pd.to_datetime(df["Review Date"], errors="coerce")
        today = pd.Timestamp.today().normalize()

        overdue = dates.notna() & (dates < today)

        for index in df.index[overdue]:
            findings.append(
                Finding(
                    severity=Severity.MEDIUM,
                    row=int(index) + 2,
                    column="Review Date",
                    message="Review date has passed.",
                    recommendation="Update the review date.",
                )
            )

        return findings