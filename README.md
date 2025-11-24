# Work in Progress

Run examples via:

```bash
uv sync --all-groups --all-extras --all-packages
uv run marimo edit packages/catalog/python/examples --no-token --port 3335 --headless
```

Make sure that you have an [OpenRouter](http://openrouter.ai) api key set in `.env` file as `OPENROUTER_API_KEY` and a `vertex-ai.json` file with your Google Cloud credentials also in the repo root folder. `vertex-ai.json` is only required for `packages/catalog/python/examples/curation/index.py`.
