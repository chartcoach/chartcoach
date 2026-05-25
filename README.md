# ChartCoach

ChartCoach is a monorepo for structured visualization guidelines, the public
guideline browser, shared UI, and catalog loaders.

The catalog stores each guideline as a compact record: recommendation, scope,
evidence, labels, and references. The same records render on the site, load from
Python and JavaScript, and support ChartCoach applications.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for setup details, local development commands, and verification checks.

## What You Can Do

- Browse chart guidance by label, context, caveat, and citation.
- Load the catalog from Python, Node.js, or browser applications.

## Repository Map

### Applications (`apps`)

* [`site`](apps/site): Astro/Starlight documentation site and guideline browser.

### Packages (`packages`)

* [`catalog-javascript`](packages/catalog-javascript): JavaScript loaders, parsers, and wire types for the guideline catalog.
* [`catalog-python`](packages/catalog-python): Python catalog package and `chartcoach` command-line entrypoint.
* [`ui`](packages/ui): Shared React UI primitives, design tokens, and ChartCoach brand assets.

## Quickstart

Install the workspace from the repository root:

```sh
corepack enable pnpm
pnpm install
uv sync --package chartcoach --all-groups
```

Run the docs site:

```sh
pnpm --dir apps/site dev
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

## License

MIT. See [`LICENSE`](LICENSE).
