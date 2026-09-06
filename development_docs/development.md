# Development workflow

Run workspace commands from the repository root. Vite+ owns JavaScript
formatting, linting, tests, and task orchestration. uv owns the Python workspace.

## Install

```sh
pnpm install
uv sync --locked --package chartcoach --all-groups --all-extras
```

`.node-version` selects the Node runtime. `.python-version` selects Python 3.12
for local Python tooling.

## JavaScript and web apps

| Command          | Contract                                     |
| ---------------- | -------------------------------------------- |
| `pnpm check`     | Check formatting and type-aware lint rules   |
| `pnpm typecheck` | Typecheck packages and both web apps         |
| `pnpm test`      | Run package test suites                      |
| `pnpm build`     | Build packages and both web apps             |
| `pnpm ready`     | Run every JavaScript check, test, and build  |
| `pnpm dev`       | Start the site and docs app through portless |

Use a package-native command for a focused loop:

```sh
pnpm --dir apps/site dev
pnpm --dir apps/site test
pnpm --dir apps/site typecheck
pnpm --dir packages/catalog test
```

Site typechecks and static builds use `fixtures/catalog-release` by default.
Set `CHARTCOACH_SITE_CATALOG_SOURCE` to build against an exact HTTP release
descriptor.

## Python

| Command                 | Contract                                       |
| ----------------------- | ---------------------------------------------- |
| `make python-format`    | Check Ruff formatting                          |
| `make python-lint`      | Run Ruff lint rules                            |
| `make python-typecheck` | Run ty with package extras                     |
| `make python-test`      | Run the Python test suite with package extras  |
| `make python-build`     | Build the Python source distribution and wheel |
| `make python-check`     | Run every Python check, test, and build        |

Run the Python gate before handing off a Python package change:

```sh
make python-check
```

Use uv directly for a focused test:

```sh
uv run --locked --package chartcoach --extra curation \
  pytest packages/chartcoach/tests/test_release_builder.py
```

## Handoff

Run the narrow command during iteration and the complete repository gate before
handoff:

```sh
make check
```

Include the exact failing command when an environment blocks a gate.
