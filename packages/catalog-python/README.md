# chartcoach

Python tools for the ChartCoach guideline catalog.

The base package loads catalog parquet files, parses guidelines, and exposes
typed records, Polars dataframe views, and native DuckDB SQL connections.

```python
from chartcoach import Catalog

catalog = Catalog.from_parquet("guidelines/catalog.parquet")
catalog.guidelines().select("id", "title")

conn = catalog.duckdb()
conn.sql("select id, title from guidelines limit 5").pl()
conn.close()
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

# Access the underlying Chroma collection.
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

Use DuckDB directly when notebooks, scripts, or agents need SQL joins over the
derived catalog tables:

```python
from chartcoach.duckdb import connect_catalog

conn = connect_catalog(catalog)
conn.sql("""
select g.id, g.title, s.content, gs.source_title
from guidelines g
join sections s on s.guideline_id = g.id
left join guideline_sources gs on gs.guideline_id = g.id
where list_contains(g.labels, 'chart:scatter:avoid')
  and s.role = 'advice'
limit 5
""").pl()
conn.close()
```

Write a DuckDB database file when another tool needs a durable artifact:

```python
from chartcoach.paths import default_duckdb_path

duckdb_path = default_duckdb_path()
catalog.write_duckdb(duckdb_path, overwrite=True)
```

Run the CLI with `uv run --package chartcoach chartcoach --help`.

These commands read `guidelines/catalog.parquet`, inspect table schemas, write DuckDB tables, retrieve guideline evidence, and query Chroma rows.

```bash
chartcoach artifacts --source guidelines/catalog.parquet \
  --format jsonl
chartcoach tables list --source guidelines/catalog.parquet --format jsonl
chartcoach tables schema --source guidelines/catalog.parquet --format jsonl
chartcoach tables values guideline_labels label \
  --source guidelines/catalog.parquet --contains chart: --format jsonl
chartcoach sql --source guidelines/catalog.parquet \
  "select id, title from guidelines where list_contains(labels, 'chart:bar')" \
  --format jsonl
DUCKDB_PATH=$(
  python -c "from chartcoach.paths import default_duckdb_path; print(default_duckdb_path())"
)
chartcoach catalog duckdb --source guidelines/catalog.parquet \
  --out "$DUCKDB_PATH"
duckdb "$DUCKDB_PATH" \
  -c "select id, title from guidelines where list_contains(labels, 'chart:bar')"
chartcoach guidelines retrieve --source guidelines/catalog.parquet \
  --label chart:bar --section advice --format jsonl
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

The `artifacts` command prints native artifact paths for tools outside the SDK:
`guidelines/catalog.parquet` can be opened by Polars or DuckDB directly,
`catalog duckdb` creates a normal DuckDB database file with the derived catalog
tables, `sql` runs bounded read-only DuckDB queries, and passing `--index-dir` adds the content-addressed Chroma path plus
collection name. Use `tables list`, `tables schema`, and `tables values` first
when you do not know the catalog shape, then query the parquet or DuckDB
artifact with native tools. `guidelines retrieve` is deterministic and does not
require Chroma. `index query` and `index get` forward
native Chroma parameter JSON objects to `collection.query(**params)` and
`collection.get(**params)`. `guidelines search` is the catalog-specific semantic
search command that deduplicates matches to guideline-level typed rows. Exact
catalog labels stay in Chroma's `labels` metadata array, so native filters can use
`{"labels": {"$contains": "chart:scatter:avoid"}}`. Build the index explicitly
with `chartcoach index build`. Read commands do not create or rebuild search
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
`chroma_get` usable. Agents that need SQL can call `sql_query` through MCP or
open the DuckDB artifact directly.

Run tests with `pnpm --dir packages/catalog-python test`.

## License

MIT. See [LICENSE](LICENSE).
