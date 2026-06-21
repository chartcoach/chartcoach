# chartcoach

Python package and CLI for the chartcoach Guideline Catalog.

Read the package docs at [docs.chartcoach.dev/python](https://docs.chartcoach.dev/python).
Read the catalog contract at [docs.chartcoach.dev/catalog](https://docs.chartcoach.dev/catalog).

For agent use, install the chartcoach skill once, then ask the current agent to use it:

```bash
npx skills add chartcoach/skills
codex 'Use $chartcoach to access visualization design guidelines. Start by giving me a thematic overview of the catalog.'
```

The skill points agents to version-matched CLI-served skills. The CLI exposes catalog primitives, and task guidance lives in `chartcoach skills get <name>`.

The base package loads manifest-described catalog bundles, parses guidelines, and exposes typed records, Polars dataframe views, and native DuckDB SQL connections.

For application imports, add the package from the application root:

```bash
uv add chartcoach
uv add 'chartcoach[index]'
uv add 'chartcoach[mcp,index]'
```

```python
from chartcoach import Catalog

catalog = Catalog.open()
catalog.guidelines().select("id", "title")

conn = catalog.duckdb()
conn.sql("select id, title from guidelines limit 5").pl()
conn.close()
```

Install `chartcoach[index]` when code needs indexed discovery. With the Default
Catalog, open the package-pinned LanceDB index from the chartcoach platformdirs
cache:

```python
from chartcoach.catalog import default_index_path
from chartcoach.search import open as open_index, search

table = open_index(default_index_path(table_name="catalog_documents"))

docs = (
    table.search("overplotted scatter plots", query_type="fts", fts_columns="text")
    .where("role = 'overview'")
    .limit(3)
    .to_list()
)

hits = search(catalog, table, "overplotted scatter plots").to_dict()["rows"]
```

The first `default_index_path()` call downloads and extracts the default index
under `artifacts/catalog/releases/<version>/<digest>/indexes/lancedb/<provider>/<model>/`.
The cache keeps `index.tar.gz` at the same relative path as the published
object and extracts the LanceDB table into the sibling `db/` directory. Later
calls reuse the local cache when the archive matches release metadata and the
LanceDB table is present.

Use `index(catalog, uri)` when code needs to create a caller-owned LanceDB
table. It writes the table at the path you provide and returns the native
LanceDB `Table`. Without an embedding function it creates a full-text table
over the `text` column. Pass any LanceDB embedding function instance when you
want LanceDB to fill the `vector` column from `text`:

```python
from chartcoach.search import index

table = index(
    catalog,
    "./chartcoach-index",
    embedding=embedding_function,
)
```

Use `open("./chartcoach-index")` for an existing caller-owned table. Use
`chartcoach.search.lance.documents(catalog)` when your code already owns a
LanceDB connection and wants to call `db.create_table(...)` directly.
Caller-owned tables should expose the catalog document columns `id`,
`parent_id`, `role`, `labels`, `content_hash`, and `text`.

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
duckdb_path = "./chartcoach-catalog.duckdb"
catalog.write_duckdb(duckdb_path, overwrite=True)
```

The LanceDB index root can also be attached through DuckDB's Lance extension:

```sql
INSTALL lance;
LOAD lance;
ATTACH './chartcoach-index' AS cc_index (TYPE LANCE);

select id, parent_id, role
from cc_index.main.catalog_documents
limit 5;
```

Run one-off CLI commands with `uvx chartcoach@latest --help`.

These commands read the package-pinned Default Catalog release, inspect table schemas, write DuckDB tables, read guideline sections, and query indexed guideline rows.
The `@latest` selector follows the newest published package. Use
`chartcoach@0.1.3` when output must stay tied to the `0.1.3` Default Catalog
release.

```bash
uvx chartcoach@latest catalog manifest --format markdown
uvx chartcoach@latest catalog schema --tables --row-counts --format jsonl
uvx chartcoach@latest catalog schema guidelines --format jsonl
uvx chartcoach@latest catalog values labels \
  --contains chart: --format jsonl
uvx chartcoach@latest catalog sql \
  "select id, title from guidelines where list_contains(labels, 'chart:bar')" \
  --format jsonl
DUCKDB_PATH=./chartcoach-catalog.duckdb
uvx chartcoach@latest catalog export duckdb \
  --out "$DUCKDB_PATH"
duckdb "$DUCKDB_PATH" \
  -c "select id, title from guidelines where list_contains(labels, 'chart:bar')"
uvx chartcoach@latest catalog query \
  --label chart:bar --format jsonl
GUIDELINE_ID="$(
  uvx chartcoach@latest catalog query \
    --contains "pie chart" \
    --limit 1 \
    --format json |
    jq -r '.[0].id'
)"
uvx chartcoach@latest catalog read "$GUIDELINE_ID" \
  --source-detail minimal --format jsonl
uvx chartcoach@latest catalog cite "$GUIDELINE_ID" \
  --format markdown
uvx --from 'chartcoach[index]@latest' chartcoach catalog find \
  --mode fts \
  --limit 3 \
  "overplotted scatter plot with too many points" --format jsonl
uvx --from 'chartcoach[index]@latest' chartcoach catalog index info \
  --format json
uvx chartcoach@latest catalog cache versions --format jsonl
uvx chartcoach@latest catalog cache list
uvx chartcoach@latest catalog cache clear
uvx --from 'chartcoach[index]@latest' chartcoach catalog cache pull
INDEX_PATH=./chartcoach-index
uvx --from 'chartcoach[index]@latest' chartcoach catalog index create --index "$INDEX_PATH"
uvx --from 'chartcoach[index]@latest' chartcoach catalog find \
  --index "$INDEX_PATH" \
  --where "role = 'overview'" \
  "overplotted scatter plot with too many points" --format jsonl
```

The package selector after `--from` installs the package with extras. The
following `chartcoach` token is the executable to run. With the Default Catalog,
indexed `find` can resolve the package-pinned default index when `--index` is
omitted. The first default indexed command downloads and extracts the LanceDB
archive below the chartcoach artifact cache root:
`artifacts/catalog/releases/<version>/<digest>/indexes/lancedb/<provider>/<model>/`.
Later default indexed commands reuse that local copy. The default examples use
`--mode fts` so no embedding credential is needed. Pass `--index` for a
caller-owned local index or a custom catalog source.

`catalog cache versions` reads the root artifact index at
`https://artifacts.chartcoach.dev/index.json`. `catalog cache pull` downloads
the newest listed release into the chartcoach artifact cache. By default it
also downloads and extracts the release's default LanceDB archive.

Every row-oriented command supports `--format jsonl`, so shell tools can handle projection and token control. Human `table` output uses rounded, wrapped columns for terminal scanning. JSON, JSONL, and CSV keep machine-readable stdout.

```bash
uvx chartcoach@latest catalog schema --format jsonl |
  jq 'select(.table == "sections")'
```

The Default Catalog is the package-pinned chartcoach Guideline Catalog release.
It comes from release metadata under
`https://artifacts.chartcoach.dev/catalog/releases/<version>/<digest>/metadata.json`
and is cached under the `artifacts/` directory inside the user's platform cache
directory. The local cache mirrors the release layout at
`artifacts/catalog/releases/<version>/<digest>/`. Normal catalog
reads download `MANIFEST.md` and `entries.parquet`. Heavier derived artifacts
such as LanceDB indexes stay described in metadata until a caller asks for them.
All chartcoach-owned default artifacts use this platformdirs cache layout. Print
the exact artifact root for the current user with:

```bash
uvx --from chartcoach@latest python -c "from chartcoach.catalog.remote import cache_root; print(cache_root() / 'artifacts')"
```

The current Default Catalog contains 781 guideline records and 262 source
references. It follows the curation scheme described in
[Structured Visualization Design Knowledge for Grounding Generative Reasoning and Situated Feedback](https://arxiv.org/abs/2512.20306),
combining 100+ visualization perception and cognitive science papers,
accessibility criteria, data journalism, rhetorical visualization research, and
36 practitioner posts from Datawrapper's
[Data Vis Do's & Don'ts](https://www.datawrapper.de/blog/category/datavis-dos-and-donts)
series.

First-download notices go to stderr, so JSON, JSONL, and CSV stdout stay
parseable. `catalog export duckdb` creates a DuckDB database file with the
derived catalog tables. Use `catalog schema`, `catalog values`, and
`catalog roles` before writing SQL against an unfamiliar catalog. `catalog read`
returns deterministic catalog records. `catalog find` deduplicates indexed
document matches to guideline-level typed rows.

Run catalog-only MCP tools with `chartcoach[mcp]`. Include `index` when agents
will call search tools.

```bash
uvx --from 'chartcoach[mcp]@latest' chartcoach mcp serve
uvx --from 'chartcoach[mcp,index]@latest' chartcoach mcp serve \
  --index ./chartcoach-index
```

Without an index, the MCP server exposes only `sql`. Pass `--index` to also
register `search` against a caller-owned LanceDB table.

Run package tests from the repository root:

```bash
uv run --package chartcoach --all-extras pytest packages/catalog-python/tests
```

## License

MIT. See [LICENSE](LICENSE).
