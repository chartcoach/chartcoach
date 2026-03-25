# ChartCoach

ChartCoach helps you search and inspect a catalog of chart guidance.

## Mental Model

- `Catalog` is the source collection of guidelines and references.
- `Index` is the prepared search and table data built from that catalog.
- `Tools` gives you a small API for semantic search, direct lookup, and SQL.
- `Coach` brings those pieces together in one ready object.

## Get Started

```python
import chartcoach as cc

coach = cc.create()
```

`create()` loads the default catalog, reuses cached work when it can, and builds the missing pieces when it has to.
It also wraps the active embedding function in a persistent per-text embedding cache by default.

## Common Tasks

Create a coach with a custom cache directory:

```python
import chartcoach as cc

coach = cc.create(cache_dir="./.cache/chartcoach")
```

Disable embedding caching for one coach:

```python
import chartcoach as cc

coach = cc.create(cache_embeddings=False)
```

Search for related guidance with plain language:

```python
results = coach.tools.search(
    "How should I label bars when I want fast comparison?",
    limit=5,
)
```

Search works by turning your query into an embedding and finding the stored guideline text that is closest in meaning.
If you already know part of the scope, you can narrow the search first with metadata filters and let semantic search rank only that smaller set.

Inspect stored documents directly:

```python
records = coach.tools.get(limit=3)
```

Ask simple SQL questions about the prepared tables:

```python
tables = coach.tools.sql("show all tables")
labels = coach.tools.sql('select * from "guideline_labels" limit 5')
```

Use a native Chroma embedding function:

```python
import os

import chromadb.utils.embedding_functions as embedding_functions
import chartcoach as cc

openrouter_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.environ["OPENROUTER_API_KEY"],
    api_base="https://openrouter.ai/api/v1",
    model_name="openai/text-embedding-3-small",
)

coach = cc.create(embedding_fn=openrouter_ef)
```

Custom embeddings are supported through actual Chroma embedding function instances.
ChartCoach caches embeddings for custom functions by default too. Pass `cache_embeddings=False` if you want to use the raw embedding function instance unchanged.
ChartCoach uses `embedding_fn.model_name` when it exists, otherwise `embedding_fn.name()`.
For the cache directory name, `/` is replaced with `-` so model names such as `openai/text-embedding-3-small` stay readable.

## Cache Behavior

By default, `create()` also enables a persistent embedding cache for the active embedding function, including Chroma's default embedding function when you do not pass `embedding_fn`.
Disable that wrapper with `cache_embeddings=False`.

ChartCoach stores cached artifacts under your cache directory in a folder chosen from:

- the catalog contents
- the embedding function name

This means different catalogs or different embedding-function names get their own cache entries.
The current layout is:

```text
<cache_root>/
  <catalog_digest>/
    <embedding-name>/
      chroma_db/
      duckdb_catalog.db
```

Embedding names are kept readable. The only path rewrite is `/` to `-`.

Use `cache_mode` to control how strict `create()` should be:

- `"reuse_or_create"`: use a matching cache if it exists, otherwise build it
- `"reuse_only"`: require a matching cache to already exist
- `"force_rebuild"`: rebuild that exact cache entry from scratch

## MCP

Use `chartcoach mcp` to expose the same tools over MCP.
