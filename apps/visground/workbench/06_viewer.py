import marimo

__generated_with = "0.21.1"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    from visground.datasets import VisGroundDataset
    from visground.viewer import VisGroundViewer

    return VisGroundDataset, VisGroundViewer, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Design Comparison Viewer

    Compare how the same request changes across the available chart conditions and inspect the evidence behind each result.
    """)
    return


@app.cell(hide_code=True)
def _(VisGroundDataset):
    store = VisGroundDataset()
    return (store,)


@app.cell(hide_code=True)
def _(VisGroundViewer, mo, store):
    widget = mo.ui.anywidget(
        VisGroundViewer(
            store=store,
        )
    )
    widget
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details>
    <summary>Stage contract</summary>

    - Required input: `03_generate.parquet`
    - Optional enrichment: `04_judgements.parquet`, cached chart images under `charts/`
    - Responsibility: provide a grounding-first interactive inspection surface for generated candidate visualizations
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details>
    <summary>Manual smoke workflow</summary>

    1. Page between cases with the previous and next controls or jump using the search box.
    2. Switch `refine` and `select`, then confirm the displayed request changes accordingly.
    3. Change grammar and audience, including partially run audience-conditioned slices.
    4. Confirm the matrix keeps the same comparison frame and uses placeholders instead of collapsing.
    5. Hover a populated cell and confirm the preview stays open while the pointer moves into it.
    6. Open a populated cell and inspect the request, chart preview, guideline IDs, rationale, and advanced details.
    7. Press `Escape` to return to the overview.
    </details>
    """)
    return


if __name__ == "__main__":
    app.run()
