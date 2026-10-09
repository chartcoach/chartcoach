from __future__ import annotations

from typing import Annotated, Literal, TypeVar

from mcp.types import CallToolResult
from pydantic import BaseModel, ConfigDict, Field, RootModel

from chartcoach._catalog.errors import CatalogErrorCode

McpLimit = Annotated[int, Field(ge=1, le=100, strict=True)]
McpId = Annotated[str, Field(min_length=1)]
McpIds = Annotated[list[McpId], Field(min_length=1, max_length=100)]
McpRoles = Annotated[list[McpId], Field(max_length=100)]


class _ResultModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class TableColumnInfo(_ResultModel):
    name: str
    type: str


class TableInfo(_ResultModel):
    name: str
    rows: int
    columns: list[TableColumnInfo]


class VocabularyInfo(_ResultModel):
    name: str
    description: str
    examples: list[str]


class ProfileInfo(_ResultModel):
    name: str
    profile_schema_version: int
    documents_version: int
    embedding_functions: list[dict[str, object]]
    dimensions: int
    distance_metric: Literal["cosine", "l2", "dot"]
    python_requirements: dict[str, str]
    lancedb_version: str
    projection: dict[str, object] | None


class DescribeToolResult(_ResultModel):
    resolved_location: str | None
    release_digest: str | None
    entries_digest: str
    manifest_digest: str
    tables: list[TableInfo]
    section_roles: list[VocabularyInfo]
    label_families: list[VocabularyInfo]
    profiles: list[str]
    profile: ProfileInfo | None


class SqlColumn(_ResultModel):
    name: str
    type: str


class SqlToolResult(_ResultModel):
    columns: list[SqlColumn]
    rows: list[dict[str, object]]
    row_count: int
    truncated: bool
    limit: int
    entries_digest: str
    manifest_digest: str
    release_digest: str | None


class SectionRecord(_ResultModel):
    role: str
    title: str
    content: str


class SourceRecord(_ResultModel):
    reference_id: str
    authors_text: str | None = None
    year: str | None = None
    source_title: str | None = None
    doi: str | None = None
    url: str | None = None
    guideline_id: str | None = None
    source_type: str | None = None
    authors: list[str] | None = None
    journal: str | None = None
    booktitle: str | None = None
    publisher: str | None = None


class GuidelineEntryRecord(_ResultModel):
    id: str
    title: str
    description: str
    labels: list[str]
    sections: list[SectionRecord]
    sources: list[SourceRecord]
    references: list[str] | None = None


class CitationSource(_ResultModel):
    reference_id: str
    source_type: str | None
    authors_text: str | None
    year: str | None
    source_title: str | None
    journal: str | None
    booktitle: str | None
    publisher: str | None
    doi: str | None
    url: str | None
    citation: str


class CitationRecord(_ResultModel):
    id: str
    title: str
    url: str
    guideline_citation: str
    sources: list[CitationSource]


class ReadToolResult(_ResultModel):
    records: list[GuidelineEntryRecord]
    entries_digest: str
    manifest_digest: str
    release_digest: str | None


class CiteToolResult(_ResultModel):
    records: list[CitationRecord]
    entries_digest: str
    manifest_digest: str
    release_digest: str | None


class GuidelineMatch(_ResultModel):
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


class SearchToolResult(_ResultModel):
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


class ErrorBody(_ResultModel):
    code: CatalogErrorCode
    message: str
    details: dict[str, object]
    hints: list[str]


class ErrorToolResult(_ResultModel):
    error: ErrorBody


_ResultT = TypeVar("_ResultT", bound=BaseModel)


class _ObjectOutput(RootModel[_ResultT]):
    # MCP object schemas require an explicit root type even for object unions.
    model_config = ConfigDict(json_schema_extra={"type": "object"})


class DescribeOutput(_ObjectOutput[DescribeToolResult | ErrorToolResult]):
    pass


class SqlOutput(_ObjectOutput[SqlToolResult | ErrorToolResult]):
    pass


class ReadOutput(_ObjectOutput[ReadToolResult | ErrorToolResult]):
    pass


class CiteOutput(_ObjectOutput[CiteToolResult | ErrorToolResult]):
    pass


class SearchOutput(_ObjectOutput[SearchToolResult | ErrorToolResult]):
    pass


DescribeCallResult = Annotated[CallToolResult, DescribeOutput]
SqlCallResult = Annotated[CallToolResult, SqlOutput]
ReadCallResult = Annotated[CallToolResult, ReadOutput]
CiteCallResult = Annotated[CallToolResult, CiteOutput]
SearchCallResult = Annotated[CallToolResult, SearchOutput]
