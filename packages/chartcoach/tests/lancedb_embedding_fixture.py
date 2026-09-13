from __future__ import annotations

import os
from typing import Any

import numpy as np
from lancedb.embeddings import TextEmbeddingFunction, get_registry

ALIAS = "chartcoach-distinct-lancedb-test"
SECRET_ALIAS = "chartcoach-variable-lancedb-test"


def registered_embedding():
    """Return a reconstructable embedding with distinct source and query methods."""

    registry = get_registry()
    try:
        definition = registry.get(ALIAS)
    except KeyError:

        @registry.register(ALIAS)
        class DistinctEmbedding(TextEmbeddingFunction):
            source_instruction: str
            query_instruction: str

            def ndims(self) -> int:
                return 4

            def compute_source_embeddings(
                self,
                texts: Any,
                *args: Any,
                **kwargs: Any,
            ) -> list[np.ndarray | None]:
                if os.environ.get("CHARTCOACH_QUERY_PROCESS") == "1":
                    raise AssertionError("query process called source embeddings")
                return self._vectors(texts, instruction=self.source_instruction)

            def compute_query_embeddings(
                self,
                query: str,
                *args: Any,
                **kwargs: Any,
            ) -> list[np.ndarray | None]:
                marker = os.environ.get("CHARTCOACH_QUERY_MARKER")
                if marker:
                    with open(marker, "a", encoding="utf-8") as output:
                        output.write("query\n")
                return self._vectors([query], instruction=self.query_instruction)

            def generate_embeddings(
                self,
                texts: Any,
                *args: Any,
                **kwargs: Any,
            ) -> list[np.ndarray | None]:
                return self._vectors(texts, instruction=self.source_instruction)

            def _vectors(
                self, texts: Any, *, instruction: str
            ) -> list[np.ndarray | None]:
                values = self.sanitize_input(texts)
                return [
                    np.asarray(
                        [
                            1.0 if "direct" in str(text).casefold() else 0.0,
                            1.0 if "label" in str(text).casefold() else 0.0,
                            float(len(instruction)),
                            1.0,
                        ],
                        dtype=np.float32,
                    )
                    for text in values
                ]

        definition = DistinctEmbedding
    return definition.create(
        source_instruction="document",
        query_instruction="query",
        max_retries=0,
    )


def variable_embedding_definition():
    """Return a registered embedding whose API key uses a LanceDB variable."""

    registry = get_registry()
    try:
        return registry.get(SECRET_ALIAS)
    except KeyError:

        @registry.register(SECRET_ALIAS)
        class VariableEmbedding(TextEmbeddingFunction):
            api_key: str

            @staticmethod
            def sensitive_keys() -> list[str]:
                return ["api_key"]

            def ndims(self) -> int:
                return 4

            def generate_embeddings(
                self,
                texts: Any,
                *args: Any,
                **kwargs: Any,
            ) -> list[np.ndarray | None]:
                values = self.sanitize_input(texts)
                return [
                    np.asarray(
                        [
                            1.0 if "direct" in str(text).casefold() else 0.0,
                            1.0 if "label" in str(text).casefold() else 0.0,
                            1.0,
                            1.0,
                        ],
                        dtype=np.float32,
                    )
                    for text in values
                ]

        return VariableEmbedding


__all__ = [
    "ALIAS",
    "SECRET_ALIAS",
    "registered_embedding",
    "variable_embedding_definition",
]
