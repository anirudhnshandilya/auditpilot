from app.frameworks.models import Control


ISO27001_CONTROLS: list[Control] = [
    Control(
        id="A.5.1",
        title="Policies for information security",
        description=(
            "Information security policies should be defined, approved, "
            "communicated, and reviewed."
        ),
        expected_evidence=[
            "Information Security Policy",
            "Policy approval record",
            "Policy review record",
        ],
        keywords=[
            "information security policy",
            "approved by",
            "policy review",
            "version",
        ],
        related_controls=["A.5.2"],
    ),
    Control(
        id="A.5.2",
        title="Information security roles and responsibilities",
        description=(
            "Information security responsibilities should be defined "
            "and assigned."
        ),
        expected_evidence=[
            "Roles and responsibilities matrix",
            "Job descriptions",
            "RACI matrix",
        ],
        keywords=[
            "roles and responsibilities",
            "accountability",
            "raci",
            "security owner",
        ],
        related_controls=["A.5.1"],
    ),
]