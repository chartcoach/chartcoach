PYTHON := uv run --locked --package chartcoach
PYTHON_ALL := $(PYTHON) --all-extras
PYTHON_PATH := packages/chartcoach

.PHONY: format lint typecheck test build

format:
	$(PYTHON) ruff format --check $(PYTHON_PATH)

lint:
	$(PYTHON) ruff check $(PYTHON_PATH)

typecheck:
	$(PYTHON_ALL) ty check $(PYTHON_PATH)

test:
	$(PYTHON_ALL) pytest $(PYTHON_PATH)/tests

build:
	uv build --package chartcoach
