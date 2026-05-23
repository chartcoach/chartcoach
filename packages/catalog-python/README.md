# chartcoach

Python tools for the ChartCoach guideline catalog.

The base package is deliberately small. It loads catalog parquet files, parses
guidelines, and exposes typed records plus Polars dataframe views.

```python
from chartcoach import Catalog

catalog = Catalog.from_parquet("guidelines/catalog.parquet")
catalog.frames.guidelines.select("id", "title")
```

Install `chartcoach[search]` when you need the optional retrieval stack:

```python
from chartcoach.search import ChromaIndex, connect_catalog

index = ChromaIndex.from_cache(catalog)
conn = connect_catalog(catalog, search=index)
```

Run the CLI with `uv run --package chartcoach chartcoach --help`.

Useful catalog commands:

```bash
chartcoach catalog --catalog guidelines/catalog.parquet relations --format jsonl
chartcoach catalog --catalog guidelines/catalog.parquet schema --format jsonl
chartcoach catalog --catalog guidelines/catalog.parquet values \
  guideline_labels label --format jsonl
chartcoach catalog --catalog guidelines/catalog.parquet values \
  sections role --format jsonl
chartcoach catalog --catalog guidelines/catalog.parquet sql \
  "select id, title from guidelines where list_contains(labels, 'chart:bar')"
chartcoach catalog --catalog guidelines/catalog.parquet retrieve \
  --label chart:bar --format jsonl
chartcoach catalog --catalog guidelines/catalog.parquet search \
  "overplotted scatter plot with too many points" --format jsonl
```

Every row-oriented command supports `--format jsonl`, so shell tools can handle
projection and token control:

```bash
chartcoach catalog --catalog guidelines/catalog.parquet schema --format jsonl |
  jq 'select(.relation == "sections")'
```

Use `relations`, `schema`, and `values` first when you do not know the catalog
shape. `retrieve` is deterministic and does not require Chroma. `search` uses
the optional Chroma index and returns guideline-level hits by default; pass
`--level document` to inspect raw indexed documents and Chroma metadata.

The MCP server exposes the catalog and search commands as agent tools:

```bash
chartcoach mcp --catalog-path guidelines/catalog.parquet \
  --cache-dir .cache/chartcoach --cache-mode reuse_only
```

Use `reuse_only` in deployed servers so catalog tools can start without mutating
cache state and search tools fail if the Chroma cache is missing or stale. Use
`chartcoach catalog search --cache-mode reuse_or_create` locally when you want
ChartCoach to build or refresh the cache before serving it over MCP. The MCP
tool surface includes `relations`, `schema`, `values`,
`list_guidelines`, `get_guideline`, `retrieve_guidelines`, `sql`, `search`,
`search_guidelines`, and `get`.

Run tests with `pnpm --dir packages/catalog-python test`.

## License

MIT. See [LICENSE](LICENSE).
