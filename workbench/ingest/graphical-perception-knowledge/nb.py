# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "duckdb==1.4.1",
#     "google-genai==1.44.0",
#     "numpy==2.3.3",
#     "polars==1.34.0",
#     "pyarrow==21.0.0",
#     "pyzotero==1.6.17",
#     "tqdm==4.67.1",
# ]
# ///

import marimo

__generated_with = "0.17.0"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""# Run Inference in Bulk""")
    return


@app.cell
def _(
    ThreadPoolExecutor,
    as_completed,
    mo,
    perception_knowledge_items,
    process_task,
):
    # Sort items once
    sorted_items = sorted(
        perception_knowledge_items,
        key=lambda x: x["data"]["title"],
    )

    # Process in parallel with ThreadPoolExecutor
    max_workers = 4
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_item = {
            executor.submit(process_task, i, item): (i, item)
            for i, item in enumerate(sorted_items)
        }

        # Process completed tasks with progress tracking
        for future in mo.status.progress_bar(
            as_completed(future_to_item), total=len(sorted_items)
        ):
            i, item = future_to_item[future]
            try:
                idx, title, status, detail = future.result()
                if status == "skipped":
                    print(f"  Skipping {detail}, already exists")
                elif status == "success":
                    print(f"  Saved to {detail}")
                else:  # error
                    print(f"  Error generating guideline for {title}: {detail}")
                results.append((idx, title, status, detail))
            except Exception as e:
                print(
                    f"  Unexpected error processing {item['data']['title']}: {e}"
                )
    return


@app.cell(hide_code=True)
def _(NB_ROOT_PATH, generate_guideline, save_generated_guideline):
    def process_task(i, item):
        """Process a single item and return result info."""
        title = item["data"]["title"]
        print(f"Processing {i}: {title}")

        out = NB_ROOT_PATH / "generated" / f"{i:02d}-{item['data']['key']}.md"
        if out.exists():
            return (i, title, "skipped", str(out))

        try:
            response = generate_guideline(item)
            save_generated_guideline(response.text, out)
            return (i, title, "success", str(out))
        except Exception as e:
            return (i, title, "error", str(e))
    return (process_task,)


@app.cell(hide_code=True)
def _():
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import threading
    return ThreadPoolExecutor, as_completed


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""# LLM Setup""")
    return


@app.cell(hide_code=True)
def _(
    METHOD_PAPER_BIB_PATH,
    TEMPLATE_PATH,
    client,
    json,
    method_paper,
    pathlib,
    types,
):
    def save_generated_guideline(response_text: str, out: pathlib.Path):
        # Save raw response for debugging
        raw_output_path = out.parent / f"{out.stem}_raw.txt"
        raw_output_path.write_text(response_text)

        # Split by separator
        guidelines = response_text.split("<split/>")

        # Save each guideline as a separate file
        for i, guideline_content in enumerate(guidelines):
            # Remove markdown fences if present
            content = (
                guideline_content.strip()
                .replace("```md\n", "")
                .replace("```\nmd", "")
                .replace("\n```", "")
            )

            # Skip empty content
            if not content:
                continue

            # Generate filename: if out has a stem, use it with index, otherwise just use index
            if out.stem:
                filename = f"{out.stem}_{i:02d}.md"
            else:
                filename = f"guideline_{i:02d}.md"

            output_path = out.parent / filename
            output_path.write_text(content)


    def generate_guideline(item: dict, model: str = "gemini-2.5-pro"):
        pdf_bytes = item.pop("pdf_bytes")
        paper_pdf = (
            types.Part.from_bytes(
                data=pdf_bytes,
                mime_type="application/pdf",
            )
            if pdf_bytes is not None
            else ""
        )

        contents = [
            "Consider the following paper detailing the methodology of collating knowledge about graphical perception from research papers.",
            method_paper,
            f"""```tex\n{METHOD_PAPER_BIB_PATH.read_text()}\n```""",
            "Here is a concrete research paper as well as the collated knowledge in JSON format",
            paper_pdf,
            f"""```json\n{json.dumps(item, indent=2)}\n```""",
            "Your task is to convert this into multiple atomic, standalone guidelines expressed in natural language markdown + YAML frontmatter format adhering to this template:",
            f"""```md\n{TEMPLATE_PATH.read_text()}\n```""",
            "IMPORTANT: Break down high-level principles into concrete, specific suggestions. Each guideline should be:",
            "- Atomic: covering one specific insight or recommendation",
            "- Standalone: complete and understandable on its own",
            "- Targeted: specific to particular chart types, audiences, or tasks",
            "- Actionable: providing concrete takeaways and trade-offs, not generic wisdom",
            "",
            "If the paper outlines a high-level principle, decompose it into multiple targeted guidelines that address specific scenarios, chart types, audiences, or tasks.",
            "",
            "Output each guideline in markdown fences (```md\n ... \n```), separated by a line containing exactly '<split/>' tag.",
            "Do not include any extra commentary or explanations outside the fenced guidelines. Never hallucinate example image URLs.",
            """Format:

            ```md
            guideline 1 content...
            ```

            <split/>

            ```md
            guideline 2 content...
            ```
            """,
        ]

        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(
                    thinking_budget=-1,
                ),
            ),
        )

        return response
    return generate_guideline, save_generated_guideline


@app.cell(hide_code=True)
def _(METHOD_PAPER_PATH, types):
    method_paper = types.Part.from_bytes(data=METHOD_PAPER_PATH.read_bytes(), mime_type="application/pdf")
    return (method_paper,)


@app.cell(hide_code=True)
def _():
    from google import genai
    from google.genai import types
    from google.oauth2 import service_account

    key_path = "workbench/vertex-ai.json"
    scopes = [
        "https://www.googleapis.com/auth/generative-language",
        "https://www.googleapis.com/auth/cloud-platform",
    ]
    credentials = service_account.Credentials.from_service_account_file(
        key_path,
        scopes=scopes,
    )
    client = genai.Client(
        vertexai=True,
        credentials=credentials,
        project="leafy-clone-469613-k7",
        location="us-central1",
    )
    return client, types


@app.cell(hide_code=True)
def _():
    import pathlib

    NB_ROOT_PATH = pathlib.Path("workbench/ingest/graphical-perception-knowledge")

    TEMPLATE_PATH = pathlib.Path("workbench/templates/latest.md")

    METHOD_PAPER_PATH = pathlib.Path(
        "workbench/ingest/graphical-perception-knowledge/2109.01271v3.pdf"
    )
    METHOD_PAPER_BIB_PATH = pathlib.Path(
        "workbench/ingest/graphical-perception-knowledge/2109.01271v3.bib"
    )
    return (
        METHOD_PAPER_BIB_PATH,
        METHOD_PAPER_PATH,
        NB_ROOT_PATH,
        TEMPLATE_PATH,
        pathlib,
    )


@app.cell(column=2, hide_code=True)
def _(mo):
    mo.md(r"""# Accessing Zotero Items Programmatically""")
    return


@app.cell(hide_code=True)
def _(perception_knowledge_items):
    perception_knowledge_items[0]
    return


@app.cell(hide_code=True)
def _(items, process_item):
    perception_knowledge_items = [
        processed_item
        for item in items
        if (processed_item := process_item(item))["knowledge_json"] is not None
    ]
    return (perception_knowledge_items,)


@app.cell(hide_code=True)
def _(json, zot):
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


    def process_item(item: dict) -> dict:
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
    return (process_item,)


@app.cell(hide_code=True)
def _(PERCEPTION_KNOWLEDGE_COLLECTION_ID, VISFEEDBACK_GROUP_ID, zotero):
    zot = zotero.Zotero(VISFEEDBACK_GROUP_ID, "group", local=True)
    items = zot.collection_items(PERCEPTION_KNOWLEDGE_COLLECTION_ID)
    return items, zot


@app.cell(hide_code=True)
def _():
    VISFEEDBACK_GROUP_ID = 6228570
    PERCEPTION_KNOWLEDGE_COLLECTION_ID = "NZN6NARL"
    return PERCEPTION_KNOWLEDGE_COLLECTION_ID, VISFEEDBACK_GROUP_ID


@app.cell(hide_code=True)
def _():
    import marimo as mo
    from pyzotero import zotero
    import polars as pl
    import duckdb
    import json
    return json, mo, zotero


if __name__ == "__main__":
    app.run()
