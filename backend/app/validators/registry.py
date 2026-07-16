from collections.abc import Iterable

from app.validators.rules.base import ValidationRule


class RuleRegistry:
    def __init__(self) -> None:
        self._rules: list[ValidationRule] = []

    def register(self, rule: ValidationRule) -> None:
        self._rules.append(rule)

    def register_many(self, rules: Iterable[ValidationRule]) -> None:
        self._rules.extend(rules)

    @property
    def rules(self) -> list[ValidationRule]:
        return list(self._rules)