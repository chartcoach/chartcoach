import marimo

__generated_with = "0.21.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    from visground.datasets import VisGroundDataset

    return VisGroundDataset, mo, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 05 Analysis

    Validate candidate-level judgements and build the analysis tables used for result summaries.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Stage Contract

    - Required input: `04_judgements.parquet`
    - Supporting metadata: `02_grounding.parquet`, optionally `01_cohort.parquet`
    - Responsibility: validate judged candidate rows, enrich them with metadata, and expand score columns for analysis
    """)
    return


@app.cell
def _(VisGroundDataset):
    store = VisGroundDataset()
    return (store,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Load And Validate Judgements
    """)
    return


@app.cell
def _(store):
    judgements_df = store.read_judgements_df()
    judgements_df
    return (judgements_df,)


@app.cell
def _(judgements_df, pl):
    required_columns = [
        "visgen_id",
        "grounding_id",
        "grounding_mode",
        "objective",
        "vis_id",
        "query",
        "audience",
        "model",
        "grammar",
        "judgement",
    ]
    present_columns = set(judgements_df.columns)
    validation_df = pl.from_dicts(
        [
            {
                "rows": judgements_df.height,
                "non_null_judgements": (
                    judgements_df.select(pl.col("judgement").is_not_null().sum()).item()
                    if "judgement" in present_columns
                    else 0
                ),
                "has_required_columns": all(
                    column in present_columns for column in required_columns
                ),
            }
        ]
    )
    validation_df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Build Analysis Table
    """)
    return


@app.cell
def _(store):
    grounding_df = store.read_grounding_df()
    cohort_df = store.read_cohort_df()
    return cohort_df, grounding_df


@app.cell
def _(cohort_df, grounding_df, judgements_df, pl):
    analysis_base_df = judgements_df.join(
        grounding_df.select(
            "grounding_id",
            request=pl.col("request"),
        ),
        on="grounding_id",
        how="left",
    ).join(
        cohort_df.select(
            "db_id",
            "chart",
            "hardness",
            "task",
            "scope",
            "time_mode",
            cohort_id=pl.col("id"),
        ),
        left_on="vis_id",
        right_on="cohort_id",
        how="left",
    )
    analysis_base_df
    return (analysis_base_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Expand Score Columns
    """)
    return


@app.cell
def _(analysis_base_df, pl):
    if analysis_base_df.is_empty() or "judgement" not in analysis_base_df.columns:
        score_df = analysis_base_df
    else:
        score_df = analysis_base_df.with_columns(
            data_fidelity=pl.col("judgement")
            .struct.field("data_fidelity")
            .struct.field("score"),
            semantic_readability=pl.col("judgement")
            .struct.field("semantic_readability")
            .struct.field("score"),
            insight_discovery=pl.col("judgement")
            .struct.field("insight_discovery")
            .struct.field("score"),
            design_style=pl.col("judgement")
            .struct.field("design_style")
            .struct.field("score"),
            visual_composition=pl.col("judgement")
            .struct.field("visual_composition")
            .struct.field("score"),
            color_harmony=pl.col("judgement")
            .struct.field("color_harmony")
            .struct.field("score"),
        )
    score_df
    return (score_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Coverage And Sanity Checks
    """)
    return


@app.cell
def _(pl, score_df):
    if score_df.is_empty():
        summary_df = pl.DataFrame(
            {
                "note": [
                    "No judged candidate rows available yet. Run 04_judging.py with VisJudge enabled."
                ]
            }
        )
    else:
        summary_df = (
            score_df.group_by("grounding_mode", "model", "grammar")
            .agg(
                pl.len().alias("n"),
                pl.col("data_fidelity").mean(),
                pl.col("semantic_readability").mean(),
                pl.col("insight_discovery").mean(),
                pl.col("design_style").mean(),
                pl.col("visual_composition").mean(),
                pl.col("color_harmony").mean(),
            )
            .sort("grounding_mode", "model", "grammar")
        )
    summary_df
    return


if __name__ == "__main__":
    app.run()
