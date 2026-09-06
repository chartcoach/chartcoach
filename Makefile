PYTHON := uv run --locked --package chartcoach
PYTHON_ALL := $(PYTHON) --all-extras
PYTHON_PATH := packages/chartcoach

.PHONY: check python-check python-format python-lint python-typecheck python-test python-build

check:
	pnpm ready
	$(MAKE) python-check
	git diff --check

python-check: python-format python-lint python-typecheck python-test python-build

python-format:
	$(PYTHON) ruff format --check $(PYTHON_PATH)

python-lint:
	$(PYTHON) ruff check $(PYTHON_PATH)

python-typecheck:
	$(PYTHON_ALL) ty check $(PYTHON_PATH)

python-test:
	$(PYTHON_ALL) pytest $(PYTHON_PATH)/tests

python-build:
	uv build --package chartcoach
