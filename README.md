# ChartCoach

ChartCoach loads manifest-described visualization guideline catalogs as typed records for agents, scripts, notebooks, search, retrieval, and SQL workflows. The same guideline records are published through the `apps/site` browser surface.

## Agent Quickstart

Install the ChartCoach skill once, then ask your agent to use it. The request stays visible and task-specific.

```bash
npx skills add chartcoach/chartcoach --skill chartcoach

codex 'Use $chartcoach to access visualization design guidelines. Start by giving me a thematic overview of the catalog.'
```

The `$chartcoach` skill points the agent to version-matched workflow content served by the installed CLI. The CLI exposes catalog, SQL, section-reading, skill, MCP, and optional LanceDB index primitives.

```python
import polars as pl
from chartcoach import Catalog

catalog = Catalog.open()

scatter_rules = (
    catalog.guidelines()
    .filter(pl.col("labels").list.contains("chart:scatter:avoid"))
    .select("id", "title", "description")
    .head(5)
)

conn = catalog.duckdb()
source_backed_sections = conn.sql(
    """
    select g.id, g.title, s.content, gs.source_title, gs.doi, gs.url
    from guidelines g
    join sections s on s.guideline_id = g.id
    left join guideline_sources gs on gs.guideline_id = g.id
    where list_contains(g.labels, 'chart:scatter:avoid')
    limit 5
    """
).pl()
conn.close()
```

The catalog row is the shared object. Python returns Polars dataframes and native DuckDB connections, the command line emits aligned human tables plus JSON, JSONL, CSV, or Markdown, and the site renders the same titles, labels, sections, citations, and source-linked pages.

## Read Guideline Sections

Use catalog filters to find exact ids, then read the sections named by the manifest.

```bash
uv run --package chartcoach chartcoach catalog query \
  --label chart:scatter:avoid \
  --format jsonl

uv run --package chartcoach chartcoach catalog read <guideline-id> \
  --section <role-from-manifest> \
  --source-detail minimal \
  --format markdown

uv run --package chartcoach chartcoach catalog cite <guideline-id> \
  --format markdown
```

`catalog read` prints deterministic guideline records. Each record includes the guideline id, title, description, labels, selected sections, and sources.
`catalog cite` prints the public guideline URL and formatted source references for verified ids.

Run one SQL query from the shell when a workflow needs joins:

```bash
uv run --package chartcoach chartcoach catalog sql \
  "select id, title from guidelines where list_contains(labels, 'chart:bar')" \
  --format jsonl
```

## Use The Catalog From JavaScript

```ts
import { readCatalog } from "@chartcoach/catalog/server";

const catalog = await readCatalog();
const barGuidelines = catalog.guidelines.filter((guideline) =>
  guideline.labels.includes("chart:bar"),
);
```

Browser code can load the same parquet file by URL through `@chartcoach/catalog/browser`.

## What A Guideline Contains

Each guideline records a concrete chart-design move with the evidence needed to inspect or apply it.

| Field | Contents |
| --- | --- |
| `id` | Stable guideline identifier |
| `title` | Portable design move |
| `description` | One-sentence scope and action |
| `labels` | Catalog-owned labels using `family:category` or `family:category:modifier` |
| `sections` | Manifest-defined section roles and source-backed section text |
| `references` | BibTeX records for the cited sources |

The default catalog resolves from the package-pinned release metadata at `https://artifacts.chartcoach.dev/catalog/releases/0.0.0/7cfd43ee820be252b8ae9058c4c36109a9c8415c6b3a5ff8a9127117b4a10c19/metadata.json` and is cached locally by the Python package. The release metadata points to `MANIFEST.md` for section-role and label-family definitions, `entries.parquet` for serialized guideline records, and derived artifacts such as LanceDB indexes. Local cache paths mirror the release layout under the user's platform cache directory.

## Search The Catalog

For the default catalog, base commands download only the manifest and entries artifacts they need. Read-only search commands resolve the package-pinned index archive from release metadata and cache it locally when `--index` is omitted. For custom retrieval, build a LanceDB index at a path you own. The index stores catalog document rows and exposes LanceDB search through the CLI, Python API, MCP, and DuckDB's Lance extension. `--index` accepts a local LanceDB database path or a URI that LanceDB can open.

```bash
uv run --package chartcoach chartcoach catalog find \
  --where "role = 'overview'" \
  "overplotted scatter plot with too many points" \
  --format jsonl
```

Build and pass a local index when searching a custom catalog or a locally managed index:

```bash
INDEX_PATH=scratch/chartcoach-index

uv run --package chartcoach chartcoach catalog index create \
  --index "$INDEX_PATH"

uv run --package chartcoach chartcoach catalog find \
  --index "$INDEX_PATH" \
  --where "role = 'overview'" \
  "overplotted scatter plot with too many points" \
  --format jsonl
```

## Open Native Files

ChartCoach keeps the catalog in formats that other tools can open directly.

| File | Use |
| --- | --- |
| `https://artifacts.chartcoach.dev/index.json` | Published catalog release index |
| `https://artifacts.chartcoach.dev/catalog/releases/<version>/<digest>/metadata.json` | Version, digest, and artifact descriptors |
| `https://artifacts.chartcoach.dev/catalog/releases/<version>/<digest>/MANIFEST.md` | Section-role and label-family definitions |
| `https://artifacts.chartcoach.dev/catalog/releases/<version>/<digest>/entries.parquet` | Catalog table |
| `https://artifacts.chartcoach.dev/catalog/releases/<version>/<digest>/indexes/.../index.tar.gz` | Derived LanceDB index archive |
| `s3://chartcoach/catalog/releases/<version>/<digest>/indexes/.../db` | Native LanceDB index prefix for direct `lancedb.connect(...)` |
| DuckDB database | Derived tables for SQL inspection |
| LanceDB index | LanceDB search over catalog document rows |
| `apps/site` | Human-facing guideline browser |

Create a DuckDB database from the catalog:

```bash
DUCKDB_PATH=scratch/catalog.duckdb

uv run --package chartcoach chartcoach catalog export duckdb \
  --out "$DUCKDB_PATH"

duckdb "$DUCKDB_PATH" \
  -c "select id, title from guidelines where list_contains(labels, 'chart:bar')"
```

Attach the search index through DuckDB's Lance extension:

```bash
duckdb -c "
INSTALL lance;
LOAD lance;
ATTACH '$INDEX_PATH' AS cc_index (TYPE LANCE);
select id, parent_id, role
from cc_index.main.catalog_documents
limit 5;
"
```

## Develop

Install the repository toolchains:

```bash
corepack enable pnpm
pnpm install
uv sync --package chartcoach --all-groups
```

Run the browser surfaces locally:

```bash
pnpm --dir apps/site dev
pnpm --dir apps/docs dev
```

Local URLs default to `http://localhost:4321/` for `apps/site` and `http://localhost:4322/` for `apps/docs`. Set `CHARTCOACH_SITE_URL`, `CHARTCOACH_DOCS_URL`, `CHARTCOACH_DOCS_EDIT_BASE_URL`, and `CHARTCOACH_REPOSITORY_URL` for deployed builds.

Run the workspace checks:

```bash
pnpm lint
pnpm typecheck
pnpm build
pnpm test
```

## License

MIT. See [LICENSE](LICENSE).
