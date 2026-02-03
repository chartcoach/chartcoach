from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, cast

from chartcoach.catalog import CatalogEntry
from chartcoach.retrieval.strategy.optional import require_dspy
from chartcoach.retrieval.strategy.types import ImageItem, RetrievalRequest

if TYPE_CHECKING:
    import dspy
else:
    dspy = require_dspy()


Applicability = Literal["applicable", "not_applicable", "unclear"]


_UTILITY_CACHE: dict[tuple[str, str], dict[str, object]] = {}


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _chart_fingerprint(request: RetrievalRequest) -> str | None:
    for item in request.context:
        if not isinstance(item, ImageItem) or item.role != "chart":
            continue
        if item.uri:
            return f"uri:{_sha256_text(item.uri)[:16]}"
        if item.data:
            return f"bytes:{hashlib.sha256(item.data).hexdigest()[:16]}"
    return None


class GuidelineUtilitySignature(dspy.Signature):
    """Score a guideline for utility/harm under a specific situation."""

    situation: str = dspy.InputField(
        desc=(
            "Scenario title + intent + context facets + optional chart image notes. "
            "Do not invent chart details; use only what is stated."
        )
    )
    guideline_title: str = dspy.InputField(desc="Guideline title (imperative advice).")
    guideline_description: str = dspy.InputField(desc="Guideline summary description.")
    guideline_labels: str = dspy.InputField(
        desc="Semicolon-separated guideline labels."
    )
    evidence: str = dspy.InputField(
        desc=(
            "Top evidence snippets (short excerpts of matching sections) that triggered retrieval. "
            "May be empty. Use them to judge applicability and risk."
        )
    )

    applicability: Applicability = dspy.OutputField(
        desc="One of: applicable, not_applicable, unclear."
    )
    actionability: int = dspy.OutputField(desc="Actionability in [1,5].")
    impact: int = dspy.OutputField(desc="Expected impact in [1,5].")
    harm: int = dspy.OutputField(
        desc="Risk/harm likelihood in [1,5] (higher = riskier)."
    )
    credibility: int = dspy.OutputField(desc="Credibility/trust in [1,5].")
    rationale: str = dspy.OutputField(desc="1-2 sentences justifying scores.")


class GuidelineUtilityBatchSignature(dspy.Signature):
    """Batch score multiple guidelines in one call to reduce LLM overhead."""

    situation: str = dspy.InputField(
        desc=(
            "Scenario title + intent + context facets + optional chart image notes. "
            "Do not invent chart details; use only what is stated."
        )
    )
    guidelines_json: str = dspy.InputField(
        desc=(
            "JSON array of guideline objects, each with: id, title, description, labels, evidence. "
            "The 'evidence' field may be empty. Score each guideline independently."
        )
    )

    results_json: str = dspy.OutputField(
        desc=(
            "Return ONLY a JSON array of result objects, one per guideline id, each with: "
            "id, applicability, actionability, impact, harm, credibility, rationale. "
            "Do not include Markdown fences or extra text."
        )
    )


@dataclass(frozen=True, slots=True)
class UtilityRerankerConfig:
    candidate_k: int = 80
    batch_size: int = 8
    max_evidence_chars: int = 600
    max_rationale_chars: int = 220
    risk_weight: float = 1.0
    unclear_penalty: float = 1.5


@dataclass(frozen=True, slots=True)
class UtilityReranker:
    lm: dspy.LM
    module: "GuidelineUtilityModule"
    config: UtilityRerankerConfig


def create_utility_reranker(
    *, lm: dspy.LM, config: UtilityRerankerConfig
) -> UtilityReranker:
    return UtilityReranker(
        lm=lm,
        module=GuidelineUtilityModule(lm=lm, config=config),
        config=config,
    )


class GuidelineUtilityModule:
    def __init__(self, *, lm: dspy.LM, config: UtilityRerankerConfig) -> None:
        self._lm = lm
        self._config = config
        self._program = dspy.Predict(GuidelineUtilitySignature)
        self._batch_program = dspy.Predict(GuidelineUtilityBatchSignature)

    @property
    def config(self) -> UtilityRerankerConfig:
        return self._config

    def _render_evidence(self, evidence: object) -> str:
        if not isinstance(evidence, list) or not evidence:
            return ""
        parts: list[str] = []
        for item in evidence:
            if not isinstance(item, dict):
                continue
            payload = cast("dict[str, object]", item)
            role = str(payload.get("role") or "").strip()
            text = str(payload.get("text") or "").strip()
            if not text:
                continue
            prefix = f"[{role}] " if role else ""
            parts.append(prefix + text)
        out = "\n".join(parts).strip()
        max_chars = max(0, int(self._config.max_evidence_chars))
        if max_chars and len(out) > max_chars:
            out = out[:max_chars].rstrip() + "..."
        return out

    @staticmethod
    def _coerce_applicability(raw: object) -> Applicability:
        if isinstance(raw, str):
            norm = raw.strip().lower().replace("-", "_")
            if norm in {"applicable", "not_applicable", "unclear"}:
                return norm  # type: ignore[return-value]
        return "unclear"

    @staticmethod
    def _coerce_int(raw: object) -> int:
        try:
            value = int(raw)  # type: ignore[arg-type]
        except (TypeError, ValueError):
            return 0
        return max(1, min(5, value))

    def score_guidelines(
        self,
        *,
        request: RetrievalRequest,
        situation_text: str,
        entries: list[CatalogEntry],
        evidence_by_id: dict[str, object],
    ) -> dict[str, dict[str, object]]:
        """Batch-score guidelines, filling the per-guideline cache as we go."""

        chart_key = _chart_fingerprint(request) or "<no-chart>"
        situation_digest = _sha256_text(situation_text)[:16]

        out: dict[str, dict[str, object]] = {}
        pending: list[CatalogEntry] = []
        for entry in entries:
            cache_key = (chart_key, f"{situation_digest}:{entry.id}")
            cached = _UTILITY_CACHE.get(cache_key)
            if cached is not None:
                out[entry.id] = {**cached, "cache": "memory"}
            else:
                pending.append(entry)

        if not pending:
            return out

        payloads: list[dict[str, str]] = []
        for entry in pending:
            payloads.append(
                {
                    "id": entry.id,
                    "title": entry.guideline.title,
                    "description": entry.guideline.description or "",
                    "labels": "; ".join(entry.guideline.labels or []),
                    "evidence": self._render_evidence(evidence_by_id.get(entry.id)),
                }
            )

        batch_size = max(1, int(self._config.batch_size))
        for i in range(0, len(payloads), batch_size):
            batch = payloads[i : i + batch_size]
            expected_ids = {item["id"] for item in batch if item.get("id")}
            guidelines_json = json.dumps(batch, ensure_ascii=False)

            pred: dspy.Prediction | None = None
            err: str | None = None
            attempts = 0
            for lm in (self._lm, self._lm.copy(cache=False)):
                attempts += 1
                try:
                    with dspy.context(lm=lm):
                        pred = self._batch_program(
                            situation=situation_text,
                            guidelines_json=guidelines_json,
                        )
                    err = None
                    break
                except Exception as e:  # noqa: BLE001
                    err = str(e)

            raw = str(
                getattr(pred, "results_json", "") if pred is not None else ""
            ).strip()
            parsed: object | None = None
            if raw:
                try:
                    parsed = json.loads(raw)
                except Exception as e:  # noqa: BLE001
                    err = f"parse_error: {e}"
                    parsed = None

            found_ids: set[str] = set()
            if isinstance(parsed, list):
                for item in parsed:
                    if not isinstance(item, dict):
                        continue
                    gid = item.get("id")
                    if not isinstance(gid, str) or not gid or gid not in expected_ids:
                        continue
                    if gid in found_ids:
                        continue
                    found_ids.add(gid)

                    applicability = self._coerce_applicability(
                        item.get("applicability")
                    )
                    actionability = self._coerce_int(item.get("actionability"))
                    impact = self._coerce_int(item.get("impact"))
                    harm = self._coerce_int(item.get("harm"))
                    credibility = self._coerce_int(item.get("credibility"))
                    rationale = str(item.get("rationale") or "").strip()
                    if (
                        self._config.max_rationale_chars
                        and len(rationale) > self._config.max_rationale_chars
                    ):
                        rationale = (
                            rationale[: self._config.max_rationale_chars].rstrip()
                            + "..."
                        )

                    utility = float(actionability + impact + credibility) - (
                        float(harm) * float(self._config.risk_weight)
                    )
                    if applicability == "not_applicable":
                        utility = -1e9
                    elif applicability == "unclear":
                        utility -= float(self._config.unclear_penalty)

                    payload = {
                        "applicability": applicability,
                        "actionability": actionability,
                        "impact": impact,
                        "harm": harm,
                        "credibility": credibility,
                        "utility": utility,
                        "rationale": rationale,
                        "error": None,
                        "attempts": attempts,
                    }

                    cache_key = (chart_key, f"{situation_digest}:{gid}")
                    _UTILITY_CACHE[cache_key] = payload
                    out[gid] = {**payload, "cache": "miss"}

            # Fill any missing ids with a conservative default (treated as unusable).
            for gid in sorted(expected_ids - found_ids):
                payload = {
                    "applicability": "unclear",
                    "actionability": 0,
                    "impact": 0,
                    "harm": 0,
                    "credibility": 0,
                    "utility": -1e9,
                    "rationale": "",
                    "error": err,
                    "attempts": attempts,
                }
                cache_key = (chart_key, f"{situation_digest}:{gid}")
                _UTILITY_CACHE[cache_key] = payload
                out[gid] = {**payload, "cache": "miss"}

        return out

    def score_guideline(
        self,
        *,
        request: RetrievalRequest,
        situation_text: str,
        entry: CatalogEntry,
        evidence: object,
    ) -> dict[str, object]:
        chart_key = _chart_fingerprint(request) or "<no-chart>"
        situation_digest = _sha256_text(situation_text)[:16]
        cache_key = (chart_key, f"{situation_digest}:{entry.id}")
        cached = _UTILITY_CACHE.get(cache_key)
        if cached is not None:
            return {**cached, "cache": "memory"}

        labels = "; ".join(entry.guideline.labels or [])
        pred: dspy.Prediction | None = None
        err: str | None = None
        attempts = 0
        evidence_text = self._render_evidence(evidence)

        for lm in (self._lm, self._lm.copy(cache=False)):
            attempts += 1
            try:
                with dspy.context(lm=lm):
                    pred = self._program(
                        situation=situation_text,
                        guideline_title=entry.guideline.title,
                        guideline_description=entry.guideline.description,
                        guideline_labels=labels,
                        evidence=evidence_text,
                    )
                err = None
                break
            except Exception as e:  # noqa: BLE001
                err = str(e)

        if pred is None:
            payload: dict[str, object] = {
                "applicability": "unclear",
                "actionability": 0,
                "impact": 0,
                "harm": 0,
                "credibility": 0,
                "utility": -1e9,
                "rationale": "",
                "error": err,
                "attempts": attempts,
            }
            _UTILITY_CACHE[cache_key] = payload
            return {**payload, "cache": "miss"}

        applicability = self._coerce_applicability(getattr(pred, "applicability", None))
        actionability = self._coerce_int(getattr(pred, "actionability", None))
        impact = self._coerce_int(getattr(pred, "impact", None))
        harm = self._coerce_int(getattr(pred, "harm", None))
        credibility = self._coerce_int(getattr(pred, "credibility", None))
        rationale = str(getattr(pred, "rationale", "") or "").strip()
        if (
            self._config.max_rationale_chars
            and len(rationale) > self._config.max_rationale_chars
        ):
            rationale = rationale[: self._config.max_rationale_chars].rstrip() + "..."

        utility = float(actionability + impact + credibility) - (
            float(harm) * float(self._config.risk_weight)
        )
        if applicability == "not_applicable":
            utility = -1e9
        elif applicability == "unclear":
            utility -= float(self._config.unclear_penalty)

        payload = {
            "applicability": applicability,
            "actionability": actionability,
            "impact": impact,
            "harm": harm,
            "credibility": credibility,
            "utility": utility,
            "rationale": rationale,
            "error": None,
            "attempts": attempts,
        }
        _UTILITY_CACHE[cache_key] = payload
        return {**payload, "cache": "miss"}


def rank_by_utility(
    *,
    request: RetrievalRequest,
    situation_text: str,
    entries: list[CatalogEntry],
    evidence_by_id: dict[str, object],
    module: GuidelineUtilityModule,
) -> list[tuple[CatalogEntry, dict[str, object]]]:
    scored: list[tuple[CatalogEntry, dict[str, object]]] = []
    if hasattr(module, "score_guidelines"):
        try:
            scores = module.score_guidelines(
                request=request,
                situation_text=situation_text,
                entries=entries,
                evidence_by_id=evidence_by_id,
            )
            for entry in entries:
                scored.append((entry, scores.get(entry.id) or {"utility": -1e9}))
        except Exception:  # noqa: BLE001
            scored = []

    if not scored:
        for entry in entries:
            score = module.score_guideline(
                request=request,
                situation_text=situation_text,
                entry=entry,
                evidence=evidence_by_id.get(entry.id),
            )
            scored.append((entry, score))
    scored.sort(key=lambda pair: (-float(pair[1].get("utility") or -1e9), pair[0].id))
    return scored
