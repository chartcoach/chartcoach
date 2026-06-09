# chartcoach

Python tools for the ChartCoach guideline catalog.

Install the ChartCoach skill once, then launch an agent with a startup prompt from the CLI:

```bash
npx skills add chartcoach/catalog
codex "$(uvx chartcoach@latest prompt --codex)"
```

Use `--claude` or `--opencode` for those agent CLIs. Pass `--task`, `--index`, and `--guidance-mode` when the agent needs task-specific catalog context.

The base package loads manifest-described catalog bundles, parses guidelines, and exposes typed records, Polars dataframe views, and native DuckDB SQL connections.

```python
from chartcoach import Catalog

catalog = Catalog.open()
catalog.guidelines().select("id", "title")

conn = catalog.duckdb()
conn.sql("select id, title from guidelines limit 5").pl()
conn.close()
```

Install `chartcoach[index]` when code needs a LanceDB table over catalog documents:

```python
from chartcoach.search import index, search

table = index(catalog, "scratch/chartcoach-index")

docs = (
    table.search("overplotted scatter plots", query_type="fts", fts_columns="text")
    .where("role = 'overview'")
    .limit(3)
    .to_list()
)

hits = search(catalog, table, "overplotted scatter plots").to_dict()["rows"]
```

`index(catalog, uri)` writes a LanceDB table over catalog documents at the path you provide and returns the native LanceDB `Table`. Without an embedding function it creates a full-text table over the `text` column. Pass any LanceDB embedding function instance when you want LanceDB to fill the `vector` column from `text`:

```python
from chartcoach.search import index

table = index(
    catalog,
    "scratch/chartcoach-index",
    embedding=embedding_function,
)
```

Use `open("scratch/chartcoach-index")` for an existing table. Use `documents(catalog)` when your code already owns a LanceDB connection and wants to call `db.create_table(...)` directly. Caller-owned tables should expose the catalog document columns `id`, `parent_id`, `role`, `labels`, `content_hash`, and `text`.

`model(embedding_function)` returns the LanceDB model used by `index(..., embedding=...)`. It defines `id`, `parent_id`, `role`, `labels`, `content_hash`, `text`, and `vector`, with `text` bound to `embedding_function.SourceField()` and `vector` bound to `embedding_function.VectorField()`.

Use DuckDB directly when notebooks, scripts, or agents need SQL joins over the derived catalog tables:

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

Write a DuckDB database file when another tool needs durable SQL tables:

```python
duckdb_path = "scratch/catalog.duckdb"
catalog.write_duckdb(duckdb_path, overwrite=True)
```

The LanceDB index root can also be attached through DuckDB's Lance extension:

```sql
INSTALL lance;
LOAD lance;
ATTACH 'scratch/chartcoach-index' AS cc_index (TYPE LANCE);

select id, parent_id, role
from cc_index.main.catalog_documents
limit 5;
```

Run the CLI with `uv run --package chartcoach chartcoach --help`.

These commands read the package-pinned default catalog artifact, inspect table schemas, write DuckDB tables, retrieve guideline evidence, and query indexed document rows.

```bash
chartcoach prompt --codex \
  --index scratch/chartcoach-index \
  --task "Review this dashboard for misleading bar axes."
chartcoach catalog manifest --format markdown
chartcoach tables list --format jsonl
chartcoach tables schema --format jsonl
chartcoach tables values guideline_labels label \
  --contains chart: --format jsonl
chartcoach sql \
  "select id, title from guidelines where list_contains(labels, 'chart:bar')" \
  --format jsonl
DUCKDB_PATH=scratch/catalog.duckdb
chartcoach catalog duckdb \
  --out "$DUCKDB_PATH"
duckdb "$DUCKDB_PATH" \
  -c "select id, title from guidelines where list_contains(labels, 'chart:bar')"
chartcoach guidelines retrieve \
  --label chart:bar --section advice --format jsonl
INDEX_PATH=scratch/chartcoach-index
chartcoach index --index "$INDEX_PATH"
chartcoach index --index "$INDEX_PATH" \
  documents \
  "overplotted scatter plot with too many points" \
  --limit 8
chartcoach guidelines search \
  --index "$INDEX_PATH" \
  --where "role = 'overview'" \
  "overplotted scatter plot with too many points" --format jsonl
```

Every row-oriented command supports `--format jsonl`, so shell tools can handle projection and token control:

```bash
chartcoach tables schema --format jsonl |
  jq 'select(.table == "sections")'
```

The default catalog comes from `https://artifacts.chartcoach.dev/metadata.json` and is cached under the user's platform cache directory. That object points to package-validated release metadata. Normal catalog reads download `MANIFEST.md` and `entries.parquet`; heavier derived artifacts such as LanceDB indexes stay described in metadata until a caller asks for them. `catalog duckdb` creates a DuckDB database file with the derived catalog tables. Use `tables list`, `tables schema`, and `tables values` before writing SQL against an unfamiliar catalog. `guidelines retrieve` returns deterministic catalog rows. `index documents` runs LanceDB search over indexed document rows. `guidelines search` deduplicates document matches to guideline-level typed rows.

Install `chartcoach[mcp]` for catalog-only MCP tools. Install both `chartcoach[mcp,index]` when agents will call search tools.

```bash
chartcoach mcp serve
```

Without an index, the MCP surface exposes only `sql`. Pass `--index` to also register `search` against an existing LanceDB table.

Run tests with `pnpm --dir packages/catalog-python test`.

## License

MIT. See [LICENSE](LICENSE).
