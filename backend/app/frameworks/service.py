from app.frameworks.iso27001 import ISO27001_CONTROLS
from app.frameworks.models import Control


class FrameworkService:
    @staticmethod
    def get_iso27001_controls() -> list[Control]:
        return ISO27001_CONTROLS

    @staticmethod
    def get_control(control_id: str) -> Control | None:
        for control in ISO27001_CONTROLS:
            if control.id == control_id:
                return control
        return None