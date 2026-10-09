"""Optional, native LanceDB embedding adapters for OpenAI-compatible endpoints."""

from __future__ import annotations

from lancedb.embeddings import register
from lancedb.embeddings.openai import OpenAIEmbeddings
from pydantic import Field


@register("chartcoach-openai-compatible")
class OpenAICompatibleEmbeddings(OpenAIEmbeddings):
    """Use arbitrary model IDs with an explicit, release-owned vector dimension.

    Inherits LanceDB's OpenAI transport, query/source embedding methods, retries,
    and sensitive registry variables. Install chartcoach[embedding-openai].
    """

    name: str = Field(min_length=1)
    dim: int = Field(gt=0)

    def ndims(self) -> int:
        return self.dim


__all__ = ["OpenAICompatibleEmbeddings"]
