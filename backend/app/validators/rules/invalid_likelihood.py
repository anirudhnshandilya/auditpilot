import pandas as pd

from app.validators.models import Finding
from app.validators.rules.base import ValidationRule
from app.validators.severity import Severity


class InvalidLikelihoodRule(ValidationRule):
    name = "invalid-likelihood"
    description = "Detect likelihood values outside the accepted range of 1 to 5."

    def validate(self, df: pd.DataFrame) -> list[Finding]:
        if "Likelihood" not in df.columns:
            return []

        findings: list[Finding] = []
        likelihood = pd.to_numeric(df["Likelihood"], errors="coerce")
        invalid_mask = likelihood.isna() | ~likelihood.between(1, 5)

        for index in df.index[invalid_mask]:
            findings.append(
                Finding(
                    severity=Severity.HIGH,
                    row=int(index) + 2,
                    column="Likelihood",
                    message=f"Invalid likelihood value: {df.at[index, 'Likelihood']}",
                    recommendation="Use a numeric likelihood value between 1 and 5.",
                )
            )

        return findings