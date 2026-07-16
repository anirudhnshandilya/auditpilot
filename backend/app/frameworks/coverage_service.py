from app.frameworks.coverage import CoverageResult
from app.frameworks.mapper import ControlMapper
from app.frameworks.service import FrameworkService
from app.services.evidence_models import EvidenceDocument


class CoverageService:
    @staticmethod
    def analyse(
        documents: list[EvidenceDocument],
    ) -> CoverageResult:
        controls = FrameworkService.get_iso27001_controls()

        covered_control_ids: set[str] = set()

        for document in documents:
            mappings = ControlMapper.map_text(document.extracted_text)

            covered_control_ids.update(
                mapping.control_id
                for mapping in mappings
            )

        all_control_ids = {
            control.id
            for control in controls
        }

        uncovered_control_ids = all_control_ids - covered_control_ids

        total_controls = len(all_control_ids)
        covered_controls = len(covered_control_ids)

        coverage_percentage = (
            round((covered_controls / total_controls) * 100, 2)
            if total_controls > 0
            else 0.0
        )

        return CoverageResult(
            total_controls=total_controls,
            covered_controls=covered_controls,
            uncovered_controls=len(uncovered_control_ids),
            coverage_percentage=coverage_percentage,
            covered_control_ids=sorted(covered_control_ids),
            uncovered_control_ids=sorted(uncovered_control_ids),
        )