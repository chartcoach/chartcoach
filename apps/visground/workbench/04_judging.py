import marimo

__generated_with = "0.21.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 04 Judging

    Run repeated VisJudge evaluations for generated chart candidates, aggregate the final judgement, and persist both final and per-run artifacts.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Stage Contract

    - Input: 03_generate.parquet
    - Outputs: 04_judgements.parquet and 04_judgement_runs.parquet
    - Responsibility: judge generated chart candidates, preserve raw repeated runs, and write the canonical aggregate result used downstream
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Runtime Configuration

    Notebook default keeps averaged repeated judging, while the runner also supports best-of-N selection when needed.
    """)
    return


@app.cell(hide_code=True)
def _(VisJudgeRunConfig):
    judge_config = VisJudgeRunConfig(
        repeats=3,
        aggregation="average",
        batch_size=16,
        parallel_jobs=3,
    )
    judge_config
    return (judge_config,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Load Candidate Inputs
    """)
    return


@app.cell(hide_code=True)
def _(store):
    candidates_df = store.read_generated_candidates_df()
    candidates_df
    return (candidates_df,)


@app.cell(hide_code=True)
def _(mo):
    def show_progress(items, total: int):
        return mo.status.progress_bar(items, total=total)

    return (show_progress,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Run VisJudge
    """)
    return


@app.cell(hide_code=True)
def _(
    VisJudgeRunner,
    candidates_df,
    judge_config,
    logger,
    show_progress,
    store,
    viseval_dataset,
    visjudge_client,
):
    runner = VisJudgeRunner(
        store=store,
        viseval_dataset=viseval_dataset,
        visjudge_client=visjudge_client,
        logger=logger,
    )
    judgements_df, judgement_runs_df = runner.judge_candidates(
        candidates_df,
        config=judge_config,
        progress=show_progress,
    )
    judgements_df
    return judgement_runs_df, judgements_df


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Inspect and Persist Results
    """)
    return


@app.cell(hide_code=True)
def _(judgement_runs_df, pl):
    judgement_runs_df.select(
        pl.len().alias("rows"),
        pl.col("judge_run_id").n_unique().alias("judge_runs"),
        pl.col("judgement").is_not_null().sum().alias("non_null_judgements"),
        pl.col("judge_error").is_not_null().sum().alias("run_errors"),
    )
    return


@app.cell(hide_code=True)
def _(judgements_df, pl):
    judgements_df.select(
        pl.len().alias("rows"),
        pl.col("judgement").is_not_null().sum().alias("non_null_judgements"),
        pl.col("judgement_success_count").mean().alias("avg_successful_runs"),
        pl.col("best_overall_score").mean().alias("avg_best_overall_score"),
    )
    return


@app.cell(hide_code=True)
def _(judgement_runs_df, store):
    store.write_judgement_runs_df(judgement_runs_df)
    return


@app.cell(hide_code=True)
def _(judgements_df, store):
    store.write_judgements_df(judgements_df)
    return


@app.cell(hide_code=True)
def _(VisEvalDataset, VisGroundDataset, VisJudgeApiClient):
    store = VisGroundDataset()
    viseval_dataset = VisEvalDataset()
    # visjudge_client = VisJudgeLmClient(lm=lm_cliproxy("gpt-5.4"))
    visjudge_client = VisJudgeApiClient()
    return store, viseval_dataset, visjudge_client


@app.cell(hide_code=True)
def _():
    import logging

    import marimo as mo
    import polars as pl
    from visground.datasets import VisEvalDataset, VisGroundDataset
    from visground.judge import (
        VisJudgeLmClient,
        VisJudgeApiClient,
        VisJudgeRunConfig,
        VisJudgeRunner,
    )
    from visground.lm import lm_cliproxy

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return (
        VisEvalDataset,
        VisGroundDataset,
        VisJudgeApiClient,
        VisJudgeRunConfig,
        VisJudgeRunner,
        logger,
        mo,
        pl,
    )


if __name__ == "__main__":
    app.run()
