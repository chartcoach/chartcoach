import marimo

__generated_with = "0.21.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 01 Cohort

    Build the chart-balanced VisEval cohort that all downstream workbench stages consume.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Input: enriched VisEval dataset.
    Output: `01_cohort.parquet`.
    """)
    return


@app.cell(hide_code=True)
def _(VisEvalCohortBuilder, VisEvalDataset, VisGroundDataset):
    store = VisGroundDataset()
    viseval_dataset = VisEvalDataset()
    viseval_cohort_builder = VisEvalCohortBuilder(viseval_dataset)
    return store, viseval_cohort_builder


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup
    """)
    return


@app.cell(hide_code=True)
def _():
    cohort_config = {
        "target_n": 7 * 5,
        "max_tasks_per_db": 6,
        "seed": 42,
    }
    return (cohort_config,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Build Cohort
    """)
    return


@app.cell(hide_code=True)
def _(cohort_config, viseval_cohort_builder):
    cohort_df = viseval_cohort_builder.build_request_df(config=cohort_config)
    cohort_df
    return (cohort_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Inspect Cohort
    """)
    return


@app.cell(hide_code=True)
def _(cohort_df, pl):
    chart_counts_df = cohort_df.group_by("chart").agg(count=pl.len()).sort("chart")
    chart_counts_df
    return


@app.cell(hide_code=True)
def _(cohort_df, pl):
    hardness_counts_df = (
        cohort_df.group_by("hardness").agg(count=pl.len()).sort("hardness")
    )
    hardness_counts_df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Persist Artifact
    """)
    return


@app.cell(hide_code=True)
def _(cohort_df, store):
    store.write_cohort_df(cohort_df)
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import polars as pl
    from visground.cohorts import VisEvalCohortBuilder
    from visground.datasets import VisGroundDataset
    from visground.datasets import VisEvalDataset

    return VisEvalCohortBuilder, VisEvalDataset, VisGroundDataset, mo, pl


if __name__ == "__main__":
    app.run()
