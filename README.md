<p align="center">
  <a href="https://chartcoach.dev/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="packages/brand/assets/brand/chartcoach-vertical-white.svg">
      <img src="packages/brand/assets/brand/chartcoach-vertical.svg" width="280" alt="chartcoach">
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://chartcoach.dev/guidelines/">Browse guidelines</a> ·
  <a href="https://docs.chartcoach.dev/">Documentation</a>
</p>

<p align="center">
  <a href="https://github.com/chartcoach/chartcoach/actions/workflows/ci.yml"><img alt="CI status" src="https://img.shields.io/github/actions/workflow/status/chartcoach/chartcoach/ci.yml?branch=main&amp;label=CI&amp;style=flat&amp;labelColor=27272a"></a>
  <a href="https://pypi.org/project/chartcoach/"><img alt="PyPI version" src="https://img.shields.io/pypi/v/chartcoach?style=flat&amp;labelColor=27272a&amp;color=d93654"></a>
  <a href="https://www.npmjs.com/package/@chartcoach/catalog"><img alt="npm version" src="https://img.shields.io/npm/v/%40chartcoach%2Fcatalog?style=flat&amp;labelColor=27272a&amp;color=d93654"></a>
  <a href="LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-71717a?style=flat&amp;labelColor=27272a"></a>
</p>

**Visualization guidelines agents can inspect and cite.**

chartcoach helps people and agents create and review charts using source-linked
guidance. Its Guideline Catalog brings together recommendations, their reasoning,
when they apply, and checks for putting them into practice.

## Try a guideline

With [uv](https://docs.astral.sh/uv/), the Python package manager, installed:

```bash
uvx chartcoach catalog read directly-label-series-instead-of-using-a-color-key \
  --format markdown
```

The command downloads and caches the public catalog, then prints the guideline
and its sources. An excerpt:

> **Move labels onto the marks**
>
> Label colored series directly on the chart instead of making readers decode
> them through a color key.

Source: Lisa Charlotte Muth, _What to consider when visualizing data for
colorblind readers_ (2020).

The [complete guideline](https://chartcoach.dev/guidelines/directly-label-series-instead-of-using-a-color-key/)
includes its reasoning, exceptions, and checks.

## Use chartcoach

- **With an agent.** Retrieve guidance for chart review, recommendations, and
  design discussions. Follow the [agent guide](https://docs.chartcoach.dev/agents)
  or connect the [MCP server](https://docs.chartcoach.dev/mcp), which exposes
  catalog tools through the Model Context Protocol.
- **In an application.** Read and cite entries through
  [Python](https://docs.chartcoach.dev/python),
  [TypeScript](https://docs.chartcoach.dev/javascript), or the
  [CLI](https://docs.chartcoach.dev/cli). Python also exposes native
  [DuckDB](https://duckdb.org/) connections for SQL and
  [LanceDB](https://lancedb.com/) tables for search.
- **For your own catalog.**
  [Author guidelines and publish catalogs](https://docs.chartcoach.dev/curation),
  with optional search indexes.

chartcoach is alpha software.

[Contributing](CONTRIBUTING.md) · [Apache-2.0](LICENSE)
