from __future__ import annotations

from collections.abc import Mapping

import polars as pl

from .collection import Catalog

GUIDELINES_RELATION = "guidelines"
SECTIONS_RELATION = "sections"
LABELS_RELATION = "labels"
GUIDELINE_LABELS_RELATION = "guideline_labels"
REFERENCES_RELATION = "reference_entries"
GUIDELINE_REFERENCES_RELATION = "guideline_references"

STRUCTURED_RELATIONS = (
    (GUIDELINES_RELATION, "guidelines_df"),
    (SECTIONS_RELATION, "sections_df"),
    (LABELS_RELATION, "labels_df"),
    (GUIDELINE_LABELS_RELATION, "guideline_labels_df"),
    (REFERENCES_RELATION, "references_df"),
    (GUIDELINE_REFERENCES_RELATION, "guideline_references_df"),
)


def catalog_relations(catalog: Catalog) -> Mapping[str, pl.DataFrame]:
    """Return the structured relations exposed by catalog tools and SQL."""

    return {
        relation_name: getattr(catalog, frame_attr)
        for relation_name, frame_attr in STRUCTURED_RELATIONS
    }


__all__ = [
    "GUIDELINES_RELATION",
    "GUIDELINE_LABELS_RELATION",
    "GUIDELINE_REFERENCES_RELATION",
    "LABELS_RELATION",
    "REFERENCES_RELATION",
    "SECTIONS_RELATION",
    "STRUCTURED_RELATIONS",
    "catalog_relations",
]
