---
name: chartcoach
description: ChartCoach CLI and Guideline Catalog skill for AI agents. Use when a task needs visualization guideline lookup, catalog inspection, guideline citation, visual critique support, LanceDB indexing, or ChartCoach CLI workflows. Start here before using ChartCoach primitives directly.
allowed-tools: "Bash(uv run chartcoach:*), Bash(chartcoach:*), Bash(uvx chartcoach:*), Bash(uvx --from chartcoach:*), Bash(uvx --from chartcoach[index]:*), Bash(uvx --from chartcoach[mcp]:*), Bash(uvx --from chartcoach[index,mcp]:*)"
hidden: true
---

# ChartCoach

Source-traced visualization guideline lookup for AI agents. Use the CLI-served skills for version-matched workflows and command examples.

## Prerequisites

ChartCoach requires Python 3.11 or newer and `uv`.

Install `uv` first if it is missing:

```text
https://docs.astral.sh/uv/getting-started/installation/
```

## Start here

This file is the stable repo-level discovery stub. It is not bundled into the Python wheel and is not served by `chartcoach skills get`.

Load the versioned workflow content from the ChartCoach CLI before running a real catalog workflow:

```bash
uv run chartcoach skills get core
uv run chartcoach skills get core --full
uv run chartcoach skills get visfeedback
uvx chartcoach skills get core
```

The CLI-served skills live under `packages/catalog-python/data/skill-data` and are packaged with `chartcoach` wheel releases. Use `chartcoach skills get <name>` so workflow text matches the installed package version.

Do not run `chartcoach skills get chartcoach`. This file is the parent skill that points to CLI-served skills. The CLI serves specialized skills such as `core` and `visfeedback`.

## Specialized skills

Load a specialized CLI-served skill when the task calls for it:

```bash
uv run chartcoach skills get core          # catalog primitives, setup, artifacts, tables, SQL, indexing, retrieval
uv run chartcoach skills get visfeedback   # visual critique workflow with guideline citations
uvx chartcoach skills list                 # list CLI-served skills from a released package
```

Run `uv run chartcoach --help` or `uvx chartcoach --help` for the primitive command surface. The help should stay lean. Procedural workflow belongs in CLI-served skills.
