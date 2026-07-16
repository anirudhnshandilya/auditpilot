from app.frameworks.coverage_service import CoverageService
from app.frameworks.scoring import ComplianceScore
from app.services.evidence_models import EvidenceDocument


class ScoringService:
    @staticmethod
    def calculate(
        documents: list[EvidenceDocument],
    ) -> ComplianceScore:
        coverage = CoverageService.analyse(documents)

        percentage = coverage.coverage_percentage

        if percentage >= 90:
            rating = "Excellent"
        elif percentage >= 75:
            rating = "Good"
        elif percentage >= 50:
            rating = "Needs Improvement"
        else:
            rating = "Poor"

        return ComplianceScore(
            score=round(percentage),
            rating=rating,
            covered_controls=coverage.covered_controls,
            uncovered_controls=coverage.uncovered_controls,
            coverage_percentage=percentage,
        )