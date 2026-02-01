from __future__ import annotations

from dataclasses import dataclass
from io import StringIO
from typing import TYPE_CHECKING, cast

import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.id_extraction import extract_guideline_ids
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .searcher import GuidelineSearcher

if TYPE_CHECKING:
    import dspy
    from dspy.utils.exceptions import AdapterParseError
else:
    dspy = require_dspy()
    from dspy.utils.exceptions import AdapterParseError  # noqa: E402


class AgenticHybridSignature(dspy.Signature):
    """
    Retrieve the most relevant visualization design guidelines for a scenario.

    You are a careful retrieval agent. Use tools to search iteratively, covering
    multiple facets (audience, task/goal, chart type/encoding, risks, clarity).

    RULES:
    - You MUST ground selections in the catalog; never invent guideline IDs.
    - Focus only on improving the chart described by the scenario title/intent, and ignore mentions of adjacent charts.
    - Use multiple searches and read full guidelines before final selection.
    - Return a diverse, non-redundant list.
    - If top_k > 0, return exactly top_k IDs (unless the catalog is smaller).
    """

    situation: str = dspy.InputField(
        desc="Scenario title + designer intent describing the chart to improve."
    )
    top_k: int = dspy.InputField(
        desc="How many guideline IDs to return.", ge=0, default=0
    )

    used_guideline_ids: list[str] = dspy.OutputField(
        desc="Unique list of guideline IDs in descending relevance order."
    )
    notes: str = dspy.OutputField(
        desc="Short rationale describing which facets you covered and any uncertainty."
    )


@dataclass(frozen=True, slots=True)
class AgenticHybridTools:
    catalog: Catalog
    searcher: GuidelineSearcher

    def list_roles(self) -> list[str]:
        """[ROLE DISCOVERY] List indexed roles/sections that can be filtered on."""
        if "role" not in self.searcher.vector_index.embedded_text_df.columns:
            return []
        return (
            self.searcher.vector_index.embedded_text_df.select("role")
            .unique("role")
            .sort("role")["role"]
            .to_list()
        )

    def _abstracts_df(self) -> pl.DataFrame:
        return self.catalog.df().select(
            "id",
            title=pl.col("guideline").struct.field("title"),
            description=pl.col("guideline").struct.field("description"),
            labels=pl.col("guideline").struct.field("labels").list.join(";"),
        )

    def hybrid_search(
        self,
        query: str,
        *,
        k: int = 50,
        roles: list[str] | None = None,
    ) -> str:
        """
        [HYBRID SEARCH] Strong default: lexical + dense fusion.

        Returns CSV with columns: id, role, score, title, description, labels.
        """
        from lancedb.rerankers import RRFReranker

        q = query.strip()
        if not q:
            return "id,role,score,title,description,labels\n"

        qvec = self.searcher.vector_index.embed_query(q)
        roles_set = None if not roles else set(roles)
        hits_df = self.searcher.search_hybrid(
            query_text=q,
            query_vector=qvec,
            reranker=RRFReranker(),
            k=int(max(1, k)),
            roles=roles_set,
            fts_columns="text",
        )

        out_df = hits_df.join(self._abstracts_df(), on="id", how="left").select(
            "id",
            "role",
            "score",
            "title",
            "description",
            "labels",
        )
        buf = StringIO()
        out_df.write_csv(buf)
        return buf.getvalue()

    def dense_search(
        self,
        query: str,
        *,
        k: int = 50,
        roles: list[str] | None = None,
    ) -> str:
        """
        [DENSE SEARCH] Semantic search over embedded catalog text.

        Returns CSV with columns: id, role, score, title, description, labels.
        """
        q = query.strip()
        if not q:
            return "id,role,score,title,description,labels\n"

        qvec = self.searcher.vector_index.embed_query(q)
        roles_set = None if not roles else set(roles)
        hits_df = self.searcher.search_dense(
            query_vector=qvec,
            k=int(max(1, k)),
            roles=roles_set,
        )
        out_df = hits_df.join(self._abstracts_df(), on="id", how="left").select(
            "id",
            "role",
            "score",
            "title",
            "description",
            "labels",
        )
        buf = StringIO()
        out_df.write_csv(buf)
        return buf.getvalue()

    def fts_search(
        self,
        query: str,
        *,
        k: int = 50,
        roles: list[str] | None = None,
    ) -> str:
        """
        [FTS SEARCH] Lexical BM25 search.

        Returns CSV with columns: id, role, score, title, description, labels.
        """
        q = query.strip()
        if not q:
            return "id,role,score,title,description,labels\n"

        roles_set = None if not roles else set(roles)
        hits_df = self.searcher.search_fts(
            query_text=q,
            k=int(max(1, k)),
            roles=roles_set,
        )
        out_df = hits_df.join(self._abstracts_df(), on="id", how="left").select(
            "id",
            "role",
            "score",
            "title",
            "description",
            "labels",
        )
        buf = StringIO()
        out_df.write_csv(buf)
        return buf.getvalue()

    def read_guidelines_by_id(self, ids: list[str]) -> list[dict]:
        """[READ] Fetch full guideline bodies + references for given IDs."""
        id_df = pl.DataFrame({"id": ids})
        matched_df = id_df.join(self.catalog.df(), on="id", how="inner")
        return matched_df.select(
            "id",
            pl.col("guideline").struct.field("title"),
            pl.col("guideline").struct.field("body"),
            "references",
        ).to_dicts()


class AgenticHybridStrategy(RetrievalStrategy):
    """Tool-using ReAct agent over hybrid/dense/FTS search + full guideline reads."""

    id = "agentic-hybrid@v1"
    _react_max_iters = 10

    def __init__(
        self,
        *,
        catalog: Catalog,
        searcher: GuidelineSearcher,
        lm: dspy.LM,
        default_k: int = 20,
        final_cross_encoder_model: str | None = "cross-encoder/ms-marco-TinyBERT-L-6",
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._lm = lm
        self._default_k = int(default_k)
        self._final_cross_encoder_model = final_cross_encoder_model

        self._tools = AgenticHybridTools(catalog=catalog, searcher=searcher)
        self._program = dspy.ReAct(
            AgenticHybridSignature,
            tools=[
                self._tools.list_roles,
                self._tools.hybrid_search,
                self._tools.dense_search,
                self._tools.fts_search,
                self._tools.read_guidelines_by_id,
            ],
            max_iters=self._react_max_iters,
        )

    @property
    def tools(self) -> AgenticHybridTools:
        return self._tools

    def _forward(self, request: RetrievalRequest) -> RetrievalResponse:
        from lancedb.rerankers import CrossEncoderReranker

        effective_k = self._default_k if request.k is None else int(request.k)
        if effective_k <= 0:
            raise ValueError("k must be positive.")

        situation = self._searcher.build_query_text(request)
        top_k = request.k if request.k is not None else 0

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}

        prediction: dspy.Prediction | None = None
        last_error: AdapterParseError | None = None
        best_ids: list[str] = []

        for lm in (self._lm, self._lm.copy(cache=False)):
            try:
                with dspy.context(lm=lm):
                    prediction = self._program(situation=situation, top_k=top_k)
                notes = str(getattr(prediction, "notes", "") or "")
                used_ids = extract_guideline_ids(
                    known_ids=set(id_to_entry),
                    raw_used=getattr(prediction, "used_guideline_ids", []),
                    feedback=notes,
                )
                if len(used_ids) > len(best_ids):
                    best_ids = used_ids
                if request.k is not None and len(used_ids) >= request.k:
                    break
            except AdapterParseError as e:
                last_error = e

        if prediction is None:
            raise ValueError(
                "Failed to parse model output while selecting the next tool step."
            ) from last_error

        notes = str(getattr(prediction, "notes", "") or "")
        fallback_used = False

        def _fallback_hybrid_ids(*, exclude: set[str]) -> list[str]:
            # We keep this strategy runnable even when the agent fails to return
            # enough IDs by falling back to a strong hybrid ranking over the catalog.
            from lancedb.rerankers import RRFReranker

            raw_k = max(50, min(3_000, effective_k * 20))
            qvec = self._searcher.vector_index.embed_query(situation)
            hits_df = self._searcher.search_hybrid(
                query_text=situation,
                query_vector=qvec,
                reranker=RRFReranker(),
                k=raw_k,
                fts_columns="text",
            )
            agg = self._searcher.aggregate_guideline_hits(hits_df, k=raw_k)
            ids = [
                gid
                for gid in agg["id"].to_list()
                if isinstance(gid, str) and gid not in exclude and gid in id_to_entry
            ]
            return ids

        if not best_ids and id_to_entry:
            fallback_used = True
            best_ids = _fallback_hybrid_ids(exclude=set())

        if len(best_ids) < effective_k and id_to_entry:
            missing = effective_k - len(best_ids)
            fill_ids = _fallback_hybrid_ids(exclude=set(best_ids))
            if fill_ids:
                fallback_used = True
                best_ids = [*best_ids, *fill_ids[:missing]]

        candidate_ids = best_ids[: max(1, effective_k)]

        final_ids = candidate_ids[:effective_k]
        cross_encoder_fallback_used = False
        if self._final_cross_encoder_model and candidate_ids:
            qvec = self._searcher.vector_index.embed_query(situation)
            hits_df = self._searcher.search_hybrid(
                query_text=situation,
                query_vector=qvec,
                reranker=CrossEncoderReranker(
                    model_name=self._final_cross_encoder_model
                ),
                k=min(len(candidate_ids), 120),
                ids=set(candidate_ids),
                fts_columns="text",
            )
            agg = self._searcher.aggregate_guideline_hits(hits_df, k=effective_k)
            reranked = [gid for gid in agg["id"].to_list() if isinstance(gid, str)]
            if reranked:
                final_ids = reranked
            else:
                cross_encoder_fallback_used = True

        if len(final_ids) < effective_k and candidate_ids:
            cross_encoder_fallback_used = True
            seen = set(final_ids)
            for gid in candidate_ids:
                if gid in seen:
                    continue
                final_ids.append(gid)
                seen.add(gid)
                if len(final_ids) >= effective_k:
                    break

        retrieved_entries = [
            id_to_entry[gid] for gid in final_ids if gid in id_to_entry
        ]
        meta: dict[str, object] = {
            **cast("dict[str, object]", self._searcher.vector_index.meta()),
            "k": effective_k,
            "used_guideline_ids": final_ids,
            "notes": notes,
            "fallback_used": fallback_used,
            "cross_encoder_fallback_used": cross_encoder_fallback_used,
            "final_cross_encoder": (
                {"model": self._final_cross_encoder_model}
                if self._final_cross_encoder_model
                else None
            ),
        }

        return RetrievalResponse(catalog=Catalog(entries=retrieved_entries), meta=meta)
