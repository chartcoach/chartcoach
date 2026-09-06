<p align="center">
  <img src="packages/brand/assets/brand/chartcoach-square-light.svg" width="128" alt="ChartCoach logo">
</p>

# ChartCoach

<p align="center">
  Research-backed guidance for better visualization decisions.
</p>

<p align="center">
  <a href="https://pypi.org/project/chartcoach/"><img src="https://img.shields.io/pypi/v/chartcoach?label=PyPI" alt="PyPI version"></a>
  <a href="https://www.npmjs.com/package/@chartcoach/catalog"><img src="https://img.shields.io/npm/v/%40chartcoach%2Fcatalog?label=npm" alt="npm version"></a>
</p>

ChartCoach helps you choose, review, and explain chart designs. Its Guideline
Catalog turns visualization research and practice into focused recommendations
with references you can inspect and cite.

Use ChartCoach to:

- compare design choices while creating a visualization
- review a chart and explain the reasoning behind suggested changes
- give agents and visualization tools source-backed design guidance

## Get started

[Browse the Guideline Catalog](https://chartcoach.dev/guidelines/) or search it
from the terminal without installing anything:

```bash
uvx chartcoach@latest catalog list --contains "percentages" --limit 5
uvx chartcoach@latest catalog read compare-percentages-with-bars-not-pies
```

The [getting started guide](https://docs.chartcoach.dev/getting-started) covers
installation and the main ways to use ChartCoach.

## Choose an interface

| I want to                                      | Start here                                               |
| ---------------------------------------------- | -------------------------------------------------------- |
| Search and read guidance from a terminal       | [CLI guide](https://docs.chartcoach.dev/cli)             |
| Ask an agent for visualization guidance        | [Agent guide](https://docs.chartcoach.dev/agents)        |
| Query the catalog from Python                  | [Python API](https://docs.chartcoach.dev/python)         |
| Load catalog records in a web application      | [JavaScript API](https://docs.chartcoach.dev/javascript) |
| Connect ChartCoach to an MCP-compatible client | [MCP guide](https://docs.chartcoach.dev/mcp)             |
| Understand the catalog structure               | [Catalog guide](https://docs.chartcoach.dev/catalog)     |

Install the ChartCoach skills to use the catalog from an agent session:

```bash
npx skills add chartcoach/skills
codex 'Hey $chartcoach, how should I show uncertainty for a general audience?'
```

Agent-readable documentation is available at
[docs.chartcoach.dev/llms.txt](https://docs.chartcoach.dev/llms.txt).

## Contribute

See [Contributing](CONTRIBUTING.md) for setup and repository checks. The
[architecture](development_docs/architecture.md) and
[development workflow](development_docs/development.md) document package
ownership and focused commands.

## License

Apache-2.0. See [LICENSE](LICENSE).
