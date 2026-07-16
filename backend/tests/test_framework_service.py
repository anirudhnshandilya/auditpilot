from app.frameworks.service import FrameworkService


def test_get_iso27001_controls() -> None:
    controls = FrameworkService.get_iso27001_controls()

    assert len(controls) == 2
    assert controls[0].id == "A.5.1"
    assert controls[1].id == "A.5.2"


def test_get_control_by_id() -> None:
    control = FrameworkService.get_control("A.5.1")

    assert control is not None
    assert control.title == "Policies for information security"


def test_get_unknown_control_returns_none() -> None:
    control = FrameworkService.get_control("A.99.99")

    assert control is None