# chartcoach

Python tools for the ChartCoach guideline catalog.

For agent use, install the ChartCoach skill once, then ask the current agent to use it:

```bash
npx skills add chartcoach/chartcoach --skill chartcoach
codex 'Use $chartcoach to access visualization design guidelines. Start by giving me a thematic overview of the catalog.'
```

The skill points agents to version-matched CLI-served skills. The CLI exposes catalog primitives, and task guidance lives in `chartcoach skills get <name>`.

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

Use `open("scratch/chartcoach-index")` for an existing table. Use `chartcoach.search.lance.documents(catalog)` when your code already owns a LanceDB connection and wants to call `db.create_table(...)` directly. Caller-owned tables should expose the catalog document columns `id`, `parent_id`, `role`, `labels`, `content_hash`, and `text`.

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

Run the CLI with `chartcoach --help`.

These commands read the package-pinned default catalog artifact, inspect table schemas, write DuckDB tables, read guideline sections, and query indexed guideline rows.

```bash
chartcoach catalog manifest --format markdown
chartcoach catalog schema --tables --row-counts --format jsonl
chartcoach catalog schema guidelines --format jsonl
chartcoach catalog values labels \
  --contains chart: --format jsonl
chartcoach catalog sql \
  "select id, title from guidelines where list_contains(labels, 'chart:bar')" \
  --format jsonl
DUCKDB_PATH=scratch/catalog.duckdb
chartcoach catalog export duckdb \
  --out "$DUCKDB_PATH"
duckdb "$DUCKDB_PATH" \
  -c "select id, title from guidelines where list_contains(labels, 'chart:bar')"
chartcoach catalog query \
  --label chart:bar --format jsonl
chartcoach catalog read <guideline-id> \
  --section <role-from-manifest> --source-detail minimal --format jsonl
chartcoach catalog cite <guideline-id> \
  --format markdown
INDEX_PATH=scratch/chartcoach-index
chartcoach catalog index create --index "$INDEX_PATH"
chartcoach catalog find \
  --index "$INDEX_PATH" \
  --where "role = 'overview'" \
  "overplotted scatter plot with too many points" --format jsonl
```

Every row-oriented command supports `--format jsonl`, so shell tools can handle projection and token control. Human `table` output uses rounded, wrapped columns for terminal scanning. JSON, JSONL, and CSV keep machine-readable stdout.

```bash
chartcoach catalog schema --format jsonl |
  jq 'select(.table == "sections")'
```

The default catalog comes from package-pinned release metadata under `https://artifacts.chartcoach.dev/catalog/releases/<version>/<digest>/metadata.json` and is cached under the user's platform cache directory. The local cache mirrors the release layout at `catalog/releases/<version>/<digest>/`. Normal catalog reads download `MANIFEST.md` and `entries.parquet`. Heavier derived artifacts such as LanceDB indexes stay described in metadata until a caller asks for them. First-download notices go to stderr, so JSON, JSONL, and CSV stdout stay parseable. `catalog export duckdb` creates a DuckDB database file with the derived catalog tables. Use `catalog schema`, `catalog values`, and `catalog roles` before writing SQL against an unfamiliar catalog. `catalog read` returns deterministic catalog records. `catalog find` deduplicates indexed document matches to guideline-level typed rows.

Install `chartcoach[mcp]` for catalog-only MCP tools. Install both `chartcoach[mcp,index]` when agents will call search tools.

```bash
chartcoach mcp serve
```

Without an index, the MCP server exposes only `sql`. Pass `--index` to also register `search` against an existing LanceDB table.

Run tests with `pnpm --dir packages/catalog-python test`.

## License

MIT. See [LICENSE](LICENSE).
