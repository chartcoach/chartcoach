# Embedding + Retrieval Architecture (Draft)

## Goal
Separate guideline representation, embedding computation, vector indexing, and retrieval so each can evolve independently without cross-coupling.

## Non-Goals
- Do not introduce a “framework” or heavy abstraction layers.
- Do not redesign guideline parsing/serialization unless required by boundary cleanup.
- Do not change notebook semantics (only update imports / wiring as needed).

## Proposed Module Boundaries
- `chartcoach.catalog`: Guideline and catalog representation + parsing/serialization.
- `chartcoach.cataloging`: Building a catalog from sources (LLM + provenance).
- `chartcoach.embedding`: Embedding + projection utilities (text -> vectors); no DuckDB/Lance.
- `chartcoach.index`: Optional vector indexing backends (DuckDB/Lance) that accept embedded vectors and materialize an index.
- `chartcoach.retrieval`: Retrieval strategies that operate over a `Catalog` and optionally a vector index.

## Dependency Direction (inversion-friendly)
- `catalog` is the “core” and should not import other layers.
- `embedding` contains both:
  - pure embedding utilities (no index deps)
  - catalog adapters (`CatalogEmbedder`, `CatalogTextSource`) that depend on `catalog`
- `chartcoach.index` depends on vector representations, not on how vectors are produced.
- `retrieval` is the integration layer that composes: `Catalog` + (optional) embedding + (optional) vector index.

## Lean APIs (what crosses boundaries)
### Embedding (`chartcoach.embedding`)
- `embed_text(text_df: pl.DataFrame, ...) -> pl.DataFrame` where `text_df` contains `{id, role, content}`.
- `project_embedded_text(embedded_text_df: pl.DataFrame, ...) -> pl.DataFrame`.
- `CatalogEmbedder(catalog).embedded_text_df(...)` as a convenience for catalog→text→vectors.

### Vector indexing (`chartcoach.index`)
- `VectorIndexBackend.index(embedded_text_df, ...) -> VectorIndex` where `VectorIndex.search(query_vector, ...)` returns ranked matches.
- Backends:
  - `DuckDBVectorIndexBackend` (optional dep: `duckdb`)
  - `LanceVectorIndexBackend` (optional dep: `lancedb`)
  - `InMemoryVectorIndexBackend` (no optional deps; useful for dev/tests)

### Catalog→text extraction (`chartcoach.embedding`)
- `CatalogTextSource.text_df(catalog: Catalog) -> pl.DataFrame` (pluggable, composable sources).

### Retrieval strategies (`chartcoach.retrieval`)
- Start with primitives only (protocol + result types), then implement concrete strategies incrementally:
  - `Retriever.retrieve(query: str, *, k: int = 10, ...) -> list[RetrievalHit]`

## Usage Sketch (post-refactor)
```python
from chartcoach.catalog import Catalog
from chartcoach.embedding import CatalogEmbedder
from chartcoach.index import DuckDBVectorIndexBackend, InMemoryVectorIndexBackend

catalog = Catalog.from_disk("guidelines")
embedder = CatalogEmbedder(catalog)

embedded = embedder.embedded_text_df(model="text-embedding-3-small", text_projector_type="litellm")

# Backend-free dev loop
mem_index = InMemoryVectorIndexBackend().index(embedded)

# DuckDB-powered SQL workflows
duck_index = DuckDBVectorIndexBackend().index(embedded)
conn = duck_index.conn  # use `.sql(...)` / `.query(...)` on DuckDB connection
```

## Next
- Add first retrieval strategies in `chartcoach.retrieval` (e.g., semantic + hybrid + rule-based), using `VectorIndex` as the backend-agnostic interface.
- Decide how you want to model queries/filters (labels, roles, audience/task metadata) as inputs to retrieval.
