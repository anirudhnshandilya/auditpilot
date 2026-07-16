import pandas as pd

from app.validators.models import Finding
from app.validators.rules.base import ValidationRule
from app.validators.severity import Severity


class MissingTitleRule(ValidationRule):
    name = "missing-title"
    description = "Detect risks without a title."

    def validate(self, df: pd.DataFrame) -> list[Finding]:
        if "Title" not in df.columns:
            return []

        findings: list[Finding] = []
        missing_title_mask = df["Title"].isna() | (
            df["Title"].astype(str).str.strip() == ""
        )

        for index in df.index[missing_title_mask]:
            findings.append(
                Finding(
                    severity=Severity.MEDIUM,
                    row=int(index) + 2,
                    column="Title",
                    message="Risk has no title.",
                    recommendation="Add a clear and concise risk title.",
                )
            )

        return findings