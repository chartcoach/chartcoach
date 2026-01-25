from __future__ import annotations

import base64
from typing import Annotated, Any, Literal

import polars as pl
from pydantic import BaseModel, ConfigDict, Field, PlainSerializer, field_serializer
from pydantic.functional_validators import BeforeValidator
from pydantic.json_schema import WithJsonSchema

from chartcoach.catalog import Catalog


def _parse_bytes_or_base64(value: object) -> bytes | None:
    if value is None:
        return None
    if isinstance(value, bytes):
        return value
    if isinstance(value, str):
        try:
            return base64.b64decode(value, validate=True)
        except Exception as e:  # noqa: BLE001
            raise ValueError("Invalid base64 payload.") from e
    raise ValueError("Expected bytes or base64 string.")


BytesField = Annotated[
    bytes | None,
    BeforeValidator(_parse_bytes_or_base64),
    PlainSerializer(
        lambda v: base64.b64encode(v).decode("ascii") if v is not None else None,
        return_type=str | None,
        when_used="json",
    ),
    WithJsonSchema(
        {
            "type": ["string", "null"],
            "contentEncoding": "base64",
        }
    ),
]


CatalogField = Annotated[
    Catalog,
    WithJsonSchema(
        {
            "type": "array",
            "items": {"type": "object"},
            "description": "Catalog entries (serialized).",
        }
    ),
]

PolarsDataFrameField = Annotated[
    pl.DataFrame,
    WithJsonSchema(
        {
            "type": "object",
            "description": "Polars DataFrame (not JSON serializable).",
        }
    ),
]


class _RetrievalBaseModel(BaseModel):
    model_config = ConfigDict(
        frozen=True,
        arbitrary_types_allowed=True,
    )


class TextItem(_RetrievalBaseModel):
    kind: Literal["text"] = "text"
    role: str = "note"
    text: str = ""
    lang: str | None = None


class ImageItem(_RetrievalBaseModel):
    kind: Literal["image"] = "image"
    role: str = "chart"
    uri: str | None = None
    mime: str | None = None
    data: BytesField = None


class TableItem(_RetrievalBaseModel):
    kind: Literal["table"] = "table"
    role: str = "dataset"
    df: PolarsDataFrameField | None = None
    uri: str | None = None
    mime: str | None = None


class FileItem(_RetrievalBaseModel):
    kind: Literal["file"] = "file"
    role: str = "attachment"
    uri: str | None = None
    mime: str | None = None
    data: BytesField = None


ContextItem = Annotated[
    TextItem | ImageItem | TableItem | FileItem,
    Field(discriminator="kind"),
]


class RetrievalRequest(_RetrievalBaseModel):
    """Context-first retrieval request with lean metadata."""

    context: list[ContextItem] = Field(default_factory=list)
    lang: str = "en"
    meta: dict[str, object] = Field(default_factory=dict)
    k: int = 10


class RetrievalResponse(_RetrievalBaseModel):
    """Retrieved guidelines (as a sub-catalog) plus lean telemetry metadata."""

    catalog: CatalogField
    meta: dict[str, object] = Field(default_factory=dict)

    @field_serializer("catalog")
    def _serialize_catalog(self, catalog: Catalog, _info) -> list[dict[str, Any]]:
        return [entry.model_dump() for entry in catalog.entries]
