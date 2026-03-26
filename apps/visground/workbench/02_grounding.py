import marimo

__generated_with = "0.21.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    flat_strategy_config = {
        "n_results": 10,
        "rrf_k": 10,
        "max_items": 5,
    }

    structured_strategy_config = {
        "n_results": 12,
        "top_k": 3,
        "rrf_k": 20,
        "max_items": 4,
    }
    return (structured_strategy_config,)


@app.cell(hide_code=True)
def _(store):
    vis_request_df = store.read_cohort_df()
    vis_request_df
    return (vis_request_df,)


@app.cell(hide_code=True)
def _(pl, vis_request_df):
    refinement_requests_df = vis_request_df.select(
        "id",
        pl.col("nl_query").alias("query"),
        "task",
        "scope",
        "time_mode",
        "chart",
        "data_profile",
        pl.lit("refine").alias("objective"),
        pl.lit(None).cast(pl.String).alias("audience"),
    )
    refinement_requests_df
    return (refinement_requests_df,)


@app.cell(hide_code=True)
def _(AUDIENCE_MODIFIER_IDS, pl, vis_request_df):
    selection_requests_df = vis_request_df.select(
        "id",
        pl.col("nl_query_canonical").alias("query"),
        "task",
        "scope",
        "time_mode",
        pl.lit(None).alias("chart"),
        "data_profile",
        pl.lit("select").alias("objective"),
        pl.lit([*AUDIENCE_MODIFIER_IDS, None]).alias("audience"),
    ).explode("audience")
    selection_requests_df
    return (selection_requests_df,)


@app.cell(hide_code=True)
def _(pl, refinement_requests_df, selection_requests_df):
    grounding_requests_df = pl.concat([refinement_requests_df, selection_requests_df])
    grounding_requests_df
    return (grounding_requests_df,)


@app.cell(hide_code=True)
def _(
    NoneGroundingStrategy,
    StructuredGroundingStrategy,
    coach,
    structured_strategy_config,
):
    structured_grounder = StructuredGroundingStrategy(
        coach,
        config=structured_strategy_config,
    )
    none_grounder = NoneGroundingStrategy()
    return none_grounder, structured_grounder


@app.cell(hide_code=True)
def _(GroundingStrategy, mo, none_grounder, pl, structured_grounder):
    def build_grounding_item(strategy: GroundingStrategy, req: dict) -> dict:
        result = strategy.retrieve(req)
        return {
            "grounding_id": "-".join(
                [
                    req["id"],
                    req["objective"],
                    strategy.mode,
                    req["audience"] or "none",
                ]
            ),
            "grounding_mode": strategy.mode,
            "request": req,
            "result": result,
        }

    def build_grounding_results_df(
        grounding_requests_df: pl.DataFrame,
    ) -> pl.DataFrame:
        grounding_results = []

        for req in mo.status.progress_bar(
            grounding_requests_df.to_dicts(),
            total=grounding_requests_df.height,
        ):
            grounding_results.append(build_grounding_item(structured_grounder, req))
            grounding_results.append(build_grounding_item(none_grounder, req))

        return pl.from_dicts(grounding_results)

    return (build_grounding_results_df,)


@app.cell(hide_code=True)
def _(build_grounding_results_df, grounding_requests_df):
    grounding_results_df = build_grounding_results_df(grounding_requests_df)
    grounding_results_df
    return (grounding_results_df,)


@app.cell(hide_code=True)
def _(grounding_results_df, pl):
    (
        grounding_results_df.group_by("grounding_mode", "request")
        .agg(count=pl.len())
        .head()
    )
    return


@app.cell(hide_code=True)
def _(grounding_results_df, store):
    store.write_grounding_df(grounding_results_df)
    return


@app.cell(hide_code=True)
def _(VisGroundDataset):
    store = VisGroundDataset()
    return (store,)


@app.cell(hide_code=True)
def _():
    import os

    import chartcoach as cc
    import chromadb.utils.embedding_functions as embedding_functions
    import marimo as mo
    import polars as pl
    from visground.datasets import VisGroundDataset
    from visground.grounding import (
        AUDIENCE_MODIFIER_IDS,
        FlatGroundingStrategy,
        GroundingStrategy,
        NoneGroundingStrategy,
        StructuredGroundingStrategy,
    )

    openai_large_ef = embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.environ["OPENROUTER_API_KEY"],
        api_base="https://openrouter.ai/api/v1",
        model_name="openai/text-embedding-3-large",
    )
    coach = cc.create(
        catalog="guidelines/catalog.parquet",
        embedding_fn=openai_large_ef,
    )
    return (
        AUDIENCE_MODIFIER_IDS,
        GroundingStrategy,
        NoneGroundingStrategy,
        StructuredGroundingStrategy,
        VisGroundDataset,
        coach,
        mo,
        pl,
    )


if __name__ == "__main__":
    app.run()
