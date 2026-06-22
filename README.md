# chartcoach

Visualization design guidelines for agents and humans, with stable ids, public pages, and source references.

chartcoach packages visualization guidelines as records that can be browsed, queried, read, and cited. Agents use the same Guideline Catalog that humans browse, so chart feedback and recommendations can point to stable guideline ids, public pages, and source references for grounded reasoning.

- Ask design questions with citations.
- Review existing charts against observed evidence.
- Recommend charts from a data task, audience, and constraints.
- Query a Guideline Catalog from the CLI, Python, JavaScript, or SQL.

## Default Catalog

The default catalog is the package-pinned chartcoach Guideline Catalog release.
When no source is passed to a CLI command or `Catalog.open()`, chartcoach reads
release metadata under
`https://artifacts.chartcoach.dev/catalog/releases/<version>/<digest>/metadata.json`.
The JavaScript package exposes the package-pinned artifact URLs through
`DEFAULT_CATALOG`. JavaScript callers fetch or read those artifacts and pass
the bytes to `loadCatalog`.
Python CLI and package downloads use the chartcoach platformdirs cache root.
All chartcoach-owned default artifacts live below
`artifacts/catalog/releases/<version>/<digest>/` inside that cache.

The current release contains 781 guideline records and 262 source references.
It follows the curation scheme described in
[Structured Visualization Design Knowledge for Grounding Generative Reasoning and Situated Feedback](https://arxiv.org/abs/2512.20306),
combining 100+ visualization perception and cognitive science papers,
accessibility criteria, data journalism, rhetorical visualization research, and
36 practitioner posts from Datawrapper's
[Data Vis Do's & Don'ts](https://www.datawrapper.de/blog/category/datavis-dos-and-donts)
series.

Read the catalog contract at
[docs.chartcoach.dev/catalog](https://docs.chartcoach.dev/catalog).

## Agent Quickstart

Install the chartcoach skill once, then ask a normal chart-design question.

```bash
npx skills add chartcoach/skills --skill chartcoach

codex 'Hey $chartcoach, why should I avoid using a pie chart?'
```

The top-level `$chartcoach` skill is a small router. It loads CLI-served skills shipped with the installed package:

| User job                                                               | Skill         |
| ---------------------------------------------------------------------- | ------------- |
| Discuss what the catalog says, compare chart choices, or trace claims  | `discuss`     |
| Review an existing chart with observed visual evidence                 | `visfeedback` |
| Recommend a chart or encoding from a data task                         | `visrec`      |
| Draft a catalog issue when retrieval exposes missing or unclear guidance | `contribute`  |
| Inspect CLI primitives, custom sources, output formats, and indexes    | `core`        |

The Guideline Catalog is maintained as a shared resource. A failed search, missing topic, weak label, or unclear record from one chart task can become a catalog issue that improves future retrieval.

`contribute` drafts that issue locally for human review. It never posts by default.

## Quickstart

Run the CLI with `uvx`, then search for a familiar chart topic:

```bash
uvx chartcoach@latest catalog query --contains "pie chart" --limit 5 --format table
```

The table view is for reading results in a terminal. Each row has a stable guideline id.
The `@latest` selector is for one-off access to the newest published package.
Use `chartcoach@0.1.3` when output must stay tied to the `0.1.3` Default
Catalog release.

When you want to use a result, switch the same query to JSON and pass the first id into `read` and `cite`:

```bash
GUIDELINE_ID="$(
  uvx chartcoach@latest catalog query \
    --contains "pie chart" \
    --limit 5 \
    --format json |
    jq -r '.[0].id'
)"

uvx chartcoach@latest catalog read "$GUIDELINE_ID" \
  --source-detail minimal \
  --format markdown

uvx chartcoach@latest catalog cite "$GUIDELINE_ID" \
  --format markdown
```

`read` returns the guideline text. `cite` returns the public guideline page and formatted source references.

Agents can inspect the same skill text directly:

```bash
uvx chartcoach@latest skills list
uvx chartcoach@latest skills get discuss
```

## Python

```python
from chartcoach import Catalog

catalog = Catalog.open()
catalog.guidelines().select("id", "title").head(5)
```

Use DuckDB for advanced queries such as joins over guideline sections, labels, and source references:

```python
conn = catalog.duckdb()
rows = conn.sql("select id, title from guidelines limit 5").pl()
conn.close()
```

## JavaScript

`@chartcoach/catalog` is currently a workspace package in this repository.

```ts
import { DEFAULT_CATALOG, loadCatalog } from "@chartcoach/catalog"

const entries = await fetch(DEFAULT_CATALOG.entriesUrl).then((response) =>
  response.arrayBuffer(),
)
const manifestText = await fetch(DEFAULT_CATALOG.manifestUrl).then((response) =>
  response.text(),
)

const catalog = await loadCatalog({ entries, manifestText })
const guideline = catalog.require("compare-percentages-with-bars-not-pies")
```

`loadCatalog` accepts caller-owned bytes. In runtimes with file APIs, read
`entries.parquet` and `MANIFEST.md` locally, then pass those values to the same
function.

## What Is In This Repo

| Path                          | What it contains                                                            |
| ----------------------------- | --------------------------------------------------------------------------- |
| `apps/site`                   | Guideline Catalog browser and public guideline pages                        |
| `apps/docs`                   | Technical docs for the catalog, APIs, CLI, and MCP                          |
| `packages/brand`              | Shared web brand assets, font imports, CSS tokens, and asset checks         |
| `packages/catalog-python`     | Python package, `chartcoach` CLI, agent skills, DuckDB, and optional search |
| `packages/catalog-javascript` | JavaScript catalog models, artifact parsers, and wire types                 |

## Learn More

- Browse guideline pages at `https://chartcoach.dev/guidelines/`.
- Read technical docs at `https://docs.chartcoach.dev/`.
- Read the catalog contract at `https://docs.chartcoach.dev/catalog`.
- Inspect docs source in [`apps/docs`](apps/docs).
- Read Python package details in [`packages/catalog-python`](packages/catalog-python).
- Read JavaScript package details in [`packages/catalog-javascript`](packages/catalog-javascript).
- Inspect the public site source in [`apps/site`](apps/site).

## Develop

Install the repository toolchains:

```bash
corepack enable pnpm
pnpm install
uv sync --package chartcoach --all-groups --all-extras
```

Run the site and docs locally:

```bash
pnpm --dir apps/site dev
pnpm --dir apps/docs dev
```

These commands run through portless. The site is available at
`https://chartcoach.localhost`, and the docs are available at
`https://docs.chartcoach.localhost`.

Run both apps with one command:

```bash
pnpm dev
```

Run workspace checks:

```bash
pnpm lint
pnpm typecheck
pnpm build
pnpm test
```

## License

MIT. See [LICENSE](LICENSE).
