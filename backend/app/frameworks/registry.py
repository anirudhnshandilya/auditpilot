from app.frameworks.iso27001 import ISO27001_CONTROLS
from app.frameworks.models import Control


FRAMEWORK_REGISTRY: dict[str, list[Control]] = {
    "iso27001": ISO27001_CONTROLS,
}