PYTHON_PACKAGE := chartcoach
PYTHON_PATH := packages/catalog-python
JS_FILTERS := --filter @chartcoach/site --filter @chartcoach/docs --filter @chartcoach/brand --filter @chartcoach/catalog
ROOT_FORMAT_FILES := package.json pnpm-workspace.yaml .github/workflows/ci.yml .github/workflows/publish.yml

export PATH := $(CURDIR)/node_modules/.bin:$(PATH)

.PHONY: js-format-check js-lint js-typecheck js-test js-build
.PHONY: py-format-check py-lint py-typecheck py-test py-build

js-format-check:
	pnpm exec oxfmt --check $(ROOT_FORMAT_FILES)
	pnpm -r $(JS_FILTERS) --if-present format:check

js-lint:
	pnpm -r $(JS_FILTERS) --if-present lint

js-typecheck:
	pnpm -r $(JS_FILTERS) --if-present typecheck

js-test:
	pnpm -r $(JS_FILTERS) --if-present test

js-build:
	pnpm -r $(JS_FILTERS) --if-present build

py-format-check:
	uv run --package $(PYTHON_PACKAGE) ruff format --check $(PYTHON_PATH)

py-lint:
	uv run --package $(PYTHON_PACKAGE) ruff check $(PYTHON_PATH)

py-typecheck:
	uv run --package $(PYTHON_PACKAGE) --extra index --extra mcp ty check $(PYTHON_PATH)
	uv run --package $(PYTHON_PACKAGE) --extra index --extra mcp pyrefly check --summary=none

py-test:
	uv run --package $(PYTHON_PACKAGE) --extra index --extra mcp pytest $(PYTHON_PATH)/tests

py-build:
	uv build --package $(PYTHON_PACKAGE)
