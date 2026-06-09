---
name: core
description: Load this before using ChartCoach. Explains catalog artifacts, manifests, tables, guideline records, indexing, search, and the CLI primitives agents should combine.
---

# ChartCoach Core

ChartCoach exposes a versioned Guideline Catalog and CLI primitives for inspecting, indexing, retrieving, and searching visualization guidance. Load this skill before using `chartcoach` commands.

## Environment

ChartCoach requires Python 3.11 or newer. `uv` is the expected runner for local checkout and one-off `uvx` usage.

If `uv` is not installed, install it first:

```text
https://docs.astral.sh/uv/getting-started/installation/
```

After `uv` is installed, it can install and manage Python versions:

```sh
uv python install 3.11
```

Choose one command prefix for the current environment:

| Context | Command prefix | Use |
| --- | --- | --- |
| Local checkout | `uv run chartcoach` | Develop or test this repository. |
| Installed package | `chartcoach` | Use an installed ChartCoach CLI. |
| One-off base CLI | `uvx chartcoach` | Run package commands without installing. |
| One-off search CLI | `uvx --from 'chartcoach[index]' chartcoach` | Include LanceDB for indexing and search. |
| One-off MCP CLI | `uvx --from 'chartcoach[mcp]' chartcoach` | Include the MCP server dependency. |
| One-off full CLI | `uvx --from 'chartcoach[index,mcp]' chartcoach` | Include both search and MCP extras. |

Base commands include catalog inspection, table inspection, SQL, prompt output, guideline list/show/retrieve, and `skills`. Search index commands require the `index` extra. MCP commands require the `mcp` extra.

## Extras

| Extra | Enables | Example |
| --- | --- | --- |
| none | Catalog inspection, tables, SQL, prompts, CLI-served skills, guideline records. | `uvx chartcoach skills get core` |
| `index` | LanceDB indexing, full-text search, vector search, hybrid search, embedding-function options. | `uvx --from 'chartcoach[index]' chartcoach index --help` |
| `mcp` | MCP server commands. | `uvx --from 'chartcoach[mcp]' chartcoach mcp serve --help` |
| `index,mcp` | Search and MCP in one tool environment. | `uvx --from 'chartcoach[index,mcp]' chartcoach --help` |

## Catalog Artifacts

Start by finding the catalog source:

```sh
chartcoach catalog manifest --format json
chartcoach tables list
```

Omit `--source` to use the package-pinned default catalog from `https://artifacts.chartcoach.dev/metadata.json`. The CLI resolves that pointer to a versioned release and caches the manifest plus entries artifacts locally. Set `CHARTCOACH_SOURCE` or pass `--source` only when the user provides a custom catalog locator. A custom catalog can be an authored guideline folder with `entries/`, a catalog bundle, or a metadata URL. The manifest defines section roles, label families, table contracts, and supported vocabulary for the current catalog. Read the manifest before filtering by labels or section roles.

## Guideline Records

Guidelines have stable ids, titles, descriptions, labels, source-backed sections, references, and serialized body text. Treat ids as the citation anchor. Treat labels and section roles as catalog-defined data, not global constants.

Use these commands to inspect records:

```sh
chartcoach guidelines list --contains "axis"
chartcoach guidelines show <guideline-id>
chartcoach guidelines retrieve --id <guideline-id> --section <role-from-manifest>
```

Guideline ids are exact. Copy them from `guidelines list` or `guidelines search --format compact` before running `show` or `retrieve`. Do not derive ids from titles or snippets.

## Tables And SQL

Use table primitives when you need exact schema, valid values, counts, or joins:

```sh
chartcoach tables schema
chartcoach tables values sections role
chartcoach tables values guideline_labels label
chartcoach tables values guideline_labels label --contains axis
chartcoach sql "select id, title from guidelines limit 5"
```

## Search Index

`chartcoach index` creates a LanceDB table from catalog document rows. A full-text index works without embeddings:

```sh
chartcoach index --index ./chartcoach-index
chartcoach guidelines search --index ./chartcoach-index --mode fts --format compact "direct labels line chart exact lookup"
chartcoach index --index ./chartcoach-index documents "direct labels" --mode fts --format json
```

Vector and hybrid search require a LanceDB embedding function. Use LanceDB-native embedding aliases and options:

```sh
chartcoach index --index ./chartcoach-index --embedding sentence-transformers --embedding-option name=all-MiniLM-L6-v2
chartcoach guidelines search --index ./chartcoach-index --mode hybrid --format compact "direct labels line chart exact lookup"
chartcoach index --index ./chartcoach-index documents "direct labels" --mode hybrid --format json
```

Embedding options are passed to LanceDB's embedding function `create()` call. Do not invent a ChartCoach embedding model layer.

Search output reports indexed document roles. Values such as `overview`, `document`, or `section.check` explain where the match came from in the index. `guidelines retrieve --section` accepts manifest section roles, such as `check`, not the indexed `section.` prefix.

## Agent Rules

- Use manifest and table commands to learn valid labels and section roles.
- Use `guidelines search --format compact` for discovery. Copy exact ids from the compact output, then use `guidelines show` or `retrieve` for citation-ready detail.
- Use `tables values --contains TEXT` when the visible value list is too broad.
- Keep searches task-specific: chart family, data type, visual encoding, reader task, failure mode, and interaction state.
- Reject adjacent hits when the top result is scoped to a different chart family, reader task, or data type. Search again with sharper observed terms.
- If search fails with a missing `--index`, build a local full-text index and retry with `--mode fts`.
- Prefer JSON or JSONL for machine parsing, `compact` for citation triage, and full Markdown when you need section text.
