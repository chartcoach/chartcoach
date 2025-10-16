# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "google-genai==1.45.0",
# ]
# ///

import marimo

__generated_with = "0.17.0"
app = marimo.App(width="columns")


@app.cell(column=0)
def _(ThreadPoolExecutor, as_completed, mo, pdf_paths, process_task):
    # Process in parallel with ThreadPoolExecutor
    max_workers = 2
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_item = {
            executor.submit(process_task, i, item): (i, item)
            for i, item in enumerate(pdf_paths)
        }

        # Process completed tasks with progress tracking
        for future in mo.status.progress_bar(
            as_completed(future_to_item), total=len(pdf_paths)
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
                print(f"  Unexpected error processing {item}: {e}")
    return


@app.cell
def _(NB_ROOT_PATH, generate_guidelines, pathlib, save_generated_guidelines):
    def process_task(i: int, item: pathlib.Path):
        """Process a single item and return result info."""
        title = item.stem
        print(f"Processing {i}: {title}")

        out = NB_ROOT_PATH / "generated" / f"DW_{i:02d}.md"
        if out.exists():
            return (i, title, "skipped", str(out))

        try:
            response = generate_guidelines(item)
            save_generated_guidelines(response.text, out)
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
def _(TEMPLATE_PATH, client, pathlib, types):
    def save_generated_guidelines(response_text: str, out: pathlib.Path):
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


    def generate_guidelines(
        post_pdf_path: pathlib.Path, model: str = "gemini-2.5-pro"
    ):
        post_pdf_bytes = post_pdf_path.read_bytes()
        post_pdf = types.Part.from_bytes(
            data=post_pdf_bytes,
            mime_type="application/pdf",
        )
        post_url = post_pdf_path.stem

        contents = [
            f"Consider the following post from datawrapper.de ({post_url}) detailing visualization dos and donts.",
            post_pdf,
            "Your task is to convert this into multiple atomic, standalone guidelines expressed in natural language markdown + YAML frontmatter format adhering to this template:",
            f"""```md\n{TEMPLATE_PATH.read_text()}\n```""",
            "IMPORTANT: Break down high-level principles into concrete, specific suggestions. Each guideline should be:",
            "- Atomic: covering one specific insight or recommendation",
            "- Standalone: complete and understandable on its own",
            "- Targeted: specific to particular chart types, audiences, or tasks",
            "- Actionable: providing concrete takeaways and trade-offs, not generic wisdom",
            "",
            "If the post outlines a high-level principle, decompose it into multiple targeted guidelines that address specific scenarios, chart types, audiences, or tasks.",
            "",
            "Output each guideline in markdown fences (```md\n ... \n```), separated by a line containing exactly '<split/>' tag.",
            "Do not include any extra commentary or explanations outside the fenced guidelines. Never hallucinate example image URLs.",
            """FORMAT:

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
    return generate_guidelines, save_generated_guidelines


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
def _(POST_PDFS_ROOT):
    pdf_paths = sorted(list(POST_PDFS_ROOT.glob("*.pdf")))
    pdf_paths
    return (pdf_paths,)


@app.cell
def _():
    import pathlib

    NB_ROOT_PATH = pathlib.Path("workbench/ingest/datawrapper")

    TEMPLATE_PATH = pathlib.Path("workbench/templates/latest.md")

    POST_PDFS_ROOT = NB_ROOT_PATH / "posts"
    return NB_ROOT_PATH, POST_PDFS_ROOT, TEMPLATE_PATH, pathlib


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
