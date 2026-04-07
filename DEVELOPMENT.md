# Development

## Toolchains

- JS/TS workspace: `pnpm`
- Python workspace + notebooks: `uv`

## Versions

- Node 24.x (`.nvmrc`): <https://nodejs.org/en/download>
- pnpm: <https://pnpm.io/installation>
- Python 3.12 (`.python-version`)
- uv: <https://docs.astral.sh/uv/getting-started/installation/>

## Bootstrap

From the repo root:

```sh
corepack enable pnpm
pnpm install
uv sync --all-packages --all-groups
```

## Env for notebooks / repro

Create a repo-root `.env` file (gitignored):

```dotenv
OPENROUTER_API_KEY=...
OPENAI_API_KEY=...
# optional, but useful for explicit repro
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENAI_BASE_URL=https://api.openai.com/v1
```

Docs:

- OpenRouter: <https://openrouter.ai/docs/quickstart>
- OpenAI API keys: <https://help.openai.com/en/articles/4936850-how-to-create-and-use-an-api-key>

Usage notes:

- `OPENROUTER_API_KEY` is used by the analysis/application notebooks and VisGround workbench code.
- `OPENAI_API_KEY` is used by the cataloging notebook via the official OpenAI client.
- Safe default before running notebooks:

```sh
set -a
source .env
set +a
```

Some example notebooks also auto-load the repo-root `.env`.

## Common commands

```sh
pnpm lint
pnpm typecheck
pnpm build
pnpm test
```

## Common entry points

JS apps:

```sh
pnpm --dir apps/site dev
pnpm --dir apps/visground-web dev
pnpm --dir apps/visground dev:anywidget
```

Python notebooks / workbench (marimo: <https://docs.marimo.io/>):

```sh
uv run --package visground marimo edit apps/visground/workbench/01_cohort.py
uv run --package guideline-analysis marimo edit packages/examples/guideline-analysis-example/main.py
uv run --package guideline-application marimo edit packages/examples/guideline-application-example/main.py
uv run --package guideline-cataloging marimo edit packages/examples/guideline-cataloging-example/main.py
```
