import pandas as pd
import pytest


@pytest.fixture
def valid_risk_dataframe():
    return pd.DataFrame(
        {
            "Risk ID": ["R001"],
            "Title": ["Weak Passwords"],
            "Description": ["Password reuse across systems"],
            "Owner": ["IT"],
            "Treatment": ["Implement MFA"],
            "Likelihood": [4],
            "Impact": [5],
            "Review Date": ["2027-01-01"],
        }
    )