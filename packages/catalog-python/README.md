# chartcoach

Python tools for the ChartCoach guideline catalog.

Install the ChartCoach skill once, then launch an agent with a startup prompt from the CLI:

```bash
npx skills add chartcoach/catalog
codex "$(uvx chartcoach@latest prompt --codex --source guidelines)"
```

Use `--claude` or `--opencode` for those agent CLIs. Pass `--task`, `--index-dir`, and `--guidance-mode` when the agent needs task-specific catalog context.

The base package loads manifest-described catalog bundles, parses guidelines, and exposes typed records, Polars dataframe views, and native DuckDB SQL connections.

```python
from chartcoach import Catalog

catalog = Catalog.from_source("guidelines")
catalog.guidelines().select("id", "title")

conn = catalog.duckdb()
conn.sql("select id, title from guidelines limit 5").pl()
conn.close()
```

Install `chartcoach[search]` when code needs the optional LanceDB index:

```python
from chartcoach import CatalogTools
from chartcoach.paths import default_index_dir

tools = CatalogTools(
    catalog,
    index_dir=default_index_dir(),
)

tools.query_documents(
    "overplotted scatter plots",
    limit=3,
    where="role = 'overview'",
)

tools.search_guidelines(
    "overplotted scatter plots",
    where="role = 'overview'",
)["rows"]
```

Build the index first with `chartcoach index build`. Read commands open the content-addressed path for the current catalog digest and document version. ChartCoach creates a LanceDB full-text table over catalog documents. Use LanceDB's schema and embedding registry directly for vector tables.

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

Write a DuckDB database file when another tool needs a durable artifact:

```python
from chartcoach.paths import default_duckdb_path

duckdb_path = default_duckdb_path()
catalog.write_duckdb(duckdb_path, overwrite=True)
```

The LanceDB index root can also be attached through DuckDB's Lance extension:

```sql
INSTALL lance;
LOAD lance;
ATTACH '/path/to/index-root' AS cc_index (TYPE LANCE);

select id, parent_id, role
from cc_index.main.catalog_documents
limit 5;
```

Run the CLI with `uv run --package chartcoach chartcoach --help`.

These commands read the `guidelines` artifact bundle, inspect table schemas, write DuckDB tables, retrieve guideline evidence, and query indexed document rows.

```bash
chartcoach prompt --codex --source guidelines \
  --task "Review this dashboard for misleading bar axes."
chartcoach artifacts --source guidelines \
  --format jsonl
chartcoach catalog manifest --source guidelines --format markdown
chartcoach tables list --source guidelines --format jsonl
chartcoach tables schema --source guidelines --format jsonl
chartcoach tables values guideline_labels label \
  --source guidelines --contains chart: --format jsonl
chartcoach sql --source guidelines \
  "select id, title from guidelines where list_contains(labels, 'chart:bar')" \
  --format jsonl
DUCKDB_PATH=$(
  python -c "from chartcoach.paths import default_duckdb_path; print(default_duckdb_path())"
)
chartcoach catalog duckdb --source guidelines \
  --out "$DUCKDB_PATH"
duckdb "$DUCKDB_PATH" \
  -c "select id, title from guidelines where list_contains(labels, 'chart:bar')"
chartcoach guidelines retrieve --source guidelines \
  --label chart:bar --section advice --format jsonl
INDEX_DIR=$(
  python -c "from chartcoach.paths import default_index_dir; print(default_index_dir())"
)
chartcoach index build --source guidelines --index-dir "$INDEX_DIR"
chartcoach index status --source guidelines \
  --index-dir "$INDEX_DIR" --format jsonl
chartcoach index query --source guidelines \
  --index-dir "$INDEX_DIR" \
  "overplotted scatter plot with too many points" \
  --limit 8
chartcoach guidelines search --source guidelines \
  --index-dir "$INDEX_DIR" \
  --where "role = 'overview'" \
  "overplotted scatter plot with too many points" --format jsonl
```

Every row-oriented command supports `--format jsonl`, so shell tools can handle projection and token control:

```bash
chartcoach tables schema --source guidelines --format jsonl |
  jq 'select(.table == "sections")'
```

The `artifacts` command prints native artifact paths for tools outside the SDK. `guidelines/MANIFEST.md` explains section roles and label families. `guidelines/catalog.parquet` can be opened by Polars or DuckDB directly. `catalog duckdb` creates a normal DuckDB database file with the derived catalog tables. Passing `--index-dir` adds the content-addressed LanceDB root and `catalog_documents` table path. Use `tables list`, `tables schema`, and `tables values` before writing SQL against an unfamiliar catalog. `guidelines retrieve` is deterministic and does not require a search index. `index query` runs full-text search over indexed document rows. `guidelines search` deduplicates matches to guideline-level typed rows. Build the index explicitly with `chartcoach index build`. Read commands do not create or rebuild search state.

Install `chartcoach[mcp]` for catalog-only MCP tools. Install both `chartcoach[mcp,search]` when agents will call search tools.

```bash
chartcoach mcp serve --source guidelines
```

The MCP surface exposes `catalog_artifacts`, `tables_list`, `tables_schema`, `tables_values`, `sql_query`, `guidelines_list`, `guidelines_get`, `guidelines_retrieve`, `guidelines_search`, and `index_query`. Pass `--index-dir` to make `guidelines_search` and `index_query` usable.

Run tests with `pnpm --dir packages/catalog-python test`.

## License

MIT. See [LICENSE](LICENSE).
