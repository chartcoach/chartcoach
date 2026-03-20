from typing import TypedDict


class VisualizationRequestRecord(TypedDict):
    """Structured request row for visualization generation."""

    id: str
    chart: str
    query: str
    task: str
    scope: str
    time_mode: str
