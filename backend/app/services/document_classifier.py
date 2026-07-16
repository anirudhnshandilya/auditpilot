from app.services.evidence_models import DocumentType


class DocumentClassifier:
    KEYWORDS: dict[DocumentType, tuple[str, ...]] = {
        DocumentType.POLICY: (
            "policy",
            "information security policy",
            "access control policy",
            "acceptable use policy",
        ),
        DocumentType.PROCEDURE: (
            "procedure",
            "process",
            "standard operating procedure",
            "work instruction",
        ),
        DocumentType.RISK_REGISTER: (
            "risk register",
            "risk id",
            "likelihood",
            "impact",
            "risk owner",
        ),
        DocumentType.ASSET_REGISTER: (
            "asset register",
            "asset id",
            "asset owner",
            "classification",
            "criticality",
        ),
        DocumentType.INCIDENT_REGISTER: (
            "incident register",
            "incident id",
            "security incident",
            "incident date",
        ),
        DocumentType.AUDIT_REPORT: (
            "audit report",
            "internal audit",
            "audit finding",
            "nonconformity",
        ),
        DocumentType.TRAINING_RECORD: (
            "training record",
            "security awareness",
            "course completion",
            "attendance record",
        ),
    }

    @classmethod
    def classify(cls, filename: str, extracted_text: str) -> DocumentType:
        searchable_content = f"{filename} {extracted_text}".lower()

        scores: dict[DocumentType, int] = {}

        for document_type, keywords in cls.KEYWORDS.items():
            scores[document_type] = sum(
                1
                for keyword in keywords
                if keyword in searchable_content
            )

        best_match = max(
            scores,
            key=lambda document_type: scores[document_type],
            default=DocumentType.UNKNOWN,
)

        if scores.get(best_match, 0) == 0:
            return DocumentType.UNKNOWN

        return best_match