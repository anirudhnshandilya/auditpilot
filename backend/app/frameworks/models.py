from dataclasses import dataclass, field


@dataclass(frozen=True)
class Control:
    id: str
    title: str
    description: str
    expected_evidence: list[str] = field(default_factory=list)
    keywords: list[str] = field(default_factory=list)
    related_controls: list[str] = field(default_factory=list)