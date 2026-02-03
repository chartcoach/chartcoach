from __future__ import annotations

import os
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Literal, Mapping

import yaml

from chartcoach.env import load_env
from chartcoach.index.sparse import SparseEmbeddingConfig
from chartcoach.retrieval.strategy.pipelines.facet_fusion import FacetFusionConfig
from chartcoach.retrieval.strategy.pipelines.focus import FocusConfig, FocusMode
from chartcoach.retrieval.strategy.pipelines.guideline_status import StatusScorerConfig
from chartcoach.retrieval.strategy.pipelines.query_fusion import QueryFusionConfig
from chartcoach.retrieval.strategy.pipelines.utility_reranker import (
    UtilityRerankerConfig,
)
from chartcoach.retrieval.strategy.pipelines.vision import ChartVisionConfig
from chartcoach.retrieval.strategy.vector_index import EmbeddingConfig


@dataclass(frozen=True, slots=True)
class LmEndpointConfig:
    model: str
    timeout_seconds: float = 120.0
    num_retries: int = 6
    temperature: float = 0.0
    max_tokens: int | None = None


@dataclass(frozen=True, slots=True)
class LmModelsConfig:
    strategy: LmEndpointConfig = LmEndpointConfig(model="gpt-5.1")
    vlm: LmEndpointConfig = LmEndpointConfig(model="gpt-5.2")
    guideline_status: LmEndpointConfig = LmEndpointConfig(model="gpt-5.1")


def _bool_env(name: str, default: bool) -> bool:
    raw = (os.environ.get(name) or "").strip().lower()
    if not raw:
        return default
    if raw in {"1", "true", "t", "yes", "y", "on"}:
        return True
    if raw in {"0", "false", "f", "no", "n", "off"}:
        return False
    return default


def _int_env(name: str, default: int) -> int:
    raw = (os.environ.get(name) or "").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _float_env(name: str, default: float) -> float:
    raw = (os.environ.get(name) or "").strip()
    if not raw:
        return default
    try:
        return float(raw)
    except ValueError:
        return default


def _deep_get(mapping: Mapping[str, Any], keys: list[str]) -> Any:
    current: Any = mapping
    for key in keys:
        if not isinstance(current, Mapping) or key not in current:
            return None
        current = current[key]
    return current


def _coerce_focus_mode(value: object, *, default: FocusMode) -> FocusMode:
    if isinstance(value, str):
        raw = value.strip().lower()
        if raw in {"all", "violations", "satisfied"}:
            return raw  # type: ignore[return-value]
    return default


def _resolve_strategy_timeout_seconds_from_env() -> float | None:
    raw = (os.environ.get("CHARTCOACH_STRATEGY_TIMEOUT_SECONDS") or "").strip()
    if not raw:
        return 600.0
    try:
        value = float(raw)
    except ValueError:
        return 600.0
    if value <= 0:
        return None
    return max(1.0, value)


def _resolve_embedding_config_from_env() -> EmbeddingConfig:
    model = os.environ.get("CHARTCOACH_EMBEDDING_MODEL") or "BAAI/bge-small-en-v1.5"
    projector = (
        os.environ.get("CHARTCOACH_EMBEDDING_PROJECTOR") or "sentence_transformers"
    )
    projector_t: Literal["sentence_transformers", "litellm"]
    if projector == "litellm":
        projector_t = "litellm"
    else:
        projector_t = "sentence_transformers"

    args: dict[str, object] = {"normalize_embeddings": True}
    if projector_t == "litellm":
        openai = load_env().openai.require()
        args = {
            "api_base": openai.api_base,
            "api_key": openai.api_key,
            "sync": True,
            "normalize_embeddings": True,
        }

    return EmbeddingConfig(
        model=model, text_projector_type=projector_t, text_projector_args=args
    )


def _resolve_sparse_embedding_config_from_env() -> SparseEmbeddingConfig:
    model = (
        os.environ.get("CHARTCOACH_SPARSE_EMBEDDING_MODEL")
        or os.environ.get("CHARTCOACH_SPARSE_MODEL")
        or "prithivida/Splade_PP_en_v1"
    )
    return SparseEmbeddingConfig(model=model)


def _resolve_lm_models_from_env() -> LmModelsConfig:
    lm_timeout = _float_env("CHARTCOACH_LM_TIMEOUT_SECONDS", 120.0)
    lm_retries = _int_env("CHARTCOACH_LM_NUM_RETRIES", 6)
    lm_temperature = _float_env("CHARTCOACH_LM_TEMPERATURE", 0.0)
    raw_max_tokens = (os.environ.get("CHARTCOACH_LM_MAX_TOKENS") or "").strip()
    lm_max_tokens = int(raw_max_tokens) if raw_max_tokens.isdigit() else None
    vlm_timeout = _float_env("CHARTCOACH_VLM_TIMEOUT_SECONDS", lm_timeout)
    vlm_retries = _int_env("CHARTCOACH_VLM_NUM_RETRIES", lm_retries)
    vlm_temperature = _float_env("CHARTCOACH_VLM_TEMPERATURE", lm_temperature)
    raw_vlm_max = (os.environ.get("CHARTCOACH_VLM_MAX_TOKENS") or "").strip()
    vlm_max_tokens = int(raw_vlm_max) if raw_vlm_max.isdigit() else lm_max_tokens
    status_timeout = _float_env(
        "CHARTCOACH_GUIDELINE_STATUS_TIMEOUT_SECONDS", lm_timeout
    )
    status_retries = _int_env("CHARTCOACH_GUIDELINE_STATUS_NUM_RETRIES", lm_retries)
    status_temperature = _float_env(
        "CHARTCOACH_GUIDELINE_STATUS_TEMPERATURE", lm_temperature
    )
    raw_status_max = (
        os.environ.get("CHARTCOACH_GUIDELINE_STATUS_MAX_TOKENS") or ""
    ).strip()
    status_max_tokens = (
        int(raw_status_max) if raw_status_max.isdigit() else lm_max_tokens
    )

    strategy_model = os.environ.get("CHARTCOACH_STRATEGY_LM_MODEL") or "gpt-5.1"
    vlm_model = os.environ.get("CHARTCOACH_STRATEGY_VLM_MODEL") or "gpt-5.2"
    status_model = (
        os.environ.get("CHARTCOACH_GUIDELINE_STATUS_LM_MODEL")
        or strategy_model
        or "gpt-5.1"
    )

    return LmModelsConfig(
        strategy=LmEndpointConfig(
            model=strategy_model,
            timeout_seconds=lm_timeout,
            num_retries=lm_retries,
            temperature=lm_temperature,
            max_tokens=lm_max_tokens,
        ),
        vlm=LmEndpointConfig(
            model=vlm_model,
            timeout_seconds=vlm_timeout,
            num_retries=vlm_retries,
            temperature=vlm_temperature,
            max_tokens=vlm_max_tokens,
        ),
        guideline_status=LmEndpointConfig(
            model=status_model,
            timeout_seconds=status_timeout,
            num_retries=status_retries,
            temperature=status_temperature,
            max_tokens=status_max_tokens,
        ),
    )


def _resolve_focus_config_from_env() -> FocusConfig:
    mode = _coerce_focus_mode(
        os.environ.get("CHARTCOACH_STRATEGY_FOCUS"),
        default="all",
    )
    allow_role_fallback = _bool_env("CHARTCOACH_STRATEGY_FOCUS_ROLE_FALLBACK", True)
    use_status_filter = _bool_env("CHARTCOACH_STRATEGY_STATUS_FILTER", False)
    return FocusConfig(
        mode=mode,
        allow_role_fallback=allow_role_fallback,
        use_status_filter=use_status_filter,
    )


def _resolve_chart_vision_config_from_env() -> ChartVisionConfig:
    integration_raw = (os.environ.get("CHARTCOACH_CHART_VISION_INTEGRATION") or "").strip()
    integration: Literal["append", "fuse_tokens"]
    raw = integration_raw.lower()
    if raw in {"fuse_tokens", "fuse"}:
        integration = "fuse_tokens"
    else:
        integration = "append"
    return ChartVisionConfig(
        enabled=_bool_env("CHARTCOACH_CHART_VISION_ENABLED", False),
        integration=integration,
        fusion_weight=_float_env("CHARTCOACH_CHART_VISION_FUSION_WEIGHT", 0.75),
        download_timeout_seconds=_float_env(
            "CHARTCOACH_CHART_VISION_DOWNLOAD_TIMEOUT_SECONDS", 20.0
        ),
        max_image_bytes=_int_env("CHARTCOACH_CHART_VISION_MAX_IMAGE_BYTES", 12_000_000),
        max_keywords=_int_env("CHARTCOACH_CHART_VISION_MAX_KEYWORDS", 16),
        max_issues=_int_env("CHARTCOACH_CHART_VISION_MAX_ISSUES", 10),
        max_visible_text=_int_env("CHARTCOACH_CHART_VISION_MAX_VISIBLE_TEXT", 10),
        max_tokens_chars=_int_env("CHARTCOACH_CHART_VISION_MAX_TOKENS_CHARS", 700),
        max_text_chars=_int_env("CHARTCOACH_CHART_VISION_MAX_TEXT_CHARS", 1400),
    )


def _int_env_first(names: list[str], default: int) -> int:
    for name in names:
        raw = (os.environ.get(name) or "").strip()
        if not raw:
            continue
        try:
            return int(raw)
        except ValueError:
            continue
    return default


def _bool_env_first(names: list[str], default: bool) -> bool:
    for name in names:
        raw = (os.environ.get(name) or "").strip().lower()
        if not raw:
            continue
        if raw in {"1", "true", "t", "yes", "y", "on"}:
            return True
        if raw in {"0", "false", "f", "no", "n", "off"}:
            return False
    return default


def _resolve_status_scorer_config_from_env() -> StatusScorerConfig:
    return StatusScorerConfig(
        candidate_multiplier=max(
            1,
            _int_env_first(
                [
                    "CHARTCOACH_STATUS_CANDIDATE_MULTIPLIER",
                    "CHARTCOACH_GUIDELINE_STATUS_CANDIDATE_MULTIPLIER",
                ],
                4,
            ),
        ),
        keep_unclear=_bool_env_first(
            [
                "CHARTCOACH_STATUS_KEEP_UNCLEAR",
                "CHARTCOACH_GUIDELINE_STATUS_KEEP_UNCLEAR",
            ],
            True,
        ),
        max_guideline_excerpt_chars=max(
            0,
            _int_env_first(
                [
                    "CHARTCOACH_STATUS_MAX_EXCERPT_CHARS",
                    "CHARTCOACH_GUIDELINE_STATUS_MAX_EXCERPT_CHARS",
                ],
                900,
            ),
        ),
        max_rationale_chars=max(
            0,
            _int_env_first(
                [
                    "CHARTCOACH_STATUS_MAX_RATIONALE_CHARS",
                    "CHARTCOACH_GUIDELINE_STATUS_MAX_RATIONALE_CHARS",
                ],
                220,
            ),
        ),
        batch_size=max(
            1,
            _int_env_first(
                [
                    "CHARTCOACH_STATUS_BATCH_SIZE",
                    "CHARTCOACH_GUIDELINE_STATUS_BATCH_SIZE",
                ],
                10,
            ),
        ),
    )


def _resolve_query_fusion_config_from_env() -> QueryFusionConfig:
    return QueryFusionConfig(
        n_queries=_int_env("CHARTCOACH_FUSION_N_QUERIES", 4),
        rrf_k=_int_env("CHARTCOACH_FUSION_RRF_K", 60),
        cross_encoder_model=os.environ.get("CHARTCOACH_FUSION_CROSS_ENCODER_MODEL")
        or "cross-encoder/ms-marco-TinyBERT-L-6",
        cross_encoder_candidate_limit=_int_env("CHARTCOACH_FUSION_XENC_CANDIDATES", 80),
    )


def _resolve_facet_fusion_config_from_env() -> FacetFusionConfig:
    return FacetFusionConfig(
        n_queries=_int_env("CHARTCOACH_FACET_FUSION_N_QUERIES", 5),
        rrf_k=_int_env("CHARTCOACH_FACET_FUSION_RRF_K", 60),
        cross_encoder_model=os.environ.get(
            "CHARTCOACH_FACET_FUSION_CROSS_ENCODER_MODEL"
        )
        or "cross-encoder/ms-marco-TinyBERT-L-6",
        cross_encoder_candidate_limit=_int_env(
            "CHARTCOACH_FACET_FUSION_XENC_CANDIDATES", 80
        ),
    )


def _resolve_utility_reranker_config_from_env() -> UtilityRerankerConfig:
    return UtilityRerankerConfig(
        candidate_k=max(1, _int_env("CHARTCOACH_UTILITY_CANDIDATE_K", 80)),
        batch_size=max(1, _int_env("CHARTCOACH_UTILITY_BATCH_SIZE", 8)),
        max_evidence_chars=max(
            0, _int_env("CHARTCOACH_UTILITY_MAX_EVIDENCE_CHARS", 600)
        ),
        max_rationale_chars=max(
            0, _int_env("CHARTCOACH_UTILITY_MAX_RATIONALE_CHARS", 220)
        ),
        risk_weight=max(0.0, _float_env("CHARTCOACH_UTILITY_RISK_WEIGHT", 1.0)),
        unclear_penalty=max(0.0, _float_env("CHARTCOACH_UTILITY_UNCLEAR_PENALTY", 1.5)),
    )


@dataclass(frozen=True, slots=True)
class RetrievalRunConfig:
    embedding: EmbeddingConfig
    sparse_embedding: SparseEmbeddingConfig
    lms: LmModelsConfig
    focus: FocusConfig
    chart_vision: ChartVisionConfig
    status_scorer: StatusScorerConfig
    query_fusion: QueryFusionConfig
    facet_fusion: FacetFusionConfig
    utility_reranker: UtilityRerankerConfig
    strategy_timeout_seconds: float | None = 600.0

    def public_dict(self) -> dict[str, Any]:
        return {
            "embedding": self.embedding.meta(),
            "sparse_embedding": asdict(self.sparse_embedding),
            "lms": {
                "strategy": asdict(self.lms.strategy),
                "vlm": asdict(self.lms.vlm),
                "guideline_status": asdict(self.lms.guideline_status),
            },
            "focus": asdict(self.focus),
            "chart_vision": asdict(self.chart_vision),
            "status_scorer": asdict(self.status_scorer),
            "query_fusion": asdict(self.query_fusion),
            "facet_fusion": asdict(self.facet_fusion),
            "utility_reranker": asdict(self.utility_reranker),
            "strategy_timeout_seconds": self.strategy_timeout_seconds,
        }


def _default_embedding_config() -> EmbeddingConfig:
    return EmbeddingConfig(
        model="BAAI/bge-small-en-v1.5",
        text_projector_type="sentence_transformers",
        text_projector_args={"normalize_embeddings": True},
    )


def _default_sparse_embedding_config() -> SparseEmbeddingConfig:
    return SparseEmbeddingConfig(model="prithivida/Splade_PP_en_v1")


def load_run_config_from_doc(
    doc: Mapping[str, Any] | None,
    *,
    use_env: bool,
) -> RetrievalRunConfig:
    """Load retrieval run config from an in-memory YAML document.

    Precedence: defaults < (optional env) < YAML overrides.
    """

    doc = dict(doc or {})

    embedding = (
        _resolve_embedding_config_from_env() if use_env else _default_embedding_config()
    )
    embedding_override = _deep_get(doc, ["embedding"])
    if isinstance(embedding_override, Mapping):
        model = embedding_override.get("model")
        if isinstance(model, str) and model.strip():
            embedding = EmbeddingConfig(
                model=model.strip(),
                text_projector_type=embedding.text_projector_type,
                text_projector_args=embedding.text_projector_args,
            )

        projector = embedding_override.get("projector")
        if isinstance(projector, str) and projector.strip():
            proj = projector.strip()
            proj_t: Literal["sentence_transformers", "litellm"]
            proj_t = "litellm" if proj == "litellm" else "sentence_transformers"
            args: dict[str, object] = {"normalize_embeddings": True}
            if proj_t == "litellm":
                openai = load_env().openai.require()
                args = {
                    "api_base": openai.api_base,
                    "api_key": openai.api_key,
                    "sync": True,
                    "normalize_embeddings": True,
                }
            embedding = EmbeddingConfig(
                model=embedding.model,
                text_projector_type=proj_t,
                text_projector_args=args,
            )

    sparse_embedding = (
        _resolve_sparse_embedding_config_from_env()
        if use_env
        else _default_sparse_embedding_config()
    )
    sparse_override = _deep_get(doc, ["sparse_embedding"])
    if isinstance(sparse_override, Mapping):
        model = sparse_override.get("model")
        if isinstance(model, str) and model.strip():
            sparse_embedding = SparseEmbeddingConfig(model=model.strip())

    lms = _resolve_lm_models_from_env() if use_env else LmModelsConfig()
    lms_override = _deep_get(doc, ["lms"])
    strategy_lm = lms.strategy
    vlm = lms.vlm
    status_lm = lms.guideline_status
    if isinstance(lms_override, Mapping):
        for key in ("strategy", "vlm", "guideline_status"):
            endpoint = lms_override.get(key)
            if not isinstance(endpoint, Mapping):
                continue
            current = (
                strategy_lm if key == "strategy" else vlm if key == "vlm" else status_lm
            )
            model = endpoint.get("model")
            timeout = endpoint.get("timeout_seconds")
            retries = endpoint.get("num_retries")
            temperature = endpoint.get("temperature")
            max_tokens = endpoint.get("max_tokens")
            updated = LmEndpointConfig(
                model=str(model).strip() if model else current.model,
                timeout_seconds=float(timeout)
                if isinstance(timeout, (int, float))
                else current.timeout_seconds,
                num_retries=int(retries)
                if isinstance(retries, int)
                else current.num_retries,
                temperature=float(temperature)
                if isinstance(temperature, (int, float))
                else current.temperature,
                max_tokens=int(max_tokens)
                if isinstance(max_tokens, int)
                else current.max_tokens,
            )
            if key == "strategy":
                strategy_lm = updated
            elif key == "vlm":
                vlm = updated
            else:
                status_lm = updated

        lms = LmModelsConfig(strategy=strategy_lm, vlm=vlm, guideline_status=status_lm)

    focus = _resolve_focus_config_from_env() if use_env else FocusConfig()
    focus_override = _deep_get(doc, ["focus"])
    if isinstance(focus_override, Mapping):
        focus = FocusConfig(
            mode=_coerce_focus_mode(focus_override.get("mode"), default=focus.mode),
            allow_role_fallback=bool(
                focus_override.get("allow_role_fallback", focus.allow_role_fallback)
            ),
            use_status_filter=bool(
                focus_override.get("use_status_filter", focus.use_status_filter)
            ),
        )

    chart_vision = (
        _resolve_chart_vision_config_from_env() if use_env else ChartVisionConfig()
    )
    vision_override = _deep_get(doc, ["chart_vision"])
    if isinstance(vision_override, Mapping):
        integration_raw = str(
            vision_override.get("integration", chart_vision.integration)
        ).strip()
        integration: Literal["append", "fuse_tokens"]
        raw = integration_raw.lower()
        if raw in {"fuse_tokens", "fuse"}:
            integration = "fuse_tokens"
        else:
            integration = "append"
        chart_vision = ChartVisionConfig(
            enabled=bool(vision_override.get("enabled", chart_vision.enabled)),
            integration=integration,
            fusion_weight=float(
                vision_override.get("fusion_weight", chart_vision.fusion_weight)
            ),
            download_timeout_seconds=float(
                vision_override.get(
                    "download_timeout_seconds", chart_vision.download_timeout_seconds
                )
            ),
            max_image_bytes=int(
                vision_override.get("max_image_bytes", chart_vision.max_image_bytes)
            ),
            max_keywords=int(
                vision_override.get("max_keywords", chart_vision.max_keywords)
            ),
            max_issues=int(vision_override.get("max_issues", chart_vision.max_issues)),
            max_visible_text=int(
                vision_override.get("max_visible_text", chart_vision.max_visible_text)
            ),
            max_tokens_chars=int(
                vision_override.get("max_tokens_chars", chart_vision.max_tokens_chars)
            ),
            max_text_chars=int(
                vision_override.get("max_text_chars", chart_vision.max_text_chars)
            ),
        )

    status_scorer = (
        _resolve_status_scorer_config_from_env() if use_env else StatusScorerConfig()
    )
    status_override = _deep_get(doc, ["status_scorer"])
    if isinstance(status_override, Mapping):
        status_scorer = StatusScorerConfig(
            candidate_multiplier=int(
                status_override.get(
                    "candidate_multiplier", status_scorer.candidate_multiplier
                )
            ),
            keep_unclear=bool(
                status_override.get("keep_unclear", status_scorer.keep_unclear)
            ),
            max_guideline_excerpt_chars=int(
                status_override.get(
                    "max_guideline_excerpt_chars",
                    status_scorer.max_guideline_excerpt_chars,
                )
            ),
            max_rationale_chars=int(
                status_override.get(
                    "max_rationale_chars", status_scorer.max_rationale_chars
                )
            ),
            batch_size=int(status_override.get("batch_size", status_scorer.batch_size)),
        )

    query_fusion = (
        _resolve_query_fusion_config_from_env() if use_env else QueryFusionConfig()
    )
    qf_override = _deep_get(doc, ["query_fusion"])
    if isinstance(qf_override, Mapping):
        query_fusion = QueryFusionConfig(
            n_queries=int(qf_override.get("n_queries", query_fusion.n_queries)),
            rrf_k=int(qf_override.get("rrf_k", query_fusion.rrf_k)),
            cross_encoder_model=str(
                qf_override.get("cross_encoder_model", query_fusion.cross_encoder_model)
            ),
            cross_encoder_candidate_limit=int(
                qf_override.get(
                    "cross_encoder_candidate_limit",
                    query_fusion.cross_encoder_candidate_limit,
                )
            ),
        )

    facet_fusion = (
        _resolve_facet_fusion_config_from_env() if use_env else FacetFusionConfig()
    )
    ff_override = _deep_get(doc, ["facet_fusion"])
    if isinstance(ff_override, Mapping):
        facet_fusion = FacetFusionConfig(
            n_queries=int(ff_override.get("n_queries", facet_fusion.n_queries)),
            rrf_k=int(ff_override.get("rrf_k", facet_fusion.rrf_k)),
            cross_encoder_model=str(
                ff_override.get("cross_encoder_model", facet_fusion.cross_encoder_model)
            ),
            cross_encoder_candidate_limit=int(
                ff_override.get(
                    "cross_encoder_candidate_limit",
                    facet_fusion.cross_encoder_candidate_limit,
                )
            ),
        )

    utility_reranker = (
        _resolve_utility_reranker_config_from_env()
        if use_env
        else UtilityRerankerConfig()
    )
    util_override = _deep_get(doc, ["utility_reranker"])
    if isinstance(util_override, Mapping):
        utility_reranker = UtilityRerankerConfig(
            candidate_k=int(
                util_override.get("candidate_k", utility_reranker.candidate_k)
            ),
            batch_size=int(
                util_override.get("batch_size", utility_reranker.batch_size)
            ),
            max_evidence_chars=int(
                util_override.get(
                    "max_evidence_chars", utility_reranker.max_evidence_chars
                )
            ),
            max_rationale_chars=int(
                util_override.get(
                    "max_rationale_chars", utility_reranker.max_rationale_chars
                )
            ),
            risk_weight=float(
                util_override.get("risk_weight", utility_reranker.risk_weight)
            ),
            unclear_penalty=float(
                util_override.get("unclear_penalty", utility_reranker.unclear_penalty)
            ),
        )

    timeout_override = _deep_get(doc, ["strategy_timeout_seconds"])
    timeout_env = _resolve_strategy_timeout_seconds_from_env() if use_env else 600.0
    timeout = timeout_env
    if isinstance(timeout_override, (int, float)):
        timeout = None if float(timeout_override) <= 0 else float(timeout_override)

    return RetrievalRunConfig(
        embedding=embedding,
        sparse_embedding=sparse_embedding,
        lms=lms,
        focus=focus,
        chart_vision=chart_vision,
        status_scorer=status_scorer,
        query_fusion=query_fusion,
        facet_fusion=facet_fusion,
        utility_reranker=utility_reranker,
        strategy_timeout_seconds=timeout,
    )


def load_run_config(
    config_path: str | Path | None = None,
    *,
    use_env: bool = True,
) -> RetrievalRunConfig:
    """Load retrieval run config with precedence: defaults < (optional env) < YAML overrides."""

    doc: dict[str, Any] = {}
    if config_path:
        path = Path(config_path)
        loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(loaded, dict):
            doc = loaded
        else:
            raise ValueError("Expected YAML mapping at --config path.")

    return load_run_config_from_doc(doc, use_env=use_env)
