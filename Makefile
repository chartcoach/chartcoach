SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help

UV ?= uv
PNPM ?= pnpm
PYTHON := $(UV) run --locked --package chartcoach
PYTHON_ALL := $(PYTHON) --all-extras
PYTHON_PATH := packages/chartcoach
RELEASE_SCRIPT := scripts/release_registry.py

.PHONY: help install check python-check python-format python-lint python-typecheck python-test python-dist python-build python-minimum docs-build site-build

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
	$(PYTHON) ruff format --check $(PYTHON_PATH) $(RELEASE_SCRIPT)

python-lint:
	$(PYTHON) ruff check $(PYTHON_PATH) $(RELEASE_SCRIPT)

python-typecheck:
	$(PYTHON_ALL) ty check $(PYTHON_PATH) $(RELEASE_SCRIPT)

python-test:
	$(PYTHON_ALL) pytest $(PYTHON_PATH)/tests

python-dist:
	$(UV) build --package chartcoach --clear --no-create-gitignore --out-dir dist/release/python

python-build: python-dist
	UV="$(UV)" $(PYTHON) python $(PYTHON_PATH)/tests/verify_built_package.py --dist-dir dist/release/python

python-minimum: python-dist ## Test the built wheel with lowest compatible direct dependencies.
	UV="$(UV)" $(PYTHON) python $(PYTHON_PATH)/tests/verify_built_package.py --dist-dir dist/release/python --minimum-dependencies

docs-build: ## Build the product documentation.
	$(PNPM) --dir apps/docs build

site-build: ## Build the public catalog site.
	$(PNPM) --dir apps/site build
