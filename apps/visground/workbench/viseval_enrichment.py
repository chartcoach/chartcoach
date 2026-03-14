import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # VisEval Dataset Enrichment
    """)
    return


@app.cell(hide_code=True)
def _(VisEvalDataset):
    viseval_dataset = VisEvalDataset()
    viseval_dataset.queries_df
    return (viseval_dataset,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We batch the NL queries that we want to canonicalize by the output visualization ID they produced in the nvbench / VisEval dataset.
    """)
    return


@app.cell(hide_code=True)
def _(viseval_dataset):
    query_batches_df = viseval_dataset.queries_df.group_by(
        "id",
        maintain_order=True,
    ).agg("nl_query")
    query_batches_df
    return (query_batches_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We use a DSPY signature to clearly express the logic based on which we generate the canonical queries.
    """)
    return


@app.cell
def _(dspy):
    class CanonicalizeVizQueries(dspy.Signature):
        """
        Synthesize a list of natural language visualization queries into a single, canonical data request.

        All input queries express the EXACT SAME underlying analytical intent, but may request different chart types, axes, or visual layouts. Your task is to extract this shared data intent and write one standardized, visually-neutral sentence.

        Rules:
        1) Remove visual prescriptions: Strip out all mentions of chart types (bar chart, pie chart, scatter plot, line graph, histogram, trend line), axes (x-axis, y-axis), and visual layout modifiers (stacked, colored by).
        2) Convert visual groupings to data mappings: Translate phrases like "colored by X" to "grouped by X".
        3) Standardize phrasing: Use a clear, direct, and neutral structure, ideally starting with "Show [metric/data] by [dimension]...".
        4) Preserve data operations: Keep any explicit data operations shared across the queries, such as sorting ("ordered by X descending"), aggregations ("average", "total"), limits ("top 5"), and transformations ("binned by month").
        5) Fix grammar: The final output must be a single, well-formed grammatical sentence without dangling modifiers or leftover visualization fragments.
        """

        queries: list[str] = dspy.InputField(
            desc="Array of NL queries that share the exact same data intent but contain varying visual instructions."
        )
        canonical_query: str = dspy.OutputField(
            desc="A single, grammatically correct sentence capturing the shared analytical intent, completely independent of visual design choices."
        )


    class JudgeCanonicalQuery(dspy.Signature):
        """
        Evaluate if a proposed canonical query correctly synthesizes a list of natural language visualization queries.

        A valid canonical query MUST:
        1. Completely strip away all visual/chart references (e.g., 'pie chart', 'bar graph', 'x-axis', 'y-axis', 'colored by').
        2. Accurately preserve the data and analytical intent (metrics, dimensions, filters, sorting, grouping, limits).
        3. Be a clean, grammatically correct sentence without awkward leftover fragments.
        """

        original_queries: list[str] = dspy.InputField(
            desc="The original visualization queries."
        )
        proposed_canonical_query: str = dspy.InputField(
            desc="The generated canonical query to evaluate."
        )

        contains_visual_artifacts: bool = dspy.OutputField(
            desc="True if words like 'chart', 'graph', 'axis', 'plot', 'scatter', 'pie' are still present."
        )
        preserves_data_operations: bool = dspy.OutputField(
            desc="True if aggregations, limits, sorting, and groupings from the original queries are kept."
        )
        is_grammatical: bool = dspy.OutputField(
            desc="True if it reads naturally, typically starting with 'Show...' without dangling fragments like 'in a'."
        )

    return CanonicalizeVizQueries, JudgeCanonicalQuery


@app.cell(hide_code=True)
def _(JudgeCanonicalQuery, dspy):
    judge = dspy.Predict(JudgeCanonicalQuery)


    def canonical_reward_fn(args: dict, pred: dspy.Prediction) -> float:
        proposed_query = pred.canonical_query.lower()

        # Fast Heuristic Check
        forbidden_terms = [
            "chart",
            "graph",
            "plot",
            "axis",
            "pie",
            "bar",
            "scatter",
            "line",
            "histogram",
            "colored by",
            "visualize",
        ]
        if any(term in proposed_query for term in forbidden_terms):
            return 0.0

        # LLM Judge Check for nuance: intent and grammar
        assessment = judge(
            original_queries=args["queries"],
            proposed_canonical_query=pred.canonical_query,
        )

        # Only acceptable outcome is perfection
        if (
            assessment.contains_visual_artifacts is False
            and assessment.preserves_data_operations is True
            and assessment.is_grammatical is True
        ):
            return 1.0

        return 0.0

    return (canonical_reward_fn,)


@app.cell(hide_code=True)
def _(generate_mapping, json, pl, query_batches_df, viseval_dataset):
    # Generate
    batches = query_batches_df["nl_query"].to_list()
    mapping = generate_mapping(batches)

    # Organize
    mapping_df = pl.from_dict(
        {
            "nl_query": list(mapping.keys()),
            "nl_query_intent": list(mapping.values()),
        }
    )

    # Persist
    mapping_output_path = (
        viseval_dataset.root.parent.parent / "enrichment" / "nl_query_intent.json"
    )
    mapping_output_path.parent.mkdir(parents=True, exist_ok=True)
    mapping_output_path.write_text(json.dumps(mapping_df.to_dicts(), indent=2))

    mapping_df
    return


@app.cell(hide_code=True)
def _(CanonicalizeVizQueries, canonical_reward_fn, dspy):
    base_canonicalizer = dspy.Predict(CanonicalizeVizQueries)
    canonicalizer = dspy.Refine(
        module=base_canonicalizer,
        N=3,
        reward_fn=canonical_reward_fn,
        threshold=1.0,
    )


    def generate_mapping(batches: list[list[str]]) -> dict[str, str]:
        # Run LLM calls in parallel
        parallel = dspy.Parallel(num_threads=8)
        result = parallel(
            [
                (
                    canonicalizer,
                    dspy.Example(queries=queries).with_inputs("queries"),
                )
                for queries in batches
            ]
        )

        # Collect results
        mapping: dict[str, str] = {}
        for i, r in enumerate(result):
            queries = batches[i]
            canonical_query = r.canonical_query
            for query in queries:
                mapping[query] = canonical_query

        return mapping

    return (generate_mapping,)


@app.cell(hide_code=True)
def _():
    import dspy

    dspy.configure(
        lm=dspy.LM(
            "openai/gpt-5.4",
            api_base="http://localhost:8317/v1",
            api_key="sk-",
        ),
        track_usage=True,
    )
    dspy.configure_cache(
        enable_disk_cache=True,
        enable_memory_cache=True,
    )
    return (dspy,)


@app.cell(hide_code=True)
def _():
    import marimo as mo
    from visground.datasets import VisEvalDataset
    import polars as pl
    import json

    return VisEvalDataset, json, mo, pl


if __name__ == "__main__":
    app.run()
