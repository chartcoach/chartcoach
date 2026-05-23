# Development Harness

ChartCoach uses `pnpm` for JavaScript packages and `uv` for Python packages, notebooks, and local scripts.

## Toolchains

* Node 24.x, managed by `package.json` `devEngines`
* pnpm, managed through Corepack
* Python 3.12, pinned by `.python-version`
* uv, used for the Python workspace

## Installation

From the repo root:

```sh
corepack enable pnpm
pnpm install
uv sync --all-packages --all-groups
```

## Environment

Create a repo-root `.env` file for notebooks and evaluation runs:

```dotenv
OPENROUTER_API_KEY=...
OPENAI_API_KEY=...
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENAI_BASE_URL=https://api.openai.com/v1
```

Load it before running shell commands that need model credentials:

```sh
set -a
source .env
set +a
```

Some marimo notebooks also load this file through their `pyproject.toml`.

## Workspace Checks

```sh
pnpm lint
pnpm typecheck
pnpm build
pnpm test
```

Use the broad commands before packaging a cross-workspace change. For a small edit, run the command closest to the changed surface first.

## Applications

```sh
pnpm --dir apps/site dev
pnpm --dir apps/visground-web dev
pnpm --dir apps/visground dev:anywidget
```

## Notebooks

```sh
uv run --package visground marimo edit apps/visground/workbench/01_cohort.py
uv run --package guideline-analysis marimo edit packages/examples/guideline-analysis-example/main.py
uv run --package guideline-application marimo edit packages/examples/guideline-application-example/main.py
uv run --package guideline-cataloging marimo edit packages/examples/guideline-cataloging-example/main.py
```

## Surface Checks

```sh
pnpm --dir apps/site lint
pnpm --dir apps/site build
pnpm --dir apps/visground-web build
pnpm --dir packages/visground-viewer test
uv run pytest apps/visground/tests
```
