# chartcoach

Python tools for the ChartCoach guideline catalog.

The base package is deliberately small. It loads catalog parquet files, parses
guidelines, and exposes typed records plus Polars dataframe views.

```python
from chartcoach import Catalog

catalog = Catalog.from_parquet("guidelines/catalog.parquet")
catalog.guidelines().select("id", "title")
```

Install `chartcoach[search]` when you need the optional Chroma retrieval stack:

```python
from chartcoach.search import ChromaIndex, search_guidelines
from chartcoach.paths import default_index_dir

# Build once with `chartcoach index build`, then open the artifact read-only.
index = ChromaIndex.from_cache(
    catalog,
    cache_dir=default_index_dir(),
    cache_mode="reuse_only",
)

# Native Chroma stays exposed.
index.collection.query(
    query_texts=["overplotted scatter plots"],
    n_results=3,
    where={"labels": {"$contains": "chart:scatter:avoid"}},
)

# `search_guidelines` returns typed guideline-level hits.
search_guidelines(
    index,
    "overplotted scatter plots",
    where={"labels": {"$contains": "chart:scatter:avoid"}},
).rows
```

Install `chartcoach[duckdb]` when you want a DuckDB database with the derived
catalog tables:

```python
import duckdb
from chartcoach.duckdb import write_duckdb
from chartcoach.paths import default_duckdb_path

duckdb_path = default_duckdb_path()
write_duckdb(catalog, duckdb_path, overwrite=True)
conn = duckdb.connect(duckdb_path)
conn.execute("select id, title from guidelines limit 5").fetchall()
```

Run the CLI with `uv run --package chartcoach chartcoach --help`.

Useful catalog commands:

```bash
chartcoach artifacts --source guidelines/catalog.parquet \
  --format jsonl
chartcoach tables list --source guidelines/catalog.parquet --format jsonl
chartcoach tables schema --source guidelines/catalog.parquet --format jsonl
chartcoach tables values guideline_labels label \
  --source guidelines/catalog.parquet --contains chart: --format jsonl
DUCKDB_PATH=$(
  python -c "from chartcoach.paths import default_duckdb_path; print(default_duckdb_path())"
)
chartcoach catalog duckdb --source guidelines/catalog.parquet \
  --out "$DUCKDB_PATH"
duckdb "$DUCKDB_PATH" \
  -c "select id, title from guidelines where list_contains(labels, 'chart:bar')"
chartcoach guidelines retrieve --source guidelines/catalog.parquet \
  --label chart:bar --section advice --format jsonl
chartcoach feedback prompt --source guidelines/catalog.parquet \
  --image path/to/chart.jpg \
  --situation "Review this chart for a quick public-facing comparison." \
  --label-prefix chart:bar --section advice --format markdown
INDEX_DIR=$(
  python -c "from chartcoach.paths import default_index_dir; print(default_index_dir())"
)
chartcoach index build --source guidelines/catalog.parquet --index-dir "$INDEX_DIR"
chartcoach index status --source guidelines/catalog.parquet \
  --index-dir "$INDEX_DIR" --format jsonl
chartcoach index query --source guidelines/catalog.parquet \
  --index-dir "$INDEX_DIR" \
  '{
    "query_texts": ["overplotted scatter plot with too many points"],
    "n_results": 8,
    "where": {"labels": {"$contains": "chart:scatter:avoid"}},
    "include": ["documents", "metadatas", "distances"]
  }'
chartcoach guidelines search --source guidelines/catalog.parquet \
  --index-dir "$INDEX_DIR" \
  --where '{"labels":{"$contains":"chart:scatter:avoid"}}' \
  "overplotted scatter plot with too many points" --format jsonl
```

Every row-oriented command supports `--format jsonl`, so shell tools can handle
projection and token control:

```bash
chartcoach tables schema --source guidelines/catalog.parquet --format jsonl |
  jq 'select(.table == "sections")'
```

Use `artifacts` when you want the underlying files instead of the SDK:
`guidelines/catalog.parquet` can be opened by Polars or DuckDB directly,
`catalog duckdb` creates a normal DuckDB database file with the derived catalog
tables, and passing `--index-dir` adds the content-addressed Chroma path plus
collection name. Use `tables list`, `tables schema`, and `tables values` first
when you do not know the catalog shape, then query the parquet or DuckDB
artifact with native tools. `guidelines retrieve` and `feedback prompt` are
deterministic and do not require Chroma. `index query` and `index get` forward
native Chroma parameter JSON objects to `collection.query(**params)` and
`collection.get(**params)`. `guidelines search` is the catalog-specific semantic
search command that deduplicates matches to guideline-level typed rows. Exact
catalog labels stay in Chroma's `labels` metadata array, so native filters can use
`{"labels": {"$contains": "chart:scatter:avoid"}}`. Build the index explicitly
with `chartcoach index build`; read commands do not create or rebuild search
state.

Install `chartcoach[mcp]` for catalog-only MCP tools. Install both
`chartcoach[mcp,search]` when agents will call Chroma-backed tools.

The MCP server exposes catalog tools without requiring a Chroma index:

```bash
chartcoach mcp serve --source guidelines/catalog.parquet
```

The MCP surface exposes deterministic catalog tools plus direct Chroma access:
`catalog_artifacts`, `tables_list`, `tables_schema`, `tables_values`,
`guidelines_list`, `guidelines_get`, `guidelines_retrieve`,
`guidelines_search`, `chroma_query`, and `chroma_get`. `chroma_query` calls
`collection.query(**params)` and `chroma_get` calls `collection.get(**params)`.
Pass `--index-dir` to make `guidelines_search`, `chroma_query`, and
`chroma_get` usable. Agents that need SQL should use `catalog_artifacts` and
open the DuckDB artifact directly.

Run tests with `pnpm --dir packages/catalog-python test`.

## License

MIT. See [LICENSE](LICENSE).
