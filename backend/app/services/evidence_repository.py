from uuid import UUID, uuid4

from app.services.evidence_models import EvidenceDocument


class EvidenceRepository:
    def __init__(self) -> None:
        self._documents: dict[UUID, EvidenceDocument] = {}

    def add(self, document: EvidenceDocument) -> UUID:
        document_id = uuid4()
        self._documents[document_id] = document
        return document_id

    def list(self) -> list[tuple[UUID, EvidenceDocument]]:
        return list(self._documents.items())

    def get(self, document_id: UUID) -> EvidenceDocument | None:
        return self._documents.get(document_id)

    def delete(self, document_id: UUID) -> bool:
        return self._documents.pop(document_id, None) is not None