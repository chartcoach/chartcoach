from __future__ import annotations

from typing import Any

DIMENSION_SPECS: dict[str, dict[str, Any]] = {
    "request_chart": {
        "label": "Chart type",
        "null_label": "All chart types",
    },
    "objective": {
        "label": "Objective",
        "order": {"select": 0, "refine": 1},
        "aliases": {
            "select": "Select",
            "refine": "Refine",
        },
    },
    "grammar": {
        "label": "Grammar",
        "aliases": {
            "altair": "Altair",
            "matplotlib": "Matplotlib",
            "plotly": "Plotly",
        },
    },
    "audience": {
        "label": "Audience",
        "null_label": "No audience",
        "aliases": {
            "novice": "Novice",
            "casual": "Casual",
            "expert": "Expert",
        },
    },
    "grounding_mode": {
        "label": "Grounding",
        "aliases": {
            "none": "Ungrounded",
            "hybrid": "Hybrid",
            "structured": "Structured",
        },
        "order": {"none": 0, "hybrid": 1, "structured": 2},
    },
    "model": {
        "label": "Model",
        "aliases": {
            "claude-sonnet-4.6": "Claude 4.6",
            "gemini-3.1-pro-preview": "Gemini 3.1",
            "gpt-5.4": "GPT-5.4",
        },
    },
}

SCORE_BREAKDOWN_SPECS: tuple[dict[str, str], ...] = (
    {
        "id": "overall",
        "label": "Overall",
        "dimension": "overall",
    },
    {
        "id": "data_fidelity",
        "label": "Data Fidelity",
        "dimension": "faithfulness",
    },
    {
        "id": "semantic_readability",
        "label": "Semantic Readability",
        "dimension": "expressiveness",
    },
    {
        "id": "insight_discovery",
        "label": "Insight Discovery",
        "dimension": "expressiveness",
    },
    {
        "id": "design_style",
        "label": "Design Style",
        "dimension": "aesthetics",
    },
    {
        "id": "visual_composition",
        "label": "Visual Composition",
        "dimension": "aesthetics",
    },
    {
        "id": "color_harmony",
        "label": "Color Harmony",
        "dimension": "aesthetics",
    },
)

VARIANT_SPECS: tuple[dict[str, Any], ...] = (
    {
        "id": "by-grounding",
        "label": "Grounding",
        "group_dimension": "grammar",
        "row_dimension": "model",
        "column_dimension": "grounding_mode",
    },
    {
        "id": "by-model",
        "label": "Model",
        "group_dimension": "grammar",
        "row_dimension": "grounding_mode",
        "column_dimension": "model",
    },
    {
        "id": "flat-by-grounding",
        "label": "Grounding",
        "group_dimension": None,
        "row_dimension": "model",
        "column_dimension": "grounding_mode",
    },
    {
        "id": "flat-by-model",
        "label": "Model",
        "group_dimension": None,
        "row_dimension": "grounding_mode",
        "column_dimension": "model",
    },
)

DEFAULT_SELECTION = {
    "objective": "select",
    "request_chart": None,
    "overview_variant": "by-grounding",
    "dimension_filters": {
        "audience": None,
    },
}

DEFAULT_SELECTION_DIMENSION_FILTERS = DEFAULT_SELECTION["dimension_filters"]


def display_label(dimension: str, value: Any) -> str:
    spec = DIMENSION_SPECS.get(dimension, {})
    if value is None:
        return str(spec.get("null_label", "None"))
    aliases = spec.get("aliases", {})
    if value in aliases:
        return str(aliases[value])
    return str(value)


def label_for_dimension(dimension: str | None) -> str:
    if dimension is None:
        return ""
    return str(DIMENSION_SPECS.get(dimension, {}).get("label", dimension))
