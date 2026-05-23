from __future__ import annotations

import dataclasses as dc
from collections.abc import Mapping, Sequence
from typing import Any, cast


@dc.dataclass(frozen=True)
class SearchResultRow:
    query_index: int
    rank: int
    document_id: str
    guideline_id: str
    role: str
    distance: object
    labels: list[str]
    document: str


def flatten_search_result(result: Mapping[str, Any]) -> list[SearchResultRow]:
    """Return one row per Chroma match from a query/get response shape."""

    ids_by_query = _nested_list(result.get("ids"))
    docs_by_query = _nested_list(result.get("documents"))
    metas_by_query = _nested_list(result.get("metadatas"))
    distances_by_query = _nested_list(result.get("distances"))
    rows: list[SearchResultRow] = []

    for query_index, ids in enumerate(ids_by_query):
        documents = _list_at(docs_by_query, query_index)
        metadatas = _list_at(metas_by_query, query_index)
        distances = _list_at(distances_by_query, query_index)
        for rank_index, doc_id in enumerate(ids):
            metadata = _mapping_at(metadatas, rank_index)
            guideline_id = metadata.get("parent_id")
            role = metadata.get("role")
            if not isinstance(doc_id, str) or not isinstance(guideline_id, str):
                continue
            rows.append(
                SearchResultRow(
                    query_index=query_index,
                    rank=rank_index + 1,
                    document_id=doc_id,
                    guideline_id=guideline_id,
                    role=role if isinstance(role, str) else "",
                    distance=_at(distances, rank_index),
                    labels=_str_list(metadata.get("labels")),
                    document=str(_at(documents, rank_index) or ""),
                )
            )
    return rows


def _nested_list(value: object) -> list[list[object]]:
    if not isinstance(value, list):
        return []
    return [
        cast(list[object], item) if isinstance(item, list) else [] for item in value
    ]


def _list_at(values: Sequence[list[object]], index: int) -> list[object]:
    if index >= len(values):
        return []
    return values[index]


def _at(values: Sequence[object], index: int) -> object:
    if index >= len(values):
        return None
    return values[index]


def _mapping_at(values: Sequence[object], index: int) -> Mapping[str, object]:
    value = _at(values, index)
    if isinstance(value, Mapping):
        return cast(Mapping[str, object], value)
    return {}


def _str_list(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, str)]


__all__ = ["SearchResultRow", "flatten_search_result"]
