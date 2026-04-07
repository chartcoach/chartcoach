# VisGround

## Viewer dev loop

Run the anywidget Vite dev server in one terminal:

```sh
pnpm --dir apps/visground dev:anywidget
```

Launch the viewer with marimo in another terminal:

```sh
VISGROUND_VIEWER_DEV=1 uv run marimo run workbench/06_viewer.py
```

Then edit the viewer sources in `packages/visground-viewer/`. The open marimo page
should update through Vite/anywidget HMR without needing leaf `pre*` hooks.

If you need a non-default Vite URL, set `VISGROUND_VIEWER_DEV_URL` before
launching marimo. By default, `06_viewer.py` now points chart images at the
hosted files base URL
`https://files.peter.gy/projects/cc/supplementary/05-empirical-study/03-pipeline/03_generated_charts/`,
so the notebook works without a separate local image server. If your images live
somewhere else, set `VISGROUND_VIEWER_IMAGE_BASE_URL` explicitly. Production
mode continues to use the built widget bundle under
`src/visground/viewer/_static/anywidget/index.js`.

`VISGROUND_VIEWER_DEV_URL` can point either to the wrapped anywidget URL
(`http://127.0.0.1:5173/js/anywidget.ts?anywidget`) or to the bare Vite entry
(`http://127.0.0.1:5173/js/anywidget.ts`). The widget normalizes the bare form
to `?anywidget` automatically so HMR stays enabled. If you pass some other
query string, it will be replaced with `?anywidget` for the same reason.
