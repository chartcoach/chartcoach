# chartcoach docs

The docs app builds the static chartcoach documentation site with Fumadocs and
Next.js. The published docs site is [docs.chartcoach.dev](https://docs.chartcoach.dev/).
Content pages render at root paths such as `/getting-started` on that domain.

Run the docs locally:

```bash
pnpm --dir apps/docs dev
```

The dev script runs through portless at `https://docs.chartcoach.localhost`.
Run `pnpm --dir apps/docs dev:app` to start Next.js directly.

Run focused checks and a build from the repository root:

```bash
pnpm --dir apps/docs check
pnpm --dir apps/docs typecheck
pnpm --dir apps/docs build
```

Run `pnpm ready` for the complete JavaScript workspace gate.

The build writes static files to `apps/docs/out`.

## Live examples

`@marimo-team/mdx-marimo` compiles `python marimo` fences during the docs build
and includes their initial output in the static page. The browser runtime uses
Pyodide to make those cells reactive after the page loads.

`source.config.ts` routes notebook compilation through the repository's `uv`
command so the build uses the same package-age policy as the Python workspace.
Every `marimo-config` declares the versioned chartcoach wheel from
`files.peter.gy`. The JavaScript page also pins `pyobservablejs==0.0.9`.
The Getting started page preloads the Pyodide builds of Polars and PyArrow, then
installs that wheel with dependency resolution disabled so its browser runtime
uses the WASM-compatible packages already loaded in the kernel.

The JavaScript notebook receives the workspace `@chartcoach/catalog` module
from `CatalogNotebookRuntime`. This keeps the live SDK behavior aligned with
the package source in the current checkout.

## Machine-readable docs routes

The docs site exports Fumadocs machine-readable routes for agents and search
tools:

- `/llms.txt`: page index generated from the Fumadocs page tree
- `/llms-full.txt`: concatenated Markdown for every docs page
- `/llms.mdx/docs/<path>/content.md`: Markdown for one docs page

Rendered docs pages include Fumadocs page actions for copying the current page
as Markdown and opening the Markdown route.
