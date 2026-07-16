import pandas as pd

from app.validators.engine import ValidationEngine


def test_duplicate_risk_ids_create_findings(
    valid_risk_dataframe: pd.DataFrame,
) -> None:
    dataframe = pd.concat(
    [valid_risk_dataframe, valid_risk_dataframe],
    ignore_index=True,
)

    dataframe.loc[1, "Title"] = "Missing MFA"
    dataframe.loc[1, "Description"] = "MFA is not enabled."

    result = ValidationEngine().validate(dataframe)

    assert result.score == 80
    assert result.audit_readiness == "Needs Improvement"
    assert len(result.findings) == 2
    assert all(finding.severity == "High" for finding in result.findings)
    assert all(finding.column == "Risk ID" for finding in result.findings)


def test_unique_risk_ids_create_no_findings(
    valid_risk_dataframe: pd.DataFrame,
) -> None:
    result = ValidationEngine().validate(valid_risk_dataframe)

    assert result.score == 100
    assert result.audit_readiness == "Ready"
    assert result.findings == []


def test_missing_owner_creates_finding(
    valid_risk_dataframe: pd.DataFrame,
) -> None:
    dataframe = valid_risk_dataframe.copy()
    dataframe.loc[0, "Owner"] = ""

    result = ValidationEngine().validate(dataframe)

    assert result.score == 90
    assert result.audit_readiness == "Ready"
    assert len(result.findings) == 1
    assert result.findings[0].column == "Owner"
    assert result.findings[0].message == "Risk has no assigned owner."


def test_invalid_likelihood_creates_finding(
    valid_risk_dataframe: pd.DataFrame,
) -> None:
    dataframe = valid_risk_dataframe.copy()
    dataframe.loc[0, "Likelihood"] = 9

    result = ValidationEngine().validate(dataframe)

    assert result.score == 90
    assert result.audit_readiness == "Ready"
    assert len(result.findings) == 1
    assert result.findings[0].column == "Likelihood"
    assert result.findings[0].message == "Invalid likelihood value: 9"


def test_invalid_impact_creates_finding(
    valid_risk_dataframe: pd.DataFrame,
) -> None:
    dataframe = valid_risk_dataframe.copy()
    dataframe.loc[0, "Impact"] = 8

    result = ValidationEngine().validate(dataframe)

    assert result.score == 90
    assert result.audit_readiness == "Ready"
    assert len(result.findings) == 1
    assert result.findings[0].column == "Impact"
    assert result.findings[0].message == "Invalid impact value: 8"


def test_missing_title_creates_finding(
    valid_risk_dataframe: pd.DataFrame,
) -> None:
    dataframe = valid_risk_dataframe.copy()
    dataframe.loc[0, "Title"] = ""

    result = ValidationEngine().validate(dataframe)

    assert result.score == 90
    assert result.audit_readiness == "Ready"
    assert len(result.findings) == 1
    assert result.findings[0].column == "Title"
    assert result.findings[0].message == "Risk has no title."


def test_empty_risk_id_creates_finding(
    valid_risk_dataframe: pd.DataFrame,
) -> None:
    dataframe = valid_risk_dataframe.copy()
    dataframe.loc[0, "Risk ID"] = ""

    result = ValidationEngine().validate(dataframe)

    assert len(result.findings) == 1
    assert result.findings[0].column == "Risk ID"


def test_missing_description_creates_finding(
    valid_risk_dataframe: pd.DataFrame,
) -> None:
    dataframe = valid_risk_dataframe.copy()
    dataframe.loc[0, "Description"] = ""

    result = ValidationEngine().validate(dataframe)

    assert len(result.findings) == 1
    assert result.findings[0].column == "Description"


def test_missing_treatment_creates_finding(
    valid_risk_dataframe: pd.DataFrame,
) -> None:
    dataframe = valid_risk_dataframe.copy()
    dataframe.loc[0, "Treatment"] = ""

    result = ValidationEngine().validate(dataframe)

    assert len(result.findings) == 1
    assert result.findings[0].column == "Treatment"


def test_missing_review_date_creates_finding(
    valid_risk_dataframe: pd.DataFrame,
) -> None:
    dataframe = valid_risk_dataframe.copy()
    dataframe.loc[0, "Review Date"] = ""

    result = ValidationEngine().validate(dataframe)

    assert len(result.findings) == 1
    assert result.findings[0].column == "Review Date"


def test_invalid_review_date_creates_finding(
    valid_risk_dataframe: pd.DataFrame,
) -> None:
    dataframe = valid_risk_dataframe.copy()
    dataframe.loc[0, "Review Date"] = "not-a-date"

    result = ValidationEngine().validate(dataframe)

    assert any(
        finding.message == "Invalid review date."
        for finding in result.findings
    )


def test_past_due_review_date_creates_finding(
    valid_risk_dataframe: pd.DataFrame,
) -> None:
    dataframe = valid_risk_dataframe.copy()
    dataframe.loc[0, "Review Date"] = "2023-01-01"

    result = ValidationEngine().validate(dataframe)

    assert any(
        finding.message == "Review date has passed."
        for finding in result.findings
    )

def test_duplicate_rows_create_findings(
    valid_risk_dataframe: pd.DataFrame,
) -> None:
    dataframe = pd.concat(
        [valid_risk_dataframe, valid_risk_dataframe],
        ignore_index=True,
    )

    result = ValidationEngine().validate(dataframe)

    duplicate_row_findings = [
        finding
        for finding in result.findings
        if finding.message == "Duplicate row detected."
    ]

    assert len(duplicate_row_findings) == 2


def test_empty_row_creates_finding(
    valid_risk_dataframe: pd.DataFrame,
) -> None:
    empty_row = pd.DataFrame(
        [{column: None for column in valid_risk_dataframe.columns}]
    )
    dataframe = pd.concat(
        [valid_risk_dataframe, empty_row],
        ignore_index=True,
    )

    result = ValidationEngine().validate(dataframe)

    assert any(
        finding.message == "Empty row detected."
        for finding in result.findings
    )


def test_missing_required_column_creates_finding(
    valid_risk_dataframe: pd.DataFrame,
) -> None:
    dataframe = valid_risk_dataframe.drop(columns=["Owner"])

    result = ValidationEngine().validate(dataframe)

    assert any(
        finding.message == "Missing required column: Owner"
        for finding in result.findings
    )