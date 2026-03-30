import marimo

__generated_with = "0.21.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 05 Analysis

    Build comparative analysis artifacts from generated candidates and VisJudge
    results. This stage treats VisJudge as a fixed comparative judge rather than an
    absolute quality scale.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Stage Contract

    - Inputs: `03_generate.parquet`, `04_judgements.parquet`
    - Outputs: `05_analysis/*.parquet`
    - Responsibility: build paired grounded-vs-none score deltas, design-variance
      comparisons, grounded guideline summaries, and a narrow regression robustness
      table
    """)
    return


@app.cell(hide_code=True)
def _(VisGroundDataset, build_analysis_bundle):
    store = VisGroundDataset()
    analysis_bundle = build_analysis_bundle(store)
    return analysis_bundle, store


@app.cell(hide_code=True)
def _(analysis_bundle):
    analysis_bundle.manifest_df()
    return


@app.cell(hide_code=True)
def _(analysis_bundle, pl):
    analysis_bundle.score_summary_df.filter(
        (pl.col("slice_name") == "all") & (pl.col("metric") == "overall")
    )
    return


@app.cell(hide_code=True)
def _(analysis_bundle):
    analysis_bundle.variance_summary_df
    return


@app.cell(hide_code=True)
def _(analysis_bundle, pl):
    analysis_bundle.guideline_summary_df.sort(
        "support",
        descending=True,
        nulls_last=True,
    ).head(20)
    return


@app.cell(hide_code=True)
def _(analysis_bundle, pl):
    analysis_bundle.guideline_associations_df.sort(
        "p_value_adj",
        nulls_last=True,
    ).head(20)
    return


@app.cell(hide_code=True)
def _(analysis_bundle, store):
    analysis_bundle.write_all(store)
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import polars as pl
    from visground.analysis import build_analysis_bundle
    from visground.datasets import VisGroundDataset

    return VisGroundDataset, build_analysis_bundle, mo, pl


if __name__ == "__main__":
    app.run()
