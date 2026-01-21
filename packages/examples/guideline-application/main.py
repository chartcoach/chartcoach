import marimo

__generated_with = "0.19.4"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Step 1: Extracting Data from the Chart Image

    Feedback requires access to the underlying data, not just the rendered pixels. We use DePlot to recover a tabular representation from the rasterized chart image.

    > Liu et al., "DePlot: One-Shot Visual Language Reasoning by Plot-to-Table Translation," ACL 2023. https://doi.org/10.18653/v1/2023.findings-acl.660
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
def _(extract_plotted_data, image):
    df = extract_plotted_data(image)
    df
    return (df,)


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


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Step 2: Inferring Column Semantics

    DePlot produces generic column headers such as `col1`. We prompt a language model to infer descriptive names from sample values, enabling downstream reasoning about what each column represents.
    """)
    return


@app.cell(hide_code=True)
def _(df, renames, type_inferred_df):
    renamed_df = type_inferred_df(df.rename(renames))
    renamed_df
    return (renamed_df,)


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
    ## Step 3: Constructing a Draco Specification

    We map the recovered data and inferred schema to a Draco specification, a renderer-agnostic representation of the chart's visual encoding. This enables constraint-based validation and perceptual cost estimation.

    > Yang et al., "Draco 2: An Extensible Platform to Model Visualization Design", IEEE VIS 2023. https://doi.org/10.1109/VIS54172.2023.00042
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
    from draco.dracox import DracoExpress
    from draco import schema_from_dataframe
    from draco.renderer.altair.altair_renderer import AltairRenderer

    return (
        AltairRenderer,
        DracoExpress,
        draco_chart_spec,
        schema_from_dataframe,
    )


@app.cell(column=3, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Baseline A: Symbolic Linting

    Symbolic tools such as VizLinter and Draco validate charts against structural rules and perceptual constraints. When a chart incurs low perceptual cost and triggers no violations, these tools report that no improvements are needed. This is correct within their scope, but perceptual efficiency is not the only criterion for design quality. A chart optimised for rapid data extraction may still fail to support a specific analytical task or suit a particular audience. Symbolic linters cannot assess such contextual factors.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### VizLinter

    VizLinter checks the Vega-Lite specification against structural rules, detecting encoding violations and deviations from common conventions.

    > Chen et al., "VizLinter: A Linter and Fixer Framework for Data Visualization," TVCG 2022. https://doi.org/10.1109/TVCG.2021.3114804
    """)
    return


@app.cell(hide_code=True)
def _(altair_chart, altair_chart_to_vl_linter_input, mo, vl_linter):
    vl_lint = vl_linter.Lint(altair_chart_to_vl_linter_input(altair_chart))
    vl_linter_violations = vl_lint.lint()
    mo.vstack(
        [
            mo.md(f"**Vega-Lite Linter Found ${len(vl_linter_violations)}$ Issues**"),
            vl_linter_violations,
        ]
    )
    return (vl_linter_violations,)


@app.cell(hide_code=True)
def _(alt):
    def altair_chart_to_vl_linter_input(chart: alt.Chart) -> dict:
        vl = chart.to_dict()
        return {
            "data": {
                "values": list(vl["datasets"].items())[0][1],
            },
            "mark": vl["mark"]["type"],
            "encoding": {
                channel: {"field": enc["field"], "type": enc["type"]}
                for channel, enc in vl["encoding"].items()
                if channel not in ["tooltip"]
            },
        }

    return (altair_chart_to_vl_linter_input,)


@app.cell(hide_code=True)
def _(draco_spec, mo):
    mo.md(rf"""
    ### Draco Features and Perceptual Cost

    Draco represents the chart as logical facts and evaluates them against hard constraints (violations) and soft constraints (trade-offs). Soft constraint activations are aggregated into a perceptual cost score, which estimates the cognitive effort required to read the chart based on empirically derived weights.

    The chart in this scenario has a perceptual cost of **${draco_spec.cost}$**:
    """)
    return


@app.cell(hide_code=True)
def _(draco_spec):
    draco_spec.features_df.to_polars()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Draco Recommendations

    To establish a baseline for perceptual efficiency, we ask Draco to generate chart specifications from scratch given the same data schema. The resulting candidates represent designs that minimise perceptual cost according to Draco's weighted constraints.

    Comparing these candidates to the user's chart can reveal missed optimisations, but deviations from the minimum-cost design may reflect intentional choices that Draco cannot evaluate.
    """)
    return


@app.cell(hide_code=True)
def _(altair_renderer, candidates, mo, renamed_df):
    mo.vstack(
        [
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
def _(construct_draco_visrec_program, drx, renamed_df):
    draco_visrec_program = construct_draco_visrec_program(renamed_df)
    models = 3
    candidates = list(drx.complete_spec(draco_visrec_program, models=models))
    return (candidates,)


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
def _():
    import vega_lite_linter as vl_linter
    import altair as alt
    import draco as drc

    return alt, drc, vl_linter


@app.cell(column=4, hide_code=True)
def _(feedback_model, mo):
    mo.md(rf"""
    ## Baseline B: Off-the-Shelf LLM

    We prompt a language model (`{feedback_model}`) with the chart image and the user's stated goals. The model produces fluent feedback, but it draws on knowledge embedded in its weights rather than verifiable sources. Without grounding, the output may include generic advice that does not address the specific situation or citations that cannot be traced to real publications.
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
            vl_linter_violations=[],
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
        vl_linter_violations: list,
        draco_features: list,
    ) -> str:
        if not vl_linter_violations and not draco_features:
            return ""

        return "\n\n".join(
            [
                "**Vega-Lite Linter Violations (VizLinter) [1]**",
                str(vl_linter_violations),
                "**Draco Activated Features (Soft Constraints) [2]**",
                str(draco_features),
                "---"
                "[1] Chen, Qing, Fuling Sun, Xinyue Xu, Zui Chen, Jiazhe Wang, and Nan Cao. “VizLinter: A Linter and Fixer Framework for Data Visualization.” IEEE Transactions on Visualization and Computer Graphics 28, no. 1 (2022): 206–16. https://doi.org/10.1109/TVCG.2021.3114804.",
                "[2] Yang, Junran, Péter Ferenc Gyarmati, Zehua Zeng, and Dominik Moritz. “Draco 2: An Extensible Platform to Model Visualization Design.” 2023 IEEE Visualization and Visual Analytics (VIS), October 2023, 166–70. https://doi.org/10.1109/VIS54172.2023.00042.",
            ]
        )

    def generate_plain_vis_feedback(
        image: Image.Image,
        situation: str,
        draco_spec_dict: draco_chart_spec.SpecificationDict,
        vl_linter_violations: list,
        draco_features: list,
    ) -> str:
        generate_feedback = dspy.Predict(VisFeedback)
        chart = dspy.Image.from_PIL(image)
        chart_spec = draco_spec_dict.model_dump_json(exclude_none=True)
        existing_chart_feedback = format_existing_chart_feedback(
            vl_linter_violations,
            draco_features,
        )

        return generate_feedback(
            chart=chart,
            situation=situation,
            chart_spec=chart_spec,
            existing_chart_feedback=existing_chart_feedback,
        ).feedback

    return (
        VisFeedback,
        format_existing_chart_feedback,
        generate_plain_vis_feedback,
    )


@app.cell(hide_code=True)
def _(mo):
    user_situation = """I am designing a visual guide for a 'Climate-Friendly Diet' brochure distributed at senior centers. 
    My specific goal is to encourage **substitution behavior** among the elderly--helping them identify high-impact proteins 
    and immediately find lower-impact alternatives (e.g., swapping Beef for Chicken) while making the chart engaging and readable. I'll bring the charts as printed material, as that's what this audience is most comfortable with. 
    I used a strict descending sort to emphasize the massive gap between the worst and best offenders. 
    Based on empirically validated research, does this sorted layout effectively support that specific substitution task for an older audience, or does it introduce cognitive friction?
    """

    user_situation_md = mo.md("\n".join(["**User Situation**", f"> {user_situation}"]))
    feedback_model = "gpt-5.2"
    return feedback_model, user_situation, user_situation_md


@app.cell(column=5, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Baseline C: LLM with Linting Context

    We provide the LLM with the violations and activated features from VizLinter and Draco. This adds technical context to the prompt. However, linting results describe structural properties of the chart; they do not explain when those properties are appropriate for a given audience or task. The model still lacks access to situated design knowledge, so its reasoning about contextual factors remains ungrounded.
    """)
    return


@app.cell(hide_code=True)
def _(
    context_enriched_vis_feedback,
    feedback_model,
    mo,
    mo_image,
    user_situation_md,
):
    mo.vstack(
        [
            user_situation_md,
            mo_image,
            mo.md(
                "\n\n".join(
                    [
                        f"### Feedback by `{feedback_model}` + VizLinter + Draco",
                        context_enriched_vis_feedback,
                    ]
                )
            ),
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
    vl_linter_violations,
):
    with dspy.context(lm=init_lm(feedback_model)):
        context_enriched_vis_feedback = generate_plain_vis_feedback(
            image=image,
            situation=user_situation,
            draco_spec_dict=draco_spec_dict,
            vl_linter_violations=vl_linter_violations,
            draco_features=draco_spec.features_df.to_polars().to_dicts(),
        )
    return (context_enriched_vis_feedback,)


@app.cell(column=6, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Catalog-Grounded Feedback via Progressive Disclosure

    We use the cataloging scheme described in the paper to ground the language model's reasoning. The agent queries the catalog through a hierarchical traversal that limits context consumption:

    1. **Discover vocabulary.** The agent retrieves available labels from the catalog's metadata to map the user's stated goals (e.g., "brochure for seniors") to the catalog's taxonomy (e.g., `audience:older-adults`).
    2. **Filter by abstract.** The agent scans guideline titles and descriptions to identify entries relevant to the user's situation without loading full content.
    3. **Retrieve full guidelines.** For promising candidates, the agent fetches the complete body text and references to verify applicability and formulate feedback.

    This traversal prevents irrelevant guidelines from consuming the model's context window. Each recommendation cites specific guideline IDs, which users can inspect to verify rationale and trace claims to primary sources.

    No design knowledge is embedded in the system prompt. All guidance comes from the catalog, which can be inspected, modified, and extended independently of the feedback system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.mermaid("""
    graph LR
        %% Styles
        classDef input fill:#eceff1,stroke:#455a64,stroke-width:2px,color:#000;
        classDef agent fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#000;
        classDef tool fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#000;
        classDef store fill:#fff9c4,stroke:#fbc02d,stroke-width:2px,stroke-dasharray: 5 5,color:#000;

        %% Inputs
        subgraph Pipeline [Pipeline Inputs]
            Img[Chart Image]:::input
            Data[DePlot Data]:::input
            Lints[Symbolic Lints<br/>Draco/VizLinter]:::input
        end
        Intent[User Intent]:::input

        %% The Central Agent
        Pipeline & Intent --> Agent[VisFeedback Agent]:::agent
        Catalog[(Knowledge Catalog)]:::store

        %% The Loop
        subgraph Loop [Progressive Disclosure Loop]
            direction TB

            %% Step 1: Discovery Tools
            Agent --1. Map Context--> DiscoveryTools
            subgraph DiscoveryTools [Step 1: Discovery]
                direction LR
                T1[Tool: Discover Topics]:::tool
                T2[Tool: Check Authority]:::tool
            end
            DiscoveryTools -.->|Vocabulary & Source Types| Agent

            %% Step 2: Search Tool
            Agent --2. Filter Topics--> SearchTools
            subgraph SearchTools [Step 2: Filtering]
                T3[Tool: Scan Abstracts]:::tool
            end
            SearchTools -.->|Titles & Descriptions| Agent

            %% Step 3: Verification Tool
            Agent --3. Verify Applicability--> VerifyTools
            subgraph VerifyTools [Step 3: Verification]
                T4[Tool: Read Full Guidelines]:::tool
            end
            VerifyTools -.->|Full Rationale & Evidence| Agent
        end

        %% Knowledge Base Connections
        T1 & T2 & T3 & T4 <--> Catalog

        %% Final Output
        Agent --> Final[Situated & Grounded<br/>Feedback]:::agent
    """)
    return


@app.cell(hide_code=True)
def _(
    feedback_model,
    grounded_vis_feedback,
    mo,
    mo_image,
    used_guidelines_df,
    user_situation_md,
):
    mo.vstack(
        [
            user_situation_md,
            mo_image,
            mo.md(
                "\n\n".join(
                    [
                        f"### Catalog-Grounded Feedback (`{feedback_model}`)",
                        grounded_vis_feedback.feedback,
                    ]
                )
            ),
            mo.md("### Used Guidelines"),
            used_guidelines_df,
            mo.md("### Agent Trajectory"),
            grounded_vis_feedback.trajectory,
        ]
    )
    return


@app.cell(hide_code=True)
def _(catalog, grounded_vis_feedback, pl):
    used_guidelines_df = pl.from_dict(
        {"id": grounded_vis_feedback.used_guideline_ids}
    ).join(
        catalog.df(),
        on="id",
        how="left",
    )
    return (used_guidelines_df,)


@app.cell(hide_code=True)
def _(
    draco_spec,
    draco_spec_dict,
    dspy,
    feedback_model,
    generate_grounded_vis_feedback,
    image,
    init_lm,
    user_situation,
    vl_linter_violations,
):
    with dspy.context(lm=init_lm(feedback_model)):
        grounded_vis_feedback = generate_grounded_vis_feedback(
            image=image,
            situation=user_situation,
            draco_spec_dict=draco_spec_dict,
            vl_linter_violations=vl_linter_violations,
            draco_features=draco_spec.features_df.to_polars().to_dicts(),
        )
    return (grounded_vis_feedback,)


@app.cell(hide_code=True)
def _(
    Image,
    VisFeedback,
    draco_chart_spec,
    dspy,
    format_existing_chart_feedback,
    list_guideline_abstracts,
    list_guideline_labels,
    list_reftypes,
    read_guidelines_by_id,
):
    class GroundedVisFeedback(VisFeedback):
        """
        An expert visualization critic that validates design choices against a rigorous knowledge catalog.

        INSTRUCTIONS:
        1. Do not rely on your internal training data for design rules.
        2. You are an investigatory agent. You must map the user's vague requirements (e.g., "make it pop", "old audience") to specific catalog labels (e.g., "color:salience", "accessibility").
        3. You must "show your work" by citing specific Guideline IDs found in the catalog.
        4. Explore the catalog thoroughly: If the user mentions multiple constraints (e.g., color AND tasks), perform multiple searches to find guidelines for each aspect. Retrieve multiple guidelines related to each relevant label or aspect to ensure comprehensive coverage.
        5. Read the full details of multiple retrieved guidelines to assess their relevance, prioritize the best and most useful ones that directly address the situation, and avoid irrelevant or redundant rules.
        6. Always reference the retrieved guideline IDs in the feedback. Ensure every suggestion cites at least one relevant guideline ID from the catalog. Guarantee that feedback avoids content repetition by providing completely distinct suggestions with unique rationales.
        """

        used_guideline_ids: list[str] = dspy.OutputField(
            desc="List of guideline IDs from the catalog that were definitively used to generate the rationale."
        )
        feedback: str = dspy.OutputField(
            desc="\n".join(
                [
                    "Feedback strictly grounded in the catalog guidelines.",
                    "Always add citations to the specific guideline IDs you used. Ensure every suggestion references at least one retrieved ID. Never cite the labels you searched for.",
                    "Ensure that you query the catalog deeply to find relevant rules before giving feedback.",
                    "Your feedback should be actionable, completely distinct top 5 suggestions, each with brief rationale.",
                    "Output in markdown format without fences.",
                ]
            )
        )

    def generate_grounded_vis_feedback(
        image: Image.Image,
        situation: str,
        draco_spec_dict: draco_chart_spec.SpecificationDict,
        vl_linter_violations: list,
        draco_features: list,
    ) -> dspy.Prediction:
        chartcoach = dspy.ReAct(
            GroundedVisFeedback,
            tools=[
                list_guideline_labels,
                list_reftypes,
                list_guideline_abstracts,
                read_guidelines_by_id,
            ],
        )
        chart = dspy.Image.from_PIL(image)
        chart_spec = draco_spec_dict.model_dump_json(exclude_none=True)
        existing_chart_feedback = format_existing_chart_feedback(
            vl_linter_violations,
            draco_features,
        )

        return chartcoach(
            chart=chart,
            situation=situation,
            chart_spec=chart_spec,
            existing_chart_feedback=existing_chart_feedback,
        )

    return (generate_grounded_vis_feedback,)


@app.cell(hide_code=True)
def _(catalog, pl):
    def _query_guidelines(
        df: pl.DataFrame,
        where_labels: list[str] | None = None,
        where_reftypes: list[str] | None = None,
    ) -> pl.DataFrame:
        matches_df = df

        if where_labels is not None:
            matches_df = matches_df.filter(
                pl.col("guideline")
                .struct.field("labels")
                .list.set_intersection(where_labels)
                .list.len()
                > 0
            )

        if where_reftypes is not None:
            matches_df = matches_df.filter(
                pl.col("references")
                .list.join("\n\n")
                .str.contains_any([f"@{rt}{{" for rt in where_reftypes])
            )

        return matches_df

    def list_guideline_labels() -> list[str]:
        """
        [TAXONOMY DISCOVERY] Discover all available topic labels in the catalog.

        Returns a sorted list of searchable labels covering visual design, tasks, accessibility, and other topics.

        WHEN TO USE:
        - Call this FIRST to understand the catalog's vocabulary
        - Map user requirements to specific catalog labels before searching
        - Identify which labels are relevant to the user's situation

        OUTPUT: List of label strings you can use in `list_guideline_abstracts(where_labels=[...])`
        """
        return (
            catalog.df()
            .select("guideline")
            .unnest("guideline")
            .select("labels")
            .explode("labels")
            .unique("labels")
            .sort("labels")["labels"]
            .to_list()
        )

    def list_reftypes() -> list[str]:
        """
        [REFERENCE TYPE DISCOVERY] Discover available source types for filtering by authority.

        Returns reference types available in the catalog for authority-based filtering.

        WHEN TO USE:
        - User requires specific authority levels in their feedback
        - Need to filter for academic rigor vs. general advice
        - Call this to discover available types, then filter in `list_guideline_abstracts(where_reftypes=[...])`

        FILTERING STRATEGY:
        - Examine the returned types and their typical authority levels
        - Choose appropriate types based on user's rigor requirements
        - Can combine multiple types or omit filtering entirely

        OUTPUT: List of reference type strings for filtering
        """
        return (
            catalog.df()
            .select("references")
            .explode("references")
            .select(
                reftype=pl.col("references").str.split("{").list.get(0).str.slice(1)
            )
            .drop_nulls()
            .unique()
        )["reftype"].to_list()

    def list_guideline_abstracts(
        where_labels: list[str] | None = None,
        where_reftypes: list[str] | None = None,
    ) -> str:
        """
        [GUIDELINE SEARCH] Search for relevant guidelines by topic and optionally filter by source authority.

        Returns CSV with columns: id, title, description, labels

        REQUIRED WORKFLOW:
        1. Discover topics: Call `list_guideline_labels()` to find relevant labels
        2. (Optional) Discover source types: Call `list_reftypes()` if filtering by authority
        3. Search iteratively: Call THIS tool multiple times for different aspects

        SEARCH STRATEGY:
        - NEVER try to cover everything in one call - break down the user's needs
        - Perform separate searches for different aspects of the user's situation
        - Consider: visual encoding, analytical tasks, audience characteristics, context
        - Each search should target a coherent subset of concerns

        FILTERING BY AUTHORITY:
        - If user specifies authority requirements: discover types first, then filter accordingly
        - Without authority requirements: omit where_reftypes for broader coverage
        - Discover available types with `list_reftypes()` before filtering

        Args:
            where_labels: Topic filters (OR logic). Discover with `list_guideline_labels()` first.
            where_reftypes: Source type filters (OR logic). Discover with `list_reftypes()` first.

        NEXT STEP: Note promising 'id' values, then call `read_guidelines_by_id([...])`
        """
        from io import StringIO

        matches_df = _query_guidelines(
            catalog.df(),
            where_labels=where_labels,
            where_reftypes=where_reftypes,
        )

        abstract_df = matches_df.select(
            pl.col("id"),
            pl.col("guideline").struct.field("title"),
            pl.col("guideline").struct.field("description"),
            pl.col("guideline").struct.field("labels").list.join(";"),
        )
        stringio = StringIO()
        abstract_df.write_csv(stringio)

        return stringio.getvalue()

    def read_guidelines_by_id(ids: list[str]) -> list[dict]:
        """
        [DETAILED RETRIEVAL] Get full content and citations for specific guidelines.

        Returns list of dicts with: id, body (full rationale + details), references

        WHEN TO USE:
        - After identifying promising guidelines via `list_guideline_abstracts()`
        - When you need the complete rationale to cite in your feedback
        - To access implementation details and supporting evidence

        CRITICAL RULES:
        - Abstracts alone are insufficient for strong arguments
        - The 'body' field contains the evidence you need to cite
        - Always retrieve before making definitive claims about a guideline
        - Use returned 'id' values as citations in your final feedback

        Args:
            ids: List of guideline IDs from `list_guideline_abstracts()` output

        OUTPUT: Full guideline content ready for citation
        """
        id_df = pl.DataFrame({"id": ids})
        matched_df = id_df.join(catalog.df(), on="id", how="inner")
        return matched_df.select(
            "id",
            pl.col("guideline").struct.field("body"),
            "references",
        ).to_dicts()

    return (
        list_guideline_abstracts,
        list_guideline_labels,
        list_reftypes,
        read_guidelines_by_id,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The table below shows the catalog instance from which guidelines are retrieved. Each row corresponds to a guideline with its metadata, section content, and references.
    """)
    return


@app.cell(hide_code=True)
def _(Catalog, catalog_parquet, pl):
    catalog = Catalog.from_df(pl.read_parquet(catalog_parquet.absolute()))
    catalog.df()
    return (catalog,)


@app.cell(hide_code=True)
def _():
    from chartcoach.catalog.catalog import Catalog

    return (Catalog,)


@app.cell(column=7, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Utility Functions

    Helper functions for image loading, column name formatting, and configuration.
    """)
    return


@app.function(hide_code=True)
def snake_to_title(text: str) -> str:
    return text.replace("_", " ").title()


@app.cell(hide_code=True)
def _(Image, httpx):
    from io import BytesIO

    def load_image(url: str) -> Image.Image:
        res = httpx.get(url)
        res.raise_for_status()
        return Image.open(BytesIO(res.content))

    return (load_image,)


@app.cell(hide_code=True)
def _(mo, pathlib):
    NB_ROOT = pathlib.Path(__file__).parent
    CATALOG_PARQUET_PATH = NB_ROOT.parent / "guideline-cataloging" / "catalog.parquet"
    catalog_parquet = mo.watch.file(CATALOG_PARQUET_PATH)
    return (catalog_parquet,)


@app.cell(hide_code=True)
def _(os):
    import dspy

    def init_lm(model_name: str) -> dspy.LM:
        return dspy.LM(
            model=model_name,
            api_base=os.environ["OPENAI_BASE_URL"],
            api_key=os.environ["OPENAI_API_KEY"],
        )

    model_name = "gpt-5.1-codex-mini"
    dspy.configure(lm=init_lm(model_name))
    dspy.configure_cache(
        enable_disk_cache=True,
        enable_memory_cache=True,
    )
    return dspy, init_lm


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


if __name__ == "__main__":
    app.run()
