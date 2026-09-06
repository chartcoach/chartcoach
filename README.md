<p align="center">
  <img src="packages/brand/assets/brand/chartcoach-square-light.svg" width="128" alt="chartcoach logo">
</p>

# chartcoach

chartcoach helps people, applications, and coding agents find visualization
guidelines and inspect the sources behind each recommendation. The Guideline
Catalog keeps a guideline's advice, limits, checks, fixes, and references in
one record.

chartcoach is alpha software. The Python package supports Python 3.10 through
3.14. Browse the catalog at
[chartcoach.dev](https://chartcoach.dev/guidelines/).

## Read one guideline

```bash
uvx --from \
  "chartcoach @ https://files.peter.gy/packages/python/chartcoach/0.2.0/892f120cb377/chartcoach-0.2.0-py3-none-any.whl" \
  chartcoach catalog read directly-label-series-instead-of-using-a-color-key \
  --source https://files.peter.gy/packages/python/chartcoach/0.2.0/docs-catalog/c0f6dbec3dd31b07763b46fd458733db0b8b50c5793cf9447458119287129420/release.json \
  --format markdown
```

This shortened excerpt includes the title and first section:

```text
## directly-label-series-instead-of-using-a-color-key

**Directly label colored series instead of relying on a color key**

...

### advice: Move labels onto the marks

Label colored series directly on the chart instead of making readers decode
them through a color key...
```

`uvx` downloads and runs the hosted 0.2.0 Python package. The `release.json`
URL fixes the three catalog records used by this example. chartcoach verifies
the release digest and the byte count and SHA-256 hash of its required files
before reading them.

## Interfaces

| Interface                                                  | What it provides                                         |
| ---------------------------------------------------------- | -------------------------------------------------------- |
| [Catalog browser](https://chartcoach.dev/guidelines/)      | Public guideline pages and search                        |
| [Python](https://docs.chartcoach.dev/python)               | Polars, DuckDB, and LanceDB access                       |
| [JavaScript](https://docs.chartcoach.dev/javascript)       | Browser and server-side catalog loading                  |
| [Catalog CLI](https://docs.chartcoach.dev/cli)             | Filtering, SQL, record reads, and citations              |
| [MCP server](https://docs.chartcoach.dev/mcp)              | Catalog tools for Model Context Protocol clients         |
| [Curate and publish](https://docs.chartcoach.dev/curation) | Authoring, validation, publication, and public selection |

## Use chartcoach with an agent

Install the CLI, save its agent instructions, and save the chart as
`chart.png`:

```bash
uv tool install \
  "chartcoach @ https://files.peter.gy/packages/python/chartcoach/0.2.0/892f120cb377/chartcoach-0.2.0-py3-none-any.whl"
chartcoach skills get core --full > chartcoach-core.md
codex -i chart.png \
  'Read chartcoach-core.md, then review the attached chart for labels and accessibility.'
```

Agent hosts can also index the documentation through
[llms.txt](https://docs.chartcoach.dev/llms.txt).

## Contribute

Repository setup, focused commands, and pull request requirements live in
[Contributing](CONTRIBUTING.md). Package ownership and catalog data flow are
mapped in [Architecture](development_docs/architecture.md).

chartcoach is licensed under the [Apache License 2.0](LICENSE).
