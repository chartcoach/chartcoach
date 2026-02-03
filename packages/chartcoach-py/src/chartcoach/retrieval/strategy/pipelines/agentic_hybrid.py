from __future__ import annotations

from dataclasses import dataclass, field
from io import StringIO
from typing import TYPE_CHECKING, cast

import polars as pl

from chartcoach.catalog import Catalog
from chartcoach.retrieval.strategy.dspy_models import create_strategy_vlm
from chartcoach.retrieval.strategy.base import RetrievalStrategy
from chartcoach.retrieval.strategy.id_extraction import extract_guideline_ids
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.types import RetrievalRequest, RetrievalResponse

from .focus import (
    FocusConfig,
    focus_config_from_env,
    fallback_roles_for_focus,
    primary_roles_for_focus,
)
from .guideline_status import filter_guidelines_by_status, shared_status_scorer
from .searcher import GuidelineSearcher
from .vision import ChartVisionModule, chart_vision_config_from_env, with_chart_vision

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
    - If the situation implies paired comparisons (e.g., before-after / year-over-year / two values per category), include at least one search about representing change or differences clearly.
    - Use multiple searches and read full guidelines before final selection.
    - Return a diverse, non-redundant list.
    - If top_k > 0, return exactly top_k IDs (unless the catalog is smaller).
    """

    situation: str = dspy.InputField(
        desc=(
            "Scenario title + designer intent describing the chart to improve. "
            "It may include optional chart image notes from a vision preprocessor."
        )
    )
    focus: str = dspy.InputField(
        desc="One of: all, violations, satisfied. Use it to prioritize which guidelines to retrieve."
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
    focus: FocusConfig = field(default_factory=FocusConfig)

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

    def _default_role_filter(self) -> set[str] | None:
        return primary_roles_for_focus(self.focus.mode)

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
        roles_set = set(roles) if roles else self._default_role_filter()
        hits_df = self.searcher.search_hybrid(
            query_text=q,
            query_vector=qvec,
            reranker=RRFReranker(),
            k=int(max(1, k)),
            roles=roles_set,
            fts_columns="text",
        )
        if (
            hits_df.is_empty()
            and not roles
            and roles_set is not None
            and self.focus.allow_role_fallback
        ):
            hits_df = self.searcher.search_hybrid(
                query_text=q,
                query_vector=qvec,
                reranker=RRFReranker(),
                k=int(max(1, k)),
                roles=fallback_roles_for_focus(self.focus.mode),
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
        roles_set = set(roles) if roles else self._default_role_filter()
        hits_df = self.searcher.search_dense(
            query_vector=qvec,
            k=int(max(1, k)),
            roles=roles_set,
        )
        if (
            hits_df.is_empty()
            and not roles
            and roles_set is not None
            and self.focus.allow_role_fallback
        ):
            hits_df = self.searcher.search_dense(
                query_vector=qvec,
                k=int(max(1, k)),
                roles=fallback_roles_for_focus(self.focus.mode),
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

        roles_set = set(roles) if roles else self._default_role_filter()
        hits_df = self.searcher.search_fts(
            query_text=q,
            k=int(max(1, k)),
            roles=roles_set,
        )
        if (
            hits_df.is_empty()
            and not roles
            and roles_set is not None
            and self.focus.allow_role_fallback
        ):
            hits_df = self.searcher.search_fts(
                query_text=q,
                k=int(max(1, k)),
                roles=fallback_roles_for_focus(self.focus.mode),
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
        focus: FocusConfig | None = None,
    ) -> None:
        super().__init__(catalog)
        self._searcher = searcher
        self._lm = lm
        self._default_k = int(default_k)
        self._final_cross_encoder_model = final_cross_encoder_model
        self._focus = focus or focus_config_from_env()

        self._vision_config = chart_vision_config_from_env()
        self._vlm = create_strategy_vlm() if self._vision_config.enabled else None
        # Lazily initialized on first use to avoid repeatedly loading weights.
        self._cross_encoder_reranker = None

        self._tools = AgenticHybridTools(
            catalog=catalog, searcher=searcher, focus=self._focus
        )
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

        vision_meta: dict[str, object] = {}
        if self._vlm is not None and self._vision_config.enabled:
            request, vision_meta = with_chart_vision(
                request,
                base_situation=self._searcher.build_base_query_text(request),
                vision=ChartVisionModule(vlm=self._vlm, config=self._vision_config),
            )

        focus_mode = self._focus.mode
        situation = self._searcher.build_query_text(request)
        top_k = request.k if request.k is not None else 0

        id_to_entry = {entry.id: entry for entry in self.catalog.entries}

        prediction: dspy.Prediction | None = None
        last_error: AdapterParseError | None = None
        best_ids: list[str] = []

        for lm in (self._lm, self._lm.copy(cache=False)):
            try:
                with dspy.context(lm=lm):
                    prediction = self._program(
                        situation=situation, focus=focus_mode, top_k=top_k
                    )
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
            roles = primary_roles_for_focus(focus_mode)
            roles_used = roles
            hits_df = self._searcher.search_hybrid(
                query_text=situation,
                query_vector=qvec,
                reranker=RRFReranker(),
                k=raw_k,
                roles=roles_used,
                fts_columns="text",
            )
            if (
                hits_df.is_empty()
                and roles is not None
                and self._focus.allow_role_fallback
            ):
                roles_used = fallback_roles_for_focus(focus_mode)
                hits_df = self._searcher.search_hybrid(
                    query_text=situation,
                    query_vector=qvec,
                    reranker=RRFReranker(),
                    k=raw_k,
                    roles=roles_used,
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
        cross_encoder_error: str | None = None
        if self._final_cross_encoder_model and candidate_ids:
            qvec = self._searcher.vector_index.embed_query(situation)
            try:
                reranker = self._cross_encoder_reranker
                if reranker is None:
                    reranker = CrossEncoderReranker(
                        model_name=self._final_cross_encoder_model
                    )
                    self._cross_encoder_reranker = reranker

                hits_df = self._searcher.search_hybrid(
                    query_text=situation,
                    query_vector=qvec,
                    reranker=reranker,
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
            except Exception as e:  # noqa: BLE001
                cross_encoder_fallback_used = True
                cross_encoder_error = str(e)

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
        status_meta: dict[str, object] = {}
        use_status_filter = focus_mode != "all" and self._focus.use_status_filter
        if use_status_filter and retrieved_entries:
            status_lm, status_module, status_cfg = shared_status_scorer()
            self._status_lm = status_lm
            pool_target = max(
                effective_k, effective_k * int(status_cfg.candidate_multiplier)
            )
            extra_needed = max(0, pool_target - len(final_ids))
            extra_ids = _fallback_hybrid_ids(exclude=set(final_ids))[:extra_needed]

            ordered_candidate_ids: list[str] = []
            seen = set()
            for gid in [*final_ids, *extra_ids]:
                if gid in seen or gid not in id_to_entry:
                    continue
                ordered_candidate_ids.append(gid)
                seen.add(gid)

            candidate_entries = [id_to_entry[gid] for gid in ordered_candidate_ids]
            filtered, status_meta = filter_guidelines_by_status(
                request=request,
                entries=candidate_entries,
                output_k=effective_k,
                focus=focus_mode,
                status_module=status_module,
                config=status_cfg,
            )
            retrieved_entries = filtered
            final_ids = [entry.id for entry in retrieved_entries]

        # Attach evidence snippets for the final guideline set by running a small
        # hybrid search restricted to the output IDs.
        hits_by_id: dict[str, dict[str, object]] = {}
        if final_ids:
            try:
                from lancedb.rerankers import RRFReranker

                qvec = self._searcher.vector_index.embed_query(situation)
                roles = primary_roles_for_focus(focus_mode)
                roles_used = roles
                raw_k = min(3_000, max(50, len(final_ids) * 10))
                hits_df = self._searcher.search_hybrid(
                    query_text=situation,
                    query_vector=qvec,
                    reranker=RRFReranker(),
                    k=raw_k,
                    roles=roles_used,
                    ids=set(final_ids),
                    fts_columns="text",
                )
                if (
                    hits_df.is_empty()
                    and roles is not None
                    and self._focus.allow_role_fallback
                ):
                    roles_used = fallback_roles_for_focus(focus_mode)
                    hits_df = self._searcher.search_hybrid(
                        query_text=situation,
                        query_vector=qvec,
                        reranker=RRFReranker(),
                        k=raw_k,
                        roles=roles_used,
                        ids=set(final_ids),
                        fts_columns="text",
                    )

                agg = self._searcher.aggregate_guideline_hits_with_evidence(
                    hits_df, k=len(final_ids)
                )
                hits_by_id = {
                    row["id"]: row
                    for row in agg.to_dicts()
                    if isinstance(row.get("id"), str)
                }
            except Exception:  # noqa: BLE001
                hits_by_id = {}
        meta: dict[str, object] = {
            **cast("dict[str, object]", self._searcher.vector_index.meta()),
            "k": effective_k,
            "used_guideline_ids": final_ids,
            "notes": notes,
            "focus": {
                "mode": focus_mode,
                "roles": (
                    sorted(role_set)
                    if (role_set := primary_roles_for_focus(focus_mode)) is not None
                    else None
                ),
            },
            "chart_vision": vision_meta,
            **status_meta,
            "fallback_used": fallback_used,
            "cross_encoder_fallback_used": cross_encoder_fallback_used,
            "cross_encoder_error": cross_encoder_error,
            "final_cross_encoder": (
                {"model": self._final_cross_encoder_model}
                if self._final_cross_encoder_model
                else None
            ),
            "hits": [
                {
                    "id": entry.id,
                    "score": float(hits_by_id.get(entry.id, {}).get("score") or 0.0),
                    "best_role": hits_by_id.get(entry.id, {}).get("best_role"),
                    "evidence": hits_by_id.get(entry.id, {}).get("evidence") or [],
                }
                for entry in retrieved_entries
            ],
        }

        return RetrievalResponse(catalog=Catalog(entries=retrieved_entries), meta=meta)
