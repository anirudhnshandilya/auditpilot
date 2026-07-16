from app.services.document_classifier import DocumentClassifier
from app.services.evidence_models import DocumentType


def test_classifies_policy() -> None:
    result = DocumentClassifier.classify(
        filename="information-security-policy.txt",
        extracted_text="This policy defines access control requirements.",
    )

    assert result == DocumentType.POLICY


def test_classifies_risk_register() -> None:
    result = DocumentClassifier.classify(
        filename="risks.csv",
        extracted_text="Risk ID,Likelihood,Impact,Risk Owner",
    )

    assert result == DocumentType.RISK_REGISTER


def test_classifies_asset_register() -> None:
    result = DocumentClassifier.classify(
        filename="assets.xlsx",
        extracted_text="Asset ID,Asset Owner,Classification,Criticality",
    )

    assert result == DocumentType.ASSET_REGISTER


def test_unknown_document_type() -> None:
    result = DocumentClassifier.classify(
        filename="notes.txt",
        extracted_text="General meeting notes with no compliance context.",
    )

    assert result == DocumentType.UNKNOWN