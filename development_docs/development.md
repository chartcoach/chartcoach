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

| Command      | Contract                                               |
| ------------ | ------------------------------------------------------ |
| `pnpm ready` | Format, lint, typecheck, test, and build the workspace |
| `pnpm dev`   | Start the site and docs app through portless           |

Use a package-native command for a focused loop:

```sh
pnpm --dir apps/site dev
pnpm --dir apps/site test
pnpm --dir apps/site typecheck
pnpm --dir packages/catalog test
```

The workspace gate supplies `fixtures/catalog-release` to site typechecks and
static builds.

## Python

| Command          | Contract                                       |
| ---------------- | ---------------------------------------------- |
| `make format`    | Check Ruff formatting                          |
| `make lint`      | Run Ruff lint rules                            |
| `make typecheck` | Run ty with package extras                     |
| `make test`      | Run the Python test suite with package extras  |
| `make build`     | Build the Python source distribution and wheel |

Run all Python gates before handing off a package change:

```sh
make format lint typecheck test build
```

Use uv directly for a focused test:

```sh
uv run --locked --package chartcoach --extra curation \
  pytest packages/chartcoach/tests/test_release_builder.py
```

## Handoff

Run the narrow command during iteration and the complete workspace gate before
handoff. For a cross-language catalog change, run `pnpm ready` and all Python
Make gates. Include the exact failing command when an environment blocks a
gate.
