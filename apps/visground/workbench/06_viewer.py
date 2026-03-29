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


if __name__ == "__main__":
    app.run()
