import io

import matplotlib.figure
import matplotlib.pyplot as plt
import PIL.Image

from visground.generation.backends import VisualizationBackend
from visground.generation.models import VisualizationRequestRecord


class MatplotlibBackend(VisualizationBackend[matplotlib.figure.Figure]):
    def build_requirements(
        self,
        req: VisualizationRequestRecord,
    ) -> list[str]:
        return [
            "Write valid matplotlib code to implement the visualization, using best practices from the library.",
            "Ensure that the assigned chart result is a `matplotlib.figure.Figure` object.",
        ]

    def materialize_visualization(self, id: str, code: str) -> matplotlib.figure.Figure:
        """Materialization with matplotlib-specific cleanup"""
        try:
            return super().materialize_visualization(id, code)
        finally:
            plt.close("all")

    def rasterize(self, chart: matplotlib.figure.Figure) -> PIL.Image.Image:
        buf = io.BytesIO()
        chart.savefig(buf, format="png", dpi=300)
        buf.seek(0)
        return PIL.Image.open(buf)
