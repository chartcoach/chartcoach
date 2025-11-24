import marimo

__generated_with = "0.18.0"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Pixel-to-Data Extraction

    To critique a chart effectively, we must understand its underlying data distribution, not just its visual surface. We use **DePlot** to linearize the rasterized image into a tabular representation, enabling downstream tools to reason about the data directly.

    > Liu, Fangyu, Julian Eisenschlos, Francesco Piccinno, et al. “DePlot: One-Shot Visual Language Reasoning by Plot-to-Table Translation.” In Findings of the Association for Computational Linguistics: ACL 2023. https://doi.org/10.18653/v1/2023.findings-acl.660.
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
    ## Semantic Enrichment

    DePlot often outputs generic headers (e.g., `col1`). To support semantic reasoning (e.g., knowing that a column represents "Food Impact" rather than just numbers), we use an LLM to infer descriptive `snake_case`schema names from sample values.
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
    ## Abstract Chart Representation

    We lift the cleaned data and image into a **Draco specification**--a renderer-agnostic formalism. This creates a "digital twin" of the visualization, allowing us to apply logical constraints and measure perceptual costs mathematically.

    > Yang, Junran, Péter Ferenc Gyarmati, Zehua Zeng, and Dominik Moritz. “Draco 2: An Extensible Platform to Model Visualization Design.” 2023 IEEE Visualization and Visual Analytics (VIS). https://doi.org/10.1109/VIS54172.2023.00042.
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
    snake_to_title,
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
    ## Baseline: Symbolic Linting

    **The Efficiency Trap:** Symbolic approaches like VizLinter and Draco excel at optimizing perceptual efficiency. However, they often conclude that a chart **cannot be improved** simply because it is perceptually "optimal" (has a low cost). This ignores the reality that **optimizing for perception is not the exclusive criterion** for design. A chart that is perfect for rapid data extraction might fail at persuasion or emotional resonance--nuances these rule-based systems struggle to reason about.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Vega-Lite Linter (VizLinter)

    We employ **VizLinter** to detect fundamental design violations. By analyzing the Vega-Lite specification against a set of rules, it identifies structural errors and deviations from standard best practices.

    > Chen, Qing, Fuling Sun, Xinyue Xu, Zui Chen, Jiazhe Wang, and Nan Cao. “VizLinter: A Linter and Fixer Framework for Data Visualization.” IEEE Transactions on Visualization and Computer Graphics 28, no. 1 (2022): 206–16. https://doi.org/10.1109/TVCG.2021.3114804.
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
    ### Draco Chart Features

    Draco decomposes the visualization into logical facts and evaluates them against a knowledge base of both **hard constraints** and **soft constraints**.

    Unlike errors, these features represent design *trade-offs* (e.g., `encoding_field` counts). Draco aggregates these into a **Global Perceptual Cost**, quantifying the theoretical "cognitive effort" required to read the chart based on empirical weights.

    Based on Draco's knowledge base, the supplied chart has a calculated **Perceptual Cost of ${draco_spec.cost}$**:
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

    Since a high perceptual cost isn't strictly an "error", simple linting is often insufficient. To understand what "optimal" looks like from a purely theoretical perspective, we ask: ***"How would Draco design this chart from scratch?"***

    By generating the mathematically optimal visualization for this specific dataset, we establish a baseline for **maximum perceptual efficiency**--which we can then compare against the user's actual design to highlight missed opportunities (or intentional rhetorical choices).
    """)
    return


@app.cell(hide_code=True)
def _(altair_renderer, candidates, mo, renamed_df, snake_to_title):
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
    ## Baseline: Off-the-shelf LLM

    **The Problem of Hallucination:** We can ask a standard model (`{feedback_model}`) to critique the chart based on the user's specific situation (e.g., "senior audience," "substitution behavior"). While fluent, these models often generate **generic design platitudes** or **hallucinate citations** to appear authoritative. They lack access to a verified body of visualization design knowledge that can be reliably observed and easily extended by users.
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
    feedback_model = "openai/gpt-5.1-chat"
    return feedback_model, user_situation, user_situation_md


@app.cell(column=5, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Baseline: Hybrid (LLM + Linting)

    We can attempt to ground the LLM by feeding it the **perceptual preference violations** detected by Draco and VizLinter.

    While this provides valid technical critiques, it still fails to address **contextual nuance**. Linters can flag "inefficient" choices, but they cannot help the LLM understand *why* those choices might be necessary for a specific audience (e.g., seniors) or rhetorical goal. The resulting feedback remains a mix of technical pedantry and hard-to-verify, potentially hallucinated advice, unanchored to empirical research.
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
    ## Agentic Exploration via Progressive Disclosure

    Unlike symbolic linters (which ignore intent) or standard LLMs (which hallucinate sources), our approach uses **Agentic Progressive Disclosure** to generate feedback that is both situated and grounded.

    This capability is directly enabled by our granular **knowledge representation**, which structurally separates high-level metadata from dense empirical evidence. Instead of overwhelming the context window with irrelevant text, the agent traverses the catalog hierarchically:

    1.  **Taxonomy Alignment (Labels):** The agent maps user intent (e.g., "brochure for seniors") to the catalog's vocabulary (e.g., `audience:elderly`) using lightweight labels.
    2.  **Guideline Filtering (Abstracts):** It scans concise `title` and `description` fields to identify promising principles without consuming token-heavy details.
    3.  **Evidence Verification (Body):** Only then does it retrieve the full `body` of specific guidelines to validate applicability and formulate grounded feedback.

    By preventing **context pollution**, this method ensures the model remains focused on the user's unique situation while retaining access to deep empirical backing--delivering the "why" that linters miss and the "truth" that raw LLMs lack.

    Note that this way **no design knowledge is hard-coded** into the system prompt. All insights are retrieved dynamically from the catalog--a centralized, flexible resource. This decoupling allows the underlying knowledge base to be **debated, forked, and remixed** by the community, ensuring the agent always draws from a living body of shared best practices rather than static, opaque rules.
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
                        f"### Feedback by Chart Coach powered by `{feedback_model}`",
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
    Below the observable, programmatically accessible catalog of guidelines based on which vis feedback is provided.
    """)
    return


@app.cell(hide_code=True)
def _(Catalog, catalog_parquet, pl):
    catalog = Catalog.from_df(pl.read_parquet(catalog_parquet.absolute()))
    catalog.df()
    return (catalog,)


@app.cell(hide_code=True)
def _():
    from chartcoach_catalog.catalog import Catalog

    return (Catalog,)


@app.cell(column=7, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Utilities
    """)
    return


@app.cell(hide_code=True)
def _(Image, httpx):
    def load_image(url: str) -> Image.Image:
        from io import BytesIO

        res = httpx.get(url)
        return Image.open(BytesIO(res.content))

    def snake_to_title(s: str) -> str:
        return s.replace("_", " ").title()

    return load_image, snake_to_title


@app.cell(hide_code=True)
def _(mo, pathlib):
    NB_ROOT = pathlib.Path(__file__).parent
    CATALOG_PARQUET_PATH = NB_ROOT.parent / "curation" / "catalog.parquet"
    catalog_parquet = mo.watch.file(CATALOG_PARQUET_PATH)
    return (catalog_parquet,)


@app.cell(hide_code=True)
def _():
    import warnings

    warnings.filterwarnings("ignore")
    return


@app.cell(hide_code=True)
def _(os):
    import dspy

    def init_lm(model_name: str) -> dspy.LM:
        return dspy.LM(
            model=f"openrouter/{model_name}",
            api_base="https://openrouter.ai/api/v1",
            api_key=os.environ["OPENROUTER_API_KEY"],
        )

    model_name = "openai/gpt-5.1"

    dspy.configure(lm=init_lm(model_name))
    dspy.configure_cache(
        enable_disk_cache=True,
        enable_memory_cache=True,
    )
    return dspy, init_lm


@app.cell(hide_code=True)
def _():
    import os
    import draco
    import httpx
    import marimo as mo
    import polars as pl
    from PIL import Image
    import pathlib
    import json

    return Image, httpx, json, mo, os, pathlib, pl


if __name__ == "__main__":
    app.run()
