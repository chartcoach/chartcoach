import io

import PIL.Image
import plotly.graph_objects as go

from visground.generation.models import VisualizationRequestRecord

from .base import VisualizationBackend


class PlotlyBackend(VisualizationBackend[go.Figure]):
    def build_requirements(
        self,
        req: VisualizationRequestRecord,
    ) -> list[str]:
        return [
            "`library-choice`: Write valid plotly code to implement the visualization, using best practices from the library.",
            "`return-rule`: Ensure that the assigned chart result is a plotly `Figure` object.",
        ]

    def rasterize(self, chart: go.Figure) -> PIL.Image.Image:
        buf = io.BytesIO()
        chart.write_image(buf, format="png", scale=4)
        buf.seek(0)
        return PIL.Image.open(buf)
