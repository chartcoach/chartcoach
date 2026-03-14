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
    viseval_dataset.queries_df
    return


@app.cell
def _(nl_query_intent_df, pl, viseval_dataset):
    viseval_dataset.queries_df.join(nl_query_intent_df, on="nl_query").select(
        "id",
        "nl_query_intent",
        "nl_query",
        pl.exclude("id", "nl_query_intent", "nl_query"),
    )
    return


@app.cell
def _(VISGROUND_DATA_ROOT, pl):
    nl_query_intent_df = pl.read_json(
        VISGROUND_DATA_ROOT / "vis-eval" / "enrichment" / "nl_query_intent.json"
    )
    nl_query_intent_df
    return (nl_query_intent_df,)


@app.cell
def _(viseval_dataset):
    viseval_dataset.df.unnest('data')
    return


@app.cell
def _():
    import marimo as mo
    from visground.datasets import VisEvalDataset, VisJudgeBenchDataset, VISGROUND_DATA_ROOT
    import polars as pl

    return VISGROUND_DATA_ROOT, VisEvalDataset, VisJudgeBenchDataset, pl


if __name__ == "__main__":
    app.run()
