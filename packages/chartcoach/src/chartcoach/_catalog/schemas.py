from __future__ import annotations

import polars as pl

SECTION_SCHEMA = pl.Struct(
    [
        pl.Field("role", pl.String),
        pl.Field("title", pl.String),
        pl.Field("content", pl.String),
    ]
)
CATALOG_SCHEMA = pl.Schema(
    {
        "id": pl.String,
        "title": pl.String,
        "description": pl.String,
        "labels": pl.List(pl.String),
        "sections": pl.List(SECTION_SCHEMA),
        "references": pl.List(pl.String),
    }
)
GUIDELINES_SCHEMA = {
    "id": pl.String,
    "title": pl.String,
    "description": pl.String,
    "labels": pl.List(pl.String),
    "body": pl.String,
    "sections": pl.List(SECTION_SCHEMA),
}
SECTIONS_SCHEMA = {
    "guideline_id": pl.String,
    "role": pl.String,
    "title": pl.String,
    "content": pl.String,
}
GUIDELINE_LABELS_SCHEMA = {
    "guideline_id": pl.String,
    "label": pl.String,
    "family": pl.String,
    "category": pl.String,
    "modifier": pl.String,
}
GUIDELINE_REFERENCES_SCHEMA = {
    "guideline_id": pl.String,
    "reference_id": pl.String,
}
REFERENCES_SCHEMA = {
    "id": pl.String,
    "source_type": pl.String,
    "authors": pl.List(pl.String),
    "authors_text": pl.String,
    "year": pl.String,
    "title": pl.String,
    "journal": pl.String,
    "booktitle": pl.String,
    "publisher": pl.String,
    "url": pl.String,
    "doi": pl.String,
    "bibtex": pl.String,
}
GUIDELINE_SOURCES_SCHEMA = {
    "guideline_id": pl.String,
    "reference_id": pl.String,
    "source_type": pl.String,
    "authors": pl.List(pl.String),
    "authors_text": pl.String,
    "year": pl.String,
    "source_title": pl.String,
    "journal": pl.String,
    "booktitle": pl.String,
    "publisher": pl.String,
    "url": pl.String,
    "doi": pl.String,
    "bibtex": pl.String,
}

__all__ = [
    "CATALOG_SCHEMA",
    "GUIDELINES_SCHEMA",
    "GUIDELINE_LABELS_SCHEMA",
    "GUIDELINE_REFERENCES_SCHEMA",
    "GUIDELINE_SOURCES_SCHEMA",
    "REFERENCES_SCHEMA",
    "SECTIONS_SCHEMA",
    "SECTION_SCHEMA",
]
