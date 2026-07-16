from dataclasses import dataclass


@dataclass(frozen=True)
class ControlMapping:
    control_id: str
    confidence: float
    matched_keywords: list[str]