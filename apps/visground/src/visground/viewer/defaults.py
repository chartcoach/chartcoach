from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import polars as pl

from chartcoach.guideline import parse_bibtex_entry

from .spec import ViewerConfig, ViewerDimensionSpec, ViewerLayout

DEFAULT_VIEWER_IMAGE_BASE_URL = (
    "https://files.peter.gy/projects/cc/supplementary/05-empirical-study/"
    "03-pipeline/03_generated_charts/"
)


def _author_label(author_field: str) -> str | None:
    authors = [part.strip() for part in author_field.split(" and ") if part.strip()]
    if not authors:
        return None

    def family_name(author: str) -> str:
        if "," in author:
            return author.split(",", 1)[0].strip()
        return author.split()[-1].strip()

    family_names = [family_name(author) for author in authors if family_name(author)]
    if not family_names:
        return None
    if len(family_names) == 1:
        return family_names[0]
    if len(family_names) == 2:
        return f"{family_names[0]} & {family_names[1]}"
    return f"{family_names[0]} et al."


def _render_source_label(reference: str) -> str | None:
    try:
        parsed = parse_bibtex_entry(reference)
    except Exception:
        parsed = {}

    author = _author_label(str(parsed.get("author") or ""))
    year = str(parsed.get("year") or "").strip()
    if author and year:
        return f"{author}, {year}"
    if author:
        return author
    return None


def build_default_viewer_config() -> ViewerConfig:
    catalog_path = (
        Path(__file__).resolve().parents[5] / "guidelines" / "catalog.parquet"
    )
    guideline_details_by_id: dict[str, dict[str, Any]] = {}

    if catalog_path.exists():
        catalog_df = pl.read_parquet(catalog_path)
        for row in catalog_df.iter_rows(named=True):
            guideline = row["guideline"]
            sections = guideline.get("sections") or []
            advice = next(
                (
                    str(section.get("content") or "").strip()
                    for section in sections
                    if section.get("role") == "advice" and section.get("content")
                ),
                "",
            )
            sources = list(
                dict.fromkeys(
                    rendered
                    for reference in (row.get("references") or [])
                    if str(reference).strip()
                    if (rendered := _render_source_label(str(reference).strip()))
                    is not None
                )
            )
            guideline_details_by_id[str(row["id"])] = {
                "title": str(guideline.get("title") or row["id"]),
                "description": str(guideline.get("description") or advice),
                "sources": sources,
            }

    image_base_url = os.getenv(
        "VISGROUND_VIEWER_IMAGE_BASE_URL", DEFAULT_VIEWER_IMAGE_BASE_URL
    )

    return ViewerConfig(
        image_base_url=image_base_url,
        case_id_field="vis_id",
        case_label_field="query",
        dimensions=(
            ViewerDimensionSpec(
                id="objective",
                label="Objective",
                aliases={"select": "Select", "refine": "Refine"},
                order={"select": 0, "refine": 1},
            ),
            ViewerDimensionSpec(
                id="request_chart",
                label="Chart type",
                null_label="All chart types",
                none_value_mode="all",
            ),
            ViewerDimensionSpec(
                id="audience",
                label="Audience",
                null_label="No audience",
                aliases={"novice": "Novice", "casual": "Casual", "expert": "Expert"},
            ),
            ViewerDimensionSpec(
                id="grammar",
                label="Grammar",
                aliases={
                    "altair": "Altair",
                    "matplotlib": "Matplotlib",
                    "plotly": "Plotly",
                },
            ),
            ViewerDimensionSpec(
                id="grounding_mode",
                label="Grounding",
                aliases={
                    "none": "Ungrounded",
                    "hybrid": "Grounded",
                    "structured": "Structured",
                },
                order={"none": 0, "hybrid": 1, "structured": 2},
            ),
            ViewerDimensionSpec(
                id="model",
                label="Model",
                aliases={
                    "gpt-5.3-codex": "GPT-5.3 Codex",
                    "claude-sonnet-4.6": "Claude 4.6",
                    "gemini-3.1-pro-preview": "Gemini 3.1",
                    "gpt-5.4": "GPT-5.4",
                },
            ),
        ),
        filter_dimensions=("objective", "request_chart", "audience"),
        axis_dimensions=("model", "grounding_mode", "grammar"),
        default_filters={
            "objective": "select",
            "request_chart": None,
            "audience": None,
        },
        default_layout=ViewerLayout(
            row_dimension="model",
            column_dimension="grounding_mode",
            group_dimension="grammar",
        ),
        guideline_details_by_id=guideline_details_by_id,
    )
