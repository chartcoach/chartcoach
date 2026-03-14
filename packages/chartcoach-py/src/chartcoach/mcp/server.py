from __future__ import annotations

import logging
from functools import cache
from typing import Any

from mcp.server import FastMCP

from ..coach import ChartCoach, ChartCoachConfig

mcp = FastMCP("chartcoach", json_response=True)
_coach: ChartCoach | None = None
logger = logging.getLogger(__name__)


@cache
def _config() -> ChartCoachConfig:
    return ChartCoachConfig.from_env()


def _coach_from_cache() -> ChartCoach:
    global _coach
    if _coach is None:
        _coach = ChartCoach.from_cache(config=_config())
    return _coach


def _reset_cached_state() -> None:
    global _coach
    _coach = None
    _config.cache_clear()


@mcp.tool()
def index_status() -> dict[str, Any]:
    """Check whether the server is pointing at a ready, queryable local index.

    Call this when you need operational confidence before issuing larger reads.
    The result tells you where the frozen artifacts live, whether each expected
    file exists, and whether the server considers the cache ready overall.

    The most useful fields for clients are usually:

    - ``ready``: whether all required artifacts are present
    - ``artifacts``: concrete local paths for manifest, parquet, Chroma, and DuckDB
    - ``manifest``: catalog source, digest, build time, and entry count

    Use this tool for health checks, debugging configuration issues, or
    confirming which catalog snapshot the server has loaded.
    """
    return ChartCoach.cache_status(config=_config())


@mcp.tool()
def read_info(sample_limit: int | None = None) -> dict[str, Any]:
    """Get the one-stop map of the ChartCoach read surface before querying it.

    This is the best first tool for a client that has not seen the server
    before. It explains how the relational and vector sides fit together and
    gives just enough sample data to plan follow-up calls without guessing.

    The response is especially useful for:

    - finding the main DuckDB relations and their columns
    - understanding how Chroma ids and metadata join back to DuckDB rows
    - seeing the available chunk roles and default query settings
    - inspecting representative documents, metadata, and field shapes

    ``sample_limit`` controls how much example data is included in the payload.
    Keep it small when you only need orientation; increase it when you want a
    richer sample before writing SQL or retrieval filters.
    """
    return (
        _coach_from_cache().tools(auto_build=False).read_info(sample_limit=sample_limit)
    )


@mcp.tool()
def duckdb_query(sql: str, row_limit: int | None = None) -> dict[str, Any]:
    """Run a read-only DuckDB query when you want exact relational analysis.

    Use this after ``read_info`` when you need counting, grouping, joins, or
    filtering over the structured catalog tables. This is the right tool when
    you already know the shape of the data and want precise tabular results.

    Typical client patterns include:

    - counting chunk roles or labels
    - joining ``embeddings`` back to ``catalog_df`` by guideline id
    - filtering guidelines by labels, sections, or text-derived summaries

    ``row_limit`` caps the returned rows, and the response tells you whether the
    output was truncated. Only a single read-only SQL statement is allowed.
    """
    return (
        _coach_from_cache()
        .tools(auto_build=False)
        .duckdb_query(
            sql,
            row_limit=row_limit,
        )
    )


@mcp.tool()
def chroma_query(
    query_texts: list[str],
    n_results: int | None = None,
    where: dict[str, Any] | None = None,
    where_document: dict[str, Any] | None = None,
    include: list[str] | None = None,
) -> dict[str, Any]:
    """Run semantic retrieval over the ChartCoach document chunks.

    Use this when you want the most relevant guidance for a natural-language
    question such as a design problem, a critique target, or a rewrite goal.
    Start with plain ``query_texts`` and add filters only when you need to
    narrow the search to a role or a known guideline family.

    Practical examples:

    - search for advice about legends, labels, clutter, or color use
    - restrict results to one chunk type with ``where={"role": "section.advice"}``
    - combine semantic search with content filters when you need a specific phrase

    ``n_results`` controls how many matches you get per query text. By default
    the response includes documents, metadata, and distances, which is usually
    enough to rank results and decide whether to follow up with ``chroma_get``
    or a DuckDB query.
    """
    return (
        _coach_from_cache()
        .tools(auto_build=False)
        .chroma_query(
            query_texts,
            n_results=n_results,
            where=where,
            where_document=where_document,
            include=include,
        )
    )


@mcp.tool()
def chroma_get(
    ids: list[str] | None = None,
    where: dict[str, Any] | None = None,
    where_document: dict[str, Any] | None = None,
    include: list[str] | None = None,
    limit: int | None = None,
    offset: int | None = None,
) -> dict[str, Any]:
    """Fetch Chroma documents directly by id or by filter instead of by similarity.

    Use this when you already know what you want to retrieve: a specific chunk,
    all chunks for one guideline, or a paginated slice of documents that match
    a metadata condition.

    Common client uses include:

    - fetching ids returned earlier by ``chroma_query``
    - listing all chunks for one guideline via ``where={"parent_id": "..."}``
    - browsing a role such as ``section.advice`` with ``limit`` and ``offset``

    This is the best tool for deterministic retrieval. By default it returns
    documents and metadata, and you can narrow or expand the payload with
    ``include`` when needed.
    """
    return (
        _coach_from_cache()
        .tools(auto_build=False)
        .chroma_get(
            ids=ids,
            where=where,
            where_document=where_document,
            include=include,
            limit=limit,
            offset=offset,
        )
    )


def main() -> None:
    """Ensure frozen artifacts exist, then run the ChartCoach MCP server."""
    global _coach
    try:
        config = _config()
        logger.info(
            "🚀 Starting ChartCoach MCP server with cache_dir=%s collection_name=%s catalog_uri=%s",
            config.cache_dir,
            config.collection_name,
            config.catalog_uri,
        )

        logger.info("🧱 Ensuring ChartCoach cache artifacts exist before server start")
        ChartCoach.ensure_cache(config=config)

        logger.info("📦 Loading ChartCoach cache-backed runtime")
        _coach = ChartCoach.from_cache(config=config)

        logger.info("🔎 Loading cached ChartCoach index into memory")
        _coach.load_index()

        logger.info("🟢 ChartCoach MCP startup complete; entering FastMCP run loop")
        mcp.run()
    except Exception:
        logger.exception("ChartCoach MCP startup failed")
        raise
