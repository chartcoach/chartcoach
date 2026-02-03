from __future__ import annotations

import hashlib
import importlib
import json
from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import Any, Literal, Protocol, TypedDict

import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.embedding import (
    CatalogEmbedder,
    CatalogTextSource,
    GuidelineAbstractTextSource,
    GuidelineFieldTextSource,
    GuidelineLabelsTextSource,
    SectionsTextSource,
    SectionsWithTitleTextSource,
)


def _sha256_hexdigest(payload: object) -> str:
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), default=str
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


SparseVector = tuple[list[int], list[float]]


class SparseEmbedder(Protocol):
    def embed(self, texts: Sequence[str]) -> list[SparseVector]: ...


class SparseIndexMeta(TypedDict):
    provider: str
    model: str
    digest: str
    text_sources: list[dict[str, object]]


@dataclass(frozen=True, slots=True)
class SparseEmbeddingConfig:
    provider: Literal["transformers"] = "transformers"
    model: str = "naver/splade-cocondenser-ensembledistil"
    max_length: int = 256
    top_k_terms: int = 128

    def digest(self) -> str:
        return _sha256_hexdigest(
            {
                "version": 1,
                "provider": self.provider,
                "model": self.model,
                "max_length": int(self.max_length),
                "top_k_terms": int(self.top_k_terms),
            }
        )[:16]


def _require_transformers():  # pragma: no cover
    try:  # pragma: no cover
        torch = importlib.import_module("torch")  # pragma: no cover
        transformers = importlib.import_module("transformers")  # pragma: no cover
    except ModuleNotFoundError as e:  # pragma: no cover
        raise RuntimeError(  # pragma: no cover
            "Neural sparse retrieval requires `torch` + `transformers`. "
            "Install `chartcoach[retrieval-sparse]`."
        ) from e
    return transformers, torch  # pragma: no cover


class _TransformersSpladeEmbedder:
    def __init__(self, *, config: SparseEmbeddingConfig) -> None:  # pragma: no cover
        transformers, torch = _require_transformers()  # pragma: no cover
        self._torch: Any = torch  # pragma: no cover
        self._config = config  # pragma: no cover
        self._tokenizer = transformers.AutoTokenizer.from_pretrained(
            config.model
        )  # pragma: no cover
        self._model = transformers.AutoModelForMaskedLM.from_pretrained(
            config.model
        )  # pragma: no cover
        self._model.eval()  # pragma: no cover
        self._device = torch.device("cpu")  # pragma: no cover
        self._model.to(self._device)  # pragma: no cover
        self._special_ids = set(
            getattr(self._tokenizer, "all_special_ids", []) or []
        )  # pragma: no cover

    def embed(self, texts: Sequence[str]) -> list[SparseVector]:  # pragma: no cover
        torch = self._torch  # pragma: no cover
        if not texts:  # pragma: no cover
            return []  # pragma: no cover

        encoded = self._tokenizer(  # pragma: no cover
            list(texts),  # pragma: no cover
            truncation=True,  # pragma: no cover
            padding=True,  # pragma: no cover
            max_length=int(self._config.max_length),  # pragma: no cover
            return_tensors="pt",  # pragma: no cover
        )  # pragma: no cover
        encoded = {
            k: v.to(self._device) for k, v in encoded.items()
        }  # pragma: no cover
        attention_mask = encoded.get("attention_mask")  # pragma: no cover

        with torch.no_grad():  # pragma: no cover
            logits = self._model(**encoded).logits  # pragma: no cover

        # SPLADE pooling: log(1 + relu(logits)), max over token positions.
        activations = torch.log1p(torch.relu(logits))  # pragma: no cover
        if attention_mask is not None:  # pragma: no cover
            activations = activations * attention_mask.unsqueeze(-1)  # pragma: no cover
        weights = activations.max(dim=1).values  # pragma: no cover

        if self._special_ids:  # pragma: no cover
            weights[:, list(self._special_ids)] = 0.0  # pragma: no cover

        top_k = max(1, int(self._config.top_k_terms))  # pragma: no cover
        top_k = min(top_k, int(weights.shape[1]))  # pragma: no cover
        values, indices = torch.topk(weights, k=top_k, dim=1)  # pragma: no cover

        out: list[SparseVector] = []  # pragma: no cover
        for row_vals, row_idx in zip(  # pragma: no cover
            values.cpu().tolist(),
            indices.cpu().tolist(),
            strict=True,  # pragma: no cover
        ):  # pragma: no cover
            kept: list[tuple[int, float]] = [  # pragma: no cover
                (int(i), float(v))  # pragma: no cover
                for i, v in zip(row_idx, row_vals, strict=True)  # pragma: no cover
                if float(v) > 0.0  # pragma: no cover
            ]  # pragma: no cover
            out.append(
                ([i for i, _v in kept], [v for _i, v in kept])
            )  # pragma: no cover
        return out  # pragma: no cover


def create_sparse_embedder(config: SparseEmbeddingConfig) -> SparseEmbedder:
    if config.provider == "transformers":
        return _TransformersSpladeEmbedder(config=config)
    raise ValueError(f"Unknown sparse embedding provider: {config.provider!r}.")


class _NullSparseEmbedder:
    def embed(self, texts: Sequence[str]) -> list[SparseVector]:
        return [([], []) for _ in texts]


@dataclass(slots=True)
class CatalogSparseIndex:
    """In-memory neural sparse index over catalog text rows (SPLADE-like).

    This is intentionally small and dependency-light: it stores a postings map
    from sparse term indices to (row_idx, weight) pairs, then performs dot
    products by accumulating over query terms.
    """

    catalog: Catalog
    sources: tuple[CatalogTextSource, ...]
    config: SparseEmbeddingConfig
    embedder: SparseEmbedder
    rows_df: pl.DataFrame
    row_ids: list[str]
    row_roles: list[str]
    row_texts: list[str]
    postings: dict[int, list[tuple[int, float]]] = field(default_factory=dict)

    @classmethod
    def from_catalog(
        cls,
        catalog: Catalog,
        *,
        sources: Sequence[CatalogTextSource],
        config: SparseEmbeddingConfig,
        embedder: SparseEmbedder | None = None,
    ) -> "CatalogSparseIndex":
        text_df = CatalogEmbedder(catalog).text_df(sources=sources)
        if text_df.is_empty():
            rows_df = pl.DataFrame({"id": [], "role": [], "text": []})
            return cls(
                catalog=catalog,
                sources=tuple(sources),
                config=config,
                embedder=embedder or _NullSparseEmbedder(),
                rows_df=rows_df,
                row_ids=[],
                row_roles=[],
                row_texts=[],
                postings={},
            )

        rows_df = text_df.select(
            "id",
            "role",
            text=pl.col("content").cast(pl.String).fill_null(""),
        )
        row_ids = rows_df.get_column("id").to_list()
        row_roles = rows_df.get_column("role").to_list()
        row_texts = rows_df.get_column("text").to_list()

        embedder = embedder or create_sparse_embedder(config)
        vectors = embedder.embed(row_texts)

        postings: dict[int, list[tuple[int, float]]] = defaultdict(list)
        for row_idx, (indices, values) in enumerate(vectors):
            for term, weight in zip(indices, values, strict=True):
                if weight == 0.0:
                    continue
                postings[int(term)].append((row_idx, float(weight)))

        return cls(
            catalog=catalog,
            sources=tuple(sources),
            config=config,
            embedder=embedder,
            rows_df=rows_df,
            row_ids=row_ids,
            row_roles=row_roles,
            row_texts=row_texts,
            postings=dict(postings),
        )

    @staticmethod
    def _describe_text_source(source: object) -> dict[str, object]:
        if isinstance(source, SectionsTextSource):
            roles = None if source.roles is None else sorted(source.roles)
            return {"type": "sections", "roles": roles}
        if isinstance(source, SectionsWithTitleTextSource):
            roles = None if source.roles is None else sorted(source.roles)
            return {"type": "sections_with_title", "roles": roles}
        if isinstance(source, GuidelineAbstractTextSource):
            return {"type": "guideline_abstract", "role": source.role}
        if isinstance(source, GuidelineFieldTextSource):
            return {
                "type": "guideline_field",
                "field": source.field,
                "role": source.role,
            }
        if isinstance(source, GuidelineLabelsTextSource):
            return {"type": "guideline_labels", "role": source.role}
        return {"type": source.__class__.__name__}

    def meta(self) -> SparseIndexMeta:
        sources_meta = [self._describe_text_source(s) for s in self.sources]
        return SparseIndexMeta(
            provider=self.config.provider,
            model=self.config.model,
            digest=_sha256_hexdigest(
                {
                    "version": 1,
                    "config": {
                        "provider": self.config.provider,
                        "model": self.config.model,
                    },
                    "text_sources": sources_meta,
                }
            )[:16],
            text_sources=sources_meta,
        )

    def search_sparse(
        self,
        query_text: str,
        *,
        k: int,
        roles: set[str] | None = None,
        ids: set[str] | None = None,
    ) -> pl.DataFrame:
        if k <= 0:
            raise ValueError("k must be positive.")

        query = query_text.strip()
        if not query or not self.row_ids:
            return pl.DataFrame({"id": [], "role": [], "score": [], "text": []})

        q_indices, q_values = self.embedder.embed([query])[0]
        if not q_indices:
            return pl.DataFrame({"id": [], "role": [], "score": [], "text": []})

        scores: dict[int, float] = defaultdict(float)
        for term, q_weight in zip(q_indices, q_values, strict=True):
            postings = self.postings.get(int(term))
            if not postings:
                continue
            for row_idx, weight in postings:
                scores[row_idx] += float(q_weight) * float(weight)

        candidates: list[tuple[int, float]] = []
        for row_idx, score in scores.items():
            if score <= 0.0:
                continue
            if roles is not None and self.row_roles[row_idx] not in roles:
                continue
            if ids is not None and self.row_ids[row_idx] not in ids:
                continue
            candidates.append((row_idx, score))

        candidates.sort(
            key=lambda pair: (-pair[1], self.row_ids[pair[0]], self.row_roles[pair[0]])
        )
        top = candidates[: int(k)]
        out_ids = [self.row_ids[row_idx] for row_idx, _score in top]
        out_roles = [self.row_roles[row_idx] for row_idx, _score in top]
        out_texts = [self.row_texts[row_idx] for row_idx, _score in top]
        out_scores = [float(score) for _row_idx, score in top]

        return pl.DataFrame(
            {"id": out_ids, "role": out_roles, "score": out_scores, "text": out_texts}
        )
