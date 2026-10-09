# Contributing

Run commands from the repository root. Install the locked JavaScript and
Python workspaces with:

```bash
make install
```

The workspace selects Node through `engines.node` in `package.json` and Python
through `.python-version`. The published Python package supports Python 3.10
through 3.14.

## Find the code to change

Discuss a change with a maintainer before implementation when it changes a
published data format, API, required dependency, site structure, or release
process. Small fixes can go directly to a pull request.

| Change                                                              | Start here                                                                     |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Guideline fields, labels, sections, or release files                | [Catalog files and records](development_docs/architecture/catalog-contract.md) |
| `open_catalog`, remote downloads, cache, index loading, or curation | [Python catalog code](development_docs/architecture/runtime-and-curation.md)   |
| Site pages, docs pages, shared web packages, or generated output    | [Web apps](development_docs/architecture/web-delivery.md)                      |
| Package publication or public catalog selection                     | [Releasing packages and catalog data](development_docs/releasing.md)           |
| Cross-package data flow and dependency direction                    | [Architecture](development_docs/architecture.md)                               |

## Develop

Start all three web apps with:

```bash
pnpm dev
```

[Portless](https://github.com/vercel-labs/portless) assigns each app an
available local port and prints its local URL. With the default proxy settings,
the primary checkout uses `https://chartcoach.localhost` and
`https://docs.chartcoach.localhost`, and `https://chat.chartcoach.localhost`. Linked
[Git worktrees](https://git-scm.com/docs/git-worktree) receive a subdomain
derived from the branch name, which lets several worktrees run the apps
concurrently.

Run a focused command while iterating:

| Area                     | Command                                                                                                                                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| JavaScript catalog       | `pnpm --dir packages/catalog test`                                                                                                                                                              |
| Public site              | `pnpm --dir apps/site test`                                                                                                                                                                     |
| Product docs             | `pnpm --dir apps/docs test`                                                                                                                                                                     |
| Python catalog loading   | `uv run --locked --package chartcoach pytest packages/chartcoach/tests/test_catalog_runtime.py`                                                                                                 |
| Python release building  | `uv run --locked --package chartcoach --extra curation pytest packages/chartcoach/tests/test_release_builder.py`                                                                                |
| Python MCP composition   | `uv run --locked --package chartcoach --all-extras pytest packages/chartcoach/tests/test_mcp_config.py packages/chartcoach/tests/test_mcp_http.py packages/chartcoach/tests/test_embeddings.py` |
| Chat app                 | `pnpm --dir apps/chat test`                                                                                                                                                                     |
| CI selection and gate    | `pnpm --filter @chartcoach/ci test`                                                                                                                                                             |
| Import and package rules | `pnpm check:architecture`                                                                                                                                                                       |

Tooling packages in `tools/ci`, `tools/architecture`, and `tools/release` own
their TypeScript scripts, dependencies, typechecks, and lint checks.
[Node.js runs TypeScript directly](https://nodejs.org/api/typescript.html),
so a script runs as `node tools/release/minimum-node.ts`. Tooling uses Node
module resolution and erasable TypeScript syntax. `pnpm ready` checks every
workspace package.

When a dependency changes, update the matching lockfile through `pnpm install`
or `uv lock`.

Published runtime dependencies use tested lower bounds. The lockfiles select
exact versions for development and CI. Set a lower bound from the APIs and
security fixes the package needs, and declare dependencies where they are
imported. Keep application and build-tool requirements scoped to their owners.
Review `pnpm update` edits to published package ranges separately from lockfile
updates so a dependency refresh preserves the tested lower bounds.

Run the Python consumer checks against the lowest compatible direct dependencies:

```bash
UV_PYTHON=3.10 make python-minimum
```

This builds the wheel, checks a minimum base installation, checks uvx MCP consumers through HTTP and stdio, then installs every
extra in the temporary environment and runs the package tests. Binary wheels
are required for third-party dependencies.
CI runs this check alongside the locked-version matrix. Exact embedding-profile
requirements describe the environment that produced stored vectors and remain
part of the catalog contract.

The normal `make python-build` gate also verifies the built wheel in an isolated
environment, launches it via `uvx`, and exercises dotenv, readiness, bearer auth,
and MCP requests through HTTP and stdio. It never needs an external model API.

## Keep shared data aligned

Python, JavaScript, the fixture, site, and chat read the same guideline and
release fields. Update the producer, readers, fixture, and public docs together
when those fields change.

Keep shared logos, fonts, and CSS variables in `packages/brand`. Import web
packages through their public package names. Add tests at the API, command,
file, or browser behavior that readers depend on.

## Validate

Run `pnpm check:unused` to find unused JavaScript and TypeScript files, exports,
and dependencies with [Knip](https://knip.dev/). The command generates the docs
collections before analysis and also runs through `pnpm ready`. Framework
plugins discover routes, build configuration, MDX, and tests. `knip.jsonc`
defines the root tooling scope. Keep public SDK entry points declared in
`package.json` exports and add precise entry patterns for code loaded by filename.

Run the full repository check before handoff:

```bash
make check
```

Add the check that matches the visible result:

| Change                           | Additional check                                        |
| -------------------------------- | ------------------------------------------------------- |
| Site page or generated site file | `make site-build` plus browser inspection               |
| Docs navigation or live example  | `make docs-build` plus browser inspection               |
| Python package contents          | Inspect the built wheel and source distribution         |
| JavaScript package contents      | Inspect `packages/catalog/dist` after its package build |
| Remote catalog selection         | Open the exact `release.json` through a public reader   |

## Open a pull request

Describe the supported behavior and the affected files. Include screenshots
for visible site or docs changes. List the commands that ran. When a check is
skipped, include the command, the reason, and the remaining risk.
