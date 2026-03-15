import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell
def _(VisEvalDataset, VisJudgeBenchDataset):
    viseval_dataset = VisEvalDataset()
    visjudge_dataset = VisJudgeBenchDataset()
    return (viseval_dataset,)


@app.cell
def _(viseval_dataset):
    viseval_dataset.vis_tasks_df
    return


@app.cell
def _(viseval_dataset):
    viseval_dataset.vis_tasks_df.select('nl_query_canonical').sample(10)
    return


@app.cell
def _(viseval_dataset):
    viseval_dataset.nl_query_canonical_df.join(viseval_dataset.vis_tasks_df, on="nl_query_canonical", how="left").sample(32)
    return


@app.cell
def _(pl, viseval_dataset):
    tdf = (
        viseval_dataset.df.unnest("data").select(
            "id",
            "db_id",
            sql=pl.col("vis_query")
            .struct.field("data_part")
            .struct.field("sql_part"),
            nl_query=pl.col("nl_queries").list.first(),
        )
    )
    tdf
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import polars as pl

    from visground.datasets import VISGROUND_DATA_ROOT, VisEvalDataset, VisJudgeBenchDataset
    from visground.executor import pyexecute

    return VisEvalDataset, VisJudgeBenchDataset, pl


if __name__ == "__main__":
    app.run()
