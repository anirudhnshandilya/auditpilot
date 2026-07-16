from collections import Counter
from dataclasses import dataclass

from app.services.evidence_models import (
    EvidenceDocument,
    EvidenceStatus,
)


@dataclass
class EvidenceSummary:
    total_documents: int
    sufficient_documents: int
    review_required_documents: int
    invalid_documents: int
    document_types: dict[str, int]
    common_issues: list[str]


class EvidenceSummaryService:
    @staticmethod
    def summarize(
        documents: list[EvidenceDocument],
    ) -> EvidenceSummary:
        document_counter = Counter(
            document.document_type.value
            for document in documents
        )

        sufficient = sum(
            document.evidence_status == EvidenceStatus.SUFFICIENT
            for document in documents
        )

        review_required = sum(
            document.evidence_status
            == EvidenceStatus.HUMAN_REVIEW_REQUIRED
            for document in documents
        )

        invalid = sum(
            document.evidence_status == EvidenceStatus.INVALID
            for document in documents
        )

        issues: Counter[str] = Counter()

        for document in documents:
            text = document.extracted_text.lower()

            if "approved by" not in text:
                issues["Missing approval"] += 1

            if (
                "version" not in text
                and "v1" not in text
                and "rev" not in text
            ):
                issues["Missing version"] += 1

            if "draft" in text:
                issues["Draft document"] += 1

        return EvidenceSummary(
            total_documents=len(documents),
            sufficient_documents=sufficient,
            review_required_documents=review_required,
            invalid_documents=invalid,
            document_types=dict(document_counter),
            common_issues=[
                issue
                for issue, _ in issues.most_common(5)
            ],
        )