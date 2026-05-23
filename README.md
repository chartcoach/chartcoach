# ChartCoach

* **Browse visualization guidelines**<br/>
  Search chart guidance by label, context, caveat, and citation.
* **Use the catalog from code**<br/>
  Load the same records from Python, Node.js, or browser applications.
* **Evaluate chart feedback**<br/>
  Build VisGround artifacts, run model judgements, and inspect results in a reusable viewer.
* **Keep examples executable**<br/>
  Explore cataloging, analysis, and application workflows as marimo notebooks.

ChartCoach is a monorepo for a visualization guideline catalog, its documentation site, shared UI components, and VisGround evaluation tooling.

The catalog stores each guideline as a compact record: recommendation, scope, evidence, labels, and references. The same records render on the site, load from Python and JavaScript, and feed VisGround experiments.

## Repository Structure

This repository contains the docs site, catalog libraries, VisGround tooling, shared UI, and notebook examples.

### Applications (`apps`)

* [`site`](apps/site): Astro/Starlight documentation site and guideline browser.
* [`visground`](apps/visground): Python package and anywidget frontend for building VisGround datasets, running evaluations, and exporting viewer artifacts.
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

Install the workspace:

* Run `corepack enable pnpm`.
* Run `pnpm install` to install JavaScript dependencies.
* Run `uv sync --all-packages --all-groups` to install Python packages and notebook dependencies.

Run the docs site:

* Run `pnpm --dir apps/site dev`.

Run the standalone VisGround viewer:

* Run `pnpm --dir apps/visground-web dev`.

Open a notebook:

* Run `uv run --package visground marimo edit apps/visground/workbench/01_cohort.py`.
* Run `uv run --package guideline-analysis marimo edit packages/examples/guideline-analysis-example/main.py`.
* Run `uv run --package guideline-application marimo edit packages/examples/guideline-application-example/main.py`.
* Run `uv run --package guideline-cataloging marimo edit packages/examples/guideline-cataloging-example/main.py`.

Check the workspace:

* Run `pnpm lint`.
* Run `pnpm typecheck`.
* Run `pnpm build`.
* Run `pnpm test`.
