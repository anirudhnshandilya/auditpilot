from dataclasses import dataclass, field
from typing import List
from app.validators.severity import Severity


@dataclass
class Finding:
    severity: Severity
    row: int
    column: str
    message: str
    recommendation: str


@dataclass
class ValidationResult:
    score: int
    audit_readiness: str
    findings: List[Finding] = field(default_factory=list)