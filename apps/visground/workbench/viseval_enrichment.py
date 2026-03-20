import marimo

__generated_with = "0.20.4"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""
    # Visualization Task Classification

    To characterize analytical intent beyond the data-structural facts (such as SQL schemas and result table statistics) already present in the original dataset, we enrich the corpus with high-level, task-oriented metadata.

    We classify each canonical query along three orthogonal axes:

    - `task`
    - `scope`
    - `time_mode`

    This operationalizes established abstractions from visualization research for a richer dataset.

    We define the primary analytical **task** (e.g., *retrieve, compare, relate*) based on the low-level components of analytic activity identified by **Amar et al. (2005)**.

    To capture the structural cardinality of the intended output, we classify the **scope** (e.g., *single-result, record-list, grouped-result*) following the "What" dimension of the multi-level task typology proposed by **Brehmer and Munzner (2013)**, a distinction **Munzner (2009)** highlights as a critical upstream characterization for ensuring visualization validity.

    Finally, we specify the **time_mode** (e.g., *ordered, cyclic, interval*) to reflect the fundamental structural temporal distinctions established by **Aigner et al. (2007)** and integrated as an orthogonal axis in the general design space of visualization tasks by **Schulz et al. (2013)**. This enrichment transforms the dataset from a collection of data-to-code implementation tasks into a repository of situated analytical intents suitable for grounding generative reasoning.
    """)
    return


@app.cell(hide_code=True)
def _(
    canonical_queries_df,
    generate_task_classifications,
    json,
    pl,
    viseval_dataset,
):
    # Generate
    canonical_queries = canonical_queries_df["nl_query_canonical"].to_list()
    task_classifications = generate_task_classifications(canonical_queries)

    # Organize
    task_classifications_df = pl.from_dicts(task_classifications)

    # Persist
    task_classifications_output_path = (
        viseval_dataset.root.parent.parent / "enrichment" / "vis_tasks.json"
    )
    task_classifications_output_path.parent.mkdir(parents=True, exist_ok=True)
    task_classifications_output_path.write_text(
        json.dumps(task_classifications_df.to_dicts(), indent=2)
    )

    task_classifications_df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Aigner, W., Miksch, S., Müller, W., Schumann, H., and Tominski, C. (2007).** "Visualizing time-oriented data—A systematic view." *Computers & Graphics*, 31(3), 401–409. https://doi.org/10.1016/j.cag.2007.01.030

    **Amar, R., Eagan, J., and Stasko, J. (2005).** "Low-level components of analytic activity in information visualization." *IEEE Symposium on Information Visualization (InfoVis 05)*, 111–117. https://doi.org/10.1109/INFVIS.2005.1532136

    **Brehmer, M., and Munzner, T. (2013).** "A Multi-Level Typology of Abstract Visualization Tasks." *IEEE Transactions on Visualization and Computer Graphics*, 19(12), 2376–2385. https://doi.org/10.1109/TVCG.2013.124

    **Munzner, T. (2009).** "A Nested Model for Visualization Design and Validation." *IEEE Transactions on Visualization and Computer Graphics*, 15(6), 921–928. https://doi.org/10.1109/TVCG.2009.111

    **Schulz, H.-J., Nocke, T., Heitzler, M., and Schumann, H. (2013).** "A Design Space of Visualization Tasks." *IEEE Transactions on Visualization and Computer Graphics*, 19(12), 2366–2375. https://doi.org/10.1109/TVCG.2013.120
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We analyze each canonical NL query and classify them based on the type of vis task they express.
    """)
    return


@app.cell(hide_code=True)
def _(mapping_df):
    canonical_queries_df = mapping_df.select("nl_query_canonical").unique(
        maintain_order=True
    )
    canonical_queries_df
    return (canonical_queries_df,)


@app.cell(hide_code=True)
def _(ClassifyVisTask, dspy, vis_task_classification_reward_fn):
    base_vis_task_classifier = dspy.Predict(ClassifyVisTask)
    vis_task_classifier = dspy.Refine(
        module=base_vis_task_classifier,
        N=3,
        reward_fn=vis_task_classification_reward_fn,
        threshold=1.0,
    )

    def generate_task_classifications(
        canonical_queries: list[str],
    ) -> list[dict[str, str]]:
        # Run LLM calls in parallel
        parallel = dspy.Parallel(num_threads=8)
        result = parallel(
            [
                (
                    vis_task_classifier,
                    dspy.Example(nl_query=nl_query).with_inputs("nl_query"),
                )
                for nl_query in canonical_queries
            ]
        )

        return [
            {"nl_query_canonical": nl_query, **dict(classification)}
            for nl_query, classification in zip(canonical_queries, result)
        ]

    return (generate_task_classifications,)


@app.cell(hide_code=True)
def _(JudgeClassifyVisTask, dspy):
    vis_task_classification_judge = dspy.Predict(JudgeClassifyVisTask)

    def vis_task_classification_reward_fn(
        args: dict,
        pred: dspy.Prediction,
    ) -> float:
        judgement = vis_task_classification_judge(
            nl_query=args["nl_query"],
            predicted_task=pred.task,
            predicted_scope=pred.scope,
            predicted_time_mode=pred.time_mode,
        )

        checks = [
            judgement.task_correct,
            judgement.scope_correct,
            judgement.time_mode_correct,
            judgement.internally_consistent,
        ]

        return sum(bool(x) for x in checks) / len(checks)

    return (vis_task_classification_reward_fn,)


@app.cell(hide_code=True)
def _(ScopeLabel, TaskLabel, TimeLabel, dspy, get_args):
    class ClassifyVisTask(dspy.Signature):
        """
        Classify the input natural-language visualization query
        into a compact task schema according to the rules below.

        Primary task rules:
        - retrieve: list or look up raw records or attributes.
        - compare: compare values across categories or groups.
        - distribute: characterize frequencies or distributions, often with bins.
        - trend: show change over ordered time.
        - compose: show proportions, shares, percentages, or composition.
        - relate: show association between two variables or two summaries.
        - extreme: find highest, lowest, top, bottom, most, least, or best/worst cases.

        Result scope rules:
        - single-result: one scalar or one selected item
        - record-list: multiple raw rows/items/attributes
        - grouped-result: one result per group/bin/category/series

        Time mode rules:
        - non-temporal: query does not center on time.
        - timepoint: query refers to one specific date or timestamp.
        - ordered-time: query compares or tracks values over time in sequence.
        - cyclic-time: query uses recurring time units such as weekday, month, or hour.
        - time-interval: query focuses on spans, durations, or start/end periods.
        """

        nl_query: str = dspy.InputField(desc="A natural-language visualization query.")

        task: TaskLabel = dspy.OutputField(desc="Best-fitting primary task label.")
        scope: ScopeLabel = dspy.OutputField(desc="Best-fitting result scope label.")
        time_mode: TimeLabel = dspy.OutputField(desc="Best-fitting time mode label.")

    class JudgeClassifyVisTask(dspy.Signature):
        """
        Judge whether a proposed task annotation is correct for one NL visualization query.

        Be strict:
        - Use only the allowed labels.
        - Evaluate the underlying analytical intent, not chart words like pie chart or bar chart.
        - Prefer the best-fitting primary task, not a merely plausible one.
        - Keep the dimensions internally consistent.
        """

        nl_query: str = dspy.InputField(desc="A natural-language visualization query.")

        predicted_task: TaskLabel = dspy.InputField(desc="Proposed primary task label.")
        predicted_scope: ScopeLabel = dspy.InputField(
            desc="Proposed result scope label."
        )
        predicted_time_mode: TimeLabel = dspy.InputField(
            desc="Proposed time mode label."
        )

        task_correct: bool = dspy.OutputField(
            desc=f"True only if the proposed task is the best-fitting label from: `{get_args(TaskLabel)}`."
        )
        scope_correct: bool = dspy.OutputField(
            desc=f"True only if the proposed scope is the best-fitting label from: `{get_args(ScopeLabel)}`."
        )
        time_mode_correct: bool = dspy.OutputField(
            desc=f"True only if the proposed time mode is the best-fitting label from: `{get_args(TimeLabel)}`."
        )
        internally_consistent: bool = dspy.OutputField(
            desc="True only if the three proposed labels are logically compatible."
        )

    return ClassifyVisTask, JudgeClassifyVisTask


@app.cell(hide_code=True)
def _(Literal):
    TaskLabel = Literal[
        "retrieve",
        "compare",
        "distribute",
        "trend",
        "compose",
        "relate",
        "extreme",
    ]

    ScopeLabel = Literal[
        "single-result",  # one scalar or one selected item
        "record-list",  # multiple raw rows/items/attributes
        "grouped-result",  # one result per group/bin/category/series
    ]

    TimeLabel = Literal[
        "non-temporal",
        "timepoint",
        "ordered-time",
        "cyclic-time",
        "time-interval",
    ]
    return ScopeLabel, TaskLabel, TimeLabel


@app.cell(hide_code=True)
def _():
    from typing import Literal, get_args

    return Literal, get_args


@app.cell(column=1, hide_code=True)
def _(mapping_df, mo):
    mo.md(rf"""
    # Natural Language Query Canonicalization

    To ensure we can test design reasoning capabilities of models, it is desirable to have a canonincal representation of these natural language queries which **perfectly preserve the analytical intent**, but **omit the design decision**.

    > {" ---> ".join(mapping_df.head(1).to_dicts()[0].values())}
    """)
    return


@app.cell(hide_code=True)
def _(generate_mapping, json, pl, query_batches_df, viseval_dataset):
    # Generate
    batches = query_batches_df["nl_query"].to_list()
    mapping = generate_mapping(batches)

    # Organize
    mapping_df = pl.from_dict(
        {
            "nl_query": list(mapping.keys()),
            "nl_query_canonical": list(mapping.values()),
        }
    )

    # Persist
    mapping_output_path = (
        viseval_dataset.root.parent.parent / "enrichment" / "nl_query_canonical.json"
    )
    mapping_output_path.parent.mkdir(parents=True, exist_ok=True)
    mapping_output_path.write_text(json.dumps(mapping_df.to_dicts(), indent=2))

    mapping_df
    return (mapping_df,)


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
def _():
    import dspy

    dspy.configure(
        lm=dspy.LM(
            "openai/gpt-5.4",
            api_base="http://localhost:8317/v1",
            api_key="sk-",
        ),
        track_usage=False,
    )
    dspy.configure_cache(
        enable_disk_cache=True,
        enable_memory_cache=True,
    )
    return (dspy,)


@app.cell(column=2, hide_code=True)
def _(base_example, mo):
    mo.md(rf"""
    # Base Dataset

    The [VisEval](https://github.com/microsoft/VisEval) dataset provides us with natural language queries such as:

    > {base_example["nl_query"]}

    Each query explicitly prescribes the type of visualization the user expects to see, such as *{base_example["chart"].lower()}* in this case. This means that when an LLM is tasked to produce a visualization based on the query, it is only responsible for figuring out a valid implementation in a given chart grammar / programming language + charting library.

    Therefore, using these items, we are not able to evaluate a model's capability in reasoning about *WHAT* design is ideal to satisfy the analytical intent. All we get to see is *HOW* good a model is at implementing the predefined design in a given grammar.
    """)
    return


@app.cell(hide_code=True)
def _(viseval_dataset):
    base_example = viseval_dataset.queries_df.head(1).to_dicts()[0]
    return (base_example,)


@app.cell(hide_code=True)
def _(VisEvalDataset):
    viseval_dataset = VisEvalDataset()
    viseval_dataset.queries_df
    return (viseval_dataset,)


@app.cell(hide_code=True)
def _():
    import marimo as mo
    from visground.datasets import VisEvalDataset
    import polars as pl
    import json

    return VisEvalDataset, json, mo, pl


if __name__ == "__main__":
    app.run()
