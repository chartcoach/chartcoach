# VisGround

Internal Python workbench and anywidget frontend for building VisGround datasets,
running evaluations, and exporting viewer artifacts.

Run the anywidget dev server with `pnpm --dir apps/visground dev:anywidget`.

Open the first workbench with:

```sh
PYTHONPATH=apps/visground/src uv run --project apps/visground marimo edit apps/visground/workbench/01_cohort.py
```

## License

MIT. See [LICENSE](../../LICENSE).
