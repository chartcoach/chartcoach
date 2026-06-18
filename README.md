# ChartCoach

Visualization design guidelines for agents and humans, with stable ids, public pages, and source references.

ChartCoach packages visualization guidelines as records that can be browsed, queried, read, and cited. Agents use the same Guideline Catalog that humans browse, so chart feedback and recommendations can point to stable guideline ids, public pages, and source references for grounded reasoning.

- Ask design questions with citations.
- Review existing charts against observed evidence.
- Recommend charts from a data task, audience, and constraints.
- Query a Guideline Catalog from the CLI, Python, JavaScript, or SQL.

## Agent Quickstart

Install the ChartCoach skill once, then ask a normal chart-design question.

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

Install the CLI, then search for a familiar chart topic:

```bash
uv tool install chartcoach

chartcoach catalog query --contains "pie chart" --limit 5 --format table
```

The table view is for reading results in a terminal. Each row has a stable guideline id.

When you want to use a result, switch the same query to JSON and pass the first id into `read` and `cite`:

```bash
GUIDELINE_ID="$(
  chartcoach catalog query \
    --contains "pie chart" \
    --limit 5 \
    --format json |
    jq -r '.[0].id'
)"

chartcoach catalog read "$GUIDELINE_ID" \
  --source-detail minimal \
  --format markdown

chartcoach catalog cite "$GUIDELINE_ID" \
  --format markdown
```

`read` returns the guideline text. `cite` returns the public guideline page and formatted source references.

Agents can inspect the same skill text directly:

```bash
chartcoach skills list
chartcoach skills get discuss
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

```ts
import { readCatalog } from "@chartcoach/catalog/server";

const catalog = await readCatalog();
const firstGuideline = catalog.guidelines[0];
```

Browser code can load the same catalog through `@chartcoach/catalog/browser`.

## What Is In This Repo

| Path                          | What it contains                                                            |
| ----------------------------- | --------------------------------------------------------------------------- |
| `apps/site`                   | Guideline Catalog browser and public guideline pages                        |
| `apps/docs`                   | Technical docs for the catalog, APIs, CLI, and MCP                          |
| `packages/catalog-python`     | Python package, `chartcoach` CLI, agent skills, DuckDB, and optional search |
| `packages/catalog-javascript` | JavaScript catalog loaders and wire types                                   |

## Learn More

- Browse guideline pages at `https://chartcoach.github.io/guidelines/`.
- Read technical docs in [`apps/docs`](apps/docs).
- Read Python package details in [`packages/catalog-python`](packages/catalog-python).
- Inspect the public site source in [`apps/site`](apps/site).

## Develop

Install the repository toolchains:

```bash
corepack enable pnpm
pnpm install
uv sync --package chartcoach --all-groups
```

Run the site and docs locally:

```bash
pnpm --dir apps/site dev
pnpm --dir apps/docs dev
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
