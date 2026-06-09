# ChartCoach

ChartCoach loads manifest-described visualization guideline catalogs as typed records for agents, scripts, notebooks, search, retrieval, and SQL workflows. The same guideline records are published through the `apps/site` browser surface.

## Agent Quickstart

Install the ChartCoach skill once, then launch an agent with a ChartCoach startup prompt.

```bash
npx skills add chartcoach/catalog

codex "$(uvx chartcoach@latest prompt --codex)"
```

Use the matching agent flag for other CLIs:

```bash
claude "$(uvx chartcoach@latest prompt --claude)"
opencode "$(uvx chartcoach@latest prompt --opencode)"
```

The prompt references the installed skill, the catalog source, optional LanceDB index, and the current task. It tells the agent to read `MANIFEST.md` for section-role and label-family semantics, retrieve targeted evidence, and include guideline ids plus public links when guidelines constrain or justify the answer.

```bash
uvx chartcoach@latest prompt \
  --codex \
  --index scratch/chartcoach-index \
  --guidance-mode feedback \
  --task "Review this dashboard for misleading bar axes."
```

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
source_backed_advice = conn.sql(
    """
    select g.id, g.title, s.content, gs.source_title, gs.doi, gs.url
    from guidelines g
    join sections s on s.guideline_id = g.id
    left join guideline_sources gs on gs.guideline_id = g.id
    where list_contains(g.labels, 'chart:scatter:avoid')
      and s.role = 'advice'
    limit 5
    """
).pl()
conn.close()
```

The catalog row is the shared object. Python returns Polars dataframes and native DuckDB connections, the command line emits table, JSON, JSONL, CSV, or Markdown, and the site renders the same titles, labels, sections, citations, and source-linked pages.

## Retrieve Guideline Evidence

Use labels to retrieve advice for a chart family, task, audience, or design lever.

```bash
uv run --package chartcoach chartcoach guidelines retrieve \
  --label chart:scatter:avoid \
  --section advice \
  --format markdown
```

The command prints deterministic evidence packets. Each packet includes the guideline id, title, description, labels, and the requested sections.

Run one SQL query from the shell when a workflow needs joins:

```bash
uv run --package chartcoach chartcoach sql \
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
| `sections` | Advice, reason, context, exceptions, costs, mistakes, check, and fix text |
| `references` | BibTeX records for the cited sources |

The default catalog resolves from `https://artifacts.chartcoach.dev/metadata.json` and is cached locally by the Python package. That object is a release pointer. The resolved release metadata points to `MANIFEST.md` for section-role and label-family definitions, `entries.parquet` for serialized guideline records, and derived artifacts such as LanceDB indexes.

## Search The Catalog

For retrieval, build a LanceDB index at a path you own. The index stores catalog document rows and exposes LanceDB search through the CLI, Python API, MCP, and DuckDB's Lance extension.

```bash
INDEX_PATH=scratch/chartcoach-index

uv run --package chartcoach chartcoach index \
  --index "$INDEX_PATH"

uv run --package chartcoach chartcoach guidelines search \
  --index "$INDEX_PATH" \
  --where "role = 'overview'" \
  "overplotted scatter plot with too many points" \
  --format jsonl
```

## Open Native Files

ChartCoach keeps the catalog in formats that other tools can open directly.

| File | Use |
| --- | --- |
| `https://artifacts.chartcoach.dev/metadata.json` | Default release pointer |
| `https://artifacts.chartcoach.dev/catalog/releases/<version>/<digest>/metadata.json` | Version, digest, and artifact descriptors |
| `https://artifacts.chartcoach.dev/catalog/releases/<version>/<digest>/MANIFEST.md` | Section-role and label-family definitions |
| `https://artifacts.chartcoach.dev/catalog/releases/<version>/<digest>/entries.parquet` | Catalog table |
| `https://artifacts.chartcoach.dev/catalog/releases/<version>/<digest>/indexes/.../index.tar.gz` | Derived LanceDB index archive |
| DuckDB database | Derived tables for SQL inspection |
| LanceDB index | LanceDB search over catalog document rows |
| `apps/site` | Human-facing guideline browser |

Create a DuckDB database from the catalog:

```bash
DUCKDB_PATH=scratch/catalog.duckdb

uv run --package chartcoach chartcoach catalog duckdb \
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
