<p align="center">
  <img src="packages/brand/assets/brand/chartcoach-square-light.svg" width="128" alt="chartcoach logo">
</p>

# chartcoach

<p align="center">
  Human and agent-friendly visualization design guidelines.
</p>

<p align="center">
  <a href="https://pypi.org/project/chartcoach/"><img src="https://img.shields.io/pypi/v/chartcoach?label=PyPI" alt="PyPI version"></a>
  <a href="https://www.npmjs.com/package/@chartcoach/catalog"><img src="https://img.shields.io/npm/v/%40chartcoach%2Fcatalog?label=npm" alt="npm version"></a>
</p>

chartcoach packages visualization design guidance as records that people and
agents can inspect, query, and cite. The Guideline Catalog powers the public
site, CLI, Python package, JavaScript package, MCP server, and agent skills.

```bash
uvx --from 'chartcoach[curation]@latest' chartcoach catalog list \
  --contains "pie chart" \
  --limit 5
```

Read a selected guideline before citing it:

```bash
uvx --from 'chartcoach[curation]@latest' chartcoach catalog read \
  compare-percentages-with-bars-not-pies
```

## Agents

Install the chartcoach skills, then invoke `$chartcoach` in an agent session.

```bash
npx skills add chartcoach/skills
codex 'Hey $chartcoach, how should I show uncertainty for a general audience?'
```

The live documentation map is available at
[docs.chartcoach.dev/llms.txt](https://docs.chartcoach.dev/llms.txt).

## Python

```bash
uv add 'chartcoach[curation]'
```

```python
from chartcoach import open_catalog, resolve_release

release = resolve_release()
catalog = open_catalog(release.digest)
print(catalog.guidelines().select("id", "title").head(5))
```

The base package loads authored folders and compiled bundles. The `curation`
extra adds published release storage, caching, LanceDB profile construction,
UMAP projections, and nearest-neighbor artifacts.

## JavaScript

```bash
npm install @chartcoach/catalog
```

```ts
import { open } from "@chartcoach/catalog";

const catalog = await open();
const guideline = catalog.require("compare-percentages-with-bars-not-pies");
```

## Explore

- Browse [chartcoach](https://chartcoach.dev/).
- Read the [agent docs](https://docs.chartcoach.dev/agents).
- Explore the [Guideline Catalog](https://chartcoach.dev/guidelines/).
- Read the [cataloging scheme](https://docs.chartcoach.dev/catalog).

## Develop

```bash
pnpm install
uv sync --locked --package chartcoach --all-groups --all-extras
```

```bash
pnpm ready
make format lint typecheck test build
```

See [Development workflow](development_docs/development.md) for focused app and
package commands.

## License

Apache-2.0. See [LICENSE](LICENSE).
