import marimo

__generated_with = "0.21.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 04 Judging

    Rasterize generated charts, build judge requests, run VisJudge, and persist candidate-level judgements.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Stage Contract

    - Inputs: `02_grounding.parquet`, `03_generate.parquet`, cached chart images under `charts/`
    - Output: `04_judgements.parquet`
    - Responsibility: turn generated chart candidates into candidate-level VisJudge rows
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup
    """)
    return


@app.cell(hide_code=True)
def _(VisualizationBackend, resolve_visualization_backend, viseval_dataset):
    def get_vis_backend(grammar: str) -> VisualizationBackend:
        return resolve_visualization_backend(grammar, viseval_dataset)

    return (get_vis_backend,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Load Upstream Outputs
    """)
    return


@app.cell(hide_code=True)
def _(store):
    grounding_df = store.read_grounding_df()
    grounding_df
    return (grounding_df,)


@app.cell(hide_code=True)
def _(store):
    generated_vis_df = store.read_generated_df()
    generated_vis_df.head()
    return (generated_vis_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Normalize Generated Visualizations
    """)
    return


@app.cell(hide_code=True)
def _(generated_vis_df, grounding_df, pl):
    visgen_df = (
        generated_vis_df.unnest("run")
        .explode("scenario", "outputs")
        .unnest("scenario")
        .unnest("input")
        .drop("id")
        .unnest("outputs")
        .join(
            grounding_df.select(
                "grounding_id",
                "grounding_mode",
                audience=pl.col("request").struct.field("audience"),
                objective=pl.col("request").struct.field("objective"),
            ),
            on="grounding_id",
            how="left",
        )
        .select(
            "visgen_id",
            "grounding_id",
            "grounding_mode",
            "objective",
            pl.col("id").alias("vis_id"),
            "query",
            "audience",
            "model",
            "grammar",
            "code",
            model_thoughts=pl.struct(
                "visualization_type",
                "query_interpretation",
                "design_rationale",
                "grounding_trace",
            ),
        )
    )
    visgen_df
    return (visgen_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Build Judge Input Groups
    """)
    return


@app.cell(hide_code=True)
def _(pl, visgen_df):
    judge_input_groups_df = (
        visgen_df.group_by("vis_id", "model", "grammar")
        .agg(group=pl.struct(pl.all()))
        .sort("vis_id", "model", "grammar")
    )
    judge_input_groups_df
    return (judge_input_groups_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Local Rendering and Request Helpers
    """)
    return


@app.cell(hide_code=True)
def _(
    Image,
    VisJudgeRequest,
    build_visjudge_prompt,
    get_audience_description,
    get_vis_backend,
    logger,
    store,
):
    def read_or_create_chart_image(visgen_result: dict) -> Image.Image:
        vis_id = visgen_result["vis_id"]
        visgen_id = visgen_result["visgen_id"]
        grammar = visgen_result["grammar"]
        code = visgen_result["code"]

        if store.chart_exists(visgen_id):
            return store.read_chart_image(visgen_id)

        vis_backend = get_vis_backend(grammar)
        chart = vis_backend.materialize_visualization(vis_id, code)
        chart_image = vis_backend.rasterize(chart)
        store.write_chart_image(visgen_id, chart_image)
        return chart_image

    def _build_visjudge_request_from_visgen_result(
        visgen_result: dict,
    ) -> VisJudgeRequest:
        chart_image = read_or_create_chart_image(visgen_result)

        visjudge_context = {}
        if (audience := visgen_result["audience"]) is not None:
            visjudge_context["The intended audience for this visualization is"] = (
                get_audience_description(audience)
            )
        prompt = build_visjudge_prompt(visjudge_context)

        return {
            "image": chart_image,
            "prompt": prompt,
        }

    def build_visjudge_request_from_visgen_result(
        visgen_result: dict,
    ) -> VisJudgeRequest | None:
        try:
            return _build_visjudge_request_from_visgen_result(visgen_result)
        except Exception as exc:
            logger.error(
                "Error building VisJudge request for vis_id %s: %s",
                visgen_result["vis_id"],
                exc,
            )
            return None

    return (build_visjudge_request_from_visgen_result,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Run VisJudge
    """)
    return


@app.cell(hide_code=True)
def _(
    VisJudgeClient,
    build_visjudge_request_from_visgen_result,
    extract_json,
    logger,
    mo,
    pl,
):
    def generate_judgements_df(
        judge_input_groups_df: pl.DataFrame,
        visjudge_client: VisJudgeClient,
    ) -> pl.DataFrame:
        results = []

        for row in mo.status.progress_bar(
            judge_input_groups_df.iter_rows(named=True),
            total=judge_input_groups_df.height,
        ):
            candidate_rows = []
            requests = []

            for visgen_result in row["group"]:
                request = build_visjudge_request_from_visgen_result(
                    {
                        "vis_id": row["vis_id"],
                        "grammar": row["grammar"],
                        **visgen_result,
                    }
                )

                if request is None:
                    continue
                candidate_rows.append(visgen_result)
                requests.append(request)

            if not requests:
                logger.warning(
                    "No valid VisJudge requests for vis_id %s, skipping.",
                    row["vis_id"],
                )
                continue

            logger.info(
                "Built %s VisJudge requests for vis_id %s",
                len(requests),
                row["vis_id"],
            )

            judgements_raw = visjudge_client.run_many(requests)

            for visgen_result, judgement_raw in zip(candidate_rows, judgements_raw):
                results.append(
                    visgen_result
                    | {
                        "judgement_raw": judgement_raw,
                        "judgement": (
                            extract_json(judgement_raw)
                            if judgement_raw is not None
                            else None
                        ),
                    }
                )

        return pl.from_dicts(results)

    return (generate_judgements_df,)


@app.cell(hide_code=True)
def _(generate_judgements_df, judge_input_groups_df, visjudge_client):
    judgements_df = generate_judgements_df(
        judge_input_groups_df,
        visjudge_client,
    )
    judgements_df
    return (judgements_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Inspect and Persist Results
    """)
    return


@app.cell(hide_code=True)
def _(judgements_df, pl):
    judgements_df.select(
        pl.len().alias("rows"),
        pl.col("judgement").is_not_null().sum().alias("non_null_judgements"),
    )
    return


@app.cell(hide_code=True)
def _(judgements_df, store):
    store.write_judgements_df(judgements_df)
    return


@app.cell(hide_code=True)
def _(VisEvalDataset, VisGroundDataset, VisJudgeLmClient, lm_cliproxy):
    store = VisGroundDataset()
    viseval_dataset = VisEvalDataset()
    # visjudge_client = VisJudgeApiClient()
    visjudge_client = VisJudgeLmClient(
        lm=lm_cliproxy("gpt-5.4"),
    )
    return store, viseval_dataset, visjudge_client


@app.cell(hide_code=True)
def _():
    import logging

    import marimo as mo
    import polars as pl
    from PIL import Image
    from visground.datasets import VisEvalDataset, VisGroundDataset
    from visground.generation import VisualizationBackend
    from visground.generation.backends import resolve_visualization_backend
    from visground.grounding import get_audience_description
    from visground.judge import (
        VisJudgeLmClient,
        VisJudgeClient,
        VisJudgeRequest,
        build_visjudge_prompt,
    )
    from visground.utils import extract_json
    from visground.lm import lm_cliproxy

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return (
        Image,
        VisEvalDataset,
        VisGroundDataset,
        VisJudgeClient,
        VisJudgeLmClient,
        VisJudgeRequest,
        VisualizationBackend,
        build_visjudge_prompt,
        extract_json,
        get_audience_description,
        lm_cliproxy,
        logger,
        mo,
        pl,
        resolve_visualization_backend,
    )


if __name__ == "__main__":
    app.run()
