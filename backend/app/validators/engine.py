import pandas as pd

from app.validators.models import ValidationResult
from app.validators.registry import RuleRegistry
from app.validators.rules.duplicate_risk_id import DuplicateRiskIdRule
from app.validators.runner import RuleRunner
from app.validators.rules.missing_owner import MissingOwnerRule
from app.validators.rules.invalid_likelihood import InvalidLikelihoodRule
from app.validators.rules.invalid_impact import InvalidImpactRule
from app.validators.rules.missing_title import MissingTitleRule
from app.validators.rules.empty_risk_id import EmptyRiskIdRule
from app.validators.rules.missing_description import MissingDescriptionRule
from app.validators.rules.invalid_review_date import InvalidReviewDateRule
from app.validators.rules.missing_review_date import MissingReviewDateRule
from app.validators.rules.missing_treatment import MissingTreatmentRule
from app.validators.rules.past_due_review_date import PastDueReviewDateRule
from app.validators.rules.duplicate_rows import DuplicateRowsRule
from app.validators.rules.empty_rows import EmptyRowsRule
from app.validators.rules.required_columns import RequiredColumnsRule

class ValidationEngine:
    def __init__(self) -> None:
        registry = RuleRegistry()
        registry.register_many(
    [
        DuplicateRiskIdRule(),
        EmptyRiskIdRule(),
        MissingOwnerRule(),
        MissingTitleRule(),
        MissingDescriptionRule(),
        MissingTreatmentRule(),
        MissingReviewDateRule(),
        InvalidReviewDateRule(),
        PastDueReviewDateRule(),
        InvalidLikelihoodRule(),
        InvalidImpactRule(),
        DuplicateRowsRule(),
        EmptyRowsRule(),
        RequiredColumnsRule(),
    ]
)
        self._runner = RuleRunner(registry)

    def validate(self, df: pd.DataFrame) -> ValidationResult:
        findings = self._runner.run(df)

        score = max(0, 100 - (len(findings) * 10))

        if score >= 90:
            readiness = "Ready"
        elif score >= 70:
            readiness = "Needs Improvement"
        else:
            readiness = "Not Ready"

        return ValidationResult(
            score=score,
            audit_readiness=readiness,
            findings=findings,
        )