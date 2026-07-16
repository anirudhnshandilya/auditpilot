from abc import ABC, abstractmethod

import pandas as pd

from app.validators.models import Finding


class ValidationRule(ABC):
    name: str
    description: str

    @abstractmethod
    def validate(self, df: pd.DataFrame) -> list[Finding]:
        """Execute the validation rule."""
        pass