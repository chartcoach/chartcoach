from typing import TypedDict


class VisualizationRequestRecord(TypedDict):
    """One fully resolved generation request."""

    id: str
    query: str
    requirements: list[str]


class ImplementationReviewResult(TypedDict):
    """Normalized implementation-review payload attached to generation attempts."""

    no_truncation: bool
    no_overlap: bool
    text_readable: bool
    data_readable: bool
    layout_balanced: bool
    data_operations_correct: bool
    self_explanatory: bool
    implementation_acceptable: bool
    requirements_followed: bool
    no_unprescribed_design: bool
    requirement_trace: dict[str, str]
    implementation_reasoning: str
    implementation_feedback: list[str]


class VisGenOutput(TypedDict):
    """Public generation output persisted by the workbench."""

    id: str
    code: str
    visualization_type: str
    grounding_trace: dict[str, str]
