from app.frameworks.models import Control
from app.frameworks.registry import FRAMEWORK_REGISTRY


class FrameworkService:
    @staticmethod
    def get_framework(
        framework: str,
    ) -> list[Control]:
        return FRAMEWORK_REGISTRY.get(framework, [])

    @staticmethod
    def get_iso27001_controls() -> list[Control]:
        return FrameworkService.get_framework("iso27001")

    @staticmethod
    def get_control(control_id: str) -> Control | None:
        controls = FrameworkService.get_iso27001_controls()

        for control in controls:
            if control.id == control_id:
                return control

        return None

    @staticmethod
    def list_frameworks() -> list[str]:
        return sorted(FRAMEWORK_REGISTRY.keys())