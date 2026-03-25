from .base import VisualizationBackend
from .altair import AltairBackend
from .matplotlib import MatplotlibBackend
from .plotly import PlotlyBackend
from visground.datasets import VisEvalDataset


def resolve_visualization_backend(
    grammar: str,
    dataset: VisEvalDataset,
) -> VisualizationBackend:
    backends: dict[str, type[VisualizationBackend]] = {
        "matplotlib": MatplotlibBackend,
        "altair": AltairBackend,
        "plotly": PlotlyBackend,
    }
    if grammar not in backends:
        raise ValueError(f"Unsupported visualization grammar: {grammar}")
    return backends[grammar](dataset)


__all__ = [
    "VisualizationBackend",
    "AltairBackend",
    "MatplotlibBackend",
    "PlotlyBackend",
    "resolve_visualization_backend",
]
