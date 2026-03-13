import marimo

__generated_with = "0.20.4"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Catalog Construction

    This notebook documents the extraction of 744 guidelines from five source categories. Each source differs in methodology and evidence type; the cataloging scheme accommodates all of them within a uniform structure.

    The resulting catalog supports the analyses in the paper: expressiveness validation, structural analysis, and grounded feedback.
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
    catalog_df = catalog.df
    catalog_df.write_parquet(REPO_ROOT / "guidelines" / "catalog.parquet")
    # catalog.write_folders(REPO_ROOT / "guidelines")
    catalog_df
    return


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Source 1: Cognitive Science and Perception Papers

    We processed 103 papers cited in Franconeri et al.'s review *"The Science of Visual Data Communication"*. These papers report findings on low-level visual processing (saliency, ensemble coding, color discrimination), higher-order cognition (bias, memory, narrative framing), and applied domains (risk communication, uncertainty visualization).

    Each paper was provided to the extraction model as a PDF. The model identified actionable design implications and mapped them to the guideline schema.

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
    misc_catalog.df
    return (misc_catalog,)


@app.cell(hide_code=True)
def _(
    CatalogEntry,
    GUIDELINE_TEMPLATE,
    MISC_PROMPT_SPEC,
    build_guideline_extraction_prompt,
    ccp,
    client,
    create_pdf_content_part,
    fence,
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
            ccp.parse_guideline(md_content) for md_content in unfence(response_text)
        ]
        references = [item_bibtex]

        return [
            CatalogEntry(guideline=guideline_obj, references=references)
            for guideline_obj in guideline_objects
        ]

    return (misc_paper_to_catalog_entries,)


@app.cell(hide_code=True)
def _(prompt_contract_digest):
    MISC_PROMPT_SPEC = {
        "allow_empty": True,
        "cardinality_instruction": (
            "Extract multiple guidelines if present. "
            "Output each in fenced ```md blocks separately, separated by blank lines."
        ),
        "evidence_scope": "Strictly base each guideline on the evidence provided in the paper and nothing else.",
        "source_specific_rules": [
            (
                "Extract only findings whose design implication is clear enough "
                "to support a concrete chart choice, critique check, or revision step."
            ),
            (
                "Omit empirical observations that are interesting but "
                "do not tell the practitioner what to choose, inspect, test, or change in a visualization."
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
    ## Source 2: Practitioner Heuristics (Datawrapper)

    Datawrapper's ["Dos and Don'ts" blog series](https://www.datawrapper.de/blog/category/datavis-dos-and-donts) contains 36 posts written by data journalists. These posts address practical concerns: when to use annotations, how to handle axis truncation, and how to balance aesthetics with clarity.

    We saved each post as a PDF and processed it through the extraction pipeline. The resulting guidelines capture editorial heuristics that rarely appear in formal systems.
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
    dw_catalog.df
    return (dw_catalog,)


@app.cell(hide_code=True)
def _(
    CatalogEntry,
    DATAWRAPPER_PROMPT_SPEC,
    GUIDELINE_TEMPLATE,
    bibtexparser,
    build_guideline_extraction_prompt,
    ccp,
    client,
    create_pdf_content_part,
    fence,
    find_datawrapper_bibtex_entry_by_path,
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
            ccp.parse_guideline(md_content) for md_content in unfence(response_text)
        ]
        references = [bibtex_entry]

        return [
            CatalogEntry(guideline=guideline_obj, references=references)
            for guideline_obj in guideline_objects
        ]

    return (datawrapper_post_pdf_to_catalog_entries,)


@app.cell(hide_code=True)
def _(prompt_contract_digest):
    DATAWRAPPER_PROMPT_SPEC = {
        "allow_empty": True,
        "cardinality_instruction": (
            "Extract multiple guidelines if present. "
            "Output each in fenced ```md blocks separately, separated by blank lines."
        ),
        "evidence_scope": "Strictly base each guideline on the evidence provided in the blog post and nothing else.",
        "source_specific_rules": [
            "Extract reusable editorial heuristics rather than retelling the blog narrative.",
            (
                "Keep platform-specific advice only when it changes "
                "a concrete visualization decision, critique step, or revision move."
            ),
        ],
    }
    DATAWRAPPER_PROMPT_DIGEST = prompt_contract_digest(
        DATAWRAPPER_PROMPT_SPEC,
        ["[@blog-post]"],
    )
    return DATAWRAPPER_PROMPT_DIGEST, DATAWRAPPER_PROMPT_SPEC


@app.cell(hide_code=True)
def _(DATAWRAPPER_REFS: list[str], ccp, pathlib):
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
        entries = ccp.parse_bibtex(DATAWRAPPER_REFS)
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
    ## Source 3: Accessibility Standards (Chartability)

    Chartability provides 50 heuristic evaluation criteria for visualization accessibility. Unlike the perception studies, these criteria derive from inclusive design principles rather than controlled experiments. They address screen reader compatibility, keyboard navigation, color contrast, and cognitive load.

    We extracted the structured heuristic items from the [Chartability workbook](https://chartability.github.io/POUR-CAF/) and mapped each to the guideline schema, preserving links to WCAG success criteria where applicable.

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
    ch_catalog.df
    return (ch_catalog,)


@app.cell(hide_code=True)
def _(
    CHARTABILITY_PAPER_BIBTEX,
    CHARTABILITY_PAPER_CITEKEY,
    CHARTABILITY_PAPER_ITEM,
    CHARTABILITY_PROMPT_SPEC,
    CatalogEntry,
    GUIDELINE_TEMPLATE,
    build_guideline_extraction_prompt,
    ccp,
    client,
    create_pdf_content_part,
    fence,
    json,
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
        guideline_obj = ccp.parse_guideline(guideline_md)
        references = [CHARTABILITY_PAPER_BIBTEX, *ch_item["references"]]

        return CatalogEntry(guideline=guideline_obj, references=references)

    return (chartability_item_to_catalog_entry,)


@app.cell(hide_code=True)
def _(prompt_contract_digest):
    CHARTABILITY_PROMPT_SPEC = {
        "allow_empty": True,
        "cardinality_instruction": (
            "Return exactly one fenced ```md block if the item supports one "
            "directly actionable guideline. Otherwise, return an empty string."
        ),
        "evidence_scope": (
            "Strictly base the guideline on the structured accessibility knowledge provided here and nothing else."
        ),
        "source_specific_rules": [
            "Translate the accessibility criterion into concrete design actions, reviewer checks, or remediation steps.",
            "Use the Chartability paper citation plus any directly relevant linked references from the provided item.",
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
    ## Source 4: Collated Graphical Perception Findings

    Zeng and Battle systematically collated findings from 58 empirical studies on graphical perception. Their work extracts performance metrics (accuracy, response time, bias) that rank visual encodings and chart types.

    For each collated paper, we retrieved both the original PDF and the structured knowledge Zeng and Battle extracted. The extraction model used both sources to generate guidelines, ensuring that the rationale traces back to specific experimental findings.

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
    prc_catalog.df
    return (prc_catalog,)


@app.cell(hide_code=True)
def _(
    COLLATED_PROMPT_SPEC,
    COLLATION_REVIEW_PAPER_BIBTEX,
    COLLATION_REVIEW_PAPER_CITEKEY,
    COLLATION_REVIEW_PAPER_ITEM,
    CatalogEntry,
    GUIDELINE_TEMPLATE,
    build_guideline_extraction_prompt,
    ccp,
    client,
    create_pdf_content_part,
    fence,
    json,
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
            ccp.parse_guideline(md_content) for md_content in unfence(response_text)
        ]

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
        "allow_empty": True,
        "cardinality_instruction": (
            "Extract multiple guidelines if present. "
            "Output each in fenced ```md blocks separately, separated by blank lines."
        ),
        "evidence_scope": (
            "Strictly base each guideline on the structured knowledge provided here. "
            "Use the PDFs only to disambiguate wording or evidence and nothing else."
        ),
        "source_specific_rules": [
            "Treat the structured knowledge as the primary signal.",
            "Discard raw comparative findings unless they imply a concrete chart decision, critique check, or revision step.",
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
    from pyzotero import zotero
    import itertools

    return itertools, zotero


@app.cell(column=5, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Source 5: Rhetorical Guidelines (Talking Charts)

    The [Talking Charts project](https://talking-charts.vda.univie.ac.at) produced 32 findings on how producers and consumers interpret visualizations. These findings address rhetoric, audience connection, and the gap between intended and received messages—aspects that perception-focused research typically omits.

    The findings were already structured as JSON with associated references. We mapped each finding to the guideline schema, preserving citation links to the underlying publications.

    **References:**
    > Gregory, K., Koesten, L., Schuster, R., Möller, T., & Davies, S. (2024). Data journeys in popular science. *Harvard Data Science Review*, 6(2).
    > Knoll, C., Möller, T., Gregory, K., & Koesten, L. (2025). The gulf of interpretation. *CHI 2025*, 1–17.
    > Koesten, L., Gregory, K., Schuster, R., Knoll, C., Davies, S., & Möller, T. (2023). What is the message? arXiv:2304.10544.
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
            "guideline": guideline,
            "references": tc_references,
            "model": DEFAULT_CLIENT_CONFIG["model"],
            "reasoning": DEFAULT_CLIENT_CONFIG["reasoning"],
        }
        for guideline in tc_findings["guidelines"]
    ]

    tc_entries = parallel_map(
        fn=param_collapsed(tc_guideline_to_catalog_entry),
        inputs=tc_tasks,
        n_jobs=16,
        desc="Processing Talking Charts guidelines",
        cache_key_provider=lambda inp: "___".join(
            [
                string_hash(json.dumps(inp)),
                TALKING_CHARTS_PROMPT_DIGEST,
            ]
        ),
    )
    tc_entries = [entry for entry in tc_entries if entry is not None]
    tc_catalog = Catalog(tc_entries)
    tc_catalog.df
    return (tc_catalog,)


@app.cell(hide_code=True)
def _(
    CatalogEntry,
    Guideline,
    build_tc_prompt,
    ccp,
    client,
    list_ref_ids,
    list_tc_guideline_references,
    pick_refs,
    unfence,
):
    def tc_guideline_to_catalog_entry(
        guideline: dict,
        references: list[str],
        model: str,
        reasoning: dict | None = None,
    ) -> CatalogEntry | None:
        # Enumerate all the reference IDs available for Talking Charts
        allowed_ref_ids = list_ref_ids(references)
        required_ref_ids = sorted(
            list_tc_guideline_references(guideline, allowed_ref_ids)
        )

        # Map knowledge to our representation
        prompt = build_tc_prompt(guideline, required_ref_ids, allowed_ref_ids)
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

        # Parse response and associate the references with the entry
        if not response_text.strip():
            return None

        fenced_guidelines = unfence(response_text)
        if not fenced_guidelines:
            return None

        md_content = fenced_guidelines[0]
        guideline_obj: Guideline = ccp.parse_guideline(md_content)
        references: list[str] = ccp.parse_bibtex(
            pick_refs(
                required_ref_ids,
                references,
            )
        )

        return CatalogEntry(guideline=guideline_obj, references=references)

    return (tc_guideline_to_catalog_entry,)


@app.cell(hide_code=True)
def _(prompt_contract_digest):
    TALKING_CHARTS_PROMPT_SPEC = {
        "allow_empty": True,
        "cardinality_instruction": (
            "Return exactly one fenced ```md block if the finding supports one directly actionable guideline. "
            "Otherwise, return an empty string."
        ),
        "evidence_scope": "Strictly base the guideline on the codified knowledge provided here and nothing else.",
        "source_specific_rules": [
            (
                "Translate rhetorical or interpretive findings into concrete framing, "
                "annotation, titling, grouping, or revision guidance."
            ),
            "If the finding cannot be operationalized into chart creation, feedback, or rework, omit it.",
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
    ## Extraction Pipeline

    Each source follows the same three-stage pattern: retrieve the document, extract guidelines using a generative model, and write structured output.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.mermaid("""
    flowchart TD
        subgraph stage1["1. Retrieve"]
            direction TB
            S1["Cognitive Science<br/>103 papers"]
            S2["Graphical Perception<br/>58 papers + metadata"]
            S3["Chartability<br/>50 heuristics"]
            S4["Datawrapper<br/>36 blog posts"]
            S5["Talking Charts<br/>32 findings"]
        end

        subgraph stage2["2. Extract"]
            direction TB
            PROMPT["Construct prompt<br/>───────────<br/>• PDF or JSON source<br/>• Guideline template<br/>• Citation format"]
            LLM["Large Language Model"]
            PARSE["Parse response<br/>───────────<br/>• Split markdown blocks<br/>• Extract sections<br/>• Attach references"]
        end

        subgraph stage3["3. Output"]
            direction TB
            PARQUET["catalog.parquet<br/>744 guidelines"]
            MD["guidelines/<br/>Markdown files"]
        end

        stage1 --> PROMPT
        PROMPT --> LLM
        LLM --> PARSE
        PARSE --> stage3

        classDef stageBox fill:#f8f9fa,stroke:#dee2e6
        classDef source fill:#e3f2fd,stroke:#1976d2
        classDef process fill:#fff8e1,stroke:#f9a825
        classDef output fill:#e8f5e9,stroke:#43a047

        class stage1,stage2,stage3 stageBox
        class S1,S2,S3,S4,S5 source
        class PROMPT,LLM,PARSE process
        class PARQUET,MD output
    """)
    return


@app.cell(hide_code=True)
def _(pathlib, string_hash):
    NB_ROOT = pathlib.Path(__file__).parent
    REPO_ROOT = NB_ROOT.parent.parent.parent
    ASSETS_ROOT = NB_ROOT / "assets"
    REPO_ROOT = NB_ROOT.parent.parent.parent
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
    WORKFLOW_LABELS = [
        "workflow:create",
        "workflow:feedback",
        "workflow:rework",
    ]

    def build_guideline_extraction_prompt(
        *,
        evidence_scope: str,
        cardinality_instruction: str,
        source_specific_rules: list[str],
        required_citations: list[str],
        allow_empty: bool = True,
    ) -> str:
        lines = [
            "Only extract guidelines that are directly actionable during visualization creation from scratch, feedback on an existing visualization, or rework of an existing visualization.",
        ]

        if allow_empty:
            lines.append(
                "If the source material cannot be translated into directly actionable visualization guidance, respond with an empty string."
            )

        lines.extend(
            [
                cardinality_instruction,
                evidence_scope,
                "Each emitted guideline is well-defined, isolated, and granular.",
                "A valid guideline changes a concrete chart decision, critique step, or revision step that a practitioner can apply without rereading the source.",
                "Reject candidates that only summarize theory, taxonomy, historical context, methodology, study setup, or narrative commentary.",
                "Reject candidates that are visualization-relevant but do not tell the practitioner what to choose, inspect, test, or change in a chart.",
                "Operationalize descriptive findings in the form 'When [condition], do [change] to achieve [goal].' If that rewrite is not supported by the source, omit the candidate.",
                "Prefer guidance that changes a concrete design lever such as chart type, encoding, scale, ordering, grouping, titling, annotation, labeling, legend design, layout, interaction, accessibility treatment, or rhetorical framing that can be implemented in a chart.",
                f"Every emitted guideline includes at least one workflow label from: {', '.join(WORKFLOW_LABELS)}.",
                "Multiple workflow labels are used only when the same guideline genuinely supports multiple workflows.",
                "The title is a specific imperative action on a concrete chart or design object.",
                "The description states the action, benefit, and triggering situation.",
                "The `check` section contains an observable failure sign and a concrete review procedure that a reviewer can run.",
                "The `fix` section consists of concrete edit operations, not abstract restatements of the advice.",
                "Bad candidate: 'Color affects interpretation.' Good candidate: 'Use a colorblind-safe sequential palette when color encodes magnitude and hue identity is not the message.'",
                "Bad candidate: 'Crowding hurts readability.' Good candidate: 'Reduce mark density or split the display into small multiples when crowding prevents item-level reading.'",
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
def _(Catalog, fence, mo):
    def display_references(catalog: Catalog):
        refs: list[str] = (
            catalog.df()
            .select("references")
            .explode("references")
            .unique()
            .sort("references")
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

    return


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
    from types import SimpleNamespace

    import marimo as mo

    from chartcoach import Catalog, CatalogEntry, Guideline
    from chartcoach.guideline import parse_bibtex, parse_guideline

    ccp = SimpleNamespace(
        parse_bibtex=parse_bibtex,
        parse_guideline=parse_guideline,
    )

    return Catalog, CatalogEntry, Guideline, ccp, json, mo, pathlib


if __name__ == "__main__":
    app.run()
