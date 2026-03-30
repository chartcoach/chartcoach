import marimo

__generated_with = "0.21.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 03 Generating

    Expand grounding bundles into model/grammar scenarios and generate candidate visualizations.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Stage Contract

    - Input: `02_grounding.parquet`
    - Output: `03_generate.parquet`
    - Responsibility: build generation requests, batch them into scenarios, and run the generation models
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Runtime Configuration
    """)
    return


@app.cell(hide_code=True)
def _(Literal):
    # ModelName = Literal["gpt-5.4", "claude-sonnet-4.6", "gemini-3.1-pro-preview"]
    ModelName = Literal["gpt-5.4", "gpt-5.3-codex"]
    # GrammarName = Literal["matplotlib", "altair", "plotly"]
    GrammarName = Literal["matplotlib", "plotly"]
    SITUATED_GRAMMARS = {"matplotlib"}
    return GrammarName, ModelName, SITUATED_GRAMMARS


@app.cell(hide_code=True)
def _(ModelName, dspy, lm_cliproxy, lm_openrouter):
    def get_lm_config(model: ModelName) -> tuple[dspy.LM, int]:
        model_map = {
            "gpt-5.4": {
                "lm": lm_cliproxy("gpt-5.4"),
                "num_threads": 16,
            },
            "gpt-5.3-codex": {
                "lm": lm_cliproxy("gpt-5.3-codex"),
                "num_threads": 16,
            },
            "claude-sonnet-4.6": {
                "lm": lm_openrouter("anthropic/claude-sonnet-4.6"),
                "num_threads": 32,
            },
            "gemini-3.1-pro-preview": {
                "lm": lm_openrouter("google/gemini-3.1-pro-preview"),
                "num_threads": 32,
            },
        }
        lm, num_threads = model_map[model].values()
        return lm, num_threads

    def get_review_lm() -> dspy.LM:
        return lm_cliproxy("gpt-5.4")

    return get_lm_config, get_review_lm


@app.cell(hide_code=True)
def _(VisualizationBackend, resolve_visualization_backend, viseval_dataset):
    def get_vis_backend(grammar: str) -> VisualizationBackend:
        return resolve_visualization_backend(grammar, viseval_dataset)

    return (get_vis_backend,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Load Input Artifact
    """)
    return


@app.cell(hide_code=True)
def _(store):
    grounding_df = store.read_grounding_df()
    grounding_df
    return (grounding_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Build Generation Requests
    """)
    return


@app.cell(hide_code=True)
def _(VisualizationRequestRecord, get_audience_description):
    def grounding_row_to_visgen_input(row: dict) -> VisualizationRequestRecord:
        requirements: list[str] = []
        for guideline_id, guidance in zip(
            row["result"]["guideline_ids"],
            row["result"]["guidance"],
        ):
            requirements.append(f"Guideline `{guideline_id}` states:\n{guidance}")

        audience = row["request"]["audience"]
        if row["grounding_mode"] == "none" and audience is not None:
            requirements.append(f"`audience`: {get_audience_description(audience)}")

        return {
            "id": row["request"]["id"],
            "query": row["request"]["query"],
            "requirements": requirements,
        }

    return (grounding_row_to_visgen_input,)


@app.cell(hide_code=True)
def _(
    GrammarName,
    ModelName,
    SITUATED_GRAMMARS,
    get_args,
    grounding_row_to_visgen_input,
    pl,
):
    def build_visgen_input_df(grounding_df: pl.DataFrame) -> pl.DataFrame:
        visgen_inputs = []

        for model in get_args(ModelName):
            for grammar in get_args(GrammarName):
                for row in grounding_df.iter_rows(named=True):
                    if (
                        row["request"]["audience"] is not None
                        and grammar not in SITUATED_GRAMMARS
                    ):
                        continue

                    grounding_id = row["grounding_id"]
                    visgen_input = grounding_row_to_visgen_input(row)
                    visgen_inputs.append(
                        {
                            "visgen_id": "-".join([grounding_id, grammar, model]),
                            "model": model,
                            "grammar": grammar,
                            "grounding_id": grounding_id,
                            "input": visgen_input,
                        }
                    )

        return pl.from_dicts(visgen_inputs)

    return (build_visgen_input_df,)


@app.cell(hide_code=True)
def _(build_visgen_input_df, grounding_df):
    visgen_input_df = build_visgen_input_df(grounding_df)
    visgen_input_df
    return (visgen_input_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Batch Scenarios
    """)
    return


@app.cell(hide_code=True)
def _(pl, visgen_input_df):
    scenario_df = (
        visgen_input_df.group_by("model", "grammar")
        .agg(scenario=pl.struct("*"))
        .sort("model", "grammar")
    )
    scenario_df
    return (scenario_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Run Generation
    """)
    return


@app.cell(hide_code=True)
def _(
    VisGenRunner,
    dspy,
    get_lm_config,
    get_review_lm,
    get_vis_backend,
    mo,
    pl,
):
    def run_scenarios(scenario_df: pl.DataFrame) -> pl.DataFrame:
        scenario_results = []

        for item in mo.status.progress_bar(
            scenario_df.iter_rows(named=True),
            total=scenario_df.height,
        ):
            model = item["model"]
            grammar = item["grammar"]
            scenario = item["scenario"]

            lm, num_threads = get_lm_config(model)
            review_lm = get_review_lm()
            vis_backend = get_vis_backend(grammar)

            with dspy.context(lm=lm):
                runner = VisGenRunner(vis_backend, reviewer_lm=review_lm)
                inputs = [d["input"] for d in scenario]
                outputs = runner.generate(inputs, num_threads=num_threads)
                scenario_results.append(
                    {
                        "run": item,
                        "outputs": outputs,
                    }
                )

        return pl.from_dicts(scenario_results)

    return (run_scenarios,)


@app.cell(hide_code=True)
def _(run_scenarios, scenario_df):
    scenario_results_df = run_scenarios(scenario_df)
    scenario_results_df.head()
    return (scenario_results_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Persist Output Artifact
    """)
    return


@app.cell(hide_code=True)
def _(scenario_results_df, store):
    store.write_generated_df(scenario_results_df)
    return


@app.cell(hide_code=True)
def _(VisEvalDataset, VisGroundDataset):
    store = VisGroundDataset()
    viseval_dataset = VisEvalDataset()
    return store, viseval_dataset


@app.cell(hide_code=True)
def _():
    from typing import Literal, get_args

    import dspy
    import marimo as mo
    import polars as pl
    from visground.datasets import VisEvalDataset, VisGroundDataset
    from visground.generation import VisGenRunner, VisualizationBackend
    from visground.generation.backends import resolve_visualization_backend
    from visground.generation.models import VisualizationRequestRecord
    from visground.grounding import get_audience_description
    from visground.lm import lm_cliproxy, lm_openrouter

    dspy.configure(lm=lm_cliproxy("gpt-5.4"))
    return (
        Literal,
        VisEvalDataset,
        VisGenRunner,
        VisGroundDataset,
        VisualizationBackend,
        VisualizationRequestRecord,
        dspy,
        get_args,
        get_audience_description,
        lm_cliproxy,
        lm_openrouter,
        mo,
        pl,
        resolve_visualization_backend,
    )


if __name__ == "__main__":
    app.run()
