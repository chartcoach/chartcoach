# Contributing

Run commands from the repository root. Install the locked JavaScript and
Python workspaces with:

```bash
make install
```

The workspace selects Node through `engines.node` in `package.json` and Python
through `.python-version`. The published Python package supports Python 3.11
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

Start both web apps with:

```bash
pnpm dev
```

[Portless](https://github.com/vercel-labs/portless) assigns each app an
available local port and prints its local URL. With the default proxy settings,
the primary checkout uses `https://chartcoach.localhost` and
`https://docs.chartcoach.localhost`. Linked
[Git worktrees](https://git-scm.com/docs/git-worktree) receive a subdomain
derived from the branch name, which lets several worktrees run both apps
concurrently.

Run a focused command while iterating:

| Area                     | Command                                                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| JavaScript catalog       | `pnpm --dir packages/catalog test`                                                                               |
| Public site              | `pnpm --dir apps/site test`                                                                                      |
| Product docs             | `pnpm --dir apps/docs test`                                                                                      |
| Python catalog loading   | `uv run --locked --package chartcoach pytest packages/chartcoach/tests/test_catalog_runtime.py`                  |
| Python release building  | `uv run --locked --package chartcoach --extra curation pytest packages/chartcoach/tests/test_release_builder.py` |
| Import and package rules | `pnpm check:architecture`                                                                                        |

When a dependency changes, update the matching lockfile through `pnpm install`
or `uv lock`.

## Keep shared data aligned

Python, JavaScript, the fixture, and both web apps read the same guideline and
release fields. Update the producer, readers, fixture, and public docs together
when those fields change.

Keep shared logos, fonts, and CSS variables in `packages/brand`. Import web
packages through their public package names. Add tests at the API, command,
file, or browser behavior that readers depend on.

## Validate

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
