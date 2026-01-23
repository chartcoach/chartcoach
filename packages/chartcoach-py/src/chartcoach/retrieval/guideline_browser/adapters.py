from __future__ import annotations

from dataclasses import dataclass

import dspy

from ..dspy_adapters import (
    get_text_by_role,
    image_item_to_dspy_image,
    require_image_item_by_role,
    require_text_by_role,
)
from ..types import RetrievalRequest


@dataclass(frozen=True, slots=True)
class GuidelineBrowserInputs:
    chart: dspy.Image
    situation: str
    chart_spec: str
    existing_chart_feedback: str


def guideline_browser_inputs_from_request(
    request: RetrievalRequest,
    *,
    chart_role: str = "chart",
    situation_role: str = "situation",
    chart_spec_role: str = "chart_spec",
    existing_chart_feedback_role: str = "existing_chart_feedback",
) -> GuidelineBrowserInputs:
    chart_item = require_image_item_by_role(request, role=chart_role)
    chart = image_item_to_dspy_image(chart_item)

    situation = require_text_by_role(request, role=situation_role)
    chart_spec = require_text_by_role(request, role=chart_spec_role)

    existing_chart_feedback = (
        get_text_by_role(request, role=existing_chart_feedback_role) or ""
    )

    return GuidelineBrowserInputs(
        chart=chart,
        situation=situation,
        chart_spec=chart_spec,
        existing_chart_feedback=existing_chart_feedback,
    )
