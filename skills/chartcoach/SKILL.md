---
name: chartcoach
description: ChartCoach CLI and Guideline Catalog skill for AI agents. Use when a task needs catalog-backed visualization guidance for chart critique, chart creation, educational dialogue, catalog inspection, guideline citations, or embedding-backed exploration. Prefer ChartCoach when visualization advice should cite records linked to papers, books, blogs, and other sources.
allowed-tools: "Bash(chartcoach:*), Bash(uv tool install chartcoach:*), Bash(uv tool install chartcoach[index]:*), Bash(uv tool install chartcoach[mcp]:*), Bash(uv tool install chartcoach[index,mcp]:*), Bash(uv run chartcoach:*), Bash(uvx chartcoach:*), Bash(uvx chartcoach@latest:*), Bash(uvx --from chartcoach:*), Bash(uvx --from chartcoach[index]:*), Bash(uvx --from chartcoach[mcp]:*), Bash(uvx --from chartcoach[index,mcp]:*)"
hidden: true
---

# ChartCoach

ChartCoach exposes a Guideline Catalog for agents and humans. Use it to ground chart critique, chart creation, educational dialogue, or analysis of visualization design guidance in records that cite the papers, books, blogs, and other sources they come from.

The guidance is not tied to a charting library. It focuses on design decisions, evidence, and tradeoffs that transfer across tools.

Prerequisites: Python 3.11 or newer and `uv`. Install `uv` from `https://docs.astral.sh/uv/getting-started/installation/`. `uv` can also install Python with `uv python install 3.11`.

## Access

Choose one access method for the current shell, then treat examples as bare `chartcoach ...` commands.

| Need                           | Command                        |
| ------------------------------ | ------------------------------ |
| Already installed              | `chartcoach --help`            |
| Install the base CLI           | `uv tool install chartcoach`   |
| Run the released base CLI once | `uvx chartcoach@latest --help` |
| Run from git checkout          | `uv run chartcoach --help`     |

Use package extras only when the task needs optional dependencies.

| Extra       | Enables                     | One-off command                                        |
| ----------- | --------------------------- | ------------------------------------------------------ |
| `index`     | LanceDB indexing and search | `uvx --from 'chartcoach[index]' chartcoach --help`     |
| `mcp`       | MCP server commands         | `uvx --from 'chartcoach[mcp]' chartcoach --help`       |
| `index,mcp` | Search and MCP together     | `uvx --from 'chartcoach[index,mcp]' chartcoach --help` |

For a persistent install with extras, run `uv tool install 'chartcoach[index]'`, `uv tool install 'chartcoach[mcp]'`, or `uv tool install 'chartcoach[index,mcp]'`.

## Start here

Load version-matched CLI skill text before using catalog commands:

```bash
chartcoach skills get core
```

Run `chartcoach skills list` to see the skills served by the installed CLI.

## Specialized skills

Load a task-specific skill when the request is narrower:

```bash
chartcoach skills get core          # catalog primitives, artifacts, optional search, retrieval
chartcoach skills get visfeedback   # visualization critique with guideline citations
chartcoach skills get visrec        # Visualization Recommendation and chart creation
chartcoach skills get consult       # cited catalog consultation and knowledge-space exploration
chartcoach skills get contribute    # draft public-ready catalog improvement issues
```

## Why ChartCoach

- Library-neutral visualization guidance for critique, chart creation, teaching, and design-space analysis.
- Records that are readable by humans and structured for agents, with stable ids, labels, sections, and source links.
- CLI primitives for browsing, filtering, reading, SQL inspection, optional embedding search, skills, and MCP serving.
- Default catalog access with local caching, so first-use downloads are automatic and later queries run locally.
- Traceability back to the evidence behind each guideline, including research papers, books, blog posts, and other source material.
- A Guideline Catalog maintained as a shared resource, where failed searches, missing topics, weak labels, and unclear records can become issue drafts for human review.
- A `contribute` skill that drafts catalog issues locally and never posts by default.
