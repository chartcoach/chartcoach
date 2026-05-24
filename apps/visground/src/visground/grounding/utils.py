from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Mapping, Sequence
from typing import Any, cast

from chartcoach import Catalog
from chartcoach.search import ChromaIndex

from .types import GroundingRecord


@dataclass(frozen=True, slots=True)
class SearchContext:
    catalog: Catalog
    index: ChromaIndex


def rrf_fuse(
    ranked_lists: Sequence[Sequence[str]],
    *,
    k: int = 60,
) -> list[str]:
    scores: dict[str, float] = {}
    for ranked in ranked_lists:
        for rank, doc_id in enumerate(ranked, start=1):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank)

    return [
        doc_id
        for doc_id, _ in sorted(
            scores.items(),
            key=lambda item: item[1],
            reverse=True,
        )
    ]


def build_grounding_record(
    search: SearchContext,
    doc_ids: Sequence[str],
) -> GroundingRecord:
    selected_doc_ids = list(doc_ids)
    if not selected_doc_ids:
        return {
            "doc_ids": [],
            "guideline_ids": [],
            "guidance": [],
        }

    document_texts = chroma_document_texts(search.index, selected_doc_ids)
    missing = [doc_id for doc_id in selected_doc_ids if doc_id not in document_texts]
    if missing:
        raise ValueError(f"Chroma index is missing document id(s): {', '.join(missing)}")
    guidance = [document_texts[doc_id] for doc_id in selected_doc_ids]

    return {
        "doc_ids": selected_doc_ids,
        "guideline_ids": [doc_id.split("---")[0] for doc_id in selected_doc_ids],
        "guidance": guidance,
    }


def chroma_document_texts(
    index: ChromaIndex,
    doc_ids: Sequence[str],
) -> dict[str, str]:
    result = cast(
        Mapping[str, object],
        index.collection.get(ids=list(doc_ids), include=["documents"]),
    )
    ids = result.get("ids")
    documents = result.get("documents")
    if not isinstance(ids, list) or not isinstance(documents, list):
        return {}
    return {
        doc_id: document
        for doc_id, document in zip(ids, documents)
        if isinstance(doc_id, str) and isinstance(document, str)
    }


def chroma_document_metadata(index: ChromaIndex) -> list[dict[str, Any]]:
    result = cast(
        Mapping[str, object],
        index.collection.get(include=["metadatas"]),
    )
    ids = result.get("ids")
    metadatas = result.get("metadatas")
    if not isinstance(ids, list) or not isinstance(metadatas, list):
        return []

    rows: list[dict[str, Any]] = []
    for doc_id, metadata in zip(ids, metadatas):
        if not isinstance(doc_id, str) or not isinstance(metadata, Mapping):
            continue
        row = {str(key): value for key, value in metadata.items()}
        row["id"] = doc_id
        rows.append(row)
    return rows
