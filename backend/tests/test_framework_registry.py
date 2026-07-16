from app.frameworks.service import FrameworkService


def test_list_frameworks() -> None:
    frameworks = FrameworkService.list_frameworks()

    assert frameworks == ["iso27001"]


def test_get_framework() -> None:
    controls = FrameworkService.get_framework("iso27001")

    assert len(controls) == 2
    assert controls[0].id == "A.5.1"


def test_unknown_framework_returns_empty_list() -> None:
    controls = FrameworkService.get_framework("nist")

    assert controls == []