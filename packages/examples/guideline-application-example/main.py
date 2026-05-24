import marimo

__generated_with = "0.22.4"
app = marimo.App(width="columns", app_title="Guideline Application")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""
    # ::lucide:bot:: Agentic Visualization Feedback

    Section 5.4 uses the structured catalog to generate grounded, actionable feedback on data visualizations.

    Current automated feedback methods present a trade-off:

    - **Rule-based checks** are reliable but rigid. They spot explicit violations but miss nuanced opportunities for perceptual or rhetorical improvement.
    - **General-purpose LLMs** can offer creative suggestions but often produce ungrounded, generic advice that is not tied to verifiable evidence.

    This notebook presents a third approach: an agent that generates reliable feedback by strategically querying our structured knowledge catalog. It follows a **progressive disclosure** protocol--first discovering catalog vocabulary with deterministic tools, then using targeted retrieval and semantic search to gather evidence before synthesizing its final recommendations.
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

    The next cells load the chart image and use [google/deplot](https://huggingface.co/google/deplot) to reverse-engineer its data and specification.
    """)
    return


@app.cell(hide_code=True)
def _(load_image, mo):
    image_source = "https://raw.githubusercontent.com/vis-nlp/ChartQA/refs/heads/main/ChartQA%20Dataset/train/png/42351550020333.png"
    image = load_image(image_source)
    mo_image = mo.image(
        image_source, style={"max-height": "400px", "object-fit": "contain"}
    )
    mo_image
    return image, image_source, mo_image


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

        processor = Pix2StructProcessor.from_pretrained("google/deplot")
        model = Pix2StructForConditionalGeneration.from_pretrained("google/deplot")

        inputs = processor(
            images=plot_img,
            text="Generate underlying data table of the figure below:",
            return_tensors="pt",
        )
        predictions = model.generate(**inputs, max_new_tokens=512)

        decoded = processor.decode(predictions[0], skip_special_tokens=True)
        SEP = " <0x0A> "
        stringio = StringIO(
            "\n".join([item.replace(" | ", "|") for item in decoded.split(SEP)])
        )

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
        # JSON avoids the reasoning-model performance hit from structured output.
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

    The agent first inspects catalog vocabulary and guideline summaries, then narrows to labels and semantic probes that match the shopper-comparison scenario, and finally reads exact guideline evidence before writing feedback.
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
        generate_plain_vis_feedback(
            image=image,
            situation=user_situation,
            draco_spec_dict=draco_spec_dict,
            draco_features=draco_spec.features_df.to_polars().to_dicts(),
        )
    return


@app.cell(hide_code=True)
def _(search_session, pl, visfeedback):
    used_guidelines_df = search_session.catalog.to_frame().join(
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
        1. Start with `values` and `list_guidelines` to discover available catalog
           vocabulary, label prefixes, section roles, and candidate guideline ids.
        2. Map the user's situation onto labels and metadata values that actually
           exist in the catalog; never invent taxonomy values.
        3. Use deterministic listing and retrieval to shortlist likely guideline ids
           with lightweight fields first.
        4. Read evidence for finalists with `retrieve_guidelines`, starting with
           overviews and escalating to specific sections only when needed.
        5. Use semantic search only after deterministic narrowing for semantic
           comparison among a small candidate set.

        Do not finish until you have inspected the vocabulary, built a shortlist, and
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
            desc="Description of the chart creator's goals, audience, outlet, reading conditions, and decision task. Use this to derive likely labels and shortlist criteria after discovering the catalog vocabulary."
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

    from chartcoach.tools import CatalogTools

    catalog_tools = CatalogTools(search_session.catalog)
    values_tool = dspy.Tool(
        catalog_tools.count_values,
        desc="Catalog vocabulary tool. Count values in catalog tables; use table='guideline_labels', column='label' to discover available labels.",
        arg_desc={
            "table": "Catalog table name, such as `guideline_labels` or `sections`.",
            "column": "Column to count, such as `label` or `role`.",
            "explode": "Whether to count list items separately.",
            "contains": "Optional substring filter for values.",
            "limit": "Maximum values to return.",
        },
    )
    list_tool = dspy.Tool(
        catalog_tools.list_guidelines,
        desc="Guideline listing tool. Use this to shortlist guideline ids and summaries before retrieving full evidence.",
        arg_desc={
            "labels": "Exact labels that every listed guideline must contain.",
            "label_prefixes": "Label prefixes such as `chart:` or `task:` for broader narrowing.",
            "contains": "Case-insensitive text to match in guideline ids, titles, or descriptions.",
            "limit": "Maximum guideline summaries to return.",
        },
    )
    retrieve_tool = dspy.Tool(
        catalog_tools.retrieve_guidelines,
        desc="Deterministic guideline retrieval tool. Use this after catalog narrowing to read exact candidate guidelines by id, labels, label prefixes, title text, or section roles.",
        arg_desc={
            "ids": "Exact guideline ids to fetch once deterministic listing or semantic search tells you which records you want.",
            "labels": "Exact labels that every returned guideline must contain.",
            "label_prefixes": "Label prefixes such as `chart:` or `task:` for broader deterministic narrowing.",
            "contains": "Case-insensitive text to match in guideline ids, titles, or descriptions.",
            "roles": "Section roles to include in each returned guideline, such as `context`, `advice`, `mistake`, `fix`, or `exceptions`.",
            "limit": "Maximum number of guidelines to return.",
        },
    )
    from chartcoach.search import search_guidelines

    def guideline_search(
        query_text: str,
        limit: int = 8,
        where: dict[str, object] | None = None,
        where_document: dict[str, object] | None = None,
    ) -> dict[str, object]:
        return search_guidelines(
            search_session.get_index(),
            query_text,
            limit=limit,
            where=where,
            where_document=where_document,
        ).to_dict()

    guideline_search_tool = dspy.Tool(
        guideline_search,
        desc="Semantic guideline search tool. Use this after deterministic filtering when wording matters more than exact labels.",
        arg_desc={
            "query_text": "Short semantic probe for matching guideline advice.",
            "limit": "Maximum unique guideline rows to return.",
            "where": "Native Chroma metadata filter, for example {'labels': {'$contains': 'chart:bar'}}.",
            "where_document": "Native Chroma document filter, for example {'$contains': 'axis'}.",
        },
    )
    visfeedback_agent = dspy.ReAct(
        VisFeedbackAgent,
        tools=[
            values_tool,
            list_tool,
            retrieve_tool,
            guideline_search_tool,
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
    from chartcoach import Catalog
    from chartcoach.paths import default_index_dir
    from types import SimpleNamespace

    catalog = Catalog.from_parquet("guidelines/catalog.parquet")
    index = None

    def get_index():
        nonlocal index
        if index is None:
            import os

            import chromadb.utils.embedding_functions as embedding_functions
            from chartcoach.search import ChromaIndex

            openai_large_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_key=os.environ["OPENROUTER_API_KEY"],
                api_base="https://openrouter.ai/api/v1",
                model_name="openai/text-embedding-3-large",
            )
            index = ChromaIndex.from_cache(
                catalog,
                cache_dir=default_index_dir(),
                embedding_fn=openai_large_ef,
                cache_mode="reuse_only",
            )
        return index

    search_session = SimpleNamespace(
        catalog=catalog,
        get_index=get_index,
    )
    return (search_session,)


@app.function(hide_code=True)
def snake_to_title(text: str) -> str:
    return text.replace("_", " ").title()


@app.cell(column=5, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:cog:: Agent and Tools

    The `VisFeedbackAgent` signature defines the evidence-gathering protocol used by DSPy's `ReAct` module.

    The agent reads the catalog through four tools:
    - `values_tool`: catalog vocabulary and label discovery
    - `list_tool`: deterministic guideline shortlisting
    - `retrieve_tool`: exact guideline evidence by ID, label, text, or section role
    - `guideline_search_tool`: semantic guideline-level matches
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.mermaid("""
    flowchart LR
        subgraph Inputs ["Grounded Context (Inputs)"]
            direction TB
            IMG["chart_image<br/>(Visual Verification)"]
            SIT["situation<br/>(Goals & Constraints)"]
            SPEC["chart_spec<br/>(Structural Reasoning)"]
        end

        Inputs --> AGENT(["VisFeedback Agent<br/>(ReAct Loop)"])

        CATALOG[("Knowledge Catalog<br/>(Parquet + Chroma)")]

        subgraph Loop ["Progressive Disclosure Loop"]
            direction TB

            subgraph Step1 ["1. Vocabulary Discovery"]
                T1["values_tool<br/>───────────<br/>• Count label values<br/>• Inspect role vocabulary<br/>• Find prefixes"]
            end

            subgraph Step2 ["2. Deterministic Shortlist"]
                T2["list_tool<br/>───────────<br/>• Filter by labels<br/>• Match summary text<br/>• Shortlist guideline IDs"]
            end

            subgraph Step3 ["3. Evidence Retrieval"]
                T3["retrieve_tool<br/>───────────<br/>• Fetch exact IDs<br/>• Filter by sections<br/>• Inspect advice"]
            end

            subgraph Step4 ["4. Guideline Search"]
                T4["guideline_search_tool<br/>───────────<br/>• Match advice semantically<br/>• Use native Chroma filters<br/>• Deduplicate by guideline"]
            end

            AGENT <==> Step1
            Step1 --> Step2
            Step2 --> Step3
            Step3 --> Step4
            Step3 <==> AGENT
            Step4 <==> AGENT
        end

        Step1 & Step2 & Step3 & Step4 <--> CATALOG

        AGENT --> FINAL["Situated & Grounded<br/>Feedback<br/>(3-5 Suggestions)"]

        classDef stageBox fill:#f1f3f5,stroke:#dee2e6,stroke-width:1px,color:#495057,font-weight:bold
        classDef input fill:#e7f5ff,stroke:#228be6,stroke-width:1.5px,color:#1864ab
        classDef agent fill:#ffffff,stroke:#343a40,stroke-width:2px,color:#212529,font-weight:bold
        classDef tool fill:#ffffff,stroke:#868e96,stroke-width:1px,stroke-dasharray: 5 5,color:#495057
        classDef store fill:#ebfbee,stroke:#40c057,stroke-width:1.5px,color:#2b8a3e

        class Inputs,Loop,Step1,Step2,Step3,Step4 stageBox
        class IMG,SIT,SPEC input
        class AGENT,FINAL agent
        class T1,T2,T3,T4 tool
        class CATALOG store
    """)
    return


@app.cell(column=6, hide_code=True)
def _(Image, httpx):
    from io import BytesIO
    from pathlib import Path

    def load_image(source: str) -> Image.Image:
        path = Path(source)
        if path.exists():
            return Image.open(path)
        res = httpx.get(source)
        res.raise_for_status()
        return Image.open(BytesIO(res.content))

    return (load_image,)


@app.cell(hide_code=True)
def _():
    return


@app.cell(hide_code=True)
def _():
    import json
    import os
    import pathlib
    import warnings

    import httpx
    import marimo as mo
    import polars as pl
    from PIL import Image

    warnings.filterwarnings("ignore")
    return Image, httpx, json, mo, os, pathlib, pl


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
