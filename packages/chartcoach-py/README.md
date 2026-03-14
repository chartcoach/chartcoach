# ChartCoach

Python package for structured visualization guidance, retrieval, and agent/tool access.

## Mental Model

- `Catalog`: the structured knowledge base
- `ChartCoach`: the high-level runtime/bootstrap facade around a `Catalog`
- `CatalogIndex`: the low-level vector/relational index object
- `CatalogIndexTools`: the raw agent-facing query surface over DuckDB and Chroma
- `chartcoach.mcp`: the MCP transport wrapper over `ChartCoach` and `CatalogIndexTools`

## MCP Runtime

- `chartcoach-mcp` is read-only once it starts serving requests.
- Set `CHARTCOACH_CATALOG_PATH` before startup so the entrypoint can ensure the
  cached parquet, Chroma collection, DuckDB file, and manifest exist first.
- The exposed discovery surface is `read_info`; richer initialization or cache
  mutation flows are not part of the MCP tool contract.
