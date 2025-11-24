import marimo

__generated_with = "0.18.0"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Unified Design Catalog

    A holistic synthesis that bridges the gap between **academic theory** and **practitioner intuition**.

    This union harmonizes distinct epistemologies--merging **100+ cognitive science papers**, quantitative **perception rankings**, rigorous **accessibility standards**, and battle-tested **editorial heuristics**--into a single, queryable schema for intelligent visualization recommendation.
    """)
    return


@app.cell(hide_code=True)
def _(NB_ROOT, ch_catalog, dw_catalog, misc_catalog, prc_catalog, tc_catalog):
    catalog = tc_catalog + prc_catalog + ch_catalog + dw_catalog + misc_catalog
    catalog_df = catalog.df()
    catalog_df.write_parquet(NB_ROOT / "catalog.parquet")
    catalog.write_folders("guidelines")
    catalog_df
    return


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cognitive Science & Perception

    A corpus of **103 papers** cited in the foundational review *"The Science of Visual Data Communication"*.

    This collection spans diverse research domains, ranging from **low-level mechanics** (saliency, ensemble coding, color perception) to **high-level cognitive factors** (bias, memory, narrative framing) and **applied contexts** (health risk communication, uncertainty visualization).

    > Franconeri, Steven L., Lace M. Padilla, Priti Shah, Jeffrey M. Zacks, and Jessica Hullman. “The Science of Visual Data Communication: What Works.” Psychological Science in the Public Interest 22, no. 3 (2021): 110–61. https://doi.org/10.1177/15291006211051956.
    """)
    return


@app.cell(hide_code=True)
def _(
    Catalog,
    GUIDELINE_TEMPLATE_DIGEST,
    itertools,
    misc_paper_to_catalog_entries,
    parallel_map,
    param_collapsed,
    processed_misc_items,
):
    misc_tasks = [
        {
            "misc_item": item,
            "model": "gemini-3-pro-preview",
        }
        for item in processed_misc_items
    ]
    misc_entry_lists = parallel_map(
        fn=param_collapsed(misc_paper_to_catalog_entries),
        inputs=misc_tasks,
        n_jobs=8,
        desc="Processing Miscallaneous papers",
        cache_key_provider=lambda inp: "___".join(
            [
                "misc",
                inp["model"],
                inp["misc_item"]["data"]["DOI"],
                GUIDELINE_TEMPLATE_DIGEST,
            ]
        ),
    )
    misc_entries = list(itertools.chain.from_iterable(misc_entry_lists))
    misc_catalog = Catalog(misc_entries)
    misc_catalog.df()
    return (misc_catalog,)


@app.cell(hide_code=True)
def _(
    CatalogEntry,
    GUIDELINE_TEMPLATE,
    ccp,
    client,
    fence,
    types,
    unfence,
    zot_item_bibtex,
    zot_item_bibtex_key,
):
    def misc_paper_to_catalog_entries(
        misc_item: dict,
        model: str,
    ) -> list[CatalogEntry]:
        misc_item_title = misc_item["data"]["title"]
        item_bibtex = zot_item_bibtex(misc_item["data"]["key"])
        item_citekey = zot_item_bibtex_key(misc_item["data"]["key"])

        response = client.models.generate_content(
            model=model,
            contents=[
                f"Consider this paper titled '{misc_item_title}', attached as PDF:",
                types.Part.from_bytes(
                    data=misc_item["pdf_bytes"],
                    mime_type="application/pdf",
                ),
                "\n".join(
                    [
                        "Your task is to convert all the knowledge it has into granular guidelines adhering to this template:",
                        fence(GUIDELINE_TEMPLATE, lang="md"),
                    ]
                ),
                "\n".join(
                    [
                        "If content is not relevant for visualization design guidelines, respond with an empty string",
                        "Otherwise, make sure that each guideline's scope is well-defined, isolated, granular.",
                        "Strictly base each guideline on the evidence provided in the paper and nothing else.",
                        "Extract multiple guidelines if present. Output each in fenced ```md blocks separately.",
                        "Split different guidelines in the output by new lines, so they can be easily separated.",
                        f"In each guideline cite the paper as [@{item_citekey}] smoothly, naturally in the guideline body.",
                        "Never include the meta comments in the final output from the guideline template, only the section role annotations.",
                    ]
                ),
            ],
        )

        guideline_objects = [
            ccp.parse_guideline(md_content) for md_content in unfence(response.text)
        ]
        references = [item_bibtex]

        return [
            CatalogEntry(guideline=guideline_obj, references=references)
            for guideline_obj in guideline_objects
        ]

    return (misc_paper_to_catalog_entries,)


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
    ## Practitioner Wisdom (Datawrapper)

    Pragmatic, editorial design heuristics extracted from Datawrapper's extensive ["Dos and Don'ts" library](https://www.datawrapper.de/blog/category/datavis-dos-and-donts) of $36$ posts. These guidelines represent the tacit knowledge of data journalism, focusing on clarity, aesthetics, and reader engagement.
    """)
    return


@app.cell(hide_code=True)
def _(
    Catalog,
    DATAWRAPPER_POST_PDF_PATHS,
    GUIDELINE_TEMPLATE_DIGEST,
    datawrapper_post_pdf_to_catalog_entries,
    itertools,
    parallel_map,
    param_collapsed,
):
    dw_tasks = [
        {
            "post_pdf_path": post_pdf_path,
            "model": "gemini-3-pro-preview",
        }
        for post_pdf_path in DATAWRAPPER_POST_PDF_PATHS
    ]
    dw_entry_lists = parallel_map(
        fn=param_collapsed(datawrapper_post_pdf_to_catalog_entries),
        inputs=dw_tasks,
        n_jobs=8,
        desc="Processing Datawrapper posts",
        cache_key_provider=lambda inp: "___".join(
            [
                inp["model"],
                inp["post_pdf_path"].stem,
                GUIDELINE_TEMPLATE_DIGEST,
            ]
        ),
    )
    dw_entries = list(itertools.chain.from_iterable(dw_entry_lists))
    dw_catalog = Catalog(dw_entries)
    dw_catalog.df()
    return (dw_catalog,)


@app.cell(hide_code=True)
def _(
    CatalogEntry,
    GUIDELINE_TEMPLATE,
    bibtexparser,
    ccp,
    client,
    fence,
    find_datawrapper_bibtex_entry_by_path,
    pathlib,
    types,
    unfence,
):
    def datawrapper_post_pdf_to_catalog_entries(
        post_pdf_path: pathlib.Path,
        model: str,
    ) -> list[CatalogEntry]:
        bibtex_entry = find_datawrapper_bibtex_entry_by_path(post_pdf_path)
        bibtex_entry_parsed = bibtexparser.loads(bibtex_entry).entries[0]
        post_title = bibtex_entry_parsed["title"]
        citekey = bibtex_entry_parsed["ID"]

        response = client.models.generate_content(
            model=model,
            contents=[
                "\n".join(
                    [
                        "Datawrapper.de has a series of blog posts on visualization design and best practices.",
                        f"Consider this one attached as PDF, titled '{post_title}':",
                    ]
                ),
                types.Part.from_bytes(
                    data=post_pdf_path.read_bytes(),
                    mime_type="application/pdf",
                ),
                "\n".join(
                    [
                        "Your task is to convert all the knowledge into granular guidelines adhering to this template:",
                        fence(GUIDELINE_TEMPLATE, lang="md"),
                    ]
                ),
                "\n".join(
                    [
                        "Make sure that each guideline's scope is well-defined, isolated, granular.",
                        "Strictly base each guideline on the evidence provided in the blog post and nothing else.",
                        "Extract multiple guidelines if present. Output each in fenced ```md blocks separately.",
                        "Split different guidelines in the output by new lines, so they can be easily separated.",
                        f"In each guideline cite the blog post as [@{citekey}] smoothly, naturally in the guideline body.",
                        "Never include the meta comments in the final output from the guideline template, only the section role annotations.",
                    ]
                ),
            ],
        )

        guideline_objects = [
            ccp.parse_guideline(md_content) for md_content in unfence(response.text)
        ]
        references = [bibtex_entry]

        return [
            CatalogEntry(guideline=guideline_obj, references=references)
            for guideline_obj in guideline_objects
        ]

    return (datawrapper_post_pdf_to_catalog_entries,)


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
def _(NB_ROOT):
    DATAWRAPPER_POST_PDF_PATHS = list((NB_ROOT / "datawrapper" / "posts").glob("*.pdf"))
    DATAWRAPPER_REFS: list[str] = (
        NB_ROOT / "datawrapper" / "references.bib"
    ).read_text()
    return DATAWRAPPER_POST_PDF_PATHS, DATAWRAPPER_REFS


@app.cell(column=3, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Inclusive Design Standards (Chartability)

    Structured accessibility heuristics that map visualization components to WCAG standards and inclusive design principles.

    > Elavsky, Frank, Cynthia Bennett, and Dominik Moritz. “How Accessible Is My Visualization? Evaluating Visualization Accessibility with Chartability.” Computer Graphics Forum 41, no. 3 (2022): 57–70. https://doi.org/10.1111/cgf.14522.

    See the workbook: https://chartability.github.io/POUR-CAF/
    """)
    return


@app.cell(hide_code=True)
def _(
    CHARTABILITY_ITEMS,
    Catalog,
    GUIDELINE_TEMPLATE_DIGEST,
    chartability_item_to_catalog_entry,
    json,
    parallel_map,
    param_collapsed,
    string_hash,
):
    ch_tasks = [
        {
            "ch_item": ch_item,
            "model": "gemini-3-pro-preview",
        }
        for ch_item in CHARTABILITY_ITEMS
    ]
    ch_entries = parallel_map(
        fn=param_collapsed(chartability_item_to_catalog_entry),
        inputs=ch_tasks,
        n_jobs=8,
        desc="Processing Chartability items",
        cache_key_provider=lambda inp: "___".join(
            [
                string_hash(json.dumps(inp["ch_item"])),
                GUIDELINE_TEMPLATE_DIGEST,
            ]
        ),
    )
    ch_catalog = Catalog(ch_entries)
    ch_catalog.df()
    return (ch_catalog,)


@app.cell(hide_code=True)
def _(
    CHARTABILITY_PAPER_BIBTEX,
    CHARTABILITY_PAPER_CITEKEY,
    CHARTABILITY_PAPER_ITEM,
    CatalogEntry,
    GUIDELINE_TEMPLATE,
    ccp,
    client,
    fence,
    json,
    types,
    unfence,
):
    def chartability_item_to_catalog_entry(
        ch_item: dict,
        model: str,
    ) -> CatalogEntry:
        response = client.models.generate_content(
            model=model,
            contents=[
                f"Consider this paper [@{CHARTABILITY_PAPER_CITEKEY}] on visualzation accessibility guidelines:",
                types.Part.from_bytes(
                    data=CHARTABILITY_PAPER_ITEM["pdf_bytes"],
                    mime_type="application/pdf",
                ),
                "\n\n".join(
                    [
                        "Focus on this specific guideline extracted from the work:",
                        fence(json.dumps(ch_item, indent=2), lang="json"),
                    ]
                ),
                "\n\n".join(
                    [
                        "Your task is to convert all the knowledge into a single guideline adhering to this template:",
                        fence(GUIDELINE_TEMPLATE, lang="md"),
                    ]
                ),
                "\n".join(
                    [
                        "Strictly base each guideline on the evidence provided in the structured knowledge and nothing else.",
                        "Output the response in fenced ```md and do not include anything else.",
                        "Always include relevant references smoothly into the text with the format [@citekey]. Strictly follow this format, do not deviate from it by adding anything extra into the brackets.",
                        f"In each guideline cite the collation paper [@{CHARTABILITY_PAPER_CITEKEY}] and the related references smoothly, naturally in the guideline body.",
                        "Never include the meta comments in the final output from the guideline template, only the section role annotations.",
                    ]
                ),
            ],
        )
        guideline_md = unfence(response.text)[0]
        guideline_obj = ccp.parse_guideline(guideline_md)
        references = [CHARTABILITY_PAPER_BIBTEX, *ch_item["references"]]

        return CatalogEntry(guideline=guideline_obj, references=references)

    return (chartability_item_to_catalog_entry,)


@app.cell(hide_code=True)
def _(
    NB_ROOT,
    json,
    process_zot_item,
    zot,
    zot_item_bibtex,
    zot_item_bibtex_key,
):
    CHARTABILITY_ITEMS = json.loads(
        (NB_ROOT / "chartability" / "items.json").read_text()
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
    ## Collated Graphical Perception Knowledge

    A systematic collation of **graphical perception** findings—how humans visually process and decode information. This catalog aggregates performance metrics (accuracy, speed, bias) from 58 empirical studies to rank visual encodings and chart types, specifically designed to inform algorithmic recommendations.

    > Zeng, Zehua, and Leilani Battle. “A Review and Collation of Graphical Perception Knowledge for Visualization Recommendation.” Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems, ACM, April 19, 2023, 1–16. https://doi.org/10.1145/3544548.3581349.
    """)
    return


@app.cell(hide_code=True)
def _(
    Catalog,
    GUIDELINE_TEMPLATE_DIGEST,
    collated_item_to_catalog_entries,
    collated_perception_knowledge_items,
    itertools,
    parallel_map,
    param_collapsed,
):
    prc_tasks = [
        {
            "collated_item": collated_item,
            "model": "gemini-3-pro-preview",
        }
        for collated_item in collated_perception_knowledge_items
    ]
    prc_entry_lists = parallel_map(
        fn=param_collapsed(collated_item_to_catalog_entries),
        inputs=prc_tasks,
        n_jobs=8,
        desc="Processing collated perception knowledge items",
        cache_key_provider=lambda inp: "___".join(
            [
                inp["model"],
                inp["collated_item"]["data"]["DOI"],
                GUIDELINE_TEMPLATE_DIGEST,
            ]
        ),
    )
    prc_entries = list(itertools.chain.from_iterable(prc_entry_lists))
    prc_catalog = Catalog(prc_entries)
    prc_catalog.df()
    return (prc_catalog,)


@app.cell(hide_code=True)
def _(
    COLLATION_REVIEW_PAPER_BIBTEX,
    COLLATION_REVIEW_PAPER_CITEKEY,
    COLLATION_REVIEW_PAPER_ITEM,
    CatalogEntry,
    GUIDELINE_TEMPLATE,
    ccp,
    client,
    fence,
    json,
    types,
    unfence,
    zot_item_bibtex,
    zot_item_bibtex_key,
):
    def collated_item_to_catalog_entries(
        collated_item: dict,
        model: str,
    ) -> list[CatalogEntry]:
        collated_item_citekey = zot_item_bibtex_key(collated_item["data"]["key"])
        response = client.models.generate_content(
            model=model,
            contents=[
                f"Consider this paper [@{COLLATION_REVIEW_PAPER_CITEKEY}] on graphical perception knowledge collation:",
                types.Part.from_bytes(
                    data=COLLATION_REVIEW_PAPER_ITEM["pdf_bytes"],
                    mime_type="application/pdf",
                ),
                f"One of the papers it collated knowledge from is this one [@{collated_item_citekey}] below:",
                types.Part.from_bytes(
                    data=collated_item["pdf_bytes"],
                    mime_type="application/pdf",
                ),
                "\n".join(
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
                "\n".join(
                    [
                        "Your task is to convert all the knowledge into granular guidelines adhering to this template:",
                        fence(GUIDELINE_TEMPLATE, lang="md"),
                    ]
                ),
                "\n".join(
                    [
                        "Make sure that each guideline's scope is well-defined, isolated, granular.",
                        "Strictly base each guideline on the evidence provided in the structured knowledge and nothing else.",
                        "Extract multiple guidelines if present. Output each in fenced ```md blocks separately.",
                        "Split different guidelines in the output by new lines, so they can be easily separated.",
                        "Always include relevant references smoothly into the text with the format [@citekey]. Strictly follow this format, do not deviate from it by adding anything extra into the brackets.",
                        f"In each guideline cite both the collation review paper [@{COLLATION_REVIEW_PAPER_CITEKEY}] and the original paper [@{collated_item_citekey}] smoothly, naturally in the guideline body.",
                        "Never include the meta comments in the final output from the guideline template, only the section role annotations.",
                    ]
                ),
            ],
        )

        guideline_objects = [
            ccp.parse_guideline(md_content) for md_content in unfence(response.text)
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
    ## Communicative Intent (Talking Charts)

    Qualitative guidelines focusing on rhetoric, resonance, and audience connection. These checklists bridge the gap between technical correctness and the ability of a chart to "speak" to lay audiences. $32$ items extracted from the [Talking Charts](https://talking-charts.vda.univie.ac.at) project's findings drawn from a variety of publications:

    > Gregory, Kathleen, Laura Koesten, Regina Schuster, Torsten Möller, and Sarah Davies. “Data Journeys in Popular Science: Producing Climate Change and COVID-19 Data Visualizations at Scientific American.” Harvard Data Science Review 6, no. 2 (2024). https://doi.org/10.1162/99608f92.141c99cf.

    > Knoll, Christian, Torsten Möller, Kathleen Gregory, and Laura Koesten. “The Gulf of Interpretation: From Chart to Message and Back Again.” Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems, ACM, April 26, 2025, 1–17. https://doi.org/10.1145/3706598.3713413.

    > Koesten, Laura, Kathleen Gregory, Regina Schuster, Christian Knoll, Sarah Davies, and Torsten Möller. “What Is the Message? Perspectives on Visual Data Communication.” arXiv:2304.10544. Preprint, arXiv, April 12, 2023. https://doi.org/10.48550/arXiv.2304.10544.

    > Koesten, Laura, Antonia Saske, Sandra Maria Starchenko, and Kathleen Gregory. “Encountering Friction, Understanding Crises: How Do Digital Natives Make Sense of Crisis Maps?” Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems, ACM, April 26, 2025, 1–15. https://doi.org/10.1145/3706598.3713520.

    > Schuster, Regina, Kathleen Gregory, Torsten Möller, and Laura Koesten. “‘Being Simple on Complex Issues’ – Accounts on Visual Data Communication About Climate Change.” IEEE Transactions on Visualization and Computer Graphics 30, no. 9 (2024): 6598–611. https://doi.org/10.1109/TVCG.2024.3352282.
    """)
    return


@app.cell(hide_code=True)
def _(
    Catalog,
    GUIDELINE_TEMPLATE_DIGEST,
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
            "model": "gemini-3-pro-preview",
        }
        for guideline in tc_findings["guidelines"]
    ]

    tc_entries = parallel_map(
        fn=param_collapsed(tc_guideline_to_catalog_entry),
        inputs=tc_tasks,
        n_jobs=8,
        desc="Processing Talking Charts guidelines",
        cache_key_provider=lambda inp: "___".join(
            [
                string_hash(json.dumps(inp)),
                GUIDELINE_TEMPLATE_DIGEST,
            ]
        ),
    )
    tc_catalog = Catalog(tc_entries)
    tc_catalog.df()
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
        model: str = "gemini-2.5-flash",
    ) -> CatalogEntry:
        # Enumerate all the reference IDs available for Talking Charts
        allowed_ref_ids = list_ref_ids(references)

        # Map knowledge to our representation
        prompt = build_tc_prompt(guideline, allowed_ref_ids)
        response = client.models.generate_content(
            model=model,
            contents=prompt,
        )

        # Parse response and associate the references with the entry
        md_content = unfence(response.text)[0]
        guideline_obj: Guideline = ccp.parse_guideline(md_content)
        references: list[str] = ccp.parse_bibtex(
            pick_refs(
                list_tc_guideline_references(guideline, allowed_ref_ids),
                references,
            )
        )

        return CatalogEntry(guideline=guideline_obj, references=references)

    return (tc_guideline_to_catalog_entry,)


@app.cell(hide_code=True)
def _(GUIDELINE_TEMPLATE, fence, prepare_guideline):
    def build_tc_prompt(guideline: dict, allowed_ref_ids: list[str]) -> str:
        prepared_guideline = prepare_guideline(guideline, allowed_ref_ids)

        return rf"""Peruse this codified piece of knowledge:

    {fence(prepared_guideline, lang="json")}

    Your task is to convert it into this representation:

    {fence(GUIDELINE_TEMPLATE, lang="md")}

    The only comments you are allowed to include in the final output are the role-tagging comments after section headers.
    Exclude comments both from the YAML frontmatter and from below the section headers too.

    Make sure to smoothly reference all the linked studies in the suggested format.
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
def _(NB_ROOT, json):
    tc_findings = json.loads((NB_ROOT / "talking-charts" / "findings.json").read_text())
    tc_references = (NB_ROOT / "talking-charts" / "references.bib").read_text()
    return tc_findings, tc_references


@app.cell(column=6, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Utilities
    """)
    return


@app.cell(hide_code=True)
def _(init_genai_client, pathlib, string_hash):
    client = init_genai_client(
        vertex_key_path="workbench/vertex-ai.json",
        project_id="vispartner",
        location="global",
    )
    NB_ROOT = pathlib.Path(__file__).parent
    GUIDELINE_TEMPLATE_PATH = pathlib.Path(
        "guidelines/__templates__/default/GUIDELINE.md"
    )
    GUIDELINE_TEMPLATE = GUIDELINE_TEMPLATE_PATH.read_text()
    GUIDELINE_TEMPLATE_DIGEST = string_hash(GUIDELINE_TEMPLATE)
    return GUIDELINE_TEMPLATE, GUIDELINE_TEMPLATE_DIGEST, NB_ROOT, client


@app.cell(hide_code=True)
def _():
    def fence(string: str, lang: str = "json") -> str:
        return f"```{lang}\n{string}\n```"

    def unfence(text: str) -> list[str]:
        import re

        pattern = r"```(?:\w+)?\n(.*?)\n```"
        return [match.strip() for match in re.findall(pattern, text, re.DOTALL)]

    def string_hash(s: str) -> str:
        import hashlib

        return hashlib.sha256(s.encode("utf-8")).hexdigest()

    return fence, string_hash, unfence


@app.cell(hide_code=True)
def _(json):
    from typing import Callable, Iterable, ParamSpec, TypeVar
    import diskcache
    from joblib import Parallel, delayed
    import tenacity
    from tqdm.auto import tqdm

    T = TypeVar("T")
    R = TypeVar("R")

    def parallel_map(
        fn: Callable[[T], R],
        inputs: Iterable[T],
        n_jobs: int = -1,
        backend: str = "threading",
        desc: str | None = None,
        cache_dir: str | None = ".cache",
        cache_key_provider: Callable[[T], str] | None = None,
    ) -> list[R]:
        """Execute fn over inputs in parallel with progress bar that updates on completion."""
        inputs_list = list(inputs)
        cache = diskcache.Cache(cache_dir) if cache_dir else None

        with tqdm(total=len(inputs_list), desc=desc) as pbar:

            @tenacity.retry(
                wait=tenacity.wait_fixed(1),
                stop=tenacity.stop_after_attempt(3),
                reraise=True,
            )
            def _wrapper(inp: T) -> R:
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

                if cache is not None:
                    cache.set(cache_key, result)

                pbar.update(1)
                return result

            results = list(
                Parallel(n_jobs=n_jobs, backend=backend, return_as="generator")(
                    delayed(_wrapper)(inp) for inp in inputs_list
                )
            )

            return results

    P = ParamSpec("P")
    R = TypeVar("R")

    def param_collapsed(fn: Callable[P, R]) -> Callable[[dict], R]:
        """Convert a function that takes parameters into one that takes a dict and unpacks it."""

        def wrapped(item: dict) -> R:
            return fn(**item)

        return wrapped

    return parallel_map, param_collapsed


@app.cell(hide_code=True)
def _():
    from google import genai
    from google.genai import types
    from google.oauth2 import service_account

    def init_genai_client(
        vertex_key_path: str, project_id: str, location: str
    ) -> genai.Client:
        scopes = [
            "https://www.googleapis.com/auth/generative-language",
            "https://www.googleapis.com/auth/cloud-platform",
        ]
        credentials = service_account.Credentials.from_service_account_file(
            vertex_key_path,
            scopes=scopes,
        )
        return genai.Client(
            vertexai=True,
            credentials=credentials,
            project=project_id,
            location=location,
        )

    return init_genai_client, types


@app.cell(hide_code=True)
def _():
    import json
    import pathlib

    import marimo as mo

    from chartcoach_catalog.catalog import Catalog
    from chartcoach_catalog.model import CatalogEntry, Guideline
    import chartcoach_catalog.parse as ccp

    return Catalog, CatalogEntry, Guideline, ccp, json, mo, pathlib


if __name__ == "__main__":
    app.run()
