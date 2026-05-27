# ChartCoach

ChartCoach loads source-traced visualization guidelines as typed records for scripts, notebooks, review tools, and agents. The same guideline records are published for people at <https://chartcoach.github.io/>.

```python
import polars as pl
from chartcoach import Catalog

catalog = Catalog.from_parquet("guidelines/catalog.parquet")

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
  --source guidelines/catalog.parquet \
  --label chart:scatter:avoid \
  --section advice \
  --format markdown
```

The command prints deterministic evidence packets. Each packet includes the guideline id, title, description, labels, and the requested sections.

Run one SQL query from the shell when a review or agent workflow needs joins:

```bash
uv run --package chartcoach chartcoach sql \
  --source guidelines/catalog.parquet \
  "select id, title from guidelines where list_contains(labels, 'chart:bar')" \
  --format jsonl
```

## Use The Catalog From JavaScript

```ts
import { loadCatalogFromParquetFile } from "@chartcoach/catalog/node";

const catalog = await loadCatalogFromParquetFile("guidelines/catalog.parquet");
const barGuidelines = catalog.entries.filter((entry) =>
  entry.guideline.labels.includes("chart:bar"),
);
```

Browser code can load the same parquet artifact by URL through `@chartcoach/catalog/browser`.

## What A Guideline Contains

Each guideline records a concrete chart-design move with the evidence needed to inspect or apply it.

| Field | Contents |
| --- | --- |
| `id` | Stable guideline identifier |
| `title` | Portable design move |
| `description` | One-sentence scope and action |
| `labels` | Controlled tags for chart type, task, audience, evidence basis, and design lever |
| `sections` | Advice, reason, context, exceptions, costs, mistakes, check, and fix text |
| `references` | BibTeX records for the cited sources |

## Build Review Tools

`chartcoach feedback prompt` builds a catalog-grounded prompt for an existing chart image.

```bash
uv run --package chartcoach chartcoach feedback prompt \
  --source guidelines/catalog.parquet \
  --image path/to/chart.jpg \
  --situation "Review this chart for a quick public-facing comparison." \
  --label-prefix chart:bar \
  --section advice \
  --format markdown
```

For semantic retrieval, build a Chroma index once and query it through either the catalog API or native Chroma parameters.

```bash
INDEX_DIR=$(uv run --package chartcoach python -c "from chartcoach.paths import default_index_dir; print(default_index_dir())")

uv run --package chartcoach chartcoach index build \
  --source guidelines/catalog.parquet \
  --index-dir "$INDEX_DIR"

uv run --package chartcoach chartcoach guidelines search \
  --source guidelines/catalog.parquet \
  --index-dir "$INDEX_DIR" \
  --where '{"labels":{"$contains":"chart:scatter:avoid"}}' \
  "overplotted scatter plot with too many points" \
  --format jsonl
```

## Inspect Native Artifacts

ChartCoach keeps the catalog in formats that other tools can open directly.

| Artifact | Use |
| --- | --- |
| `guidelines/catalog.parquet` | Source catalog table |
| DuckDB database | Derived tables for SQL inspection |
| Chroma index | Content-addressed semantic search |
| <https://chartcoach.github.io/> | Human-facing guideline browser and API docs |

Create a DuckDB artifact from the catalog:

```bash
DUCKDB_PATH=$(uv run --package chartcoach python -c "from chartcoach.paths import default_duckdb_path; print(default_duckdb_path())")

uv run --package chartcoach chartcoach catalog duckdb \
  --source guidelines/catalog.parquet \
  --out "$DUCKDB_PATH"

duckdb "$DUCKDB_PATH" \
  -c "select id, title from guidelines where list_contains(labels, 'chart:bar')"
```

## Develop

Install the repository toolchains:

```bash
corepack enable pnpm
pnpm install
uv sync --package chartcoach --all-groups
```

Run the site locally:

```bash
pnpm --dir apps/site dev
```

Run the workspace checks:

```bash
pnpm lint
pnpm typecheck
pnpm build
pnpm test
```

## License

MIT. See [LICENSE](LICENSE).
