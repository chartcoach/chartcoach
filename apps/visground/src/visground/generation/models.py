from typing import TypedDict


class VisualizationRequestRecord(TypedDict):
    """One fully resolved generation request."""

    id: str
    query: str
    requirements: list[str]
