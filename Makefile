SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help

UV ?= uv
PNPM ?= pnpm
PYTHON := $(UV) run --locked --package chartcoach
PYTHON_ALL := $(PYTHON) --all-extras
PYTHON_PATH := packages/chartcoach

.PHONY: help install check python-check python-format python-lint python-typecheck python-test python-build python-minimum docs-build site-build

help: ## List development targets.
	@awk 'BEGIN {FS = ":.*## "} /^[a-zA-Z0-9_-]+:.*## / {printf "  %-18s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install locked JavaScript and Python workspaces.
	$(PNPM) install --frozen-lockfile
	$(UV) sync --locked --package chartcoach --all-groups --all-extras

check: ## Run every repository handoff gate.
	$(PNPM) ready
	$(MAKE) python-check
	git diff --check

python-check: python-format python-lint python-typecheck python-test python-build ## Check the Python package.

python-format:
	$(PYTHON) ruff format --check $(PYTHON_PATH)

python-lint:
	$(PYTHON) ruff check $(PYTHON_PATH)

python-typecheck:
	$(PYTHON_ALL) ty check $(PYTHON_PATH)

python-test:
	$(PYTHON_ALL) pytest $(PYTHON_PATH)/tests

python-build:
	$(UV) build --package chartcoach
	UV="$(UV)" $(PYTHON) python $(PYTHON_PATH)/tests/verify_built_package.py

python-minimum: python-build ## Test the built wheel with lowest compatible direct dependencies.
	UV="$(UV)" $(PYTHON) python $(PYTHON_PATH)/tests/verify_built_package.py --minimum-dependencies

docs-build: ## Build the product documentation.
	$(PNPM) --dir apps/docs build

site-build: ## Build the public catalog site.
	$(PNPM) --dir apps/site build
