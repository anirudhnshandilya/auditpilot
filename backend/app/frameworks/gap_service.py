from app.frameworks.coverage_service import CoverageService
from app.frameworks.gaps import ComplianceGap
from app.frameworks.service import FrameworkService
from app.services.evidence_models import EvidenceDocument


class GapService:
    @staticmethod
    def detect(
        documents: list[EvidenceDocument],
    ) -> list[ComplianceGap]:
        coverage = CoverageService.analyse(documents)

        gaps: list[ComplianceGap] = []

        for control_id in coverage.uncovered_control_ids:
            control = FrameworkService.get_control(control_id)

            if control is None:
                continue

            gaps.append(
                ComplianceGap(
                    control_id=control.id,
                    control_title=control.title,
                    expected_evidence=control.expected_evidence,
                    severity="Medium",
                    recommendation=(
                        f"Provide evidence for {control.id} "
                        f"({control.title})."
                    ),
                )
            )

        return gaps