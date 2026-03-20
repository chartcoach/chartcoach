import marimo

__generated_with = "0.21.1"
app = marimo.App(width="columns")


@app.cell(column=0)
def _(pl, run_matrix, vis_request_df):
    MODELS = [
        "gpt-5.4",
        "claude-sonnet-4.6",
        "gemini-3.1-pro-preview",
    ]
    GRAMMARS = [
        "matplotlib",
        "altair",
        "plotly",
    ]
    SPECIFICATIONS = [
        "prescribed",  # Chart type is prescribed in query
        "open",  # Only the analytical intent is prescribed, chart type is omitted
    ]
    GROUNDINGS = [
        "none",  # No guidelines injected, LLM relies on its embedded knowledge
        "flat-grounding",  # Full guideline body embedded and retrieved, injected fully
        "structured-grounding",  # Structured, hybrid retrieval and guideline injection
    ]

    generation_results = run_matrix(
        vis_request_df,
        models=MODELS,
        grammars=GRAMMARS,
        specifications=SPECIFICATIONS,
        groundings=GROUNDINGS,
    )
    generation_results_df = pl.from_dicts(generation_results)
    generation_results_df
    return


@app.cell(hide_code=True)
def _(
    AltairBackend,
    MatplotlibBackend,
    PlotlyBackend,
    VisGenRunner,
    VisualizationBackend,
    dspy,
    lm_cliproxy,
    lm_openrouter,
    lm_vertex,
    pl,
    viseval_dataset,
):
    def get_lm_config(model: str) -> tuple[dspy.LM, int]:
        MODEL_MAP = {
            "gpt-5.4": {
                "lm": lm_cliproxy("gpt-5.4"),
                "num_threads": 16,
            },
            "claude-sonnet-4.6": {
                "lm": lm_openrouter("anthropic/claude-sonnet-4.6"),
                "num_threads": 32,
            },
            "gemini-3.1-pro-preview": {
                "lm": lm_vertex("gemini-3.1-pro-preview"),
                "num_threads": 12,
            },
        }
        lm, num_threads = MODEL_MAP[model].values()
        return lm, num_threads

    def get_vis_backend(
        grammar: str,
        grounding: str,
    ) -> VisualizationBackend:
        VISBACKEND_MAP: dict[str, type[VisualizationBackend]] = {
            "matplotlib": MatplotlibBackend,
            "altair": AltairBackend,
            "plotly": PlotlyBackend,
        }
        return VISBACKEND_MAP[grammar](viseval_dataset)

    def get_request_dicts(
        vis_request_df: pl.DataFrame,
        specification: str,
    ) -> list[dict]:
        SPECIFICATION_COL_MAP = {
            "prescribed": "nl_query",
            "open": "nl_query_canonical",
        }
        query_col = SPECIFICATION_COL_MAP[specification]
        return vis_request_df.select(
            "id",
            "chart",
            "db_id",
            pl.col(query_col).alias("query"),
            "task",
            "scope",
            "time_mode",
        ).to_dicts()

    def run_scenario(
        vis_request_df: pl.DataFrame,
        model: str,
        grammar: str,
        specification: str,
        grounding: str,
    ) -> list[dict]:
        requests = get_request_dicts(vis_request_df, specification)
        lm, num_threads = get_lm_config(model)
        vis_backend = get_vis_backend(grammar, grounding)
        runner = VisGenRunner(vis_backend)

        with dspy.context(lm=lm):
            outputs = runner.generate(requests, num_threads=num_threads)

        return [
            {
                "scenario": {
                    "model": model,
                    "grammar": grammar,
                    "specification": specification,
                    "grounding": grounding,
                },
                "result": output,
            }
            for output in outputs
        ]

    def run_matrix(
        vis_request_df: pl.DataFrame,
        models: list[str],
        grammars: list[str],
        specifications: list[str],
        groundings: list[str],
    ) -> list[dict]:
        scenario_outputs = []

        for model in models:
            for grammar in grammars:
                for specification in specifications:
                    for grounding in groundings:
                        scenario_outputs.extend(
                            run_scenario(
                                vis_request_df,
                                model,
                                grammar,
                                specification,
                                grounding,
                            )
                        )
        return scenario_outputs

    return (run_matrix,)


@app.cell(hide_code=True)
def _():
    from visground.generation.backends import (
        MatplotlibBackend,
        AltairBackend,
        PlotlyBackend,
        VisualizationBackend,
    )
    from visground.generation.runner import VisGenRunner

    return (
        AltairBackend,
        MatplotlibBackend,
        PlotlyBackend,
        VisGenRunner,
        VisualizationBackend,
    )


@app.cell(hide_code=True)
def _():
    import dspy
    import os

    dspy.configure_cache(
        enable_disk_cache=True,
        enable_memory_cache=True,
        disk_size_limit_bytes=16 * 1024 * 1024 * 1024,
    )

    def lm_cliproxy(model: str) -> dspy.LM:
        return dspy.LM(
            f"openai/{model}",
            api_base="http://localhost:8317/v1",
            api_key="sk-",
        )

    def lm_openrouter(model: str) -> dspy.LM:
        return dspy.LM(
            f"openai/{model}",
            api_base="https://openrouter.ai/api/v1",
            api_key=os.environ["OPENROUTER_API_KEY"],
        )

    def lm_gemini(model: str) -> dspy.LM:
        return dspy.LM(
            f"gemini/{model}",
            api_key=os.environ["GEMINI_API_KEY"],
        )

    def lm_vertex(model: str) -> dspy.LM:
        return dspy.LM(
            f"vertex_ai/{model}",
            vertex_credentials=os.environ["VERTEX_CREDENTIALS"],
            vertex_location="global",
        )

    dspy.configure(lm=lm_cliproxy("gpt-5.4"))
    return dspy, lm_cliproxy, lm_openrouter, lm_vertex, os


@app.cell(column=1)
def _(os):
    import chartcoach as cc
    import chromadb.utils.embedding_functions as embedding_functions

    openai_small_ef = embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.environ["OPENROUTER_API_KEY"],
        api_base="https://openrouter.ai/api/v1",
        model_name="openai/text-embedding-3-small",
    )

    coach = cc.create(
        catalog="guidelines/catalog.parquet",
        embedding_fn=openai_small_ef,
    )
    return (coach,)


@app.cell
def _(coach):
    coach.catalog.df
    return


@app.cell
def _(coach):
    coach.index.collection.query(
        query_texts=["pie chart"], where={"role": "section.advice"}
    )
    return


@app.cell
def _():
    return


@app.cell(column=2, hide_code=True)
def _(mo):
    mo.md(r"""
    # Evaluation Cohort Construction
    """)
    return


@app.cell(hide_code=True)
def _(vis_request_base_df, vis_request_sampled_aux_df):
    vis_request_df = vis_request_sampled_aux_df.select(id="original_id").join(
        vis_request_base_df,
        how="left",
        on="id",
    )
    vis_request_df
    return (vis_request_df,)


@app.cell(hide_code=True)
def _(MAX_TASKS_PER_DB, TARGET_N, mo):
    mo.md(rf"""
    We construct a stratified subset of the VisEval dataset ($N={TARGET_N}$) to evaluate our cataloging scheme. A naive random sample risks over-representing common databases (domains) and duplicate query paraphrases. Instead, we use a deterministic, four-step sampling strategy to ensure the benchmark tests diverse and ambiguous design scenarios.

    ### 1. Intent Deduplication and Ambiguity Scoring

    The raw dataset contains multiple natural language paraphrases for the same underlying SQL query and data table. Evaluating all of them inflates the $N$-count without testing new design reasoning. 

    *   **Method:** We group the dataset by our enriched `nl_query_canonical` field, collapsing paraphrases into unique analytical intents.
    *   **Ambiguity Scoring:** During grouping, we aggregate all acceptable `chart` types for each intent. Intents with multiple valid chart types (e.g., both Pie and Bar are acceptable) are prioritized. This tests the system's ability to make situated design choices when multiple encodings are technically valid.

    ### 2. Ecological Validity (Domain Round-Robin)

    Visualization systems must generalize across different semantic domains (e.g., finance, healthcare, sports) and data schemas. 

    *   **Method:** We group tasks by their source database (`db_id`) and rank them based on ambiguity and VisEval hardness.
    *   **Round-Robin Selection:** We select exactly one task from *every* available database domain before permitting a second task from *any* domain (capped at ${MAX_TASKS_PER_DB}$). This ensures the final cohort spans the maximum number of unique data domains possible.

    ### 3. Analytical Task Balancing

    Real-world visualization encompasses a variety of analytical tasks (e.g., `compare`, `trend`, `distribute`). Unchecked, common tasks like `compare` will crowd out rarer tasks, limiting benchmark coverage.

    *   **Method:** While performing the domain round-robin, we calculate a secondary rank partitioned by the analytical `task`. 
    *   **Interleaved Sorting:** By interleaving the selection across task families, we ensure the final cohort maintains a balanced distribution of analytical tasks.

    By sorting the dataset by **1) Domain Breadth**, **2) Task Balance**, **3) Chart Ambiguity**, and **4) Hardness**, this sampling algorithm yields a benchmark cohort that isolates the evaluation to the most challenging and diverse design choices in the corpus.
    """)
    return


@app.cell(hide_code=True)
def _(pl, vis_request_base_df):
    TARGET_N = 150
    MAX_TASKS_PER_DB = 3

    vis_request_sampled_aux_df = (
        vis_request_base_df
        # 1. Map categorical hardness to a numeric score to prioritize challenging tasks.
        .with_columns(
            hardness_score=pl.col("hardness").replace(
                {
                    "Easy": 1,
                    "Medium": 2,
                    "Hard": 3,
                    "Extra Hard": 4,
                }
            )
        )
        # 2. Collapse paraphrase variants by grouping on the canonical analytical intent.
        .group_by(
            "nl_query_canonical",
            "db_id",
            "task",
            "scope",
            "time_mode",
        )
        # 3. Aggregate metadata per intent. Crucially, collect all acceptable chart
        # types to identify tasks where the design choice is inherently ambiguous.
        .agg(
            pl.col("chart").unique().alias("valid_charts"),
            pl.col("hardness").first().alias("hardness"),
            pl.col("hardness_score").max().alias("hardness_score"),
            pl.col("nl_query").first().alias("representative_nl_query"),
            pl.col("id").first().alias("original_id"),
        )
        .with_columns(num_valid_charts=pl.col("valid_charts").list.len())
        # 4. Shuffle to eliminate systemic bias before applying deterministic sort rules.
        .sample(fraction=1.0, seed=42)
        # 5. Prioritize highly ambiguous (multiple valid charts) and difficult tasks.
        .sort(by=["num_valid_charts", "hardness_score"], descending=[True, True])
        # 6. Assign a rank (1, 2, 3...) to tasks within each database. Because of the
        # preceding sort, rank 1 is the most challenging/ambiguous task for that DB.
        .with_columns(
            pl.int_range(1, pl.len() + 1).over("db_id").alias("db_balance_rank")
        )
        # 7. Apply the hard cap per database domain (e.g., drop rank 3+ if MAX is 2).
        .filter(pl.col("db_balance_rank") <= MAX_TASKS_PER_DB)
        # 8. Compute a task rank *partitioned by the DB rank pass*. This ensures that
        # when we collect all the "1st picks" from the DBs, we round-robin across the
        # analytical tasks (compare, trend, etc.) rather than over-representing one.
        .with_columns(
            pl.int_range(1, pl.len() + 1)
            .over(["db_balance_rank", "task"])
            .alias("task_balance_rank")
        )
        # 9. Final Sort:
        # - db_balance_rank (ASC): Guarantees we take exactly 1 from EVERY available DB
        #   before taking a 2nd from ANY DB.
        # - task_balance_rank (ASC): Interleaves the analytical tasks evenly.
        # - Tie-breakers (DESC): Fall back to the most ambiguous and difficult tasks.
        .sort(
            by=[
                "db_balance_rank",
                "task_balance_rank",
                "num_valid_charts",
                "hardness_score",
            ],
            descending=[False, False, True, True],
        )
        # 10. Truncate to the final evaluation cohort size.
        .head(TARGET_N)
    )

    vis_request_sampled_aux_df
    return MAX_TASKS_PER_DB, TARGET_N, vis_request_sampled_aux_df


@app.cell(hide_code=True)
def _(mo, vis_request_df):
    mo.md(rf"""
    The dataframe below is the full set of ${vis_request_df.height}$ visualizations from the VisEval dataset by canonical analytical intent from which we take a stratified sample for factorial evaluation.
    """)
    return


@app.cell(hide_code=True)
def _(pl, viseval_dataset):
    vis_request_base_df = (
        viseval_dataset.queries_enriched_df.select(
            "id",
            "chart",
            "hardness",
            "db_id",
            "nl_query",
            "enrichment",
        )
        .unnest("enrichment")
        .group_by("id", maintain_order=True)
        .agg(data=pl.struct("*"))
        .select("id", pl.col("data").list.first())
        .unnest("data")
    )
    vis_request_base_df
    return (vis_request_base_df,)


@app.cell(hide_code=True)
def _(VisEvalDataset):
    viseval_dataset = VisEvalDataset()
    return (viseval_dataset,)


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import polars as pl

    from visground.datasets import VisEvalDataset

    return VisEvalDataset, mo, pl


if __name__ == "__main__":
    app.run()
