<p align="center">
  <img src="https://chartcoach.dev/brand/chartcoach-square-light.svg" width="128" alt="chartcoach logo">
</p>

# chartcoach

<p align="center">
  Human and agent-friendly visualization design guidelines.
</p>

<p align="center">
  <a href="https://pypi.org/project/chartcoach/"><img src="https://img.shields.io/pypi/v/chartcoach?label=PyPI" alt="PyPI version"></a>
  <a href="https://www.npmjs.com/package/@chartcoach/catalog"><img src="https://img.shields.io/npm/v/%40chartcoach%2Fcatalog?label=npm" alt="npm version"></a>
</p>

chartcoach packages visualization design guidance as records you can browse,
query, cite, and use in agent workflows. The same Guideline Catalog powers the
public site, CLI, Python package, JavaScript package, and agent skills.

```bash
uvx chartcoach@latest catalog query --contains "pie chart" --limit 5 --format table
```

## Agents

Install the chartcoach skill once, then ask a chart design question.

```bash
npx skills add chartcoach/skills
codex 'Hey $chartcoach, how should I show uncertainty for a general audience?'
```

Agents can also read the current docs map at
[docs.chartcoach.dev/llms.txt](https://docs.chartcoach.dev/llms.txt).

## Python

```bash
uv add chartcoach
```

```python
import chartcoach

cc = chartcoach.open()
cc.catalog.guidelines().select("id", "title").head(5)
```

Use DuckDB when you want SQL over guideline records, sections, labels, and
source references.

## JavaScript

```bash
npm install @chartcoach/catalog
```

```ts
import { DEFAULT_CATALOG, loadCatalog } from "@chartcoach/catalog"

const entries = await (await fetch(DEFAULT_CATALOG.entriesUrl)).arrayBuffer()
const manifestText = await (await fetch(DEFAULT_CATALOG.manifestUrl)).text()

const catalog = await loadCatalog({ entries, manifestText })
```

## Explore

- 🌐 Browse [chartcoach](https://chartcoach.dev/).
- ✨ Read the [agent docs](https://docs.chartcoach.dev/agents).
- 📚 Explore the [Guideline Catalog](https://chartcoach.dev/guidelines/).
- 🧭 Read about the [cataloging scheme](https://docs.chartcoach.dev/catalog).

## Develop

```bash
corepack enable pnpm
pnpm install
uv sync --package chartcoach --all-groups --all-extras
```

```bash
pnpm dev
pnpm lint
pnpm typecheck
pnpm test
```

## License

MIT. See [LICENSE](LICENSE).
