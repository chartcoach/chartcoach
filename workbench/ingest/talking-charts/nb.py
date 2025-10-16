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
def _(NB_ROOT_PATH, data, generate_guidelines, save_generated_guidelines):
    response = generate_guidelines(data)
    save_generated_guidelines(response.text, NB_ROOT_PATH / "generated" / "TC.md")
    return


@app.cell
def _(TEMPLATE_PATH, client, json, pathlib, types):
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


    def generate_guidelines(data: dict, model: str = "gemini-2.5-pro"):
        contents = [
            "Consider the following structured representation of rhetorical visualization design guidelines:",
            f"""```json\n{json.dumps(data, indent=2)}\n```""",
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


@app.cell(column=1)
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

    NB_ROOT_PATH = pathlib.Path("workbench/ingest/talking-charts")

    TEMPLATE_PATH = pathlib.Path("workbench/templates/latest.md")

    DATA_JSON_PATH = NB_ROOT_PATH / "data.json"
    return DATA_JSON_PATH, NB_ROOT_PATH, TEMPLATE_PATH, pathlib


@app.cell
def _():
    import marimo as mo
    import json
    return (json,)


if __name__ == "__main__":
    app.run()
