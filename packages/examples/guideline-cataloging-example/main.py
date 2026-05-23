import marimo

__generated_with = "0.22.4"
app = marimo.App(width="columns", app_title="Guideline Cataloging")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""
    # ::lucide:network:: Cataloging Heterogeneous Visualization Design Knowledge

    This notebook demonstrates the expressiveness of our guideline cataloging scheme. Visualization design knowledge exists in many disparate forms. It ranges from controlled psychology experiments and structured performance metrics to editorial heuristics and qualitative rhetoric. Instead of treating these as incompatible domains, this process shows how our schema can accommodate different sources of knowledge. For each distinct source type, we use a generative model to map its unique evidence format into our standardized, operational guideline structure.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.mermaid("""
    flowchart TD
        subgraph stage1["1. Retrieve"]
            direction TB
            S1["Cognitive Science<br/>106 papers"]
            S4["Datawrapper<br/>36 blog posts"]
            S3["Chartability<br/>50 heuristics"]
            S2["Graphical Perception<br/>51 papers + metadata"]
            S5["Talking Charts<br/>32 findings"]
        end

        subgraph stage2["2. Extract"]
            direction TB
            PROMPT["Construct prompt<br/>───────────<br/>• PDF or JSON source<br/>• Guideline template<br/>• Citation format"]
            LLM(["Large Language Model"])
            PARSE["Parse response<br/>───────────<br/>• Split markdown blocks<br/>• Extract sections<br/>• Attach references"]
        end

        subgraph stage3["3. Output"]
            direction TB
            PARQUET[("catalog.parquet<br/>781 guidelines")]
            MD["guidelines/<br/>Markdown files"]
        end

        stage1 --> PROMPT
        PROMPT --> LLM
        LLM --> PARSE
        PARSE --> stage3

        %% Professional Color Palette
        classDef stageBox fill:#f1f3f5,stroke:#dee2e6,stroke-width:1px,color:#495057,font-weight:bold
        classDef source fill:#e7f5ff,stroke:#228be6,stroke-width:1.5px,color:#1864ab
        classDef process fill:#ffffff,stroke:#868e96,stroke-width:1.5px,color:#212529
        classDef output fill:#ebfbee,stroke:#40c057,stroke-width:1.5px,color:#2b8a3e

        %% Apply Classes
        class stage1,stage2,stage3 stageBox
        class S1,S2,S3,S4,S5 source
        class PROMPT,LLM,PARSE process
        class PARQUET,MD output
    """)
    return


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:brain:: Source 1: Cognitive Science and Perception

    We processed 106 academic papers cited in Franconeri et al.'s review *"The Science of Visual Data Communication"*. These papers provide empirical evidence on low-level visual processing, cognitive biases, and applied domains like risk communication. Converting these academic PDFs tests the schema's ability to translate descriptive experimental findings into actionable visualization design guidelines without losing their original context.

    **Reference:**
    > Franconeri, S. L., Padilla, L. M., Shah, P., Zacks, J. M., & Hullman, J. (2021). The science of visual data communication: What works. *Psychological Science in the Public Interest*, 22(3), 110–161.
    """)
    return


@app.cell(hide_code=True)
def _(
    Catalog,
    DEFAULT_CLIENT_CONFIG,
    MISC_PROMPT_DIGEST,
    itertools,
    misc_paper_to_catalog_entries,
    parallel_map,
    param_collapsed,
    processed_misc_items,
):
    misc_tasks = [
        {
            "misc_item": item,
            "model": DEFAULT_CLIENT_CONFIG["model"],
            "reasoning": DEFAULT_CLIENT_CONFIG["reasoning"],
        }
        for item in processed_misc_items
    ]
    misc_entry_lists = parallel_map(
        fn=param_collapsed(misc_paper_to_catalog_entries),
        inputs=misc_tasks,
        n_jobs=16,
        desc="Processing Miscallaneous papers",
        cache_key_provider=lambda inp: "___".join(
            [
                "misc",
                inp["model"],
                inp["misc_item"]["data"]["DOI"],
                MISC_PROMPT_DIGEST,
            ]
        ),
    )
    misc_entries = list(itertools.chain.from_iterable(misc_entry_lists))
    misc_catalog = Catalog(misc_entries)
    misc_catalog.frame
    return (misc_catalog,)


@app.cell(hide_code=True)
def _(display_references, misc_catalog):
    display_references(misc_catalog)
    return


@app.cell(hide_code=True)
def _(
    CatalogEntry,
    GUIDELINE_TEMPLATE,
    MISC_PROMPT_SPEC,
    build_guideline_extraction_prompt,
    client,
    create_pdf_content_part,
    fence,
    finalize_guideline_batch,
    parse_guideline,
    unfence,
    zot_item_bibtex,
    zot_item_bibtex_key,
):
    def misc_paper_to_catalog_entries(
        misc_item: dict,
        model: str,
        reasoning: dict | None = None,
    ) -> list[CatalogEntry]:
        misc_item_title = misc_item["data"]["title"]
        item_bibtex = zot_item_bibtex(misc_item["data"]["key"])
        item_citekey = zot_item_bibtex_key(misc_item["data"]["key"])

        response = client.responses.create(
            model=model,
            reasoning=reasoning,
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": f"Consider this paper titled '{misc_item_title}', attached as PDF:",
                        },
                        create_pdf_content_part(misc_item["pdf_bytes"]),
                        {
                            "type": "input_text",
                            "text": "\n".join(
                                [
                                    "Your task is to convert the paper into directly actionable visualization guidelines adhering to this template:",
                                    fence(GUIDELINE_TEMPLATE, lang="md"),
                                ]
                            ),
                        },
                        {
                            "type": "input_text",
                            "text": build_guideline_extraction_prompt(
                                evidence_scope=MISC_PROMPT_SPEC["evidence_scope"],
                                required_basis=MISC_PROMPT_SPEC["required_basis"],
                                cardinality_instruction=MISC_PROMPT_SPEC[
                                    "cardinality_instruction"
                                ],
                                source_specific_rules=MISC_PROMPT_SPEC[
                                    "source_specific_rules"
                                ],
                                required_citations=[f"[@{item_citekey}]"],
                                allow_empty=MISC_PROMPT_SPEC["allow_empty"],
                            ),
                        },
                    ],
                },
            ],
        )
        response_text = response.output_text

        guideline_objects = [
            parse_guideline(md_content) for md_content in unfence(response_text)
        ]
        guideline_objects = finalize_guideline_batch(
            guideline_objects,
            required_basis=MISC_PROMPT_SPEC["required_basis"],
        )
        references = [item_bibtex]

        return [
            CatalogEntry(guideline=guideline_obj, references=references)
            for guideline_obj in guideline_objects
        ]

    return (misc_paper_to_catalog_entries,)


@app.cell(hide_code=True)
def _(prompt_contract_digest):
    MISC_PROMPT_SPEC = {
        "required_basis": "basis:empirical",
        "allow_empty": True,
        "cardinality_instruction": (
            "Extract multiple guidelines if present. "
            "Output each in fenced ```md blocks separately, separated by blank lines."
        ),
        "evidence_scope": (
            "Strictly base each guideline on the evidence provided in this processed paper and nothing else."
        ),
        "source_specific_rules": [
            (
                "Extract only findings whose design implication is clear enough "
                "to support a concrete chart choice, critique check, or revision step."
            ),
            (
                "Omit empirical observations that are interesting but "
                "do not tell the practitioner what to choose, inspect, test, or change in a visualization."
            ),
            (
                "Do not import design advice, labels, domain assumptions, or remediation steps that the paper does not actually discuss."
            ),
            (
                "If the paper reports an effect but does not justify a concrete operational chart move, omit it rather than guessing."
            ),
        ],
    }
    MISC_PROMPT_DIGEST = prompt_contract_digest(
        MISC_PROMPT_SPEC,
        ["[@paper]"],
    )
    return MISC_PROMPT_DIGEST, MISC_PROMPT_SPEC


@app.cell(hide_code=True)
def _(ZOTERO_MISC_COLLECTION_ID, process_zot_item, zot):
    misc_items = zot.everything(zot.collection_items(ZOTERO_MISC_COLLECTION_ID))
    processed_misc_items_maybe_wo_pdf = [process_zot_item(item) for item in misc_items]
    processed_misc_items = [
        item
        for item in processed_misc_items_maybe_wo_pdf
        if item["pdf_bytes"] is not None
    ]
    return (processed_misc_items,)


@app.cell(hide_code=True)
def _():
    ZOTERO_MISC_COLLECTION_ID = "LXD29TR5"
    return (ZOTERO_MISC_COLLECTION_ID,)


@app.cell(column=2, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:pen-tool:: Source 2: Practitioner Heuristics

    Formal academic systems often miss the tacit knowledge of daily practice. To capture editorial experience, we processed 36 blog posts from Datawrapper's ["Dos and Don'ts" blog series](https://www.datawrapper.de/blog/category/datavis-dos-and-donts) series authored by data journalists. These sources focus on applied choices like axis truncation, annotation, and structural clarity. This tests whether our schema can represent unstructured, platform-agnostic journalism advice.
    """)
    return


@app.cell(hide_code=True)
def _(
    Catalog,
    DATAWRAPPER_POST_PDF_PATHS,
    DATAWRAPPER_PROMPT_DIGEST,
    DEFAULT_CLIENT_CONFIG,
    datawrapper_post_pdf_to_catalog_entries,
    itertools,
    parallel_map,
    param_collapsed,
):
    dw_tasks = [
        {
            "post_pdf_path": post_pdf_path,
            "model": DEFAULT_CLIENT_CONFIG["model"],
            "reasoning": DEFAULT_CLIENT_CONFIG["reasoning"],
        }
        for post_pdf_path in DATAWRAPPER_POST_PDF_PATHS
    ]
    dw_entry_lists = parallel_map(
        fn=param_collapsed(datawrapper_post_pdf_to_catalog_entries),
        inputs=dw_tasks,
        n_jobs=16,
        desc="Processing Datawrapper posts",
        cache_key_provider=lambda inp: "___".join(
            [
                inp["model"],
                inp["post_pdf_path"].stem,
                DATAWRAPPER_PROMPT_DIGEST,
            ]
        ),
    )
    dw_entries = list(itertools.chain.from_iterable(dw_entry_lists))
    dw_catalog = Catalog(dw_entries)
    dw_catalog.frame
    return (dw_catalog,)


@app.cell(hide_code=True)
def _(display_references, dw_catalog):
    display_references(dw_catalog)
    return


@app.cell(hide_code=True)
def _(
    DATAWRAPPER_PROMPT_SPEC,
    CatalogEntry,
    GUIDELINE_TEMPLATE,
    bibtexparser,
    build_guideline_extraction_prompt,
    client,
    create_pdf_content_part,
    fence,
    finalize_guideline_batch,
    find_datawrapper_bibtex_entry_by_path,
    parse_guideline,
    pathlib,
    unfence,
):
    def datawrapper_post_pdf_to_catalog_entries(
        post_pdf_path: pathlib.Path,
        model: str,
        reasoning: dict | None = None,
    ) -> list[CatalogEntry]:
        bibtex_entry = find_datawrapper_bibtex_entry_by_path(post_pdf_path)
        bibtex_entry_parsed = bibtexparser.loads(bibtex_entry).entries[0]
        post_title = bibtex_entry_parsed["title"]
        citekey = bibtex_entry_parsed["ID"]

        response = client.responses.create(
            model=model,
            reasoning=reasoning,
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "\n".join(
                                [
                                    "Datawrapper.de has a series of blog posts on visualization design and best practices.",
                                    f"Consider this one attached as PDF, titled '{post_title}':",
                                ]
                            ),
                        },
                        create_pdf_content_part(post_pdf_path.read_bytes()),
                        {
                            "type": "input_text",
                            "text": "\n\n".join(
                                [
                                    "Your task is to convert the post into directly actionable visualization guidelines adhering to this template:",
                                    fence(GUIDELINE_TEMPLATE, lang="md"),
                                ]
                            ),
                        },
                        {
                            "type": "input_text",
                            "text": build_guideline_extraction_prompt(
                                evidence_scope=DATAWRAPPER_PROMPT_SPEC[
                                    "evidence_scope"
                                ],
                                required_basis=DATAWRAPPER_PROMPT_SPEC[
                                    "required_basis"
                                ],
                                cardinality_instruction=DATAWRAPPER_PROMPT_SPEC[
                                    "cardinality_instruction"
                                ],
                                source_specific_rules=DATAWRAPPER_PROMPT_SPEC[
                                    "source_specific_rules"
                                ],
                                required_citations=[f"[@{citekey}]"],
                                allow_empty=DATAWRAPPER_PROMPT_SPEC["allow_empty"],
                            ),
                        },
                    ],
                },
            ],
        )

        response_text = response.output_text
        guideline_objects = [
            parse_guideline(md_content) for md_content in unfence(response_text)
        ]
        guideline_objects = finalize_guideline_batch(
            guideline_objects,
            required_basis=DATAWRAPPER_PROMPT_SPEC["required_basis"],
        )
        references = [bibtex_entry]

        return [
            CatalogEntry(guideline=guideline_obj, references=references)
            for guideline_obj in guideline_objects
        ]

    return (datawrapper_post_pdf_to_catalog_entries,)


@app.cell(hide_code=True)
def _(prompt_contract_digest):
    DATAWRAPPER_PROMPT_SPEC = {
        "required_basis": "basis:heuristic",
        "allow_empty": True,
        "cardinality_instruction": (
            "Extract multiple guidelines if present. "
            "Output each in fenced ```md blocks separately, separated by blank lines."
        ),
        "evidence_scope": (
            "Strictly base each guideline on the evidence provided in this processed blog post and nothing else."
        ),
        "source_specific_rules": [
            "Extract reusable editorial heuristics rather than retelling the blog narrative.",
            (
                "Keep platform-specific advice only when it changes "
                "a concrete visualization decision, critique step, or revision move."
            ),
            (
                "When a rule is a reusable cross-grammar finishing move, emit an appropriate `polish:*` label."
            ),
            (
                "Do not upgrade a local example or platform-specific workflow into a broader best practice unless the post itself states that broader rule."
            ),
            (
                "Do not add off-source tooltip, caption, or annotation advice just because it sounds like common editorial practice."
            ),
        ],
    }
    DATAWRAPPER_PROMPT_DIGEST = prompt_contract_digest(
        DATAWRAPPER_PROMPT_SPEC,
        ["[@blog-post]"],
    )
    return DATAWRAPPER_PROMPT_DIGEST, DATAWRAPPER_PROMPT_SPEC


@app.cell(hide_code=True)
def _(DATAWRAPPER_REFS: list[str], parse_bibtex, pathlib):
    def _datawrapper_path_to_post_url(path: pathlib.Path) -> str:
        """
        Pathname: www_datawrapper_de_blog_10-ways-to-use-fewer-colors-in-your-data-visualizations.pdf
        Returns: https://www.datawrapper.de/blog/10-ways-to-use-fewer-colors-in-your-data-visualizations
        """
        return path.stem.replace(
            "www_datawrapper_de_",
            "https://www.datawrapper.de/",
        ).replace("_", "/")

    def find_datawrapper_bibtex_entry_by_path(path: pathlib.Path) -> str:
        url = _datawrapper_path_to_post_url(path)
        entries = parse_bibtex(DATAWRAPPER_REFS)
        entry = [entry for entry in entries if url in str(entry)]

        if not entry:
            raise ValueError(f"No bibtex entry found for URL: {url}")

        return entry[0]

    return (find_datawrapper_bibtex_entry_by_path,)


@app.cell(hide_code=True)
def _(ASSETS_ROOT):
    DATAWRAPPER_POST_PDF_PATHS = list(
        (ASSETS_ROOT / "datawrapper" / "posts").glob("*.pdf")
    )
    DATAWRAPPER_REFS: list[str] = (
        ASSETS_ROOT / "datawrapper" / "references.bib"
    ).read_text()
    return DATAWRAPPER_POST_PDF_PATHS, DATAWRAPPER_REFS


@app.cell(column=3, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:person-standing:: Source 3: Accessibility Standards

    Chartability provides 50 evaluation criteria for visualization accessibility. Unlike perception studies based on controlled experiments, these derive directly from inclusive design principles and WCAG standards. Extracting items from the [Chartability workbook](https://chartability.github.io/POUR-CAF/) demonstrates how the schema accommodates broad accessibility principles by translating them into targeted chart critique and remediation steps.

    **Reference:**
    > Elavsky, F., Bennett, C., & Moritz, D. (2022). How accessible is my visualization? Evaluating visualization accessibility with Chartability. *Computer Graphics Forum*, 41(3), 57–70.
    """)
    return


@app.cell(hide_code=True)
def _(
    CHARTABILITY_ITEMS,
    CHARTABILITY_PROMPT_DIGEST,
    Catalog,
    DEFAULT_CLIENT_CONFIG,
    chartability_item_to_catalog_entry,
    json,
    parallel_map,
    param_collapsed,
    string_hash,
):
    ch_tasks = [
        {
            "ch_item": ch_item,
            "model": DEFAULT_CLIENT_CONFIG["model"],
            "reasoning": DEFAULT_CLIENT_CONFIG["reasoning"],
        }
        for ch_item in CHARTABILITY_ITEMS
    ]
    ch_entries = parallel_map(
        fn=param_collapsed(chartability_item_to_catalog_entry),
        inputs=ch_tasks,
        n_jobs=16,
        desc="Processing Chartability items",
        cache_key_provider=lambda inp: "___".join(
            [
                string_hash(json.dumps(inp["ch_item"])),
                CHARTABILITY_PROMPT_DIGEST,
            ]
        ),
    )
    ch_entries = [entry for entry in ch_entries if entry is not None]
    ch_catalog = Catalog(ch_entries)
    ch_catalog.frame
    return (ch_catalog,)


@app.cell(hide_code=True)
def _(ch_catalog, display_references):
    display_references(ch_catalog)
    return


@app.cell(hide_code=True)
def _(
    CHARTABILITY_PAPER_BIBTEX,
    CHARTABILITY_PAPER_CITEKEY,
    CHARTABILITY_PAPER_ITEM,
    CHARTABILITY_PROMPT_SPEC,
    CatalogEntry,
    GUIDELINE_TEMPLATE,
    build_guideline_extraction_prompt,
    client,
    create_pdf_content_part,
    fence,
    finalize_guideline_batch,
    json,
    parse_guideline,
    unfence,
):
    def chartability_item_to_catalog_entry(
        ch_item: dict,
        model: str,
        reasoning: dict | None = None,
    ) -> CatalogEntry | None:
        response = client.responses.create(
            model=model,
            reasoning=reasoning,
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": f"Consider this paper [@{CHARTABILITY_PAPER_CITEKEY}] on visualzation accessibility guidelines:",
                        },
                        create_pdf_content_part(CHARTABILITY_PAPER_ITEM["pdf_bytes"]),
                        {
                            "type": "input_text",
                            "text": "\n\n".join(
                                [
                                    "Focus on this specific guideline extracted from the work:",
                                    fence(json.dumps(ch_item, indent=2), lang="json"),
                                ]
                            ),
                        },
                        {
                            "type": "input_text",
                            "text": "\n\n".join(
                                [
                                    "Your task is to convert this accessibility item into one directly actionable visualization guideline adhering to this template:",
                                    fence(GUIDELINE_TEMPLATE, lang="md"),
                                ]
                            ),
                        },
                        {
                            "type": "input_text",
                            "text": build_guideline_extraction_prompt(
                                evidence_scope=CHARTABILITY_PROMPT_SPEC[
                                    "evidence_scope"
                                ],
                                required_basis=CHARTABILITY_PROMPT_SPEC[
                                    "required_basis"
                                ],
                                cardinality_instruction=CHARTABILITY_PROMPT_SPEC[
                                    "cardinality_instruction"
                                ],
                                source_specific_rules=CHARTABILITY_PROMPT_SPEC[
                                    "source_specific_rules"
                                ],
                                required_citations=[f"[@{CHARTABILITY_PAPER_CITEKEY}]"],
                                allow_empty=CHARTABILITY_PROMPT_SPEC["allow_empty"],
                            ),
                        },
                    ],
                },
            ],
        )
        response_text = response.output_text
        if not response_text.strip():
            return None

        fenced_guidelines = unfence(response_text)
        if not fenced_guidelines:
            return None

        guideline_md = fenced_guidelines[0]
        guideline_batch = finalize_guideline_batch(
            [parse_guideline(guideline_md)],
            required_basis=CHARTABILITY_PROMPT_SPEC["required_basis"],
        )
        if not guideline_batch:
            return None
        guideline_obj = guideline_batch[0]
        references = [CHARTABILITY_PAPER_BIBTEX, *ch_item["references"]]

        return CatalogEntry(guideline=guideline_obj, references=references)

    return (chartability_item_to_catalog_entry,)


@app.cell(hide_code=True)
def _(prompt_contract_digest):
    CHARTABILITY_PROMPT_SPEC = {
        "required_basis": "basis:accessibility",
        "allow_empty": True,
        "cardinality_instruction": (
            "Return exactly one fenced ```md block if the item supports one "
            "directly actionable guideline. Otherwise, return an empty string."
        ),
        "evidence_scope": (
            "Strictly base the guideline on the structured accessibility knowledge provided here and nothing else. Do not add accessibility guidance that is not actually present in this processed material."
        ),
        "source_specific_rules": [
            "Translate the accessibility criterion into concrete design actions, reviewer checks, or remediation steps.",
            "Use the Chartability paper citation plus any directly relevant linked references from the provided item.",
            (
                "Emit `polish:*` only when the accessibility guidance also produces a visible decluttering, hierarchy, spacing, annotation, or palette improvement."
            ),
            (
                "Only include actions, checks, and fixes that are supported by the provided item or its linked references included here."
            ),
            (
                "Do not import extra WCAG or general accessibility best practices that are not actually present in the provided material."
            ),
            "If the item describes a principle without a concrete chart change, critique procedure, or rework step, omit it.",
        ],
    }
    CHARTABILITY_PROMPT_DIGEST = prompt_contract_digest(
        CHARTABILITY_PROMPT_SPEC,
        ["[@chartability-paper]"],
    )
    return CHARTABILITY_PROMPT_DIGEST, CHARTABILITY_PROMPT_SPEC


@app.cell(hide_code=True)
def _(
    ASSETS_ROOT,
    json,
    process_zot_item,
    zot,
    zot_item_bibtex,
    zot_item_bibtex_key,
):
    CHARTABILITY_ITEMS = json.loads(
        (ASSETS_ROOT / "chartability" / "items.json").read_text()
    )
    CHARTABILITY_PAPER_ZOTERO_KEY = "Q3NQHM8X"
    CHARTABILITY_PAPER_CITEKEY = zot_item_bibtex_key(CHARTABILITY_PAPER_ZOTERO_KEY)
    CHARTABILITY_PAPER_BIBTEX = zot_item_bibtex(CHARTABILITY_PAPER_ZOTERO_KEY)
    CHARTABILITY_PAPER_ITEM = process_zot_item(zot.item(CHARTABILITY_PAPER_ZOTERO_KEY))
    return (
        CHARTABILITY_ITEMS,
        CHARTABILITY_PAPER_BIBTEX,
        CHARTABILITY_PAPER_CITEKEY,
        CHARTABILITY_PAPER_ITEM,
    )


@app.cell(column=4, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:bar-chart-2:: Source 4: Collated Graphical Perception

    Zeng and Battle systematically collated findings from over 50 empirical studies, providing quantitative data that ranks visual encodings based on accuracy and response time. By feeding the model both the original paper PDFs and the pre-extracted JSON data, we test how the schema handles complex comparative rankings and performance metrics without hallucinating design advice beyond the experimental data.

    **Reference:**
    > Zeng, Z., & Battle, L. (2023). A review and collation of graphical perception knowledge for visualization recommendation. *Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems*, 1–16.
    """)
    return


@app.cell(hide_code=True)
def _(
    COLLATED_PROMPT_DIGEST,
    Catalog,
    DEFAULT_CLIENT_CONFIG,
    collated_item_to_catalog_entries,
    collated_perception_knowledge_items,
    itertools,
    parallel_map,
    param_collapsed,
):
    prc_tasks = [
        {
            "collated_item": collated_item,
            "model": DEFAULT_CLIENT_CONFIG["model"],
            "reasoning": DEFAULT_CLIENT_CONFIG["reasoning"],
        }
        for collated_item in collated_perception_knowledge_items
    ]
    prc_entry_lists = parallel_map(
        fn=param_collapsed(collated_item_to_catalog_entries),
        inputs=prc_tasks,
        n_jobs=16,
        desc="Processing collated perception knowledge items",
        cache_key_provider=lambda inp: "___".join(
            [
                inp["model"],
                inp["collated_item"]["data"]["DOI"],
                COLLATED_PROMPT_DIGEST,
            ]
        ),
    )
    prc_entries = list(itertools.chain.from_iterable(prc_entry_lists))
    prc_catalog = Catalog(prc_entries)
    prc_catalog.frame
    return (prc_catalog,)


@app.cell(hide_code=True)
def _(display_references, prc_catalog):
    display_references(prc_catalog)
    return


@app.cell(hide_code=True)
def _(
    COLLATED_PROMPT_SPEC,
    COLLATION_REVIEW_PAPER_BIBTEX,
    COLLATION_REVIEW_PAPER_CITEKEY,
    COLLATION_REVIEW_PAPER_ITEM,
    CatalogEntry,
    GUIDELINE_TEMPLATE,
    build_guideline_extraction_prompt,
    client,
    create_pdf_content_part,
    fence,
    finalize_guideline_batch,
    json,
    parse_guideline,
    unfence,
    zot_item_bibtex,
    zot_item_bibtex_key,
):
    def collated_item_to_catalog_entries(
        collated_item: dict,
        model: str,
        reasoning: dict | None = None,
    ) -> list[CatalogEntry]:
        collated_item_citekey = zot_item_bibtex_key(collated_item["data"]["key"])

        response = client.responses.create(
            model=model,
            reasoning=reasoning,
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": f"Consider this paper [@{COLLATION_REVIEW_PAPER_CITEKEY}] on graphical perception knowledge collation:",
                        },
                        create_pdf_content_part(
                            COLLATION_REVIEW_PAPER_ITEM["pdf_bytes"]
                        ),
                        {
                            "type": "input_text",
                            "text": f"One of the papers it collated knowledge from is this one [@{collated_item_citekey}] below:",
                        },
                        create_pdf_content_part(collated_item["pdf_bytes"]),
                        {
                            "type": "input_text",
                            "text": "\n".join(
                                [
                                    "This is the structured knowledge extracted from that paper:",
                                    fence(
                                        json.dumps(
                                            collated_item["knowledge_json"],
                                            indent=2,
                                        ),
                                        lang="json",
                                    ),
                                ]
                            ),
                        },
                        {
                            "type": "input_text",
                            "text": "\n".join(
                                [
                                    "Your task is to convert the structured graphical-perception knowledge into directly actionable visualization guidelines adhering to this template:",
                                    fence(GUIDELINE_TEMPLATE, lang="md"),
                                ]
                            ),
                        },
                        {
                            "type": "input_text",
                            "text": build_guideline_extraction_prompt(
                                evidence_scope=COLLATED_PROMPT_SPEC["evidence_scope"],
                                required_basis=COLLATED_PROMPT_SPEC["required_basis"],
                                cardinality_instruction=COLLATED_PROMPT_SPEC[
                                    "cardinality_instruction"
                                ],
                                source_specific_rules=COLLATED_PROMPT_SPEC[
                                    "source_specific_rules"
                                ],
                                required_citations=[
                                    f"[@{COLLATION_REVIEW_PAPER_CITEKEY}]",
                                    f"[@{collated_item_citekey}]",
                                ],
                                allow_empty=COLLATED_PROMPT_SPEC["allow_empty"],
                            ),
                        },
                    ],
                },
            ],
        )

        response_text = response.output_text

        guideline_objects = [
            parse_guideline(md_content) for md_content in unfence(response_text)
        ]
        guideline_objects = finalize_guideline_batch(
            guideline_objects,
            required_basis=COLLATED_PROMPT_SPEC["required_basis"],
        )

        references = [
            COLLATION_REVIEW_PAPER_BIBTEX,
            zot_item_bibtex(collated_item["data"]["key"]),
        ]
        return [
            CatalogEntry(guideline=guideline_obj, references=references)
            for guideline_obj in guideline_objects
        ]

    return (collated_item_to_catalog_entries,)


@app.cell(hide_code=True)
def _(prompt_contract_digest):
    COLLATED_PROMPT_SPEC = {
        "required_basis": "basis:empirical",
        "allow_empty": True,
        "cardinality_instruction": (
            "Extract multiple guidelines if present. "
            "Output each in fenced ```md blocks separately, separated by blank lines."
        ),
        "evidence_scope": (
            "Strictly base each guideline on the structured knowledge provided here. "
            "Use the PDFs only to disambiguate wording or evidence and nothing else. Do not add design guidance that is not actually supported by this processed evidence."
        ),
        "source_specific_rules": [
            "Treat the structured knowledge as the primary signal.",
            "Discard raw comparative findings unless they imply a concrete chart decision, critique check, or revision step.",
            (
                "Emit `polish:*` only when the evidence clearly supports a visible cross-grammar finishing move, not just a chart-family ranking."
            ),
            (
                "Do not infer broader design rules, applicability conditions, or fixes that the collated item and cited paper do not actually support."
            ),
            (
                "When the evidence compares named alternatives, express the smallest portable principle clearly supported by that comparison and keep named exemplars in supporting sections unless the name itself is the finding."
            ),
        ],
    }
    COLLATED_PROMPT_DIGEST = prompt_contract_digest(
        COLLATED_PROMPT_SPEC,
        ["[@collation-review]", "[@original-paper]"],
    )
    return COLLATED_PROMPT_DIGEST, COLLATED_PROMPT_SPEC


@app.cell(hide_code=True)
def _(
    find_item_by_doi,
    processed_zot_items,
    zot_item_bibtex,
    zot_item_bibtex_key,
):
    # A Review and Collation of Graphical Perception Knowledge for Visualization Recommendation (Zeng et al., 2023)
    COLLATION_REVIEW_PAPER_DOI = "10.1145/3544548.3581349"
    COLLATION_REVIEW_PAPER_ITEM = find_item_by_doi(
        processed_zot_items,
        COLLATION_REVIEW_PAPER_DOI,
    )
    COLLATION_REVIEW_PAPER_CITEKEY = zot_item_bibtex_key(
        COLLATION_REVIEW_PAPER_ITEM["data"]["key"]
    )
    COLLATION_REVIEW_PAPER_BIBTEX = zot_item_bibtex(
        COLLATION_REVIEW_PAPER_ITEM["data"]["key"]
    )
    return (
        COLLATION_REVIEW_PAPER_BIBTEX,
        COLLATION_REVIEW_PAPER_CITEKEY,
        COLLATION_REVIEW_PAPER_ITEM,
    )


@app.cell(hide_code=True)
def _(process_zot_item, zot_items):
    processed_zot_items = [process_zot_item(item) for item in zot_items]
    collated_perception_knowledge_items = [
        item for item in processed_zot_items if item["knowledge_json"] is not None
    ]
    return collated_perception_knowledge_items, processed_zot_items


@app.cell(hide_code=True)
def _(json, zot):
    def find_item_by_doi(all_items: list[dict], doi: str) -> dict:
        for item in all_items:
            if item["data"].get("DOI") == doi:
                return item

        raise ValueError(f"Item with DOI {doi} not found.")

    def find_knowledge_json(children: list[dict]) -> dict | None:
        for child in children:
            if (
                child["data"]["itemType"] == "attachment"
                and child["data"]["contentType"] == "application/json"
            ):
                key = child["data"]["key"]
                return json.loads(zot.file(key).decode("utf-8"))

        return None

    def find_pdf(children: list[dict]) -> bytes | None:
        for child in children:
            if (
                child["data"]["itemType"] == "attachment"
                and child["data"]["contentType"] == "application/pdf"
            ):
                key = child["data"]["key"]
                return zot.file(key)

        return None

    def process_zot_item(item: dict) -> dict:
        key = item["key"]
        data = item["data"]
        children: list[dict] = zot.children(key)
        pdf_bytes = find_pdf(children)
        knowledge_json = find_knowledge_json(children)

        return {
            "data": data,
            "knowledge_json": knowledge_json,
            "pdf_bytes": pdf_bytes,
        }

    def zot_item_bibtex(
        item_key: str, exclude_keys: list[str] = ["abstract", "file"]
    ) -> str:
        import bibtexparser

        bibtex_str = zot.item(item_key, format="bibtex").decode("utf-8")
        db = bibtexparser.loads(bibtex_str)

        for entry in db.entries:
            for exclude_key in set(exclude_keys):
                entry.pop(exclude_key, None)

        return bibtexparser.dumps(db)

    def zot_item_bibtex_key(item_key: str) -> str:
        import bibtexparser

        bibtex_str = zot.item(item_key, format="bibtex").decode("utf-8")
        db = bibtexparser.loads(bibtex_str)

        return db.entries[0]["ID"]

    return (
        find_item_by_doi,
        process_zot_item,
        zot_item_bibtex,
        zot_item_bibtex_key,
    )


@app.cell(hide_code=True)
def _(PERCEPTION_KNOWLEDGE_COLLECTION_ID, VISFEEDBACK_GROUP_ID, zotero):
    zot = zotero.Zotero(VISFEEDBACK_GROUP_ID, "group", local=True)
    zot_items = zot.collection_items(PERCEPTION_KNOWLEDGE_COLLECTION_ID)
    return zot, zot_items


@app.cell(hide_code=True)
def _():
    VISFEEDBACK_GROUP_ID = 6228570
    PERCEPTION_KNOWLEDGE_COLLECTION_ID = "FQ7DK82F"
    return PERCEPTION_KNOWLEDGE_COLLECTION_ID, VISFEEDBACK_GROUP_ID


@app.cell(hide_code=True)
def _():
    import itertools

    from pyzotero import zotero

    return itertools, zotero


@app.cell(column=5, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:message-square:: Source 5: Qualitative Rhetoric

    A chart is a communication tool subject to interpretation. The [Talking Charts project](https://talking-charts.vda.univie.ac.at) provides 32 findings on rhetoric, audience trust, and the gap between intended and received messages. Representing this pre-structured JSON data tests the schema's capacity to handle qualitative, socio-technical observations and structure them as explicit constraints for framing, titling, and annotation.

    **References:**
    > Gregory, K., Koesten, L., Schuster, R., Möller, T., & Davies, S. (2024). Data journeys in popular science. *Harvard Data Science Review*, 6(2).

    > Knoll, C., Möller, T., Gregory, K., & Koesten, L. (2025). The gulf of interpretation. *CHI 2025*, 1–17.

    > Koesten, L., Gregory, K., Schuster, R., Knoll, C., Davies, S., & Möller, T. (2023). What is the message?
    > arXiv:2304.10544.

    > Koesten, L., Saske, A., Starchenko, S. M., & Gregory, K. (2025). Encountering friction, understanding crises. *CHI 2025*, 1–15.

    > Schuster, R., Gregory, K., Möller, T., & Koesten, L. (2024). Being simple on complex issues. *IEEE TVCG*, 30(9), 6598–6611.
    """)
    return


@app.cell(hide_code=True)
def _(
    Catalog,
    DEFAULT_CLIENT_CONFIG,
    TALKING_CHARTS_PROMPT_DIGEST,
    json,
    parallel_map,
    param_collapsed,
    string_hash,
    tc_findings,
    tc_guideline_to_catalog_entry,
    tc_references,
):
    tc_tasks = [
        {
            "guideline_index": guideline_index,
            "guideline": guideline,
            "references": tc_references,
            "model": DEFAULT_CLIENT_CONFIG["model"],
            "reasoning": DEFAULT_CLIENT_CONFIG["reasoning"],
        }
        for guideline_index, guideline in enumerate(tc_findings["guidelines"], start=1)
    ]

    tc_results = parallel_map(
        fn=param_collapsed(tc_guideline_to_catalog_entry),
        inputs=tc_tasks,
        n_jobs=16,
        desc="Processing Talking Charts guidelines",
        cache_key_provider=lambda inp: "___".join(
            [
                "talking-charts-v3",
                string_hash(json.dumps(inp, sort_keys=True)),
                TALKING_CHARTS_PROMPT_DIGEST,
            ]
        ),
    )
    tc_failures = [failure for entry, failure in tc_results if failure is not None]
    if tc_failures:
        raise ValueError(
            "Talking Charts extraction failed for the following findings:\n- "
            + "\n- ".join(tc_failures)
        )

    tc_entries = [entry for entry, _ in tc_results if entry is not None]
    if len(tc_entries) != len(tc_tasks):
        raise ValueError(
            f"Talking Charts extraction produced {len(tc_entries)} entries for "
            f"{len(tc_tasks)} findings."
        )
    tc_catalog = Catalog(tc_entries)
    tc_catalog.frame
    return (tc_catalog,)


@app.cell(hide_code=True)
def _(display_references, tc_catalog):
    display_references(tc_catalog)
    return


@app.cell(hide_code=True)
def _(
    CatalogEntry,
    Guideline,
    TALKING_CHARTS_PROMPT_SPEC,
    build_tc_prompt,
    client,
    explain_guideline_rejection,
    fence,
    finalize_guideline_batch,
    list_ref_ids,
    list_tc_guideline_references,
    parse_bibtex,
    parse_guideline,
    pick_refs,
    unfence,
):
    def tc_guideline_to_catalog_entry(
        guideline_index: int,
        guideline: dict,
        references: list[str],
        model: str,
        reasoning: dict | None = None,
    ) -> tuple[CatalogEntry | None, str | None]:
        def preview_response(text: str, limit: int = 280) -> str:
            compact = " ".join(text.split())
            if len(compact) <= limit:
                return compact
            return compact[: limit - 3] + "..."

        def parse_single_guideline_response(
            response_text: str,
        ) -> tuple[Guideline | None, str | None]:
            if not response_text.strip():
                return None, "model returned empty output"

            fenced_guidelines = unfence(response_text)
            if len(fenced_guidelines) != 1:
                return (
                    None,
                    "expected exactly one fenced guideline block, "
                    f"got {len(fenced_guidelines)}",
                )

            try:
                parsed_guideline = parse_guideline(fenced_guidelines[0])
            except Exception as exc:  # noqa: BLE001
                return None, f"guideline markdown could not be parsed: {exc}"

            failure_reason = explain_guideline_rejection(
                parsed_guideline,
                required_basis=TALKING_CHARTS_PROMPT_SPEC["required_basis"],
            )
            if failure_reason is not None:
                return None, failure_reason

            guideline_batch = finalize_guideline_batch(
                [parsed_guideline],
                required_basis=TALKING_CHARTS_PROMPT_SPEC["required_basis"],
            )
            if not guideline_batch:
                return None, "guideline failed final deduplication"
            return guideline_batch[0], None

        def build_retry_prompt(
            *,
            base_prompt: str,
            response_text: str,
            failure_reason: str,
        ) -> str:
            previous_response = response_text.strip() or "<empty response>"
            return "\n\n".join(
                [
                    base_prompt,
                    "The previous response was invalid and must be repaired.",
                    f"Validation failure: {failure_reason}.",
                    (
                        "Do not omit or skip this Talking Charts finding. "
                        "Repair the same item into exactly one valid guideline."
                    ),
                    (
                        "Return only one fenced ```md block with valid frontmatter "
                        "and source-faithful context, exceptions, check, and fix sections."
                    ),
                    "Previous invalid response:",
                    fence(previous_response, lang="text"),
                ]
            )

        # Enumerate all the reference IDs available for Talking Charts
        allowed_ref_ids = list_ref_ids(references)
        required_ref_ids = sorted(
            list_tc_guideline_references(guideline, allowed_ref_ids)
        )

        # Map knowledge to our representation
        base_prompt = build_tc_prompt(guideline, required_ref_ids, allowed_ref_ids)
        prompt = base_prompt
        last_failure = "unknown failure"
        last_response_text = ""
        guideline_obj: Guideline | None = None

        for _ in range(3):
            response = client.responses.create(
                model=model,
                reasoning=reasoning,
                input=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )
            response_text = response.output_text
            candidate_guideline, failure_reason = parse_single_guideline_response(
                response_text
            )
            if candidate_guideline is not None:
                guideline_obj = candidate_guideline
                break

            last_failure = failure_reason or "unknown failure"
            last_response_text = response_text
            prompt = build_retry_prompt(
                base_prompt=base_prompt,
                response_text=response_text,
                failure_reason=last_failure,
            )

        if guideline_obj is None:
            failure = (
                f"#{guideline_index} {guideline['checklist_group']} / "
                f"{guideline['item']}: {last_failure}"
            )
            if last_response_text.strip():
                failure += " | response preview: " + preview_response(
                    last_response_text
                )
            return None, failure

        references: list[str] = parse_bibtex(
            pick_refs(
                required_ref_ids,
                references,
            )
        )

        return CatalogEntry(guideline=guideline_obj, references=references), None

    return (tc_guideline_to_catalog_entry,)


@app.cell(hide_code=True)
def _(prompt_contract_digest):
    TALKING_CHARTS_PROMPT_SPEC = {
        "required_basis": "basis:rhetorical",
        "allow_empty": False,
        "cardinality_instruction": (
            "Return exactly one fenced ```md block. Every Talking Charts finding in this dataset must be converted into one guideline; do not omit, merge, or skip any item. "
        ),
        "evidence_scope": (
            "Strictly base the guideline on the codified knowledge provided here and nothing else. Do not add rhetorical or framing advice that is not actually discussed in this processed finding."
        ),
        "source_specific_rules": [
            (
                "Every Talking Charts item in this curated set must become one guideline. "
                "If a finding is broad or evaluative, rewrite it as the narrowest source-faithful critique, framing, context, annotation, or workflow step rather than omitting it."
            ),
            (
                "Translate rhetorical or interpretive findings into concrete framing, "
                "annotation, titling, grouping, or revision guidance."
            ),
            (
                "Workflow, audience-testing, or review-process findings may become review or testing guidance when that is the actionable move directly supported by the evidence."
            ),
            (
                "When the finding is mainly about framing, context, credibility, resonance, or workflow, emit an appropriate `communication:*` label."
            ),
            (
                "When the finding is a cross-grammar finishing move that makes charts visibly clearer or stronger, emit an appropriate `polish:*` label."
            ),
            (
                "Keep source-specific caption, context, or credibility examples out of title and advice unless that specific example is the finding."
            ),
            "Ensure that you convert every single item to a dedicated guideline with no exception. For 32 items I need 32 output guidelines!!!",
        ],
    }
    TALKING_CHARTS_PROMPT_DIGEST = prompt_contract_digest(
        TALKING_CHARTS_PROMPT_SPEC,
        ["[@linked-study]"],
    )
    return TALKING_CHARTS_PROMPT_DIGEST, TALKING_CHARTS_PROMPT_SPEC


@app.cell(hide_code=True)
def _(
    GUIDELINE_TEMPLATE,
    TALKING_CHARTS_PROMPT_SPEC,
    build_guideline_extraction_prompt,
    fence,
    prepare_guideline,
):
    def build_tc_prompt(
        guideline: dict,
        required_ref_ids: list[str],
        allowed_ref_ids: list[str],
    ) -> str:
        prepared_guideline = prepare_guideline(guideline, allowed_ref_ids)
        required_citations = [f"[@{ref_id}]" for ref_id in required_ref_ids]

        return rf"""Peruse this codified piece of knowledge:

    {fence(prepared_guideline, lang="json")}

    Your task is to convert it into one directly actionable visualization guideline in this representation:

    {fence(GUIDELINE_TEMPLATE, lang="md")}

    {
            build_guideline_extraction_prompt(
                required_basis=TALKING_CHARTS_PROMPT_SPEC["required_basis"],
                evidence_scope=TALKING_CHARTS_PROMPT_SPEC["evidence_scope"],
                cardinality_instruction=TALKING_CHARTS_PROMPT_SPEC[
                    "cardinality_instruction"
                ],
                source_specific_rules=TALKING_CHARTS_PROMPT_SPEC[
                    "source_specific_rules"
                ],
                required_citations=required_citations,
                allow_empty=TALKING_CHARTS_PROMPT_SPEC["allow_empty"],
            )
        }

    In the YAML frontmatter always add bibliography: `references.bib`.

    Respond only with the final converted guideline in markdown format, fenced, starting with "```md" and ending with "```".
    """

    return (build_tc_prompt,)


@app.cell(hide_code=True)
def _(json):
    def list_tc_guideline_references(
        guideline: dict,
        allowed_ref_ids: set[str],
    ) -> set[str]:
        """Extracts the reference IDs used in a particular Talking Charts guideline."""
        return {
            item["study_id"]
            for item in guideline["evidence"]
            if item["study_id"] in allowed_ref_ids
        }

    def prepare_guideline(guideline: dict, allowed_ref_ids: set[str]) -> str:
        # Make sure we only use refs from our Talking Charts-specific references.bib file
        evidence: list[dict] = [
            item
            for item in guideline["evidence"]
            if item["study_id"] in allowed_ref_ids
        ]
        prepared_guideline = guideline | {"evidence": evidence}
        return json.dumps(prepared_guideline, indent=2)

    return list_tc_guideline_references, prepare_guideline


@app.cell(hide_code=True)
def _():
    import bibtexparser

    def list_ref_ids(refs: str) -> set[str]:
        """Given a bibtex string with multiple items, return the set of their IDs."""
        db = bibtexparser.loads(refs)
        return set(db.entries_dict.keys())

    def pick_refs(ids: list[str], from_all_refs: str) -> str:
        """Given a list of ids and a bibtex string with multiple items, return a bibtex string with only the picked items."""
        db = bibtexparser.loads(from_all_refs)
        picked_entries = [
            entry for id, entry in db.entries_dict.items() if id in set(ids)
        ]
        db.entries = picked_entries

        return bibtexparser.dumps(db)

    return bibtexparser, list_ref_ids, pick_refs


@app.cell(hide_code=True)
def _(ASSETS_ROOT, json):
    tc_findings = json.loads(
        (ASSETS_ROOT / "talking-charts" / "findings.json").read_text()
    )
    tc_references = (ASSETS_ROOT / "talking-charts" / "references.bib").read_text()
    return tc_findings, tc_references


@app.cell(column=6, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:database:: Catalog Compilation

    This notebook synthesizes 781 guidelines drawn from these five domains. By mapping psychology papers, editorial blogs, accessibility standards, perception metrics, and qualitative rhetoric into the exact same structural template, we validate the flexibility of the cataloging scheme.

    The resulting unified dataset of structured visualization design knowledge supports our downstream analyses, including structural analysis and automated chart feedback.
    """)
    return


@app.cell(hide_code=True)
def _(
    REPO_ROOT,
    ch_catalog,
    dw_catalog,
    misc_catalog,
    prc_catalog,
    tc_catalog,
):
    catalog = tc_catalog + prc_catalog + ch_catalog + dw_catalog + misc_catalog
    catalog_df = catalog.frame
    catalog_df.write_parquet(REPO_ROOT / "guidelines" / "catalog.parquet")
    # catalog.write_folder(REPO_ROOT / "guidelines")
    catalog_df
    return (catalog,)


@app.cell(column=7, hide_code=True)
def _(mo):
    mo.md(r"""
    ## ::lucide:book-open:: Guideline Example

    Every extracted guideline is a structured document, combining YAML metadata with discrete Markdown sections (such as context, exceptions, and fix).

    This structure enables programmatic access. The example rendered below is generated dynamically by interacting with a strongly typed Python object. Rather than parsing raw text, we use a typed API to query specific elements—pulling the title, metadata, and individual sections directly from the object to format them in this notebook.

    In fact, the body of the guideline below is rendered in markdown using Python expression below, iterating over all the role-typed guideline sections and accessing the `role`, `title` and `content` properties:

    ```python
    {
        "\n".join(
            [
                "\n".join(
                    [
                        f"> role:{section.role}\n\n",
                        f"### {section.title}",
                        section.content,
                    ]
                )
                for section in example_guideline_entry.guideline.sections
            ]
        )
    }
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    """)
    return


@app.cell
def _(example_guideline_entry):
    example_guideline_entry.guideline.sections[0]
    return


@app.cell
def _(catalog):
    example_guideline_entry = catalog.entries[0]
    return (example_guideline_entry,)


@app.cell(hide_code=True)
def _(example_guideline_entry, mo):
    mo.md(rf"""
    ## {example_guideline_entry.guideline.title}
    """)
    return


@app.cell(hide_code=True)
def _(example_guideline_entry, fence, mo):
    mo.md(rf"""
    {fence(example_guideline_entry.guideline.to_markdown().split("---")[1].strip(), lang="yaml")}
    """)
    return


@app.cell(hide_code=True)
def _(example_guideline_entry, mo):
    mo.md(rf"""
    {
        "\n".join(
            [
                "\n".join(
                    [
                        f"> role:{section.role}\n\n",
                        f"### {section.title}",
                        section.content,
                    ]
                )
                for section in example_guideline_entry.guideline.sections
            ]
        )
    }
    """)
    return


@app.cell(column=8, hide_code=True)
def _(mo):
    mo.md(r"""
    # ::lucide:bot:: Guideline Extraction Prompts
    """)
    return


@app.cell(hide_code=True)
def _(GUIDELINE_TEMPLATE, fence, mo):
    mo.md(rf"""
    ### Guideline Template

    {fence(GUIDELINE_TEMPLATE, lang="md")}
    """)
    return


@app.cell(hide_code=True)
def _(extraction_prompt_md, fence, mo):
    mo.md(rf"""
    ### Extraction Prompt

    {fence(extraction_prompt_md, lang="md")}
    """)
    return


@app.cell(hide_code=True)
def _(build_guideline_extraction_prompt):
    extraction_prompt_md = build_guideline_extraction_prompt(
        required_basis="{required basis label to track the source of evidence, e.g. basis:empirical or basis:rhetorical}",
        evidence_scope="{instruction on how to cite evidence from the source}",
        cardinality_instruction="{instruction on whether an ingested item should map from a single or potentially many guidelines}",
        source_specific_rules=["{rule1}", "{rule2}"],
        required_citations=["{@citekey1}", "{@citekey2}"],
    )
    return (extraction_prompt_md,)


@app.cell(column=9, hide_code=True)
def _(mo, pathlib, string_hash):
    NB_ROOT = mo.notebook_dir()
    REPO_ROOT = NB_ROOT.parent.parent.parent
    ASSETS_ROOT = NB_ROOT / "assets"
    GUIDELINE_TEMPLATE_PATH = REPO_ROOT / pathlib.Path(
        "guidelines/__templates__/default/GUIDELINE.md"
    )
    GUIDELINE_TEMPLATE = GUIDELINE_TEMPLATE_PATH.read_text()
    GUIDELINE_TEMPLATE_DIGEST = string_hash(GUIDELINE_TEMPLATE)
    DEFAULT_CLIENT_CONFIG = {
        "model": "gpt-5.4",
        "reasoning": {"effort": "high"},
    }
    return (
        ASSETS_ROOT,
        DEFAULT_CLIENT_CONFIG,
        GUIDELINE_TEMPLATE,
        GUIDELINE_TEMPLATE_DIGEST,
        REPO_ROOT,
    )


@app.cell(hide_code=True)
def _(GUIDELINE_TEMPLATE_DIGEST, string_hash):
    PURPOSE_LABELS = [
        "purpose:select",
        "purpose:refine",
    ]
    BASIS_LABELS = [
        "basis:empirical",
        "basis:heuristic",
        "basis:accessibility",
        "basis:rhetorical",
    ]

    def build_guideline_extraction_prompt(
        *,
        required_basis: str,
        evidence_scope: str,
        cardinality_instruction: str,
        source_specific_rules: list[str],
        required_citations: list[str],
        allow_empty: bool = True,
    ) -> str:
        lines = [
            "Your primary task is to extract and structure directly actionable visualization guidelines.",
            # CONTRACT 1: PURPOSE
            "First, classify each guideline by its primary `purpose`:",
            "- `purpose:select`: Guidance for CHOOSING BETWEEN chart families or structural arrangements (the WHAT of design). Example: 'Replace a pie chart with a bar chart for comparison.'",
            "- `purpose:refine`: Guidance for IMPROVING the implementation, polish, readability, annotation, accessibility, rhetoric, or encoding of an ALREADY-CHOSEN chart or structure (the HOW of design). Example: 'Sort the bars of a bar chart in descending order.'",
            "- If the intervention changes channel, component, palette, annotation, caption, accessibility treatment, or framing inside an already-chosen chart or layout, it is `purpose:refine`, not `purpose:select`.",
            f"Every emitted guideline MUST include exactly one purpose label from: {', '.join(PURPOSE_LABELS)}.",
            f"Every emitted guideline MUST include exactly one basis label and it MUST be `{required_basis}`. Allowed basis labels are: {', '.join(BASIS_LABELS)}.",
            # CONTRACT 2: DIRECTIONAL LABELS (POLARITY)
            "\nSecond, assign directional polarity to labels using a tripartite 'category:value:polarity' format:",
            "- Use ':use' if the guideline explicitly RECOMMENDS or PROMOTES a choice. Example: 'chart:bar:use'.",
            "- Use ':avoid' if the guideline explicitly WARNS AGAINST or DISCOURAGES a choice. Example: 'chart:pie-donut:avoid'.",
            "- Use NO polarity (Neutral) if the label represents a CONTEXTUAL CONDITION. Example: 'task:compare' means 'this guideline applies when the user wants to compare'.",
            "Guidelines with 'purpose:select' MUST include both a ':use' label and an ':avoid' label in the SAME decision family (`chart` or `structure`).",
            "\nThird, keep labels sparse and high-signal:",
            "- Treat labels as a retrieval index, not as an exhaustive summary of the guideline.",
            "- Use only the taxonomy declared in the template. Do NOT invent new categories or emit `custom:*` labels. If no allowed label fits cleanly, omit the label.",
            "- Most guidelines should have 4-8 labels total. Include more only when each extra label materially changes retrieval; rarely exceed 10.",
            "- By default, emit at most one label per category. Add multiple labels in one category only when the guideline explicitly contrasts alternatives or inseparably spans several conditions.",
            "- Add contextual labels (`task`, `scope`, `time`, `chart`, `structure`, `data`, `audience`, `literacy`, `needs`, `access`) only when the advice truly depends on that condition. Do not enumerate all plausible charts, data types, audiences, or workflows.",
            "- Prefer the most discriminative design-lever label. If the rule is mainly about a component, channel, quality, or accessibility treatment, label that directly instead of attaching many broad chart-type labels.",
            "- Avoid weak default labels such as `audience:general-public`, `literacy:general`, `structure:single-view`, `time:non-temporal`, or `data:quantitative` unless that applicability is explicit and materially important.",
            "- Bad label behavior: turning one broad accessibility rule into a long list of every plausible task, chart, time mode, data type, and audience.",
            "- Good label behavior: keep only the smallest label set that captures the recommendation, its main design lever, and the one or two conditions that materially narrow where it applies.",
            "- Emit the new generic families (`lever`, `operator`, `reading-mode`, `density`, `measure`, `group-cardinality`, `shape`, `temporal-pattern`, `communication`, `polish`) only when the source makes them explicit enough to drive retrieval. If unsure, omit.",
            "- `communication` is only for framing, context, credibility, resonance, or workflow guidance. `polish` is only for cross-grammar finishing moves that visibly improve charts.",
            "\nFourth, be strictly source-faithful:",
            "- Every claim, trigger condition, boundary condition, label, audience, check, fix, and example MUST be explicitly discussed in the processed source or be a direct minimal operational rewrite of it.",
            "- Include only what is actually discussed or clearly evidenced in the processed source. Never fill gaps from general datavis knowledge, common best practices, or likely defaults.",
            "- If the source supports a broader portable principle, express that principle in the title and description, then make the advice operational with concrete source-faithful instances. Keep named exemplars, tools, palettes, devices, platforms, or domains out of title and description unless the source explicitly makes them the finding.",
            "- When you include concrete instances in advice, abstract them away from the exact source scenario. Replace source-specific domain nouns, row labels, one-off measures, and literal question text with the portable design role they illustrate unless that specificity is itself the finding.",
            "- Do not over-specify a portable principle into a narrow named recommendation unless that narrow named form is itself the important finding in the source.",
            "- Do not add generic provenance, tooltip, caption, annotation, or accessibility advice unless the processed source makes that intervention causal to the guidance.",
            "- If a candidate, label, exception, audience, or fix is only plausible, partial, or guessed, omit it.",
        ]

        if allow_empty:
            lines.append(
                "If the source material cannot be translated into directly actionable visualization guidance without guessing or filling gaps, respond with an empty string."
            )

        lines.extend(
            [
                cardinality_instruction,
                evidence_scope,
                "Faithfulness outranks coverage. It is better to skip a possible guideline than to hallucinate, broaden, or pollute one.",
                "Use only evidence from the processed source material in this prompt. Do not import facts from neighboring studies, general datavis knowledge, or your prior beliefs.",
                "Each emitted guideline is well-defined, isolated, and granular.",
                "Each emitted guideline advocates one well-defined principle or one bounded contrast. Do not mix multiple acceptable alternatives into the same guideline.",
                "A valid guideline changes a concrete chart decision, critique step, or revision step that a practitioner can apply without rereading the source.",
                "Reject candidates that only summarize theory, taxonomy, historical context, methodology, study setup, or narrative commentary.",
                "Reject candidates that are visualization-relevant but do not tell the practitioner what to choose, inspect, test, or change in a chart.",
                "Operationalize descriptive findings in the form 'When [condition], do [change] to achieve [goal].' If that rewrite is not supported by the source, omit the candidate.",
                "If X is appropriate in one condition and Y is appropriate in another, emit separate guidelines with separate contexts rather than one 'use X or Y' guideline.",
                "Do not hedge with unresolved `or` choices between alternative chart types, components, or actions. Use `or` only when the alternatives are inseparable steps of one action or a literal source phrase that still resolves to one concrete recommendation.",
                "Do not invent task, scope, time, chart, structure, data, audience, access, or literacy conditions that the source does not actually support.",
                "Prefer omission to broad but plausible guidance. If the candidate lacks a clear trigger condition, clear break condition, or clear reviewer check, omit it.",
                "If two candidates overlap, keep only the narrower and more condition-bounded one.",
                # CONTRACT 4: DESCRIPTION
                "",
                "The `description` MUST follow this semantic contract: "
                "'For [task/scope/time context], [use|prefer|avoid] [design lever] on [chart/structure/data context] "
                "to [improve|maximize|prevent] [quality target or risk] and [mitigate|address] [common mistakes] "
                "for [audience/literacy/situational context].'",
                "Ensure the choice of verbs in the description (e.g., use vs avoid) exactly matches the directional polarity of the labels.",
                "The title is a specific imperative action on a concrete design lever stated at the portable-principle level. Do not put a named tool, palette, device, or source-specific exemplar in the title unless it is itself the finding.",
                "Keep `title` and `description` retrieval-stable and principle-level. Do not force concrete examples into those fields when the source supports a broader portable rule.",
                "The `advice` section heading must be short, portable, and design-lever focused. It should name the action or manipulated object, not the exact source scenario, domain entity, row label, or literal question text.",
                "The `advice` section is the operational surface for downstream generation. Start with the portable principle, then immediately ground it in 1-3 concrete source-faithful instances stated inline.",
                "Concrete instances in `advice` MUST name explicit chart families, components, labels, annotations, layout changes, encodings, or other design actions when the source supports them.",
                "Concrete instances in `advice` MUST stay portable. Name the design role, comparison, summary field, annotation, or structural move, not the exact source scenario or quoted question unless the source makes that specificity the real finding.",
                "Do not leave `advice` at broad adjectives such as familiar, basic, clear, readable, simple, or appropriate without naming the manipulated design lever and at least one concrete supported action or contrast.",
                "For `purpose:select`, the `advice` section MUST name at least one supported recommended option and one supported discouraged option when the evidence supports a bounded contrast.",
                "For `purpose:select`, keep the guideline to one recommended option versus one alternative in a single bounded contrast. Do not bundle several acceptable options into the same guideline.",
                "For `purpose:refine`, the `advice` section MUST name the manipulated object directly, such as the axis, legend, label, annotation, title, caption, baseline, order, palette, mark size, or spacing.",
                "The `context` section must read like 'Use when (all true)' and include at least two observable constraints taken from the source-supported condition space.",
                "The `exceptions` section must read like 'Do not use when (any true)' and explicitly mirror the context condition space. If the source does not support a real boundary condition, omit the guideline rather than inventing one.",
                "The `check` section contains an observable failure sign and a concrete review procedure that a reviewer can run.",
                "For `purpose:select`, the `check` section must include a direct A/B style decision test between the chosen and rejected options.",
                "The `fix` section consists of concrete edit operations, not abstract restatements of the advice. Do not add generic cleanup steps that are not supported by the source.",
                "Bad candidate: 'Color affects interpretation.' Good candidate: 'Use a colorblind-safe sequential palette when color encodes magnitude and hue identity is not the message.'",
                "Bad advice: 'Choose a familiar basic chart type when the chart's job is to help lay viewers compare values.' Good advice: 'Choose a familiar chart family for simple comparisons. For example, use a bar chart for one-dimensional category comparison instead of a bubble chart or other unfamiliar artful form when the source supports that contrast.'",
                "Bad advice: 'Make the chart clearer.' Good advice: 'Label each visible axis with what it measures. For example, add explicit x/y labels and disclose any axis truncation directly on the chart when the source supports that repair.'",
                "Bad advice: 'Add a summary column that states the table's main comparison. For example, add a total-games column so each city row directly answers \"which hosted the most games\" instead of making readers infer it from stage-by-stage date cells.' Good advice: 'Add a summary column that states the table's main comparison. For example, add a total or answer column so each row directly answers the main comparison instead of forcing readers to infer it from multiple detail columns.'",
                "Bad advice heading: 'Add a summary column for the row-level answer about hosted games.' Good advice heading: 'Add a summary column for the main comparison.'",
                "Bad guideline: 'Use X or Y for this task.' Good pattern: emit separate guidelines such as 'Use X when ...' and 'Use Y when ...', each with its own context and boundary conditions.",
                *source_specific_rules,
                "Place all citekeys only in the `reason` section under `**Evidence:**`.",
                "Never place citekeys in advice, context, exceptions, costs, mistakes, check, or fix.",
                "Do not repeat the same citekey within a section. If one source supports multiple points, synthesize them into one evidence span and cite it once.",
                "Use only the exact citekey format [@citekey]. Do not add anything else inside the brackets.",
            ]
        )

        if required_citations:
            if len(required_citations) == 1:
                lines.append(
                    f"Required citation for every emitted guideline: {required_citations[0]}."
                )
            else:
                lines.append(
                    "Required citations for every emitted guideline: "
                    + ", ".join(required_citations[:-1])
                    + f", and {required_citations[-1]}."
                )

        lines.append(
            "Never include the meta comments in the final output from the guideline template, only the section role annotations."
        )
        return "\n".join(lines)

    def prompt_contract_digest(spec: dict, required_citations: list[str]) -> str:
        return string_hash(
            "\n\n".join(
                [
                    GUIDELINE_TEMPLATE_DIGEST,
                    build_guideline_extraction_prompt(
                        required_basis=spec["required_basis"],
                        evidence_scope=spec["evidence_scope"],
                        cardinality_instruction=spec["cardinality_instruction"],
                        source_specific_rules=spec["source_specific_rules"],
                        required_citations=required_citations,
                        allow_empty=spec["allow_empty"],
                    ),
                ]
            )
        )

    return build_guideline_extraction_prompt, prompt_contract_digest


@app.cell(hide_code=True)
def _(Guideline):
    def _dedupe_labels(labels: list[str]) -> list[str]:
        return list(dict.fromkeys(labels))

    def _with_required_basis(guideline: Guideline, required_basis: str) -> Guideline:
        labels = [label for label in guideline.labels if not label.startswith("basis:")]
        labels.insert(
            1 if labels and labels[0].startswith("purpose:") else 0, required_basis
        )
        return guideline.model_copy(update={"labels": _dedupe_labels(labels)})

    def _has_self_conflict(labels: list[str]) -> bool:
        states: dict[str, set[str]] = {}
        for label in labels:
            parts = label.split(":")
            if len(parts) == 3 and parts[-1] in {"use", "avoid"}:
                key = ":".join(parts[:-1])
                states.setdefault(key, set()).add(parts[-1])
        return any(polarities == {"use", "avoid"} for polarities in states.values())

    def _same_family_select_contrast(labels: list[str]) -> bool:
        decision_categories = {"chart", "structure"}
        decisions: dict[str, set[str]] = {}
        for label in labels:
            parts = label.split(":")
            if len(parts) != 3 or parts[-1] not in {"use", "avoid"}:
                continue
            if parts[0] not in decision_categories:
                continue
            decisions.setdefault(parts[0], set()).add(parts[-1])
        return any(polarities == {"use", "avoid"} for polarities in decisions.values())

    def _section_map(guideline: Guideline) -> dict[str, str]:
        return {
            section.role: section.content.strip()
            for section in guideline.sections
            if section.role != "__dangling__"
        }

    def explain_guideline_rejection(
        guideline: Guideline,
        *,
        required_basis: str,
    ) -> str | None:
        guideline = _with_required_basis(guideline, required_basis)
        labels = guideline.labels

        purpose_labels = [label for label in labels if label.startswith("purpose:")]
        if len(purpose_labels) != 1:
            return f"expected exactly one purpose label, got {purpose_labels or 'none'}"

        basis_labels = [label for label in labels if label.startswith("basis:")]
        if basis_labels != [required_basis]:
            return (
                f"expected basis label {required_basis}, got {basis_labels or 'none'}"
            )

        if _has_self_conflict(labels):
            return "guideline contains conflicting use and avoid labels for the same choice"

        sections = _section_map(guideline)
        required_roles = {"context", "exceptions", "check"}
        for role in sorted(required_roles):
            if len(sections.get(role, "")) < 24:
                return f"section '{role}' is missing or too short"

        if purpose_labels[0] == "purpose:select" and not _same_family_select_contrast(
            labels
        ):
            return (
                "purpose:select guidelines must contrast a same-family "
                "use label and avoid label"
            )

        return None

    def _validate_guideline(
        guideline: Guideline,
        *,
        required_basis: str,
    ) -> Guideline | None:
        guideline = _with_required_basis(guideline, required_basis)
        if (
            explain_guideline_rejection(
                guideline,
                required_basis=required_basis,
            )
            is not None
        ):
            return None

        return guideline

    def finalize_guideline_batch(
        guideline_objects: list[Guideline],
        *,
        required_basis: str,
    ) -> list[Guideline]:
        validated = [
            validated_guideline
            for guideline_obj in guideline_objects
            if (
                validated_guideline := _validate_guideline(
                    guideline_obj,
                    required_basis=required_basis,
                )
            )
            is not None
        ]
        seen: set[tuple[str, str, tuple[str, ...]]] = set()
        unique_guidelines: list[Guideline] = []
        for guideline in validated:
            signature = (
                guideline.title.strip().lower(),
                guideline.description.strip().lower(),
                tuple(guideline.labels),
            )
            if signature in seen:
                continue
            seen.add(signature)
            unique_guidelines.append(guideline)
        return unique_guidelines

    return explain_guideline_rejection, finalize_guideline_batch


@app.cell(hide_code=True)
def _(Catalog, fence, mo):
    def display_references(catalog: Catalog):
        refs: list[str] = (
            catalog.frame.select("references")
            .explode("references")
            .unique()
            .sort("references")
            .drop_nulls()
            .get_column("references")
            .to_list()
        )

        return mo.md(
            "\n".join(
                [
                    "### Ingested Literature",
                    "",
                    fence("\n\n".join(refs), lang="bibtex"),
                ]
            )
        )

    return (display_references,)


@app.cell(hide_code=True)
def _():
    import hashlib
    import re

    def fence(text: str, lang: str = "json") -> str:
        return f"```{lang}\n{text}\n```"

    def unfence(text: str) -> list[str]:
        pattern = r"```(?:\w+)?\n(.*?)\n```"
        return [match.strip() for match in re.findall(pattern, text, re.DOTALL)]

    def string_hash(text: str) -> str:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    return fence, string_hash, unfence


@app.cell(hide_code=True)
def _(json):
    from collections.abc import Callable, Iterable, Mapping
    from typing import Any, TypeVar

    import diskcache
    from joblib import Parallel, delayed
    from tenacity import retry, stop_after_attempt, wait_fixed
    from tqdm.auto import tqdm

    T = TypeVar("T")
    R = TypeVar("R")

    def parallel_map(
        fn: Callable[[T], R],
        inputs: Iterable[T],
        *,
        n_jobs: int = -1,
        backend: str = "threading",
        desc: str | None = None,
        cache_dir: str | None = ".cache",
        cache_key_provider: Callable[[T], str] | None = None,
    ) -> list[R]:
        inputs_list = list(inputs)
        cache = diskcache.Cache(cache_dir) if cache_dir else None

        with tqdm(total=len(inputs_list), desc=desc) as pbar:

            @retry(wait=wait_fixed(1), stop=stop_after_attempt(3), reraise=True)
            def _wrapper(inp: T) -> R:
                cache_key: str | None = None
                if cache is not None:
                    cache_key = (
                        json.dumps(inp, sort_keys=True, default=str)
                        if cache_key_provider is None
                        else cache_key_provider(inp)
                    )
                    cached = cache.get(cache_key)
                    if cached is not None:
                        pbar.update(1)
                        return cached

                result = fn(inp)

                if cache is not None and cache_key is not None:
                    cache.set(cache_key, result)

                pbar.update(1)
                return result

            return list(
                Parallel(n_jobs=n_jobs, backend=backend, return_as="generator")(
                    delayed(_wrapper)(inp) for inp in inputs_list
                )
            )

    def param_collapsed(fn: Callable[..., R]) -> Callable[[Mapping[str, Any]], R]:
        def wrapped(item: Mapping[str, Any]) -> R:
            return fn(**item)

        return wrapped

    return parallel_map, param_collapsed


@app.cell(hide_code=True)
def _():
    import base64
    import time

    def create_pdf_content_part(pdf_bytes: bytes) -> dict[str, str]:
        encoded_file = base64.b64encode(pdf_bytes).decode("utf-8")
        base64_url = f"data:application/pdf;base64,{encoded_file}"
        filename = f"document-{int(time.time())}.pdf"

        return {
            "type": "input_file",
            "filename": filename,
            "file_data": base64_url,
        }

    return (create_pdf_content_part,)


@app.cell(hide_code=True)
def _():
    import openai

    client = openai.Client()
    return (client,)


@app.cell(hide_code=True)
def _():
    import json
    import pathlib
    import marimo as mo
    from chartcoach import Catalog, CatalogEntry, Guideline
    from chartcoach.guideline import parse_bibtex, parse_guideline

    return (
        Catalog,
        CatalogEntry,
        Guideline,
        json,
        mo,
        parse_bibtex,
        parse_guideline,
        pathlib,
    )


if __name__ == "__main__":
    app.run()
