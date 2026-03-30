import marimo

__generated_with = "0.21.1"
app = marimo.App(width="columns")


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

    return (
        ViewerConfig,
        ViewerDimensionSpec,
        ViewerLayout,
        VisGroundDataset,
        VisGroundViewer,
        mo,
        os,
    )


@app.cell(hide_code=True)
def _(VisGroundDataset):
    store = VisGroundDataset()
    candidates_df = store.read_generated_candidates_df()
    judgements_df = (
        store.read_judgements_df() if store.judgements_path().exists() else None
    )
    return candidates_df, judgements_df


@app.cell(hide_code=True)
def _(ViewerConfig, ViewerDimensionSpec, ViewerLayout, os):
    viewer_config = ViewerConfig(
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
                    "hybrid": "Hybrid",
                    "structured": "Structured",
                },
                order={"none": 0, "hybrid": 1, "structured": 2},
            ),
            ViewerDimensionSpec(
                id="model",
                label="Model",
                aliases={
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
        image_base_url=os.getenv(
            "VISGROUND_VIEWER_IMAGE_BASE_URL",
            "http://127.0.0.1:8000",
        ),
    )
    return (viewer_config,)


@app.cell(hide_code=True)
def _(mo, os):
    debug_default = os.getenv("VISGROUND_VIEWER_DEBUG", "0") == "1"
    debug_switch = mo.ui.switch(debug_default, label="Debug")
    debug_switch
    return (debug_switch,)


@app.cell(hide_code=True)
def _(
    VisGroundViewer,
    candidates_df,
    debug_switch,
    judgements_df,
    mo,
    viewer_config,
):
    widget = mo.ui.anywidget(
        VisGroundViewer(
            candidates_df=candidates_df,
            judgements_df=judgements_df,
            viewer_config=viewer_config,
            debug=debug_switch.value,
        )
    )
    widget
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
