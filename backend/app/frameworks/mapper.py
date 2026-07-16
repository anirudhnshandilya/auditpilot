from app.frameworks.iso27001 import ISO27001_CONTROLS
from app.frameworks.mapping import ControlMapping


class ControlMapper:
    @staticmethod
    def map_text(text: str) -> list[ControlMapping]:
        text = text.lower()

        mappings: list[ControlMapping] = []

        for control in ISO27001_CONTROLS:
            matched_keywords = [
                keyword
                for keyword in control.keywords
                if keyword.lower() in text
            ]

            if not matched_keywords:
                continue

            confidence = min(
                len(matched_keywords) / len(control.keywords),
                1.0,
            )

            mappings.append(
                ControlMapping(
                    control_id=control.id,
                    confidence=round(confidence, 2),
                    matched_keywords=matched_keywords,
                )
            )

        mappings.sort(
            key=lambda mapping: mapping.confidence,
            reverse=True,
        )

        return mappings