import marimo

__generated_with = "0.18.1"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=False)
def _(mo):
    mo.md(r"""
    ## Catalog Construction

    This notebook documents the extraction of 744 guidelines from five source categories. Each source differs in methodology and evidence type; the cataloging scheme accommodates all of them within a uniform structure.

    The resulting catalog supports the analyses in the paper: expressiveness validation, structural analysis, and grounded feedback.
    """)
    return


@app.cell(hide_code=False)
def _(NB_ROOT, ch_catalog, dw_catalog, misc_catalog, prc_catalog, tc_catalog):
    catalog = tc_catalog + prc_catalog + ch_catalog + dw_catalog + misc_catalog
    catalog_df = catalog.df()
    catalog_df.write_parquet(NB_ROOT / "catalog.parquet")
    catalog.write_folders("guidelines")
    catalog_df
    return


@app.cell(hide_code=False)
def _(mo):
    mo.md(r"""
    ### Summary Statistics

    The bar chart below shows the number of guidelines extracted from each source category. These counts correspond to Table 1 in the paper.
    """)
    return


@app.cell(hide_code=False)
def _(alt, guidelines_with_source_df, mo):
    guidelines_by_source_chart = alt.layer(
        *[
            alt.Chart(guidelines_with_source_df)
            .mark_bar()
            .encode(
                x=alt.X("count()", title="Number of Guidelines"),
                y=alt.Y("source", title="Source", sort="-x"),
            ),
            alt.Chart(guidelines_with_source_df)
            .mark_text(align="left", dx=3)
            .encode(
                x=alt.X("count()", title="Number of Guidelines"),
                y=alt.Y("source", title="Source", sort="-x"),
                text=alt.Text("count()", format="d"),
            ),
        ]
    )
    mo.vstack(
        [
            mo.md("### Guidelines by Source"),
            guidelines_by_source_chart,
        ]
    )
    return


@app.cell(hide_code=False)
def _(catalogs_by_source, pl):
    guidelines_with_source_df = pl.concat(
        [
            catalog.df().select(pl.lit(source).alias("source"), pl.all())
            for source, catalog in catalogs_by_source.items()
        ]
    ).unique("id", maintain_order=True)
    return (guidelines_with_source_df,)


@app.cell(hide_code=False)
def _(ch_catalog, dw_catalog, misc_catalog, prc_catalog, tc_catalog):
    catalogs_by_source = {
        "Collated Perception Knowledge": prc_catalog,
        "Talking Charts": tc_catalog,
        "Chartability Accessibility Standards": ch_catalog,
        "Datawrapper Posts": dw_catalog,
        "Cognitive Science & Perception Papers": misc_catalog,
    }
    return (catalogs_by_source,)


@app.cell(hide_code=False)
def _():
    import altair as alt
    import polars as pl

    return alt, pl


@app.cell(column=1, hide_code=False)
def _(mo):
    mo.md(r"""
    ## Source 1: Cognitive Science and Perception Papers

    We processed 103 papers cited in Franconeri et al.'s review *"The Science of Visual Data Communication"*. These papers report findings on low-level visual processing (saliency, ensemble coding, color discrimination), higher-order cognition (bias, memory, narrative framing), and applied domains (risk communication, uncertainty visualization).

    Each paper was provided to the extraction model as a PDF. The model identified actionable design implications and mapped them to the guideline schema.

    **Reference:**

    > Franconeri, S. L., Padilla, L. M., Shah, P., Zacks, J. M., & Hullman, J. (2021). The science of visual data communication: What works. *Psychological Science in the Public Interest*, 22(3), 110–161.
    """)
    return


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
def _(display_references, misc_catalog):
    display_references(misc_catalog)
    return


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
def _(ZOTERO_MISC_COLLECTION_ID, process_zot_item, zot):
    misc_items = zot.everything(zot.collection_items(ZOTERO_MISC_COLLECTION_ID))
    processed_misc_items_maybe_wo_pdf = [process_zot_item(item) for item in misc_items]
    processed_misc_items = [
        item
        for item in processed_misc_items_maybe_wo_pdf
        if item["pdf_bytes"] is not None
    ]
    return (processed_misc_items,)


@app.cell(hide_code=False)
def _():
    ZOTERO_MISC_COLLECTION_ID = "LXD29TR5"
    return (ZOTERO_MISC_COLLECTION_ID,)


@app.cell(column=2, hide_code=False)
def _(mo):
    mo.md(r"""
    ## Source 2: Practitioner Heuristics (Datawrapper)

    Datawrapper's ["Dos and Don'ts" blog series](https://www.datawrapper.de/blog/category/datavis-dos-and-donts) contains 36 posts written by data journalists. These posts address practical concerns: when to use annotations, how to handle axis truncation, and how to balance aesthetics with clarity.

    We saved each post as a PDF and processed it through the extraction pipeline. The resulting guidelines capture editorial heuristics that rarely appear in formal systems.
    """)
    return


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
def _(display_references, dw_catalog):
    display_references(dw_catalog)
    return


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
def _(NB_ROOT):
    DATAWRAPPER_POST_PDF_PATHS = list((NB_ROOT / "datawrapper" / "posts").glob("*.pdf"))
    DATAWRAPPER_REFS: list[str] = (
        NB_ROOT / "datawrapper" / "references.bib"
    ).read_text()
    return DATAWRAPPER_POST_PDF_PATHS, DATAWRAPPER_REFS


@app.cell(column=3, hide_code=False)
def _(mo):
    mo.md(r"""
    ## Source 3: Accessibility Standards (Chartability)

    Chartability provides 50 heuristic evaluation criteria for visualization accessibility. Unlike the perception studies, these criteria derive from inclusive design principles rather than controlled experiments. They address screen reader compatibility, keyboard navigation, color contrast, and cognitive load.

    We extracted the structured heuristic items from the [Chartability workbook](https://chartability.github.io/POUR-CAF/) and mapped each to the guideline schema, preserving links to WCAG success criteria where applicable.

    **Reference:**
    > Elavsky, F., Bennett, C., & Moritz, D. (2022). How accessible is my visualization? Evaluating visualization accessibility with Chartability. *Computer Graphics Forum*, 41(3), 57–70.
    """)
    return


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
def _(ch_catalog, display_references):
    display_references(ch_catalog)
    return


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
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


@app.cell(column=4, hide_code=False)
def _(mo):
    mo.md(r"""
    ## Source 4: Collated Graphical Perception Findings

    Zeng and Battle systematically collated findings from 58 empirical studies on graphical perception. Their work extracts performance metrics (accuracy, response time, bias) that rank visual encodings and chart types.

    For each collated paper, we retrieved both the original PDF and the structured knowledge Zeng and Battle extracted. The extraction model used both sources to generate guidelines, ensuring that the rationale traces back to specific experimental findings.

    **Reference:**
    > Zeng, Z., & Battle, L. (2023). A review and collation of graphical perception knowledge for visualization recommendation. *Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems*, 1–16.
    """)
    return


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
def _(display_references, prc_catalog):
    display_references(prc_catalog)
    return


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
def _(process_zot_item, zot_items):
    processed_zot_items = [process_zot_item(item) for item in zot_items]
    collated_perception_knowledge_items = [
        item for item in processed_zot_items if item["knowledge_json"] is not None
    ]
    return collated_perception_knowledge_items, processed_zot_items


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
def _(PERCEPTION_KNOWLEDGE_COLLECTION_ID, VISFEEDBACK_GROUP_ID, zotero):
    zot = zotero.Zotero(VISFEEDBACK_GROUP_ID, "group", local=True)
    zot_items = zot.collection_items(PERCEPTION_KNOWLEDGE_COLLECTION_ID)
    return zot, zot_items


@app.cell(hide_code=False)
def _():
    VISFEEDBACK_GROUP_ID = 6228570
    PERCEPTION_KNOWLEDGE_COLLECTION_ID = "FQ7DK82F"
    return PERCEPTION_KNOWLEDGE_COLLECTION_ID, VISFEEDBACK_GROUP_ID


@app.cell(hide_code=False)
def _():
    from pyzotero import zotero
    import itertools

    return itertools, zotero


@app.cell(column=5, hide_code=False)
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


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
def _(NB_ROOT, json):
    tc_findings = json.loads((NB_ROOT / "talking-charts" / "findings.json").read_text())
    tc_references = (NB_ROOT / "talking-charts" / "references.bib").read_text()
    return tc_findings, tc_references


@app.cell(column=6, hide_code=False)
def _(mo):
    mo.md(r"""
    ## Extraction Pipeline

    Each source follows the same three-stage pattern: retrieve the document, extract guidelines using a generative model, and write structured output.
    """)
    return


@app.cell(hide_code=False)
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
            LLM["Gemini 3 Pro Preview"]
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


@app.cell(hide_code=False)
def _(GUIDELINE_TEMPLATE, fence, mo):
    mo.md(rf"""
    ## Guideline Template

    The guideline template below defines the structure that each extracted guideline adheres to and is used as a prompt to LLMs to guide the extraction process. 

    {fence(GUIDELINE_TEMPLATE, lang="md")}
    """)
    return


@app.cell(hide_code=False)
def _(init_genai_client, pathlib, string_hash):
    client = init_genai_client(
        vertex_key_path="vertex-ai.json",
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


@app.cell(hide_code=False)
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

    return (display_references,)


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
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


@app.cell(hide_code=False)
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
