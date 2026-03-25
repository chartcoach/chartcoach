from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass
from functools import reduce
from operator import and_, or_
from typing import Any, NotRequired, TypedDict, cast

import chartcoach as cc
import polars as pl
from chromadb import K

from ..types import (
    AUDIENCE_MODIFIER_SPECS,
    AudienceModifierId,
    GroundingRecord,
    GroundingRequest,
    GroundingStrategyMode,
)
from ..utils import build_grounding_record


class StructuredGroundingConfig(TypedDict):
    # Chroma fetch depth for each individual structured search job before
    # parent-level reciprocal-rank fusion.
    n_results: int
    # Maximum number of parent guidelines kept after fusion, before those
    # parents expand back out into section docs for prompt injection.
    top_k: int
    # Final cap on the returned `doc_ids` / `guidance` items after parent
    # expansion and materialization. Defaults to 4 when omitted.
    max_items: NotRequired[int]
    # Reciprocal-rank fusion damping constant. Larger values flatten the rank
    # contribution from each search job; smaller values reward top hits more.
    # Final injected section count can exceed `top_k` because each kept parent
    # can contribute multiple output roles.
    rrf_k: int


def _normalize_keyword(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", text.lower())).strip()


def _keyword_tokens(text: str) -> tuple[str, ...]:
    normalized = _normalize_keyword(text)
    if not normalized:
        return ()
    return tuple(normalized.split())


def _polarity_filter_expr(
    polarities: list[str | None] | None,
) -> pl.Expr:
    if not polarities:
        return pl.lit(True)

    return reduce(
        or_,
        [
            pl.col("polarity").eq(pl.lit(polarity))
            if polarity is not None
            else pl.col("polarity").is_null()
            for polarity in set(polarities)
        ],
    )


def _label_row_to_string(row: dict[str, str | None]) -> str:
    parts = [
        cast(str, row["category"]),
        cast(str, row["subcategory"]),
    ]
    polarity = row.get("polarity")
    if polarity is not None:
        parts.append(polarity)
    return ":".join(parts)


def _find_relevant_labels(
    coach: cc.Coach,
    *,
    category: str,
    keyword: str | None,
    polarities: list[str | None] | None,
) -> list[str]:
    if keyword is None:
        return []

    normalized_keyword = _normalize_keyword(keyword)
    if not normalized_keyword:
        return []

    candidate_rows = (
        coach.catalog.labels_df.filter(category=category)
        .filter(_polarity_filter_expr(polarities))
        .to_dicts()
    )
    if not candidate_rows:
        return []

    exact_matches = [
        row
        for row in candidate_rows
        if _normalize_keyword(cast(str, row["subcategory"])) == normalized_keyword
    ]
    if exact_matches:
        return sorted({_label_row_to_string(row) for row in exact_matches})

    query_tokens = set(_keyword_tokens(keyword))
    if not query_tokens:
        return []

    scored_rows: list[tuple[tuple[int, int, int], dict[str, str | None]]] = []
    for row in candidate_rows:
        label_tokens = set(_keyword_tokens(cast(str, row["subcategory"])))
        if not label_tokens:
            continue
        overlap = len(query_tokens & label_tokens)
        if overlap == 0:
            continue
        score = (
            overlap,
            -len(query_tokens - label_tokens),
            -len(label_tokens - query_tokens),
        )
        scored_rows.append((score, row))

    if not scored_rows:
        return []

    best_score = max(score for score, _ in scored_rows)
    best_rows = [row for score, row in scored_rows if score == best_score]
    return sorted({_label_row_to_string(row) for row in best_rows})


def _metadata_filter(
    *,
    role: str,
    purpose_labels: list[str],
    label_groups: list[list[str]],
) -> dict[str, Any]:
    conditions: list[Any] = [
        K("role") == f"section.{role}",
    ]
    if purpose_labels:
        conditions.append(
            reduce(
                or_,
                (K("labels").contains(label) for label in purpose_labels),
            )
        )
    for labels in label_groups:
        if labels:
            conditions.append(
                reduce(
                    or_,
                    (K("labels").contains(label) for label in labels),
                )
            )
    return reduce(and_, conditions).to_dict()


def labels_for_family(
    coach: cc.Coach,
    family: str,
    *,
    polarities: list[str | None] | None = None,
) -> list[str]:
    rows = (
        coach.catalog.labels_df.filter(category=family)
        .filter(_polarity_filter_expr(polarities))
        .to_dicts()
    )
    return sorted({_label_row_to_string(row) for row in rows})


def _audience_modifier(
    audience: AudienceModifierId | None,
) -> dict[str, list[str] | str] | None:
    if audience is None:
        return None

    spec = AUDIENCE_MODIFIER_SPECS[audience]
    return {
        "description": spec["description"],
        "labels": [
            *spec["literacy_labels"],
            *spec["audience_labels"],
            *spec["needs_labels"],
        ],
    }


def _label_groups_for_refinement(
    coach: cc.Coach,
    req: GroundingRequest,
) -> list[list[str]]:
    return [
        _find_relevant_labels(
            coach,
            category="chart",
            keyword=req["chart"],
            polarities=["use", None],
        ),
        _find_relevant_labels(
            coach,
            category="task",
            keyword=req["task"],
            polarities=None,
        ),
        _find_relevant_labels(
            coach,
            category="scope",
            keyword=req["scope"],
            polarities=None,
        ),
        *_profile_label_groups(coach, req),
    ]


def _label_groups_for_selection(
    coach: cc.Coach,
    req: GroundingRequest,
) -> list[list[str]]:
    return [
        _find_relevant_labels(
            coach,
            category="task",
            keyword=req["task"],
            polarities=None,
        ),
        _find_relevant_labels(
            coach,
            category="scope",
            keyword=req["scope"],
            polarities=None,
        ),
        *_profile_label_groups(coach, req),
    ]


def _profile_label_groups(
    coach: cc.Coach,
    req: GroundingRequest,
) -> list[list[str]]:
    if (profile := req.get("data_profile")) is None:
        return []

    retrieval_labels = profile.get("retrieval_labels", [])
    labels_by_family: dict[str, list[str]] = defaultdict(list)
    for label in retrieval_labels:
        family = label.split(":", 1)[0]
        labels_by_family[family].append(label)
    return list(labels_by_family.values())


def _rhetoric_label_groups(
    coach: cc.Coach,
    req: GroundingRequest,
) -> list[list[str]]:
    groups = [
        labels_for_family(coach, "communication", polarities=["use", None]),
    ]
    if (audience_modifier := _audience_modifier(req["audience"])) is not None:
        groups.append(cast(list[str], audience_modifier["labels"]))
    return groups


def _polish_label_groups(
    coach: cc.Coach,
    req: GroundingRequest,
) -> list[list[str]]:
    groups = [labels_for_family(coach, "polish", polarities=["use", None])]
    if not any(groups):
        groups.extend(
            [
                labels_for_family(coach, family, polarities=["use", None])
                for family in ["aesthetic", "component", "channel", "access", "quality"]
            ]
        )
    groups.extend(_profile_label_groups(coach, req))
    return groups


def _refine_search_specs(req: GroundingRequest) -> list[tuple[str, list[str]]]:
    return [
        (
            "advice",
            [
                req["query"],
                (
                    f"For a {req['chart'] or 'chart'} used for {req['task']} in a "
                    f"{req['scope']} and {req['time_mode']} setting, what concrete "
                    "design changes improve readability and fidelity?"
                ),
                (f"{req['query']} Need concrete advice to improve the chart design."),
            ],
        ),
        (
            "check",
            [
                req["query"],
                (
                    f"For a {req['chart'] or 'chart'} used for {req['task']} in a "
                    f"{req['scope']} and {req['time_mode']} setting, what are the "
                    "failure signs and quick checks for readability and fidelity?"
                ),
                (
                    f"{req['query']} Need checks, failure signs, and common "
                    "mistakes to avoid."
                ),
            ],
        ),
    ]


def _select_search_specs(
    req: GroundingRequest,
    *,
    audience_modifier: dict[str, list[str] | str] | None,
) -> list[tuple[str, list[str]]]:
    advice_queries = [
        req["query"],
        (
            f"For a {req['task']} task in a {req['scope']} and "
            f"{req['time_mode']} setting, which chart design should be used?"
        ),
        (f"{req['query']} Need actionable advice for choosing the chart design."),
    ]
    context_queries = [
        req["query"],
        (
            f"For a {req['task']} task in a {req['scope']} and "
            f"{req['time_mode']} setting, when is a chart choice appropriate?"
        ),
        (
            f"{req['query']} Need the context where a chart design is "
            "appropriate for this task."
        ),
    ]
    exceptions_queries = [
        req["query"],
        (
            f"For a {req['task']} task in a {req['scope']} and "
            f"{req['time_mode']} setting, when should a chart choice be avoided?"
        ),
        (
            f"{req['query']} Need boundary conditions and cases where a chart "
            "choice would fail."
        ),
    ]
    if audience_modifier is not None:
        audience_description = cast(str, audience_modifier["description"])
        advice_queries.append(
            (
                f"{audience_description} For a {req['task']} task with "
                f"{req['scope']} and {req['time_mode']}, which chart design "
                "should be used?"
            )
        )
        context_queries.append(
            (
                f"{audience_description} For a {req['task']} task with "
                f"{req['scope']} and {req['time_mode']}, when is a chart choice "
                "appropriate?"
            )
        )
        exceptions_queries.append(
            (
                f"{audience_description} For a {req['task']} task with "
                f"{req['scope']} and {req['time_mode']}, when should a chart "
                "choice be avoided?"
            )
        )
    return [
        ("advice", advice_queries),
        ("context", context_queries),
        ("exceptions", exceptions_queries),
    ]


def _rhetoric_search_specs(
    req: GroundingRequest,
    *,
    audience_modifier: dict[str, list[str] | str] | None,
) -> list[tuple[str, list[str]]]:
    audience_prefix = (
        f"{cast(str, audience_modifier['description'])} "
        if audience_modifier is not None
        else ""
    )
    return [
        (
            "advice",
            [
                req["query"],
                (
                    f"{audience_prefix}How should this visualization be framed, "
                    "explained, or narrated so the message lands clearly and credibly?"
                ),
            ],
        ),
        (
            "context",
            [
                (
                    f"{audience_prefix}What surrounding context, framing, or "
                    "credibility cues help readers interpret this visualization "
                    "correctly?"
                ),
            ],
        ),
    ]


def _polish_search_specs(req: GroundingRequest) -> list[tuple[str, list[str]]]:
    return [
        (
            "advice",
            [
                req["query"],
                (
                    "What cross-grammar finishing moves would make this "
                    "visualization cleaner, clearer, and more visually compelling?"
                ),
            ],
        ),
        (
            "check",
            [
                (
                    "What quick checks reveal clutter, weak hierarchy, weak "
                    "annotation, or low communication quality in this chart?"
                ),
            ],
        ),
    ]


def _dedupe_query_texts(query_texts: list[str]) -> list[str]:
    return list(dict.fromkeys(query_texts))


def _query_parent_rankings(
    collection: Any,
    *,
    query_texts: list[str],
    role: str,
    purpose_labels: list[str],
    label_groups: list[list[str]],
    n_results: int,
) -> list[list[str]]:
    non_empty_groups = [labels for labels in label_groups if labels]
    fallback_groups = [
        non_empty_groups[:index] for index in range(len(non_empty_groups), -1, -1)
    ]

    for effective_groups in fallback_groups:
        result = collection.query(
            query_texts=query_texts,
            where=_metadata_filter(
                role=role,
                purpose_labels=purpose_labels,
                label_groups=effective_groups,
            ),
            n_results=n_results,
            include=["metadatas"],
        )
        parent_rankings: list[list[str]] = []
        for metadata_rows in cast(
            list[list[dict[str, Any]]],
            result["metadatas"] or [],
        ):
            parent_ranking = list(
                dict.fromkeys(
                    cast(str, metadata["parent_id"]) for metadata in metadata_rows
                )
            )
            if parent_ranking:
                parent_rankings.append(parent_ranking)
        if parent_rankings:
            return parent_rankings

    return []


def _refine_search_jobs(
    coach: cc.Coach,
    req: GroundingRequest,
) -> list[tuple[str, str, list[str], list[list[str]]]]:
    label_groups = _label_groups_for_refinement(coach, req)
    jobs = [
        (role, "core", _dedupe_query_texts(query_texts), label_groups)
        for role, query_texts in _refine_search_specs(req)
    ]
    jobs.extend(
        (
            role,
            "rhetoric",
            _dedupe_query_texts(query_texts),
            _rhetoric_label_groups(coach, req),
        )
        for role, query_texts in _rhetoric_search_specs(
            req,
            audience_modifier=_audience_modifier(req["audience"]),
        )
    )
    jobs.extend(
        (
            role,
            "polish",
            _dedupe_query_texts(query_texts),
            _polish_label_groups(coach, req),
        )
        for role, query_texts in _polish_search_specs(req)
    )
    return jobs


def _select_search_jobs(
    coach: cc.Coach,
    req: GroundingRequest,
) -> list[tuple[str, str, list[str], list[list[str]]]]:
    # Always run a task-only branch. If audience is present, also run the
    # audience-conditioned branch, but keep audience as a bounded reranker.
    search_jobs = [
        (
            role,
            "core",
            _dedupe_query_texts(query_texts),
            _label_groups_for_selection(coach, req),
        )
        for role, query_texts in _select_search_specs(req, audience_modifier=None)
    ]

    if (audience_modifier := _audience_modifier(req["audience"])) is not None:
        search_jobs.extend(
            [
                (
                    role,
                    "audience",
                    _dedupe_query_texts(query_texts),
                    _label_groups_for_selection(coach, req),
                )
                for role, query_texts in _select_search_specs(
                    req,
                    audience_modifier=audience_modifier,
                )
            ]
        )

    search_jobs.extend(
        (
            role,
            "rhetoric",
            _dedupe_query_texts(query_texts),
            _rhetoric_label_groups(coach, req),
        )
        for role, query_texts in _rhetoric_search_specs(
            req,
            audience_modifier=_audience_modifier(req["audience"]),
        )
    )
    search_jobs.extend(
        (
            role,
            "polish",
            _dedupe_query_texts(query_texts),
            _polish_label_groups(coach, req),
        )
        for role, query_texts in _polish_search_specs(req)
    )

    return search_jobs


def _output_roles(req: GroundingRequest) -> list[str]:
    if req["objective"] == "refine":
        return ["section.advice", "section.check", "section.context"]
    return ["section.advice", "section.context", "section.exceptions"]


def _rank_job_weight(*, role: str, branch: str) -> float:
    branch_weights = {
        "core": 1.0,
        "audience": 0.6,
        "rhetoric": 0.85,
        "polish": 0.75,
    }
    weight = branch_weights.get(branch, 1.0)
    if role == "exceptions":
        return weight * 0.85
    return weight


def _accumulate_rank_scores(
    scores: dict[str, float],
    rankings: list[list[str]],
    *,
    k: int,
    weight: float,
) -> None:
    for ranked in rankings:
        for rank, parent_id in enumerate(ranked, start=1):
            scores[parent_id] = scores.get(parent_id, 0.0) + weight / (k + rank)


def _build_parent_label_maps(
    docs_df: pl.DataFrame,
) -> tuple[dict[str, list[str]], dict[str, dict[str, str]]]:
    parent_labels = {
        cast(str, row["parent_id"]): cast(list[str], row["labels"])
        for row in docs_df.filter(pl.col("role") == "document")
        .select("parent_id", "labels")
        .unique("parent_id")
        .to_dicts()
    }
    parent_docs: dict[str, dict[str, str]] = defaultdict(dict)
    for row in docs_df.select("id", "parent_id", "role").to_dicts():
        parent_docs[cast(str, row["parent_id"])][cast(str, row["role"])] = cast(
            str, row["id"]
        )
    return parent_labels, dict(parent_docs)


def _label_polarities(labels: list[str]) -> dict[str, str | None]:
    states: dict[str, set[str]] = defaultdict(set)
    for label in labels:
        parts = label.split(":")
        if len(parts) == 3 and parts[-1] in {"use", "avoid"}:
            states[f"{parts[0]}:{parts[1]}"].add(parts[-1])

    resolved: dict[str, str | None] = {}
    for key, polarities in states.items():
        if len(polarities) == 1:
            resolved[key] = next(iter(polarities))
        else:
            resolved[key] = None
    return resolved


def _conflict_penalty(
    candidate_id: str,
    selected_ids: list[str],
    *,
    parent_polarities: dict[str, dict[str, str | None]],
) -> tuple[bool, float]:
    candidate_polarities = parent_polarities.get(candidate_id, {})
    hard_conflict = False
    penalty = 0.0

    for selected_id in selected_ids:
        selected_polarities = parent_polarities.get(selected_id, {})
        for key, candidate_state in candidate_polarities.items():
            if candidate_state is None:
                continue
            selected_state = selected_polarities.get(key)
            if selected_state is None or selected_state == candidate_state:
                continue
            if key.startswith("chart:") or key.startswith("channel:"):
                hard_conflict = True
            else:
                penalty += 0.1

    return hard_conflict, penalty


def _audience_label_bonus(
    labels: list[str],
    *,
    audience_labels: list[str],
) -> float:
    if not audience_labels:
        return 0.0
    matches = len(set(labels) & set(audience_labels))
    if matches == 0:
        return 0.0
    return 0.25 * (matches / len(audience_labels))


def _time_label_adjustment(
    labels: list[str],
    *,
    request_time_labels: list[str],
) -> float:
    request_keys = {":".join(label.split(":")[:2]) for label in request_time_labels}
    if not request_keys:
        return 0.0

    parent_time_keys = {
        ":".join(parts[:2])
        for label in labels
        if len(parts := label.split(":")) >= 2 and parts[0] == "time"
    }
    if not parent_time_keys:
        return 0.0
    if parent_time_keys & request_keys:
        return 0.15
    return -0.5


def _profile_match_bonus(
    labels: list[str],
    *,
    profile: Any,
) -> float:
    if profile is None:
        return 0.0

    expected_labels = cast(list[str], profile.get("retrieval_labels", []))
    if not expected_labels:
        return 0.0

    matches = len(set(expected_labels) & set(labels))
    return 0.15 * matches


def _lane_top_candidates(
    scores: dict[str, float],
    *,
    exclude: set[str],
    limit: int = 8,
) -> list[str]:
    return [
        parent_id
        for parent_id, _ in sorted(
            (
                (parent_id, score)
                for parent_id, score in scores.items()
                if parent_id not in exclude
            ),
            key=lambda item: (-item[1], item[0]),
        )[:limit]
    ]


def _select_parent_ids(
    ranked_candidates: list[str],
    *,
    target_count: int,
    combined_scores: dict[str, float],
    parent_polarities: dict[str, dict[str, str | None]],
) -> list[str]:
    selected_ids: list[str] = []
    remaining_ids = list(dict.fromkeys(ranked_candidates))

    while remaining_ids and len(selected_ids) < target_count:
        feasible: list[tuple[float, str]] = []
        fallback: list[tuple[float, str]] = []
        for parent_id in remaining_ids:
            hard_conflict, penalty = _conflict_penalty(
                parent_id,
                selected_ids,
                parent_polarities=parent_polarities,
            )
            score = combined_scores.get(parent_id, 0.0) - penalty
            if hard_conflict:
                fallback.append((score, parent_id))
            else:
                feasible.append((score, parent_id))

        pool = feasible or fallback
        if not pool:
            break

        _, next_parent = max(pool, key=lambda item: (item[0], item[1]))
        selected_ids.append(next_parent)
        remaining_ids = [
            parent_id for parent_id in remaining_ids if parent_id != next_parent
        ]

    return selected_ids


def _assemble_doc_ids(
    parent_ids: list[str],
    *,
    output_roles: list[str],
    parent_docs: dict[str, dict[str, str]],
    role_scores: dict[str, dict[str, float]],
    max_items: int,
) -> list[str]:
    per_parent_roles: dict[str, list[str]] = {}
    for parent_id in parent_ids:
        available_roles = [
            role for role in output_roles if role in parent_docs.get(parent_id, {})
        ]
        supported_roles = sorted(
            [
                role
                for role in available_roles
                if role_scores.get(parent_id, {}).get(role, 0.0) > 0
            ],
            key=lambda role: (-role_scores[parent_id][role], output_roles.index(role)),
        )
        unsupported_roles = [
            role for role in available_roles if role not in supported_roles
        ]
        per_parent_roles[parent_id] = supported_roles + unsupported_roles[:1]

    doc_ids: list[str] = []
    while len(doc_ids) < max_items:
        made_progress = False
        for parent_id in parent_ids:
            if len(doc_ids) >= max_items:
                break
            remaining_roles = per_parent_roles.get(parent_id, [])
            if not remaining_roles:
                continue
            role = remaining_roles.pop(0)
            doc_id = parent_docs[parent_id].get(role)
            if doc_id is None:
                continue
            doc_ids.append(doc_id)
            made_progress = True
        if not made_progress:
            break

    return doc_ids


@dataclass(slots=True)
class StructuredGroundingStrategy:
    coach: cc.Coach
    config: StructuredGroundingConfig
    mode: GroundingStrategyMode = "structured"

    def retrieve(self, req: GroundingRequest) -> GroundingRecord:
        """Retrieve one grounding record using section-aware catalog search."""

        if req["objective"] == "refine":
            search_jobs = _refine_search_jobs(self.coach, req)
        else:
            search_jobs = _select_search_jobs(self.coach, req)
        purpose_labels = _find_relevant_labels(
            self.coach,
            category="purpose",
            keyword=req["objective"],
            polarities=None,
        )

        output_roles = _output_roles(req)
        max_items = self.config.get("max_items", 4)
        docs_df = self.coach.catalog.docs_df.unnest("metadata")
        parent_labels, parent_docs = _build_parent_label_maps(docs_df)
        parent_polarities = {
            parent_id: _label_polarities(labels)
            for parent_id, labels in parent_labels.items()
        }

        core_scores: dict[str, float] = {}
        audience_scores: dict[str, float] = {}
        rhetoric_scores: dict[str, float] = {}
        polish_scores: dict[str, float] = {}
        role_scores: dict[str, dict[str, float]] = defaultdict(dict)

        for role, branch, query_texts, label_groups in search_jobs:
            parent_rankings = _query_parent_rankings(
                self.coach.index.collection,
                query_texts=query_texts,
                role=role,
                purpose_labels=purpose_labels,
                label_groups=label_groups,
                n_results=self.config["n_results"],
            )
            if not parent_rankings:
                continue

            job_weight = _rank_job_weight(role=role, branch=branch)
            if branch == "core":
                target_scores = core_scores
            elif branch == "audience":
                target_scores = audience_scores
            elif branch == "rhetoric":
                target_scores = rhetoric_scores
            else:
                target_scores = polish_scores
            _accumulate_rank_scores(
                target_scores,
                parent_rankings,
                k=self.config["rrf_k"],
                weight=job_weight,
            )
            section_role = f"section.{role}"
            for parent_ranking in parent_rankings:
                for rank, parent_id in enumerate(parent_ranking, start=1):
                    role_scores[parent_id][section_role] = role_scores[parent_id].get(
                        section_role,
                        0.0,
                    ) + job_weight / (self.config["rrf_k"] + rank)

        if not core_scores:
            return build_grounding_record(self.coach, [])

        rerank_pool_size = self.config["top_k"] * 6
        core_pool = [
            parent_id
            for parent_id, _ in sorted(
                core_scores.items(),
                key=lambda item: (-item[1], item[0]),
            )[:rerank_pool_size]
        ]

        if req["audience"] is not None and len(core_pool) < self.config["top_k"]:
            for parent_id, _ in sorted(
                audience_scores.items(),
                key=lambda item: (-item[1], item[0]),
            ):
                if parent_id not in core_pool:
                    core_pool.append(parent_id)
                    break

        decision_scores = {
            parent_id: core_scores.get(parent_id, 0.0) for parent_id in core_pool
        }
        request_time_labels = _find_relevant_labels(
            self.coach,
            category="time",
            keyword=req["time_mode"],
            polarities=None,
        )
        for parent_id in core_pool:
            time_adjustment = _time_label_adjustment(
                parent_labels.get(parent_id, []),
                request_time_labels=request_time_labels,
            )
            decision_scores[parent_id] += time_adjustment
            decision_scores[parent_id] += _profile_match_bonus(
                parent_labels.get(parent_id, []),
                profile=req.get("data_profile"),
            )
        if (audience_modifier := _audience_modifier(req["audience"])) is not None:
            audience_labels = cast(list[str], audience_modifier["labels"])
            for parent_id in core_pool:
                time_adjustment = _time_label_adjustment(
                    parent_labels.get(parent_id, []),
                    request_time_labels=request_time_labels,
                )
                if time_adjustment < 0:
                    continue
                decision_scores[parent_id] += audience_scores.get(parent_id, 0.0)
                decision_scores[parent_id] += _audience_label_bonus(
                    parent_labels.get(parent_id, []),
                    audience_labels=audience_labels,
                )

        decision_target = min(2, self.config["top_k"])
        parent_ids = _select_parent_ids(
            _lane_top_candidates(
                decision_scores, exclude=set(), limit=rerank_pool_size
            ),
            target_count=decision_target,
            combined_scores=decision_scores,
            parent_polarities=parent_polarities,
        )

        selected_set = set(parent_ids)
        for lane_scores in (rhetoric_scores, polish_scores):
            if len(parent_ids) >= self.config["top_k"]:
                break
            lane_candidates = _lane_top_candidates(
                lane_scores,
                exclude=selected_set,
                limit=rerank_pool_size,
            )
            if not lane_candidates:
                continue
            lane_parent_ids = _select_parent_ids(
                lane_candidates,
                target_count=1,
                combined_scores=lane_scores,
                parent_polarities=parent_polarities,
            )
            for parent_id in lane_parent_ids:
                if parent_id in selected_set:
                    continue
                parent_ids.append(parent_id)
                selected_set.add(parent_id)

        if len(parent_ids) < self.config["top_k"]:
            backfill_candidates = _lane_top_candidates(
                decision_scores,
                exclude=selected_set,
                limit=rerank_pool_size,
            )
            while backfill_candidates and len(parent_ids) < self.config["top_k"]:
                next_parent_ids = _select_parent_ids(
                    backfill_candidates,
                    target_count=1,
                    combined_scores=decision_scores,
                    parent_polarities=parent_polarities,
                )
                if not next_parent_ids:
                    break
                next_parent = next_parent_ids[0]
                parent_ids.append(next_parent)
                selected_set.add(next_parent)
                backfill_candidates = _lane_top_candidates(
                    decision_scores,
                    exclude=selected_set,
                    limit=rerank_pool_size,
                )

        if not parent_ids:
            return build_grounding_record(self.coach, [])

        doc_ids = _assemble_doc_ids(
            parent_ids,
            output_roles=output_roles,
            parent_docs=parent_docs,
            role_scores=role_scores,
            max_items=max_items,
        )
        return build_grounding_record(
            self.coach,
            doc_ids,
        )
