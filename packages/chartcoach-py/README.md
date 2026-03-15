# ChartCoach

Python package for structured visualization guidance, retrieval, and agent/tool access.

## Mental Model

- `Catalog`: the structured knowledge base
- `ChartCoach`: the high-level runtime/bootstrap facade around a `Catalog`
- `CatalogIndex`: the low-level vector/relational index object
- `CatalogIndexTools`: the raw agent-facing query surface over DuckDB and Chroma
- `chartcoach.mcp`: the MCP transport wrapper over `ChartCoach` and `CatalogIndexTools`

## MCP Runtime

- Use `chartcoach mcp` to start the read-only MCP server.
- `chartcoach mcp --help` documents the full launch surface, including the
  config and runtime env vars that each flag overrides.
- CLI flags override environment variables. For convenient spawning the command
  falls back to env vars and then its built-in defaults.
- Set `CHARTCOACH_CATALOG_PATH` or pass `--catalog-path` before startup so the
  entrypoint can ensure the cached parquet, Chroma collection, DuckDB file, and
  manifest exist first.
- The MCP read surface is just `duckdb_query`, `chroma_query`, and `chroma_get`.
- Use `duckdb_query("SHOW ALL TABLES")` and `duckdb_query("DESCRIBE ...")` for
  relational discovery; richer initialization or cache mutation flows are not
  part of the MCP tool contract.
