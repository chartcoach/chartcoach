import marimo

__generated_with = "0.22.4"
app = marimo.App(width="columns", app_title="Guideline Application")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""
    # ::lucide:bot:: Agentic Visualization Feedback

    This notebook accompanies Section 5.4 of the paper. It demonstrates how our structured catalog enables an AI agent to provide grounded, actionable feedback on data visualizations.

    Current automated feedback methods present a trade-off:

    - **Rule-based checks** are reliable but rigid. They spot explicit violations but miss nuanced opportunities for perceptual or rhetorical improvement.
    - **General-purpose LLMs** can offer creative suggestions but often produce ungrounded, generic advice that is not tied to verifiable evidence.

    This notebook presents a third approach: an agent that generates reliable feedback by strategically querying our structured knowledge catalog. It follows a **progressive disclosure** protocol--first using SQL to learn the catalog's structure, then using targeted retrieval and semantic search to gather evidence before synthesizing its final recommendations.
    """)
    return


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:bar-chart-3:: The Scenario: A Chart for a Grocery Flyer
    """)
    return


@app.cell(hide_code=True)
def _(user_situation_md):
    user_situation_md
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We start with a bar chart about water use from [Our World in Data](https://ourworldindata.org/water-access-resources-sanitation). The specific scenario at hand is to use it in a grocery flyer to help shoppers quickly compare the water usage of beef with lower-water alternatives like chicken or eggs.

    The design question is whether the current descending sort order is effective for the rapid, comparison-focused task of a shopper.

    The cells below load the chart image and use [google/deplot](https://huggingface.co/google/deplot) to reverse-engineer its data and specification to prepare it for analysis.
    """)
    return


@app.cell(hide_code=True)
def _(load_image, mo):
    image_url = "https://raw.githubusercontent.com/vis-nlp/ChartQA/refs/heads/main/ChartQA%20Dataset/train/png/42351550020333.png"
    image = load_image(image_url)
    mo_image = mo.image(
        image_url, style={"max-height": "400px", "object-fit": "contain"}
    )
    mo_image
    return image, mo_image


@app.cell(hide_code=True)
def _(df, generate_column_renames):
    renames = generate_column_renames(df)
    renames
    return (renames,)


@app.cell(hide_code=True)
def _(dspy, pl):
    class ColumnRenamer(dspy.Signature):
        """Rename columns in a DataFrame to be more descriptive and to be in snake_case."""

        columns: list[str] = dspy.InputField()
        renames: dict[str, str] = dspy.OutputField(
            desc="Mapping of original column names to new names. New names always in snake_case."
        )

    def generate_column_renames(df: pl.DataFrame) -> dict[str, str]:
        columns: list[str] = []
        for column in df.columns:
            sample_values = (
                df[column]
                .unique(maintain_order=True)
                .sample(min(df.height, 5))
                .to_list()
            )
            columns.append(f"Column: `{column}`\nSample values: {sample_values}")

        rename_columns = dspy.Predict(ColumnRenamer)
        return rename_columns(columns=columns).renames

    return (generate_column_renames,)


@app.cell(hide_code=True)
def _(extract_plotted_data, image):
    df = extract_plotted_data(image)
    df
    return (df,)


@app.cell(hide_code=True)
def _(df, renames, type_inferred_df):
    renamed_df = type_inferred_df(df.rename(renames))
    renamed_df
    return (renamed_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Conversion to Draco Specification

    We convert the rasterized chart image into a visualization specification format that [Draco 2](https://github.com/cmudig/draco2) can use for analysis for visualization design guideline violations.
    """)
    return


@app.cell(hide_code=True)
def _(
    altair_renderer,
    chart_to_draco_spec_dict,
    clean_draco_spec_dict,
    drx,
    image,
    renamed_df,
):
    draco_spec_dict = chart_to_draco_spec_dict(image=image, df=renamed_df)
    draco_spec = drx.spec(clean_draco_spec_dict(draco_spec_dict))
    altair_chart = draco_spec.render(
        renamed_df,
        label_mapping=snake_to_title,
        renderer=altair_renderer,
    )
    altair_chart
    return altair_chart, draco_spec, draco_spec_dict


@app.cell(hide_code=True)
def _(Image, pl):
    def extract_plotted_data(plot_img: Image.Image) -> pl.DataFrame:
        from io import StringIO

        from transformers import (
            Pix2StructForConditionalGeneration,
            Pix2StructProcessor,
        )

        # Initialize model and processor
        processor = Pix2StructProcessor.from_pretrained("google/deplot")
        model = Pix2StructForConditionalGeneration.from_pretrained("google/deplot")

        # Run inference
        inputs = processor(
            images=plot_img,
            text="Generate underlying data table of the figure below:",
            return_tensors="pt",
        )
        predictions = model.generate(**inputs, max_new_tokens=512)

        # Decode predictions and convert into CSV-like format
        decoded = processor.decode(predictions[0], skip_special_tokens=True)
        SEP = " <0x0A> "
        stringio = StringIO(
            "\n".join([item.replace(" | ", "|") for item in decoded.split(SEP)])
        )

        # Leverage Polars to parse the CSV-like data
        return pl.read_csv(stringio, separator="|")

    return (extract_plotted_data,)


@app.cell(hide_code=True)
def _(pl):
    def type_inferred_df(df: pl.DataFrame) -> pl.DataFrame:
        res_df = df

        maybe_year_column = [
            c
            for c in df.columns
            if "year" in c.lower() and not df[c].dtype.is_temporal()
        ]
        for col in maybe_year_column:
            res_df = res_df.with_columns(pl.col(col).cast(pl.String).str.to_date("%Y"))

        return res_df

    return (type_inferred_df,)


@app.cell(column=2, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:ruler:: Baseline A: Symbolic Checks

    We first evaluate the chart's specification with Draco. This checks structural and perceptual constraints in a form the notebook can inspect.

    The check confirms that the chart is structurally sound, but it does not answer the situational question: is this design effective for a grocery flyer comparison task?
    """)
    return


@app.cell(hide_code=True)
def _(altair_chart, mo):
    mo.vstack(
        [
            mo.md("**Evaluated Visualization**"),
            altair_chart,
        ]
    )
    return


@app.cell(hide_code=True)
def _(altair_renderer, candidates, mo, renamed_df):
    mo.vstack(
        [
            mo.md(
                "**Draco finds that the used visualizations is already the most optimal design choice from a perceptual effectiveness perspective**"
            )
        ]
        + [
            mo.vstack(
                [
                    mo.md(f"**Candidate {i + 1} has a cost of ${spec.cost}$**"),
                    spec.render(
                        df=renamed_df,
                        label_mapping=snake_to_title,
                        renderer=altair_renderer,
                    ),
                ]
            )
            for i, spec in enumerate(candidates)
        ]
    )
    return


@app.cell(hide_code=True)
def _(Image, draco_chart_spec, dspy, json, pathlib, pl, schema_from_dataframe):
    class DracoSpecDictGenerator(dspy.Signature):
        """Generate a Draco chart specification from a DataFrame schema."""

        chart: dspy.Image = dspy.InputField(desc="Image of the chart.")
        field_schema_json: str = dspy.InputField(
            desc="JSON representation of the Dataframe's schema whose data is plotted in the chart."
        )
        # We generate JSON instead of structured output to avoid perf drop of reasoning models
        draco_spec_json: str = dspy.OutputField(
            desc="\n\n".join(
                [
                    "JSON representation of the Draco chart specification.",
                    "It must adhere to the `SpecificationDict` model as defined in:",
                    f"```python\n{pathlib.Path(draco_chart_spec.__file__).read_text()}\n```",
                ]
            )
        )

    def chart_to_draco_spec_dict(
        image: Image.Image,
        df: pl.DataFrame,
    ) -> draco_chart_spec.SpecificationDict:
        generate_draco_spec = dspy.Predict(DracoSpecDictGenerator)
        chart = dspy.Image.from_PIL(image)
        field_schema_json = json.dumps(schema_from_dataframe(df), indent=2)
        draco_spec_json = generate_draco_spec(
            chart=chart,
            field_schema_json=field_schema_json,
        ).draco_spec_json

        return draco_chart_spec.SpecificationDict.model_validate_json(draco_spec_json)

    return (chart_to_draco_spec_dict,)


@app.cell(hide_code=True)
def _(draco_chart_spec):
    def clean_draco_spec_dict(
        spec_dict: draco_chart_spec.SpecificationDict,
    ) -> dict:
        dict_without_nones = spec_dict.model_dump(exclude_none=True)

        # Clingo parsing fails when encountering float values like 1.0, so we convert them to int
        return eval(str(dict_without_nones).replace(".0", ""))

    return (clean_draco_spec_dict,)


@app.cell(hide_code=True)
def _(AltairRenderer, DracoExpress):
    drx = DracoExpress()
    altair_renderer = AltairRenderer(mark_config={"line": {"point": True}})
    return altair_renderer, drx


@app.cell(hide_code=True)
def _():
    import draco.renderer.altair.types as draco_chart_spec
    from draco import schema_from_dataframe
    from draco.dracox import DracoExpress
    from draco.renderer.altair.altair_renderer import AltairRenderer

    return (
        AltairRenderer,
        DracoExpress,
        draco_chart_spec,
        schema_from_dataframe,
    )


@app.cell(hide_code=True)
def _():
    import altair as alt
    import draco as drc

    return alt, drc


@app.cell(hide_code=True)
def _(drc, pl):
    def construct_draco_visrec_program(df: pl.DataFrame):
        data_schema_dict = drc.schema_from_dataframe(df)
        data_schema_facts = drc.dict_to_facts(data_schema_dict)
        base_facts = [
            *data_schema_facts,
            "entity(view,root,v0).",
            "entity(mark,v0,m0).",
        ]
        field_requires = [f"require(field, {field})." for field in df.columns]

        return [
            *base_facts,
            *field_requires,
        ]

    return (construct_draco_visrec_program,)


@app.cell(hide_code=True)
def _(construct_draco_visrec_program, drx, renamed_df):
    draco_visrec_program = construct_draco_visrec_program(renamed_df)
    models = 3
    candidates = list(drx.complete_spec(draco_visrec_program, models=models))
    return (candidates,)


@app.cell(column=3, hide_code=True)
def _(feedback_model, mo):
    mo.md(rf"""
    ## ::lucide:unlink:: Baseline B: Ungrounded LLM Feedback

    Next, we prompt a general-purpose language model (`{feedback_model}`) with the chart image and the user's situation.

    The model produces fluent, conversational advice. However, this feedback is not grounded in a verifiable knowledge source. The suggestions are generic and cannot be traced back to specific evidence, making them difficult to trust or justify in a design context.
    """)
    return


@app.cell(hide_code=True)
def _(feedback_model, mo, mo_image, plain_vis_feedback, user_situation_md):
    mo.vstack(
        [
            user_situation_md,
            mo_image,
            mo.md(
                "\n\n".join(
                    [
                        f"### Feedback by `{feedback_model}`",
                        plain_vis_feedback,
                    ]
                )
            ),
        ]
    )
    return


@app.cell(hide_code=True)
def _(
    draco_spec_dict,
    dspy,
    feedback_model,
    generate_plain_vis_feedback,
    image,
    init_lm,
    user_situation,
):
    with dspy.context(lm=init_lm(feedback_model)):
        plain_vis_feedback = generate_plain_vis_feedback(
            image=image,
            situation=user_situation,
            draco_spec_dict=draco_spec_dict,
            draco_features=[],
        )
    return (plain_vis_feedback,)


@app.cell(hide_code=True)
def _(Image, draco_chart_spec, dspy):
    class VisFeedback(dspy.Signature):
        """Generate actionable visualization design feedback for a given chart, referencing knowledge sources of all suggestions."""

        chart: dspy.Image = dspy.InputField(desc="Image of the chart to evaluate.")
        situation: str = dspy.InputField(
            desc="Description of the analytical and rhetorical goals of the chart creator, including the target audience and context."
        )
        chart_spec: str = dspy.InputField(
            desc="JSON string representing the schema of the DataFrame plotted in the chart."
        )
        existing_chart_feedback: str = dspy.InputField(
            desc="Existing feedback on the chart from other sources, if any, to build upon."
        )
        feedback: str = dspy.OutputField(
            desc="Feedback on the chart. If the chart is good, state that it is satisfactory. Otherwise, provide top max 3-5 most important actionable suggestions to improve the chart, each with rationale. Output in markdown format without fences."
        )

    def format_existing_chart_feedback(
        draco_features: list,
    ) -> str:
        if not draco_features:
            return ""

        return "\n\n".join(
            [
                "**Draco Activated Features (Soft Constraints) [1]**",
                str(draco_features),
                "---"
                "[1] Yang, Junran, Péter Ferenc Gyarmati, Zehua Zeng, and Dominik Moritz. “Draco 2: An Extensible Platform to Model Visualization Design.” 2023 IEEE Visualization and Visual Analytics (VIS), October 2023, 166–70. https://doi.org/10.1109/VIS54172.2023.00042.",
            ]
        )

    def generate_plain_vis_feedback(
        image: Image.Image,
        situation: str,
        draco_spec_dict: draco_chart_spec.SpecificationDict,
        draco_features: list,
    ) -> str:
        generate_feedback = dspy.Predict(VisFeedback)
        chart = dspy.Image.from_PIL(image)
        chart_spec = draco_spec_dict.model_dump_json(exclude_none=True)
        existing_chart_feedback = format_existing_chart_feedback(
            draco_features,
        )

        return generate_feedback(
            chart=chart,
            situation=situation,
            chart_spec=chart_spec,
            existing_chart_feedback=existing_chart_feedback,
        ).feedback

    return (generate_plain_vis_feedback,)


@app.cell(hide_code=True)
def _(mo):
    user_situation = """We're adapting this chart from a city drought report for a grocery flyer aimed at general-public shoppers. They will likely see it briefly while deciding what protein to buy for dinner. Our goal is to help someone considering beef quickly compare it with lower-water alternatives like chicken, eggs, or pulses. We kept the bars sorted from highest to lowest water use so beef stands out, but we're not sure that ranking is the best layout for this quick substitute-comparison task."""

    user_situation_md = mo.md("\n".join(["**User Situation**", f"> {user_situation}"]))
    feedback_model = "openai/gpt-5.4"
    return feedback_model, user_situation, user_situation_md


@app.cell(column=4, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:badge-check:: Our Approach: Grounded Agentic Feedback

    Finally, we use our catalog-grounded agent. This agent combines the reasoning of an LLM with the structured reliability of a database, and is constrained to act upon the verifiable knowledge within our catalog.

    The **Agent Trajectory** below reveals this evidence-gathering strategy in detail:
    1.  **Discovery:** It begins not with a guess, but with discovery. The agent first runs `sql` queries (`SHOW ALL TABLES`, `SELECT ... FROM guideline_labels`) to inspect the catalog's schema and learn the available vocabulary.
    2.  **Narrowing:** Armed with this knowledge, it maps the user's situation ("comparison task," "general audience") to the catalog's specific labels. It then constructs a more targeted `sql` query to create a shortlist of relevant guideline IDs.
    3.  **Verification:** Finally, it retrieves the full text for the most promising candidates to read their detailed rationale and advice. The trace shows the agent even adapting to a failed tool call by using `sql` again to ensure it can access the necessary evidence.

    This multi-step protocol of discovery, narrowing, and verification ensures every piece of advice is based on evidence the agent has explicitly read from the catalog, preventing the kind of ungrounded suggestions seen from a generic LLM.
    """)
    return


@app.cell(hide_code=True)
def _(mo, mo_image, used_guidelines_df, user_situation_md, visfeedback):
    mo.vstack(
        [
            user_situation_md,
            mo_image,
            mo.md("### Grounded Feedback"),
            mo.md(visfeedback.feedback),
            mo.md("**Used Guidelines**"),
            used_guidelines_df,
            mo.md("**Agent Trajectory**"),
            visfeedback.trajectory,
        ]
    )
    return


@app.cell(hide_code=True)
def _(
    draco_spec,
    draco_spec_dict,
    dspy,
    feedback_model,
    generate_plain_vis_feedback,
    image,
    init_lm,
    user_situation,
):
    with dspy.context(lm=init_lm(feedback_model)):
        context_enriched_vis_feedback = generate_plain_vis_feedback(
            image=image,
            situation=user_situation,
            draco_spec_dict=draco_spec_dict,
            draco_features=draco_spec.features_df.to_polars().to_dicts(),
        )
    return


@app.cell(hide_code=True)
def _(search_session, pl, visfeedback):
    used_guidelines_df = search_session.catalog.frame.join(
        pl.from_dict({"id": visfeedback.guideline_ids}),
        on="id",
        how="right",
    ).select("guideline", "references")
    return (used_guidelines_df,)


@app.cell(hide_code=True)
def _(search_session, dspy):
    class VisFeedbackAgent(dspy.Signature):
        """Generate grounded visualization feedback by progressively disclosing the catalog.

        Follow this protocol:
        1. Start with `sql` to discover the available DuckDB schema and vocabulary.
           Begin with queries such as `show all tables`, `describe <table>`, and
           small samples like `select * from <table> limit 5` or
           `select distinct ...`.
        2. Map the user's situation onto labels and metadata values that actually
           exist in the catalog; never invent taxonomy values.
        3. Use SQL to shortlist likely guideline ids with lightweight fields first.
        4. Read evidence for finalists with `get`, starting with overviews and
           escalating to specific sections only when needed.
        5. Use `search` only after SQL narrowing for semantic
           comparison among a small candidate set.

        Do not finish until you have inspected the schema, built a shortlist, and
        read enough retrieved evidence to justify every cited guideline id.

        Base every recommendation on retrieved evidence, keep the feedback specific to
        the chart and situation, and return only the 3-5 highest-leverage suggestions.
        If a current chart choice is appropriate for the stated situation, say so
        instead of forcing a rewrite.

        Never retrieve guidelines which have no effect on the design because e.g. they
        are already satisfied by the current chart or irrelevant to the situation.
        Prioritize reading guidelines which would result in impactful changes and genuinely
        help the user given their specific goal, audience and context.
        """

        chart_image: dspy.Image = dspy.InputField(
            desc="Image of the chart to evaluate. Use it to inspect the current design choices and verify whether retrieved guidance actually applies to this chart."
        )
        situation: str = dspy.InputField(
            desc="Description of the chart creator's goals, audience, outlet, reading conditions, and decision task. Use this to derive likely labels and shortlist criteria after discovering the catalog schema."
        )
        chart_spec: str = dspy.InputField(
            desc="JSON string of the chart's structured specification. Use it to reason about marks, encodings, axes, sorting, legends, and other structural choices; do not use it as a literal search query."
        )
        feedback: str = dspy.OutputField(
            desc="Markdown feedback without fences. If the chart is already a good fit for the stated situation, say so. Otherwise provide the 3-5 highest-leverage actionable suggestions, each grounded in retrieved evidence and citing the relevant guideline ids inline when practical. Do not cite guidance you did not inspect."
        )
        guideline_ids: list[str] = dspy.OutputField(
            desc="Unique guideline ids that directly support the feedback, ordered by importance. Only include ids whose retrieved evidence you actually inspected."
        )

    sql_tool = dspy.Tool(
        search_session.tools.sql,
        desc="Primary discovery tool. Use this first to inspect schema, sample tables, discover the available label vocabulary, and build SQL shortlist queries before any semantic search.",
        arg_desc={
            "sql": "Use this first. Discover the schema with queries like `show all tables`, `describe <table>`, `select * from <table> limit 5`, and `select distinct ...`. After discovery, use SQL to shortlist candidate guideline ids and lightweight metadata before reading full docs.",
            "row_limit": "Maximum number of rows to return. Raise it only when the default sample is too small to understand the table or shortlist.",
        },
    )
    get_tool = dspy.Tool(
        search_session.tools.get,
        desc="Deterministic retrieval tool. Use this after SQL narrowing to read exact candidate docs by id, or with carefully discovered metadata filters when exact ids are not yet known.",
        arg_desc={
            "ids": "Exact document ids to fetch once SQL or prior samples tell you which docs you want. Prefer this when you already know the precise records to read.",
            "where": "Optional Chroma metadata filter. Discover the available metadata fields by sampling first, and use boolean operators like `$and` when you need multiple predicates.",
            "where_document": "Optional literal text filter for already narrowed docs. Use sparingly after you understand the document shapes.",
            "include": "Optional response fields to include. Leave null unless you specifically need a custom payload.",
            "limit": "Maximum number of matching docs to return when filtering.",
            "offset": "Skip this many matching docs when paginating through a filtered set.",
        },
    )
    search_tool = dspy.Tool(
        search_session.tools.search,
        desc="Secondary semantic retrieval tool over indexed text docs. Use only after SQL discovery or on a small candidate set; do not use this as the first step.",
        arg_desc={
            "query_texts": "Short semantic probes over the indexed text docs. Use this only after SQL narrowing or when you need to compare meaning among a small candidate set; do not begin with the full raw situation if SQL can first reveal the schema and label vocabulary.",
            "limit": "Maximum number of nearest-neighbor docs to return.",
            "where": "Optional Chroma metadata filter. Sample docs first to learn valid metadata fields and use boolean operators like `$and` for multiple predicates.",
            "where_document": "Optional literal text filter on document bodies after you have already narrowed the search space.",
            "include": "Optional response fields to include. Leave null unless you specifically need a custom subset.",
        },
    )
    visfeedback_agent = dspy.ReAct(
        VisFeedbackAgent,
        tools=[
            sql_tool,
            get_tool,
            search_tool,
        ],
        max_iters=32,
    )
    return (visfeedback_agent,)


@app.cell(hide_code=True)
def _(
    draco_spec_dict,
    dspy,
    feedback_model,
    image,
    init_lm,
    user_situation,
    visfeedback_agent,
):
    with dspy.context(lm=init_lm(feedback_model)):
        visfeedback = visfeedback_agent(
            chart_image=image,
            chart_spec=draco_spec_dict.model_dump_json(exclude_none=True),
            situation=user_situation,
        )
    return (visfeedback,)


@app.cell(hide_code=True)
def _():
    import os

    import chromadb.utils.embedding_functions as embedding_functions
    from chartcoach import Catalog
    from chartcoach.search import open_search_session

    openai_large_ef = embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.environ["OPENROUTER_API_KEY"],
        api_base="https://openrouter.ai/api/v1",
        model_name="openai/text-embedding-3-large",
    )
    search_session = open_search_session(
        Catalog.from_parquet("guidelines/catalog.parquet"),
        embedding_fn=openai_large_ef,
    )
    return search_session, os


@app.function(hide_code=True)
def snake_to_title(text: str) -> str:
    return text.replace("_", " ").title()


@app.cell(column=5, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:cog:: Agent & Tool Implementation

    The agent is implemented using DSPy's `ReAct` module. Its core logic is defined in the `VisFeedbackAgent` signature, which instructs the model to follow the progressive disclosure protocol.

    The agent has access to three distinct tools for interacting with the catalog, each with a specific role:
    - **`sql_tool`**: For initial discovery of schema and vocabulary.
    - **`get_tool`**: For deterministic retrieval of guidelines by ID or metadata.
    - **`search_tool`**: For secondary semantic refinement over small candidate sets.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.mermaid("""
    flowchart LR
        %% Inputs
        subgraph Inputs ["Grounded Context (Inputs)"]
            direction TB
            IMG["chart_image<br/>(Visual Verification)"]
            SIT["situation<br/>(Goals & Constraints)"]
            SPEC["chart_spec<br/>(Structural Reasoning)"]
        end

        %% The Central Agent
        Inputs --> AGENT(["VisFeedback Agent<br/>(ReAct Loop)"])

        %% Knowledge Base
        CATALOG[("Knowledge Catalog<br/>(DuckDB + Chroma)")]

        %% The Progressive Disclosure Loop
        subgraph Loop ["Progressive Disclosure Loop"]
            direction TB

            %% Step 1: SQL Discovery
            subgraph Step1 ["1. Guideline Discovery"]
                T1["sql_tool<br/>───────────<br/>• Inspect Schema<br/>• Map Vocabulary<br/>• Build SQL Shortlist"]
            end

            %% Step 2: Deterministic Get
            subgraph Step2 ["2. Target Retrieval"]
                T2["get_tool<br/>───────────<br/>• Fetch exact IDs<br/>• Metadata filtering<br/>• Inspect sections"]
            end

            %% Step 3: Semantic Search
            subgraph Step3 ["3. Semantic Refinement"]
                T3["search_tool<br/>───────────<br/>• Semantic Probes<br/>• Compare candidates<br/>• Use as secondary pass"]
            end

            AGENT <==> Step1
            Step1 --> Step2
            Step2 <==> AGENT
            Step2 --> Step3
            Step3 <==> AGENT
        end

        %% Knowledge Base Connections
        Step1 & Step2 & Step3 <--> CATALOG

        %% Final Output
        AGENT --> FINAL["Situated & Grounded<br/>Feedback<br/>(3-5 Suggestions)"]

        %% Professional Style Definitions
        classDef stageBox fill:#f1f3f5,stroke:#dee2e6,stroke-width:1px,color:#495057,font-weight:bold
        classDef input fill:#e7f5ff,stroke:#228be6,stroke-width:1.5px,color:#1864ab
        classDef agent fill:#ffffff,stroke:#343a40,stroke-width:2px,color:#212529,font-weight:bold
        classDef tool fill:#ffffff,stroke:#868e96,stroke-width:1px,stroke-dasharray: 5 5,color:#495057
        classDef store fill:#ebfbee,stroke:#40c057,stroke-width:1.5px,color:#2b8a3e

        %% Apply Classes
        class Inputs,Loop,Step1,Step2,Step3 stageBox
        class IMG,SIT,SPEC input
        class AGENT,FINAL agent
        class T1,T2,T3 tool
        class CATALOG store
    """)
    return


@app.cell(column=6, hide_code=True)
def _(Image, httpx):
    from io import BytesIO

    def load_image(url: str) -> Image.Image:
        res = httpx.get(url)
        res.raise_for_status()
        return Image.open(BytesIO(res.content))

    return (load_image,)


@app.cell(hide_code=True)
def _(mo):
    NB_ROOT = mo.notebook_dir()
    REPO_ROOT = NB_ROOT.parent.parent.parent
    CATALOG_PARQUET_PATH = REPO_ROOT / "guidelines" / "catalog.parquet"
    return


@app.cell(hide_code=True)
def _():
    import json
    import pathlib
    import warnings

    import httpx
    import marimo as mo
    import polars as pl
    from PIL import Image

    warnings.filterwarnings("ignore")
    return Image, httpx, json, mo, pathlib, pl


@app.cell(hide_code=True)
def _(os):
    import dspy

    def init_lm(model_name: str) -> dspy.LM:
        return dspy.LM(
            model=f"openai/{model_name}",
            api_base="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )

    model_name = "openai/gpt-5.4"
    dspy.configure(lm=init_lm(model_name))
    return dspy, init_lm


if __name__ == "__main__":
    app.run()
