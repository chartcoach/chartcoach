<p align="center">
  <img src="https://chartcoach.dev/brand/chartcoach-square-light.svg" width="128" alt="chartcoach logo">
</p>

# chartcoach

<p align="center">
  Python package and CLI for visualization design guidance.
</p>

<p align="center">
  <a href="https://pypi.org/project/chartcoach/"><img src="https://img.shields.io/pypi/v/chartcoach?label=PyPI" alt="PyPI version"></a>
</p>

chartcoach gives notebooks, scripts, command-line workflows, and agents access
to the chartcoach Guideline Catalog. Use it to find chart guidance, read
recommendations, cite sources, and query the catalog with [DuckDB](https://duckdb.org/) and [LanceDB](https://lancedb.com/).

Read the full Python docs at
[docs.chartcoach.dev/python](https://docs.chartcoach.dev/python).

## Install

```bash
uv add chartcoach
```

```bash
pip install chartcoach
```

Install `chartcoach[index]` for local search. Install `chartcoach[mcp]` when an
agent needs MCP tools.

## CLI

```bash
uvx chartcoach@latest catalog query --contains "pie chart" --limit 5 --format table
```

## Python

```python
import chartcoach

cc = chartcoach.open()
cc.catalog.guidelines().select("id", "title").head(5)
```

Query the catalog with DuckDB when a notebook or script needs SQL:

```python
conn = cc.catalog.duckdb()
conn.sql("select id, title from guidelines limit 5").pl()
conn.close()
```

## Agents

Equip agents with chartcoach through
[chartcoach/skills](https://github.com/chartcoach/skills).

```bash
npx skills add chartcoach/skills
```

## Learn More

- 🌐 Browse [chartcoach](https://chartcoach.dev/).
- 📚 Explore the [Guideline Catalog](https://chartcoach.dev/guidelines/).
- 🧭 Read the [catalog docs](https://docs.chartcoach.dev/catalog).
- ✨ Read the [agent docs](https://docs.chartcoach.dev/agents).

## License

Apache-2.0. See [LICENSE](LICENSE).
