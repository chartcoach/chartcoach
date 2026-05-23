# ChartCoach

ChartCoach is a monorepo for structured visualization guidelines, the public
guideline browser, shared UI, and VisGround evaluation tooling.

The catalog stores each guideline as a compact record: recommendation, scope,
evidence, labels, and references. The same records render on the site, load from
Python and JavaScript, and feed VisGround experiments.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for setup details, local development commands, and verification checks.

## What You Can Do

- Browse chart guidance by label, context, caveat, and citation.
- Load the catalog from Python, Node.js, or browser applications.
- Build VisGround artifacts, run model judgements, and inspect parquet exports.
- Run cataloging, analysis, and application workflows as marimo notebooks.

## Repository Map

### Applications (`apps`)

* [`site`](apps/site): Astro/Starlight documentation site and guideline browser.
* [`visground`](apps/visground): Internal Python workbench and anywidget frontend for building VisGround datasets, running evaluations, and exporting viewer artifacts.
* [`visground-web`](apps/visground-web): Standalone Vite app that hosts the VisGround viewer against a parquet artifact.

### Packages (`packages`)

* [`catalog-javascript`](packages/catalog-javascript): JavaScript loaders, parsers, and wire types for the guideline catalog.
* [`catalog-python`](packages/catalog-python): Python catalog package and `chartcoach` command-line entrypoint.
* [`ui`](packages/ui): Shared React UI primitives, design tokens, and ChartCoach brand assets.
* [`visground-viewer`](packages/visground-viewer): Reusable React viewer for VisGround parquet exports and anywidget bridges.

### Examples (`packages/examples`)

* [`guideline-analysis-example`](packages/examples/guideline-analysis-example): marimo notebook for structural analysis over the catalog.
* [`guideline-application-example`](packages/examples/guideline-application-example): marimo notebook for grounded visualization feedback.
* [`guideline-cataloging-example`](packages/examples/guideline-cataloging-example): marimo notebook for turning source material into catalog entries.

## Quickstart

Install the workspace from the repository root:

```sh
corepack enable pnpm
pnpm install
uv sync --package chartcoach --package visground --all-groups
```

Example notebooks are standalone uv projects. They depend on the local
`chartcoach` package by path, but their research dependencies stay out of the
root lockfile.

Run the docs site:

```sh
pnpm --dir apps/site dev
```

Run the standalone VisGround viewer:

```sh
pnpm --dir apps/visground-web dev
```

Open a notebook:

```sh
PYTHONPATH=apps/visground/src uv run --project apps/visground marimo edit apps/visground/workbench/01_cohort.py
uv run --project packages/examples/guideline-analysis-example marimo edit packages/examples/guideline-analysis-example/main.py
uv run --project packages/examples/guideline-application-example marimo edit packages/examples/guideline-application-example/main.py
uv run --project packages/examples/guideline-cataloging-example marimo edit packages/examples/guideline-cataloging-example/main.py
```

Check the workspace:

```sh
pnpm lint
pnpm typecheck
pnpm build
pnpm test
```

## Docs

- [`CONTRIBUTING.md`](CONTRIBUTING.md): human setup, contribution flow, and checks.
- [`AGENTS.md`](AGENTS.md): agent execution contract and source-boundary rules.
- [`apps/site`](apps/site): public site and guideline browser.
- [`apps/visground`](apps/visground): VisGround internal Python workbench.
- [`packages/visground-viewer`](packages/visground-viewer): reusable viewer package.

## License

MIT. See [`LICENSE`](LICENSE).
