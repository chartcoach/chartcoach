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
            "`library-choice`: Write valid altair code to implement the visualization. Keep the implementation idiomatic, but do not add extra design or data behavior beyond the query and requirements.",
            "`return-rule`: Ensure that the assigned chart result is an altair `Chart` object.",
            "`direct-values`: Only when a visible requirement explicitly calls for direct values, explicit callouts, or local annotation on emphasized marks, implement them with explicit layered Altair text and/or annotation marks in the chart itself rather than only through titles, subtitles, or axis-label hacks.",
        ]

    def rasterize(self, chart: alt.Chart) -> PIL.Image.Image:
        buf = io.BytesIO()
        chart.save(buf, format="png", scale_factor=4)
        buf.seek(0)
        return PIL.Image.open(buf)
