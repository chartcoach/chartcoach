from __future__ import annotations

from collections.abc import Mapping
from importlib.metadata import PackageNotFoundError, version
from typing import TYPE_CHECKING, Any, Literal, cast

from typing_extensions import TypedDict

from .errors import (
    CatalogCapabilityError,
    CatalogEmbeddingError,
    CatalogError,
    CatalogProfileError,
    CatalogValidationError,
)
from .identity import catalog_identity
from .profiles import ProfileMetadata, validate_embedding_model

if TYPE_CHECKING:
    from .model import Catalog


class GuidelineMatch(TypedDict):
    """One unique guideline match from index search."""

    rank: int
    id: str
    title: str
    description: str
    labels: list[str]
    matched_document_id: str
    matched_role: str
    matched_excerpt: str
    excerpt_truncated: bool
    score: float | None
    score_kind: Literal["distance", "relevance"]


class SearchResult(TypedDict):
    """One bounded index search result with catalog digests and location."""

    query: str
    profile: str
    mode: Literal["fts", "vector", "hybrid"]
    score_kind: Literal["distance", "relevance"]
    matches: list[GuidelineMatch]
    match_count: int
    documents_considered: int
    documents_truncated: bool
    limit: int
    where: str | None
    resolved_location: str | None
    entries_digest: str
    manifest_digest: str
    release_digest: str | None


def catalog_search(
    catalog: Catalog,
    text: str,
    *,
    profile: str,
    mode: Literal["fts", "vector", "hybrid"] = "fts",
    limit: int = 10,
    where: str | None = None,
) -> SearchResult:
    """Search one index profile and return compact guideline matches."""

    if not isinstance(text, str) or not text.strip():
        raise CatalogValidationError("Search text must be a non-empty string.")
    if mode not in {"fts", "vector", "hybrid"}:
        raise CatalogValidationError(f"Unsupported search mode: {mode!r}.")
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
        raise CatalogValidationError("Search limit must be at least 1.")

    metadata = catalog._profile_metadata(profile)
    if mode != "fts":
        _validate_semantic_environment(metadata, profile=profile)

    table = catalog._search_table(profile)
    try:
        query = table.search(
            text,
            query_type=mode,
            fts_columns="text",
            vector_column_name="vector",
        )
        if where:
            query = query.where(where)
        if mode != "fts":
            query = cast(Any, query).distance_type(metadata.distance_metric)
        document_hits = query.limit(limit + 1).to_list()
    except CatalogError:
        raise
    except Exception as exc:
        if mode == "fts":
            raise CatalogValidationError(
                f"LanceDB full-text search failed for profile {profile!r}.",
                details={"profile": profile, "exception_type": type(exc).__name__},
            ) from exc
        raise CatalogEmbeddingError(
            f"LanceDB embedding search failed for profile {profile!r}.",
            details={"profile": profile, "exception_type": type(exc).__name__},
            hints=[
                "Register the profile alias, install its exact requirements, and set required registry variables."
            ],
        ) from exc

    considered = document_hits[:limit]
    parent_ids: list[str] = []
    for hit in considered:
        parent_id = _match_string(hit, "parent_id")
        if parent_id not in parent_ids:
            parent_ids.append(parent_id)
    candidates = {
        str(row["id"]): row
        for row in catalog.query(
            ids=parent_ids, limit=max(1, len(parent_ids))
        ).to_dicts()
    }
    score_kind: Literal["distance", "relevance"] = (
        "distance" if mode == "vector" else "relevance"
    )
    matches: list[GuidelineMatch] = []
    seen: set[str] = set()
    for hit in considered:
        guideline_id = _match_string(hit, "parent_id")
        if guideline_id in seen:
            continue
        seen.add(guideline_id)
        record = candidates.get(guideline_id)
        if record is None:
            raise CatalogProfileError(
                f"Indexed guideline entry is absent from the catalog: {guideline_id}",
                details={"profile": profile, "guideline_id": guideline_id},
            )
        excerpt, excerpt_truncated = _excerpt(_match_string(hit, "text"))
        matches.append(
            {
                "rank": len(matches) + 1,
                "id": guideline_id,
                "title": _record_string(record, "title"),
                "description": _record_string(record, "description"),
                "labels": _record_labels(record),
                "matched_document_id": _match_string(hit, "id"),
                "matched_role": _match_string(hit, "role"),
                "matched_excerpt": excerpt,
                "excerpt_truncated": excerpt_truncated,
                "score": _match_score(hit),
                "score_kind": score_kind,
            }
        )

    identity = catalog_identity(catalog)
    return {
        "query": text,
        "profile": profile,
        "mode": mode,
        "score_kind": score_kind,
        "matches": matches,
        "match_count": len(matches),
        "documents_considered": len(considered),
        "documents_truncated": len(document_hits) > limit,
        "limit": limit,
        "where": where,
        "resolved_location": catalog._resolved_location,
        "entries_digest": identity["entries_digest"],
        "manifest_digest": identity["manifest_digest"],
        "release_digest": identity["release_digest"],
    }


def _validate_semantic_environment(metadata: ProfileMetadata, *, profile: str) -> None:
    binding = metadata.embedding_functions[0]
    try:
        from lancedb.embeddings import get_registry
    except ModuleNotFoundError as exc:
        raise CatalogCapabilityError(
            "Semantic search requires the chartcoach index dependencies.",
            details={"profile": profile},
            hints=["Install chartcoach[index]."],
        ) from exc
    try:
        definition = get_registry().get(binding.name)
    except KeyError as exc:
        raise CatalogCapabilityError(
            f"Embedding alias {binding.name!r} is not registered.",
            details={"profile": profile, "alias": binding.name},
            hints=[
                "Register a trusted LanceDB EmbeddingFunction class under this alias before semantic search."
            ],
        ) from exc

    validate_embedding_model(
        binding.model,
        allowed_fields=frozenset(definition.model_fields),
        sensitive_fields=frozenset(definition.sensitive_keys()),
    )
    mismatches: dict[str, str] = {}
    for distribution, expected in metadata.python_requirements.items():
        try:
            actual = version(distribution)
        except PackageNotFoundError:
            actual = "missing"
        if actual != expected:
            mismatches[distribution] = actual
    if mismatches:
        raise CatalogCapabilityError(
            f"Profile {profile!r} requirements are unavailable or incompatible.",
            details={
                "profile": profile,
                "expected": dict(metadata.python_requirements),
                "actual": mismatches,
            },
            hints=[
                "Install the exact versions reported by catalog.describe(profile=...)."
            ],
        )


def _excerpt(text: str) -> tuple[str, bool]:
    if len(text) <= 360:
        return text, False
    return text[:357] + "...", True


def _match_string(row: Mapping[str, object], key: str) -> str:
    value = row.get(key)
    if not isinstance(value, str) or not value:
        raise CatalogProfileError(f"Indexed document is missing string field {key!r}.")
    return value


def _match_score(row: Mapping[str, object]) -> float | None:
    for key in ("_relevance_score", "_score", "_distance"):
        value = row.get(key)
        if isinstance(value, int | float):
            return float(value)
    return None


def _record_string(row: Mapping[str, object], key: str) -> str:
    value = row.get(key)
    if not isinstance(value, str):
        raise CatalogProfileError(f"Catalog record has invalid field {key!r}.")
    return value


def _record_labels(row: Mapping[str, object]) -> list[str]:
    labels = row.get("labels")
    if not isinstance(labels, list) or not all(
        isinstance(item, str) for item in labels
    ):
        raise CatalogProfileError("Catalog record has invalid labels.")
    return labels


__all__ = ["GuidelineMatch", "SearchResult", "catalog_search"]
