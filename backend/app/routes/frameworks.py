from fastapi import APIRouter, HTTPException

from app.frameworks.coverage_service import CoverageService
from app.frameworks.service import FrameworkService
from app.services.evidence_service import evidence_repository
from app.frameworks.gap_service import GapService
from app.frameworks.scoring_service import ScoringService

router = APIRouter(prefix="/frameworks", tags=["Frameworks"])


@router.get("/iso27001")
def list_iso27001_controls() -> list[dict[str, object]]:
    controls = FrameworkService.get_iso27001_controls()

    return [
        {
            "id": control.id,
            "title": control.title,
            "description": control.description,
            "expected_evidence": control.expected_evidence,
            "keywords": control.keywords,
            "related_controls": control.related_controls,
        }
        for control in controls
    ]


@router.get("/iso27001/coverage")
def get_iso27001_coverage() -> dict[str, object]:
    documents = [
        evidence
        for _, evidence in evidence_repository.list()
    ]

    coverage = CoverageService.analyse(documents)

    return {
        "total_controls": coverage.total_controls,
        "covered_controls": coverage.covered_controls,
        "uncovered_controls": coverage.uncovered_controls,
        "coverage_percentage": coverage.coverage_percentage,
        "covered_control_ids": coverage.covered_control_ids,
        "uncovered_control_ids": coverage.uncovered_control_ids,
    }

@router.get("/iso27001/score")
def get_iso27001_score() -> dict[str, object]:
    documents = [
        evidence
        for _, evidence in evidence_repository.list()
    ]

    score = ScoringService.calculate(documents)

    return {
        "score": score.score,
        "rating": score.rating,
        "covered_controls": score.covered_controls,
        "uncovered_controls": score.uncovered_controls,
        "coverage_percentage": score.coverage_percentage,
    }

@router.get("/iso27001/gaps")
def get_iso27001_gaps() -> list[dict[str, object]]:
    documents = [
        evidence
        for _, evidence in evidence_repository.list()
    ]

    gaps = GapService.detect(documents)

    return [
        {
            "control_id": gap.control_id,
            "control_title": gap.control_title,
            "expected_evidence": gap.expected_evidence,
            "severity": gap.severity,
            "recommendation": gap.recommendation,
        }
        for gap in gaps
    ]

@router.get("/iso27001/{control_id}")
def get_iso27001_control(control_id: str) -> dict[str, object]:
    control = FrameworkService.get_control(control_id)

    if control is None:
        raise HTTPException(
            status_code=404,
            detail="Control not found.",
        )

    return {
        "id": control.id,
        "title": control.title,
        "description": control.description,
        "expected_evidence": control.expected_evidence,
        "keywords": control.keywords,
        "related_controls": control.related_controls,
    }