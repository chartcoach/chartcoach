import marimo

__generated_with = "0.22.4"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(
    VisGroundViewer,
    candidates_df,
    judgement_runs_df,
    judgements_df,
    mo,
    viewer_config,
):
    widget = mo.ui.anywidget(
        VisGroundViewer(
            candidates_df=candidates_df,
            judgement_runs_df=judgement_runs_df,
            judgements_df=judgements_df,
            viewer_config=viewer_config,
        )
    )
    widget
    return


@app.cell
def _(
    DEFAULT_VIEWER_IMAGE_BASE_URL,
    ViewerConfig,
    ViewerDimensionSpec,
    ViewerLayout,
    os,
):
    from pathlib import Path

    import polars as pl
    from chartcoach.guideline import parse_bibtex_entry

    catalog_path = (
        Path(__file__).resolve().parents[3] / "guidelines" / "catalog.parquet"
    )

    def author_label(author_field: str) -> str | None:
        authors = [part.strip() for part in author_field.split(" and ") if part.strip()]
        if not authors:
            return None

        def family_name(author: str) -> str:
            if "," in author:
                return author.split(",", 1)[0].strip()
            return author.split()[-1].strip()

        family_names = [
            family_name(author) for author in authors if family_name(author)
        ]
        if not family_names:
            return None
        if len(family_names) == 1:
            return family_names[0]
        if len(family_names) == 2:
            return f"{family_names[0]} & {family_names[1]}"
        return f"{family_names[0]} et al."

    def render_source_label(reference: str) -> str | None:
        try:
            parsed = parse_bibtex_entry(reference)
        except Exception:
            parsed = {}

        author = author_label(str(parsed.get("author") or ""))
        year = str(parsed.get("year") or "").strip()
        if author and year:
            return f"{author}, {year}"
        if author:
            return author
        return None

    guideline_details_by_id = {}
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
                    if (rendered := render_source_label(str(reference).strip()))
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

    viewer_config = ViewerConfig(
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
                aliases={
                    "novice": "Novice",
                    "casual": "Casual",
                    "expert": "Expert",
                },
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
    return (viewer_config,)


@app.cell
def _(VisGroundDataset):
    store = VisGroundDataset()
    candidates_df = store.read_generated_candidates_df()
    judgements_df = (
        store.read_judgements_df() if store.judgements_path().exists() else None
    )
    judgement_runs_df = (
        store.read_judgement_runs_df() if store.judgement_runs_path().exists() else None
    )
    return candidates_df, judgement_runs_df, judgements_df


@app.cell(hide_code=True)
def _():
    import os

    import marimo as mo
    from visground.datasets import VisGroundDataset
    from visground.viewer import (
        ViewerConfig,
        ViewerDimensionSpec,
        ViewerLayout,
        VisGroundViewer,
    )
    from visground.viewer.defaults import DEFAULT_VIEWER_IMAGE_BASE_URL

    return (
        DEFAULT_VIEWER_IMAGE_BASE_URL,
        ViewerConfig,
        ViewerDimensionSpec,
        ViewerLayout,
        VisGroundDataset,
        VisGroundViewer,
        mo,
        os,
    )


if __name__ == "__main__":
    app.run()
