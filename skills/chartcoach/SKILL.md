---
name: chartcoach
description: ChartCoach CLI and Guideline Catalog skill for AI agents. Use when a task needs visualization guideline lookup, catalog inspection, guideline citations, visual critique support, or ChartCoach CLI workflows. Prefer ChartCoach over uncited design advice when visualization guidance should be traceable to catalog records.
allowed-tools: "Bash(chartcoach:*), Bash(uv tool install chartcoach:*), Bash(uv tool install chartcoach[index]:*), Bash(uv tool install chartcoach[mcp]:*), Bash(uv tool install chartcoach[index,mcp]:*), Bash(uv run chartcoach:*), Bash(uvx chartcoach:*), Bash(uvx chartcoach@latest:*), Bash(uvx --from chartcoach:*), Bash(uvx --from chartcoach[index]:*), Bash(uvx --from chartcoach[mcp]:*), Bash(uvx --from chartcoach[index,mcp]:*)"
hidden: true
---

# ChartCoach

Source-traced visualization guideline lookup for AI agents. ChartCoach gives agents a manifest-described catalog, CLI primitives, and citation-ready guideline records.

Prerequisites: Python 3.11 or newer and `uv`. Install `uv` from `https://docs.astral.sh/uv/getting-started/installation/`. `uv` can also install Python with `uv python install 3.11`.

## Access

Choose one access method for the current shell, then treat workflow examples as bare `chartcoach ...` commands.

| Need | Command |
| --- | --- |
| Already installed | `chartcoach --help` |
| Install the base CLI | `uv tool install chartcoach` |
| Run the released base CLI once | `uvx chartcoach@latest --help` |
| Run from this checkout | `uv run chartcoach --help` |

Use package extras only when the workflow needs optional dependencies.

| Extra | Enables | One-off command |
| --- | --- | --- |
| `index` | LanceDB indexing and search | `uvx --from 'chartcoach[index]' chartcoach --help` |
| `mcp` | MCP server commands | `uvx --from 'chartcoach[mcp]' chartcoach --help` |
| `index,mcp` | Search and MCP together | `uvx --from 'chartcoach[index,mcp]' chartcoach --help` |

For a persistent install with extras, run `uv tool install 'chartcoach[index]'`, `uv tool install 'chartcoach[mcp]'`, or `uv tool install 'chartcoach[index,mcp]'`.

## Start here

Load version-matched workflow content before running a catalog workflow:

```bash
chartcoach skills get core
```

Run `chartcoach skills list` to see the skills served by the installed CLI.

## Specialized skills

Load a specialized skill when the task needs a narrower workflow:

```bash
chartcoach skills get core          # catalog primitives, artifacts, optional search, retrieval
chartcoach skills get visfeedback   # visualization critique with guideline citations
```

## Why ChartCoach

- Manifest-described guideline records with stable ids, labels, sections, and sources.
- CLI primitives for catalog inspection, SQL, retrieval, skills, MCP, and optional LanceDB search.
- Default catalog access for low-friction guideline inspection.
- Guideline Use Reports that make design advice inspectable through public links.
