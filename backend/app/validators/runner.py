import pandas as pd

from app.validators.models import Finding
from app.validators.registry import RuleRegistry


class RuleRunner:
    def __init__(self, registry: RuleRegistry) -> None:
        self._registry = registry

    def run(self, df: pd.DataFrame) -> list[Finding]:
        findings: list[Finding] = []

        for rule in self._registry.rules:
            findings.extend(rule.validate(df))

        return findings