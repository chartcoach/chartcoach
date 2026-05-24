import io

import matplotlib

matplotlib.use("Agg")
import matplotlib.figure
import matplotlib.pyplot as plt
import PIL.Image

from visground.generation.models import VisualizationRequestRecord

from .base import VisualizationBackend


class MatplotlibBackend(VisualizationBackend[matplotlib.figure.Figure]):
    def build_requirements(
        self,
        req: VisualizationRequestRecord,
    ) -> list[str]:
        return [
            "`library-choice`: Write valid matplotlib code to implement the visualization. Keep the implementation idiomatic, but do not add extra design or data behavior beyond the query and requirements.",
            "`return-rule`: Ensure that the assigned chart result is a `matplotlib.figure.Figure` object.",
        ]

    def build_visualization(self, id: str, code: str) -> matplotlib.figure.Figure:
        """Build after forcing matplotlib's non-interactive backend."""
        patched_code = "\n".join(
            [
                "import matplotlib",
                'matplotlib.use("Agg")',
                "",
                code,
            ]
        )
        try:
            return super().build_visualization(id, patched_code)
        finally:
            plt.close("all")

    def rasterize(self, chart: matplotlib.figure.Figure) -> PIL.Image.Image:
        buf = io.BytesIO()
        chart.savefig(buf, format="png", dpi=300)
        buf.seek(0)
        return PIL.Image.open(buf)
