import io

import altair as alt
import PIL.Image

from visground.generation.models import VisualizationRequestRecord

from .base import VisualizationBackend


class AltairBackend(VisualizationBackend[alt.Chart]):
    def build_requirements(
        self,
        req: VisualizationRequestRecord,
    ) -> list[str]:
        return [
            "Write valid altair code to implement the visualization, using best practices from the library.",
            "Ensure that the assigned chart result is an altair `Chart` object.",
        ]

    def rasterize(self, chart: alt.Chart) -> PIL.Image.Image:
        buf = io.BytesIO()
        chart.save(buf, format="png", scale_factor=4)
        buf.seek(0)
        return PIL.Image.open(buf)
