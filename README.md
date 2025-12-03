# Structured Visualization Design Knowledge

This repository contains the cataloging scheme and demonstration materials for the EuroVis 2026 full-paper submission: _Structured Visualization Design Knowledge for Grounding Generative Reasoning and Situated Feedback_

The cataloging scheme structures visualization design knowledge as natural-language guidelines with typed metadata. Guidelines are authorable by domain experts without programming, queryable by machines through semantic similarity or categorical filters, and traceable to their sources through explicit provenance.

## Repository Structure

```
packages/
└── catalog/
    └── python/
        ├── src/                    # Catalog data structures and utilities
        └── examples/
            ├── cataloging/         # Guideline extraction from source texts
            ├── analysis/           # Embedding-based knowledge space analysis
            └── application/        # Grounded feedback demonstration
```

## Viewing the Examples

Each example directory contains static exports for reproducibility:

- **`index.pdf`** — A snapshot of the notebook at the time of submission. Since some operations involve non-deterministic LLM calls, running the notebook may produce different outputs. The PDF preserves the exact results discussed in the paper.
- **`index.html`** — A static HTML export with limited interactivity. Can be viewed in any browser without running Python.
- **`index.py`** — The source [Marimo](https://marimo.io) notebook. Requires credentials and dependencies to run (see below).

## Running the Notebooks

To execute the notebooks interactively:

```bash
uv sync --all-groups --all-extras --all-packages
uv run marimo edit packages/catalog/python/examples --no-token --port 3335 --headless
```

### Required Credentials

Create a `.env` file in the repository root:

```
OPENROUTER_API_KEY=your_key_here
```

The cataloging example (`packages/catalog/python/examples/cataloging/index.py`) additionally requires:

- Google Cloud credentials for Vertex AI (place `vertex-ai.json` in the repository root)
- A locally running [Zotero](https://www.zotero.org/) instance with the literature items used as knowledge sources

## Example Notebooks

**Cataloging.** Demonstrates mapping diverse source texts (perception research, accessibility standards, practitioner heuristics) to the cataloging scheme. Uses a generative model to extract guidelines while preserving provenance through BibTeX references. Source materials are included in subdirectories (`chartability/`, `datawrapper/`, `talking-charts/`).

**Analysis.** Demonstrates embedding-based operators over the catalog: analogical transfer (similar advice, different contexts), conflict detection (similar contexts, divergent advice), viewpoint divergence (one source's advice matches another's listed mistakes), and boundary detection (context-exception handoffs between guidelines).

**Application.** Demonstrates grounded feedback generation. Compares symbolic linting (VizLinter, Draco), off-the-shelf LLM feedback, and catalog-grounded feedback via progressive disclosure. The agent retrieves guidelines relevant to the user's stated audience and task, citing specific guideline IDs that users can verify.
