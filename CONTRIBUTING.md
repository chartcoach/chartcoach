# Contributing

Install the JavaScript and Python workspaces from the repository root:

```sh
pnpm install
uv sync --locked --package chartcoach --all-groups --all-extras
```

The workspace selects Node through `.node-version`. Local Python tooling uses
Python 3.12 from `.python-version`. The published Python package supports
Python 3.11 through 3.14.

## Propose a change

Discuss a change with a maintainer before implementation when it affects:

- the catalog record shape, manifest, or release layout
- a published Python, JavaScript, CLI, or MCP contract
- required dependencies or optional dependency boundaries
- public site information architecture or visual direction
- package publishing or catalog publication

Small fixes can go directly to a pull request.

## Develop

Start both web apps with:

```sh
pnpm dev
```

Run the complete JavaScript gate with:

```sh
pnpm ready
```

`pnpm ready` runs Vite+ checks, workspace tests, and a fixture-backed workspace
build. Use a package command for a focused check while iterating.

Run the Python gates with:

```sh
make format lint typecheck test build
```

Run a focused test while iterating, then run the complete gate for every
workspace affected by the change.

## Keep contracts aligned

- Update Python, JavaScript, fixtures, and consuming apps together when the wire
  shape changes.
- Add the matching lockfile change when a dependency changes.
- Keep shared web assets and styles in `packages/brand`.
- Keep public documentation aligned with released behavior.
- Add tests at the nearest public API, CLI, file, or runtime boundary.

## Open a pull request

Describe the supported behavior, the affected boundary, and the commands run.
Include screenshots for visible site or docs changes. Report a skipped check
with the command, failure, and remaining risk.

Repository contracts:

- [Architecture and ownership](development_docs/architecture.md)
- [Development workflow](development_docs/development.md)
- [Releases and catalog data](development_docs/releases-and-data.md)
