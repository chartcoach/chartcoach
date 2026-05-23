# chartcoach

Python tools for the ChartCoach guideline catalog.

The base package is deliberately small. It loads catalog parquet files, parses
guidelines, and exposes typed records plus Polars dataframe views.

```python
from chartcoach import Catalog

catalog = Catalog.from_parquet("guidelines/catalog.parquet")
catalog.frames.guidelines.select("id", "title")
```

Install `chartcoach[search]` when you need the optional retrieval stack:

```python
from chartcoach.search import ChromaIndex, connect_catalog

index = ChromaIndex.from_cache(catalog)
conn = connect_catalog(catalog, search=index)
```

Run the CLI with `uv run --package chartcoach chartcoach --help`.

Run tests with `pnpm --dir packages/catalog-python test`.

## License

MIT. See [LICENSE](LICENSE).
