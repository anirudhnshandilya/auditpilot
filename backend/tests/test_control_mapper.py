from app.frameworks.mapper import ControlMapper


def test_maps_policy_to_a_5_1() -> None:
    mappings = ControlMapper.map_text(
        "Information Security Policy Version 1.0 "
        "Approved by the CISO after policy review."
    )

    assert len(mappings) >= 1
    assert mappings[0].control_id == "A.5.1"
    assert mappings[0].confidence == 1.0


def test_maps_roles_document_to_a_5_2() -> None:
    mappings = ControlMapper.map_text(
        "This RACI matrix defines information security "
        "roles and responsibilities and accountability."
    )

    assert len(mappings) >= 1
    assert mappings[0].control_id == "A.5.2"
    assert mappings[0].confidence >= 0.5


def test_unknown_text_returns_no_mappings() -> None:
    mappings = ControlMapper.map_text(
        "General meeting notes with no security content."
    )

    assert mappings == []


def test_results_are_sorted_by_confidence() -> None:
    mappings = ControlMapper.map_text(
        "Information Security Policy approved by the CISO. "
        "The document also mentions accountability."
    )

    confidences = [mapping.confidence for mapping in mappings]

    assert confidences == sorted(confidences, reverse=True)