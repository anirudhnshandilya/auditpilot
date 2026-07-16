import re
from dataclasses import dataclass

from app.services.evidence_models import EvidenceStatus


@dataclass
class EvidenceStatusResult:
    status: EvidenceStatus
    reasons: list[str]


class EvidenceStatusEngine:
    DRAFT_PATTERNS = (
        r"\bdraft\b",
        r"\bfor review\b",
        r"\binternal draft\b",
    )

    APPROVAL_PATTERNS = (
        r"\bapproved by\b",
        r"\bauthorised by\b",
        r"\bauthorized by\b",
        r"\bapproval date\b",
    )

    VERSION_PATTERNS = (
        r"\bversion\s+\d+(?:\.\d+)*\b",
        r"\bv\d+(?:\.\d+)*\b",
        r"\brevision\s+[a-z0-9]+\b",
        r"\brev\s+[a-z0-9]+\b",
    )

    @classmethod
    def evaluate(cls, extracted_text: str) -> EvidenceStatusResult:
        text = extracted_text.lower()
        reasons: list[str] = []

        if any(re.search(pattern, text) for pattern in cls.DRAFT_PATTERNS):
            reasons.append("Document appears to be a draft.")
            return EvidenceStatusResult(
                status=EvidenceStatus.HUMAN_REVIEW_REQUIRED,
                reasons=reasons,
            )

        has_approval = any(
            re.search(pattern, text)
            for pattern in cls.APPROVAL_PATTERNS
        )
        has_version = any(
            re.search(pattern, text)
            for pattern in cls.VERSION_PATTERNS
        )

        if not has_approval:
            reasons.append("Approval information was not detected.")

        if not has_version:
            reasons.append("Version information was not detected.")

        if reasons:
            return EvidenceStatusResult(
                status=EvidenceStatus.HUMAN_REVIEW_REQUIRED,
                reasons=reasons,
            )

        return EvidenceStatusResult(
            status=EvidenceStatus.SUFFICIENT,
            reasons=[],
        )