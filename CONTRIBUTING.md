# Contributing

chartcoach is a research monorepo for a visualization guideline catalog, the
public site, shared UI, and catalog loaders.

## Checklist

Before sending a substantial change, make sure you have:

- discussed broad API, data-shape, dependency, artifact, or UX changes first
- installed both JavaScript and Python workspaces
- run the checks closest to the files you touched
- updated matching readers, docs, and lockfiles when a contract changes.

## Substantial Changes

Open an issue or talk with a maintainer before work that changes:

1. catalog record shapes or parsing semantics
2. published Python or JavaScript APIs
3. required or optional dependencies
4. generated artifact policy or stored data layout
5. public site information architecture or visual direction
6. default configuration
7. broad internal boundaries or package ownership.

## Setup

Prerequisites:

- Node 24, managed through `package.json` `devEngines`
- pnpm through Corepack
- Python 3.12 for local development, pinned by `.python-version`
- uv for Python packages.

The published `chartcoach` Python package supports Python 3.11 through 3.14.
Local tooling is pinned to one interpreter so lockfile runs stay predictable.

Install from the repository root:

```sh
corepack enable pnpm
pnpm install
uv sync --package chartcoach --all-groups
```

## Common Commands

```sh
pnpm --dir apps/site dev
```

## Checks

Run the closest command first, then broaden before packaging a
cross-workspace change.

```sh
pnpm lint
pnpm typecheck
pnpm build
pnpm test
```

Package-specific checks:

```sh
pnpm --dir apps/site lint
pnpm --dir apps/site build
pnpm --dir packages/catalog-javascript test
pnpm --dir packages/catalog-python test
uv build --package chartcoach
uv run ruff check .
uv run ty check .
uv run pyrefly check --summary=none
```

## Publishing

Releases publish the Python package `chartcoach` and the npm package
`@chartcoach/catalog` from `.github/workflows/publish.yml`.

Use the same version in `packages/catalog-python/pyproject.toml` and
`packages/catalog-javascript/package.json`, then check the tag before pushing:

```sh
./scripts/release.sh check-version v0.1.5
```

The script accepts tags with or without a leading `v`. It fails when the Python
and npm package versions differ, or when the tag does not match the package
version.

Pushing a matching `X.Y.Z` or `vX.Y.Z` tag starts the publish workflow. The
build job installs pnpm and uv, runs the format, lint, typecheck, test, and
build gates, builds the PyPI and npm packages, and uploads both outputs as
GitHub artifacts. Separate jobs download those artifacts and publish them with
trusted publishing through GitHub OIDC. After both publishes finish,
`changelogithub` updates the GitHub release notes.

## Data and Artifacts

Catalog entries are source data. Keep `guideline.md`, `references.bib`, Python
loaders, JavaScript loaders, and browser rendering in sync.

## Documentation

Public copy should be short, concrete, and source-backed. Prefer direct claims
about what a reader can inspect or run. Avoid filler and vague rationale.
