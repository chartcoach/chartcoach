# Contributing

ChartCoach is a research monorepo for a visualization guideline catalog, the
public site, shared UI, and VisGround evaluation tooling.

## Checklist

Before sending a substantial change, make sure you have:

- discussed broad API, data-shape, dependency, artifact, or UX changes first;
- installed both JavaScript and Python workspaces;
- run the checks closest to the files you touched;
- updated matching readers, docs, examples, and lockfiles when a contract changes.

## Substantial Changes

Open an issue or talk with a maintainer before work that changes:

1. catalog record shapes or parsing semantics;
2. published Python or JavaScript APIs;
3. required or optional dependencies;
4. generated artifact policy or stored data layout;
5. public site information architecture or visual direction;
6. VisGround evaluation semantics;
7. default configuration;
8. broad internal boundaries or package ownership.

## Setup

Prerequisites:

- Node 24, managed through `package.json` `devEngines`;
- pnpm through Corepack;
- Python 3.12 for local development, pinned by `.python-version`;
- uv for Python packages and notebooks.

The published `chartcoach` Python package supports Python 3.11 through 3.15.
Local tooling is pinned to one interpreter so lockfile and notebook runs stay
predictable.

Install from the repository root:

```sh
corepack enable pnpm
pnpm install
uv sync --package chartcoach --package visground --all-groups
```

The notebook examples are standalone uv projects because their research
dependencies do not all share one installable environment. They depend on the
local `chartcoach` package by path and stay out of the root lockfile.

For notebooks and evaluation runs, create a root `.env` file:

```dotenv
OPENROUTER_API_KEY=...
OPENAI_API_KEY=...
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENAI_BASE_URL=https://api.openai.com/v1
```

Load it in shells that need model credentials:

```sh
set -a
source .env
set +a
```

## Common Commands

```sh
pnpm --dir apps/site dev
pnpm --dir apps/visground-web dev
pnpm --dir apps/visground dev:anywidget
```

Open notebooks with uv. The example notebooks are standalone projects with
their own dependency sets, and each one points at the local `chartcoach`
package by path.

```sh
PYTHONPATH=apps/visground/src uv run --project apps/visground marimo edit apps/visground/workbench/01_cohort.py
uv run --project packages/examples/guideline-analysis-example marimo edit packages/examples/guideline-analysis-example/main.py
uv run --project packages/examples/guideline-application-example marimo edit packages/examples/guideline-application-example/main.py
uv run --project packages/examples/guideline-cataloging-example marimo edit packages/examples/guideline-cataloging-example/main.py
```

## Checks

Run the narrowest useful command first, then broaden before packaging a
cross-workspace change.

```sh
pnpm lint
pnpm typecheck
pnpm build
pnpm test
```

Surface-specific checks:

```sh
pnpm --dir apps/site lint
pnpm --dir apps/site build
pnpm --dir apps/visground-web build
pnpm --dir packages/catalog-javascript test
pnpm --dir packages/visground-viewer test
pnpm --dir apps/visground test
pnpm --dir packages/catalog-python test
uv build --package chartcoach
uv run ruff check .
uv run ty check .
```

## Data and Artifacts

Catalog entries are source data. Keep `guideline.md`, `references.bib`, Python
loaders, JavaScript loaders, and browser rendering in sync.

VisGround run outputs are generated artifacts. Keep bulky generated files out of
the repository unless the file is an intentional small fixture or web-host sample.
Set `VISGROUND_VIEWER_DEV_PUBLIC_ARTIFACT_PATH` when a notebook should write a
viewer export directly into a local web app's `public/data` folder.

## Documentation

Public copy should be short, concrete, and source-backed. Prefer direct claims
about what a reader can inspect or run. Avoid filler and generic rationale.
