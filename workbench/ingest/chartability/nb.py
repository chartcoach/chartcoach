# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "google-genai==1.45.0",
#     "tqdm==4.67.1",
# ]
# ///

import marimo

__generated_with = "0.17.0"
app = marimo.App(width="columns")


@app.cell(column=0)
def _(ThreadPoolExecutor, as_completed, data, mo, process_task):
    # Process in parallel with ThreadPoolExecutor
    max_workers = 4
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_item = {
            executor.submit(process_task, i, item): (i, item)
            for i, item in enumerate(data)
        }

        # Process completed tasks with progress tracking
        for future in mo.status.progress_bar(
            as_completed(future_to_item),
            total=len(data),
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
                    f"  Unexpected error processing {item['title']}: {e}"
                )
    return


@app.cell
def _(NB_ROOT_PATH, generate_guideline, save_generated_guideline):
    def process_task(i, item):
        """Process a single item and return result info."""
        title = item["title"]
        print(f"Processing {i}: {title}")

        out = NB_ROOT_PATH / "generated" / f"CH_{i:02d}.md"
        if out.exists():
            return (i, title, "skipped", str(out))

        try:
            response = generate_guideline(item)
            save_generated_guideline(response.text, out)
            return (i, title, "success", str(out))
        except Exception as e:
            return (i, title, "error", str(e))
    return (process_task,)


@app.cell
def _():
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import threading
    return ThreadPoolExecutor, as_completed


@app.cell(column=1)
def _(PAPER_BIB_PATH, TEMPLATE_PATH, client, data, json, pathlib, types):
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


    def generate_guideline(item: dict, model: str = "gemini-2.5-flash"):
        contents = [
            "This paper collated checklists for accessibility-related guidelines:",
            "```tex\n" + PAPER_BIB_PATH.read_text() + "\n```",
            "Consider the following structured representation of an accessibility-related visualization design guideline:",
            f"""```json\n{json.dumps(data, indent=2)}\n```""",
            "Your task is to convert this into a single atomic, standalone guideline expressed in natural language markdown + YAML frontmatter format adhering to this template:",
            f"""```md\n{TEMPLATE_PATH.read_text()}\n```""",
            "Ensure in sources this Chartability paper is always present, as it is the one that collated the checklists. Cite it as 'Elavsky et al., 2022'",
            "",
            "Output a single guideline in markdown fences (```md\n ... \n```).",
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


@app.cell
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


@app.cell(column=2)
def _(data):
    data
    return


@app.cell
def _(DATA_JSON_PATH, json):
    data = json.loads(DATA_JSON_PATH.read_text())
    return (data,)


@app.cell
def _():
    import pathlib

    NB_ROOT_PATH = pathlib.Path("workbench/ingest/chartability")

    TEMPLATE_PATH = pathlib.Path("workbench/templates/latest.md")

    DATA_JSON_PATH = NB_ROOT_PATH / "data.json"

    PAPER_BIB_PATH = NB_ROOT_PATH / "ref.bib"
    return DATA_JSON_PATH, NB_ROOT_PATH, PAPER_BIB_PATH, TEMPLATE_PATH, pathlib


@app.cell
def _():
    import marimo as mo
    import json
    return json, mo


if __name__ == "__main__":
    app.run()
