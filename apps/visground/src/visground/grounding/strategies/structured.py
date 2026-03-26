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
                (
                    f"For a {req['chart'] or 'chart'} used for {req['task']} in a "
                    f"{req['scope']} and {req['time_mode']} setting, what concrete "
                    "design changes improve readability and fidelity?"
                ),
                (
                    f"Need chart-specific guidance to refine an existing "
                    f"{req['chart'] or 'chart'} for {req['task']} without generic "
                    "provenance or storytelling advice."
                ),
            ],
        ),
        (
            "check",
            [
                (
                    f"For a {req['chart'] or 'chart'} used for {req['task']} in a "
                    f"{req['scope']} and {req['time_mode']} setting, what are the "
                    "failure signs and quick checks for readability and fidelity?"
                ),
                (
                    f"Need quick checks, failure signs, and common mistakes for "
                    f"an existing {req['chart'] or 'chart'} used for {req['task']}."
                ),
            ],
        ),
        (
            "fix",
            [
                (
                    f"For a {req['chart'] or 'chart'} used for {req['task']} in a "
                    f"{req['scope']} and {req['time_mode']} setting, what concrete "
                    "edit operations would improve readability and fidelity?"
                ),
                (
                    f"Need concrete edit operations to improve an existing "
                    f"{req['chart'] or 'chart'} for {req['task']} without adding "
                    "generic context or provenance advice."
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
        (
            f"For a {req['task']} task in a {req['scope']} and "
            f"{req['time_mode']} setting, which chart design should be used?"
        ),
        (
            f"Need actionable, bounded chart-choice guidance for {req['task']} "
            f"in a {req['scope']} and {req['time_mode']} setting."
        ),
    ]
    context_queries = [
        (
            f"For a {req['task']} task in a {req['scope']} and "
            f"{req['time_mode']} setting, when is a chart choice appropriate?"
        ),
        (
            f"Need the applicability conditions for the right chart choice for "
            f"{req['task']} in a {req['scope']} and {req['time_mode']} setting."
        ),
    ]
    check_queries = [
        (
            f"For a {req['task']} task in a {req['scope']} and "
            f"{req['time_mode']} setting, what quick decision test distinguishes "
            "the right chart choice from a weaker alternative?"
        ),
        (
            f"{req['query']} Need a quick check to validate the chosen chart "
            "design against weaker alternatives."
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
        check_queries.append(
            (
                f"{audience_description} For a {req['task']} task with "
                f"{req['scope']} and {req['time_mode']}, what quick decision "
                "test distinguishes the right chart choice?"
            )
        )
    return [
        ("advice", advice_queries),
        ("check", check_queries),
        ("context", context_queries),
    ]


def _select_query_search_specs(
    req: GroundingRequest,
    *,
    audience_modifier: dict[str, list[str] | str] | None,
) -> list[tuple[str, list[str]]]:
    query_texts = [
        req["query"],
        (
            f"{req['query']} Need chart-choice guidance that matches the query "
            "semantics without importing unrelated domain-specific examples."
        ),
    ]
    if audience_modifier is not None:
        query_texts.append(
            (
                f"{cast(str, audience_modifier['description'])} {req['query']} "
                "Need chart-choice guidance aligned with this audience."
            )
        )
    return [("advice", query_texts), ("check", [req["query"]])]


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
                "query",
                _dedupe_query_texts(query_texts),
                _label_groups_for_selection(coach, req),
            )
            for role, query_texts in _select_query_search_specs(
                req,
                audience_modifier=audience_modifier,
            )
        )
    else:
        search_jobs.extend(
            (
                role,
                "query",
                _dedupe_query_texts(query_texts),
                _label_groups_for_selection(coach, req),
            )
            for role, query_texts in _select_query_search_specs(
                req,
                audience_modifier=None,
            )
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
        return ["section.advice", "section.check", "section.fix"]
    return ["section.advice", "section.check", "section.context"]


def _rank_job_weight(*, role: str, branch: str) -> float:
    branch_weights = {
        "core": 1.0,
        "query": 0.55,
        "audience": 0.6,
        "rhetoric": 0.85,
        "polish": 0.75,
    }
    weight = branch_weights.get(branch, 1.0)
    role_weights = {
        "advice": 1.0,
        "check": 0.7,
        "fix": 0.65,
        "context": 0.45,
        "exceptions": 0.4,
    }
    return weight * role_weights.get(role, 1.0)


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


def _label_key(label: str) -> str:
    parts = label.split(":")
    if len(parts) < 2:
        return label
    return ":".join(parts[:2])


def _labels_by_family(labels: list[str]) -> dict[str, set[str]]:
    labels_by_family: dict[str, set[str]] = defaultdict(set)
    for label in labels:
        key = _label_key(label)
        family = key.split(":", 1)[0]
        labels_by_family[family].add(key)
    return labels_by_family


def _request_family_keys(
    coach: cc.Coach,
    req: GroundingRequest,
) -> dict[str, set[str]]:
    request_family_keys: dict[str, set[str]] = defaultdict(set)

    def add_labels(labels: list[str]) -> None:
        for label in labels:
            key = _label_key(label)
            family = key.split(":", 1)[0]
            request_family_keys[family].add(key)

    if req["objective"] == "refine":
        add_labels(
            _find_relevant_labels(
                coach,
                category="chart",
                keyword=req["chart"],
                polarities=["use", None],
            )
        )

    add_labels(
        _find_relevant_labels(
            coach,
            category="task",
            keyword=req["task"],
            polarities=None,
        )
    )
    add_labels(
        _find_relevant_labels(
            coach,
            category="scope",
            keyword=req["scope"],
            polarities=None,
        )
    )
    add_labels(
        _find_relevant_labels(
            coach,
            category="time",
            keyword=req["time_mode"],
            polarities=None,
        )
    )

    if (audience_modifier := _audience_modifier(req["audience"])) is not None:
        add_labels(cast(list[str], audience_modifier["labels"]))

    if (profile := req.get("data_profile")) is not None:
        add_labels(profile.get("retrieval_labels", []))

    return request_family_keys


def _compatibility_signature(
    labels: list[str],
    *,
    request_family_keys: dict[str, set[str]],
) -> tuple[bool, int, int]:
    parent_family_keys = _labels_by_family(labels)
    hard_mismatch_families = {"chart", "structure", "time", "audience", "literacy"}

    hard_mismatch = False
    matches = 0
    soft_mismatches = 0

    for family, request_keys in request_family_keys.items():
        if not request_keys:
            continue
        parent_keys = parent_family_keys.get(family)
        if not parent_keys:
            continue
        if parent_keys & request_keys:
            matches += 1
            continue
        if family in hard_mismatch_families:
            hard_mismatch = True
        else:
            soft_mismatches += 1

    return hard_mismatch, matches, soft_mismatches


def _adjust_scores_for_request_compatibility(
    scores: dict[str, float],
    *,
    parent_labels: dict[str, list[str]],
    request_family_keys: dict[str, set[str]],
    require_match: bool = False,
) -> dict[str, float]:
    adjusted_scores: dict[str, float] = {}

    for parent_id, score in scores.items():
        labels = parent_labels.get(parent_id, [])
        hard_mismatch, matches, soft_mismatches = _compatibility_signature(
            labels,
            request_family_keys=request_family_keys,
        )
        if hard_mismatch:
            continue
        if require_match and matches == 0:
            continue
        adjusted_scores[parent_id] = score + (0.05 * matches) - (0.03 * soft_mismatches)

    return adjusted_scores


def _query_title_alignment_bonus(
    query: str,
    title: str | None,
) -> float:
    if title is None:
        return 0.0

    query_tokens = set(_keyword_tokens(query))
    title_tokens = set(_keyword_tokens(title))
    if not query_tokens or not title_tokens:
        return 0.0

    overlap = len(query_tokens & title_tokens)
    if overlap == 0:
        return 0.0
    return 0.12 * overlap


def _task_operator_bonus(
    req: GroundingRequest,
    labels: list[str],
) -> float:
    if req["task"] != "relate":
        return 0.0
    if any(label.startswith("operator:") for label in labels):
        return 0.35
    return -0.1


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

    candidate_use_keys = {
        key
        for key, state in candidate_polarities.items()
        if state == "use" and (key.startswith("chart:") or key.startswith("structure:"))
    }

    for selected_id in selected_ids:
        selected_polarities = parent_polarities.get(selected_id, {})
        selected_use_keys = {
            key
            for key, state in selected_polarities.items()
            if state == "use"
            and (key.startswith("chart:") or key.startswith("structure:"))
        }
        if candidate_use_keys and selected_use_keys:
            if candidate_use_keys != selected_use_keys:
                hard_conflict = True
                continue
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


def _has_chart_structure_select_contrast(labels: list[str]) -> bool:
    decisions: dict[str, set[str]] = defaultdict(set)
    for label in labels:
        parts = label.split(":")
        if len(parts) != 3 or parts[-1] not in {"use", "avoid"}:
            continue
        if parts[0] not in {"chart", "structure"}:
            continue
        decisions[parts[0]].add(parts[-1])
    return any(polarities == {"use", "avoid"} for polarities in decisions.values())


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

        if selected_ids and not feasible:
            break

        pool = feasible or fallback
        if not pool:
            break

        _, next_parent = max(pool, key=lambda item: (item[0], item[1]))
        selected_ids.append(next_parent)
        remaining_ids = [
            parent_id for parent_id in remaining_ids if parent_id != next_parent
        ]

    return selected_ids


def _score_search_jobs(
    coach: cc.Coach,
    *,
    search_jobs: list[tuple[str, str, list[str], list[list[str]]]],
    purpose_labels: list[str],
    config: StructuredGroundingConfig,
) -> tuple[
    dict[str, float],
    dict[str, float],
    dict[str, float],
    dict[str, float],
    dict[str, dict[str, float]],
]:
    core_scores: dict[str, float] = {}
    audience_scores: dict[str, float] = {}
    rhetoric_scores: dict[str, float] = {}
    polish_scores: dict[str, float] = {}
    role_scores: dict[str, dict[str, float]] = defaultdict(dict)

    for role, branch, query_texts, label_groups in search_jobs:
        parent_rankings = _query_parent_rankings(
            coach.index.collection,
            query_texts=query_texts,
            role=role,
            purpose_labels=purpose_labels,
            label_groups=label_groups,
            n_results=config["n_results"],
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
            k=config["rrf_k"],
            weight=job_weight,
        )
        section_role = f"section.{role}"
        for parent_ranking in parent_rankings:
            for rank, parent_id in enumerate(parent_ranking, start=1):
                role_scores[parent_id][section_role] = role_scores[parent_id].get(
                    section_role,
                    0.0,
                ) + job_weight / (config["rrf_k"] + rank)

    return core_scores, audience_scores, rhetoric_scores, polish_scores, role_scores


def _assemble_doc_ids(
    parent_ids: list[str],
    *,
    output_roles: list[str],
    parent_docs: dict[str, dict[str, str]],
    role_scores: dict[str, dict[str, float]],
    max_items: int,
    max_roles_per_parent: int = 2,
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
        if supported_roles:
            per_parent_roles[parent_id] = supported_roles[:max_roles_per_parent]
        else:
            per_parent_roles[parent_id] = available_roles[:1]

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

        output_roles = _output_roles(req)
        max_items = min(self.config.get("max_items", 4), 6)
        docs_df = self.coach.catalog.docs_df.unnest("metadata")
        parent_labels, parent_docs = _build_parent_label_maps(docs_df)
        parent_titles = {
            cast(str, row["id"]): cast(str, row["title"])
            for row in self.coach.catalog.df.select("guideline")
            .unnest("guideline")
            .select("id", "title")
            .to_dicts()
        }
        parent_polarities = {
            parent_id: _label_polarities(labels)
            for parent_id, labels in parent_labels.items()
        }
        request_family_keys = _request_family_keys(self.coach, req)

        primary_purpose_labels = _find_relevant_labels(
            self.coach,
            category="purpose",
            keyword=req["objective"],
            polarities=None,
        )
        (
            core_scores,
            audience_scores,
            rhetoric_scores,
            polish_scores,
            role_scores,
        ) = _score_search_jobs(
            self.coach,
            search_jobs=search_jobs,
            purpose_labels=primary_purpose_labels,
            config=self.config,
        )
        core_scores = _adjust_scores_for_request_compatibility(
            core_scores,
            parent_labels=parent_labels,
            request_family_keys=request_family_keys,
            require_match=True,
        )
        audience_scores = _adjust_scores_for_request_compatibility(
            audience_scores,
            parent_labels=parent_labels,
            request_family_keys=request_family_keys,
        )
        rhetoric_scores = _adjust_scores_for_request_compatibility(
            rhetoric_scores,
            parent_labels=parent_labels,
            request_family_keys=request_family_keys,
        )
        polish_scores = _adjust_scores_for_request_compatibility(
            polish_scores,
            parent_labels=parent_labels,
            request_family_keys=request_family_keys,
        )

        if req["objective"] == "select" and not core_scores:
            (
                core_scores,
                audience_scores,
                rhetoric_scores,
                polish_scores,
                role_scores,
            ) = _score_search_jobs(
                self.coach,
                search_jobs=search_jobs,
                purpose_labels=["purpose:refine"],
                config=self.config,
            )
            core_scores = _adjust_scores_for_request_compatibility(
                core_scores,
                parent_labels=parent_labels,
                request_family_keys=request_family_keys,
                require_match=True,
            )
            audience_scores = _adjust_scores_for_request_compatibility(
                audience_scores,
                parent_labels=parent_labels,
                request_family_keys=request_family_keys,
            )
            rhetoric_scores = _adjust_scores_for_request_compatibility(
                rhetoric_scores,
                parent_labels=parent_labels,
                request_family_keys=request_family_keys,
            )
            polish_scores = _adjust_scores_for_request_compatibility(
                polish_scores,
                parent_labels=parent_labels,
                request_family_keys=request_family_keys,
            )

        if req["objective"] == "select" and core_scores:
            primary_core_pool = [
                parent_id
                for parent_id, _ in sorted(
                    core_scores.items(),
                    key=lambda item: (-item[1], item[0]),
                )[: self.config["top_k"] * 6]
            ]
            has_true_select_parent = any(
                _has_chart_structure_select_contrast(
                    parent_labels.get(parent_id, []),
                )
                for parent_id in primary_core_pool
            )
            if not has_true_select_parent:
                (
                    core_scores,
                    audience_scores,
                    rhetoric_scores,
                    polish_scores,
                    role_scores,
                ) = _score_search_jobs(
                    self.coach,
                    search_jobs=search_jobs,
                    purpose_labels=["purpose:refine"],
                    config=self.config,
                )

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
            if req["objective"] == "select":
                if _has_chart_structure_select_contrast(
                    parent_labels.get(parent_id, []),
                ):
                    decision_scores[parent_id] += 0.2
                else:
                    decision_scores[parent_id] -= 0.2
                decision_scores[parent_id] += _task_operator_bonus(
                    req,
                    parent_labels.get(parent_id, []),
                )
                decision_scores[parent_id] += _query_title_alignment_bonus(
                    req["query"],
                    parent_titles.get(parent_id),
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

        parent_budget = min(3, self.config["top_k"])
        decision_target = min(2, parent_budget)
        parent_ids = _select_parent_ids(
            _lane_top_candidates(
                decision_scores, exclude=set(), limit=rerank_pool_size
            ),
            target_count=decision_target,
            combined_scores=decision_scores,
            parent_polarities=parent_polarities,
        )

        selected_set = set(parent_ids)
        best_core_score = max(decision_scores.values(), default=0.0)
        orthogonal_floor = best_core_score * 0.5
        orthogonal_candidates: list[tuple[float, str]] = []
        for lane_scores in (rhetoric_scores, polish_scores):
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
            if not lane_parent_ids:
                continue
            lane_parent_id = lane_parent_ids[0]
            lane_score = lane_scores.get(lane_parent_id, 0.0)
            if lane_score < orthogonal_floor:
                continue
            orthogonal_candidates.append((lane_score, lane_parent_id))

        if orthogonal_candidates and len(parent_ids) < parent_budget:
            _, orthogonal_parent_id = max(
                orthogonal_candidates,
                key=lambda item: (item[0], item[1]),
            )
            if orthogonal_parent_id not in selected_set:
                parent_ids.append(orthogonal_parent_id)
                selected_set.add(orthogonal_parent_id)

        if len(parent_ids) < parent_budget:
            backfill_candidates = [
                parent_id
                for parent_id in _lane_top_candidates(
                    decision_scores,
                    exclude=selected_set,
                    limit=rerank_pool_size,
                )
                if not _conflict_penalty(
                    parent_id,
                    parent_ids,
                    parent_polarities=parent_polarities,
                )[0]
            ]
            while backfill_candidates and len(parent_ids) < parent_budget:
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
                backfill_candidates = [
                    parent_id
                    for parent_id in _lane_top_candidates(
                        decision_scores,
                        exclude=selected_set,
                        limit=rerank_pool_size,
                    )
                    if not _conflict_penalty(
                        parent_id,
                        parent_ids,
                        parent_polarities=parent_polarities,
                    )[0]
                ]

        if not parent_ids:
            return build_grounding_record(self.coach, [])

        doc_ids = _assemble_doc_ids(
            parent_ids,
            output_roles=output_roles,
            parent_docs=parent_docs,
            role_scores=role_scores,
            max_items=max_items,
            max_roles_per_parent=2,
        )
        return build_grounding_record(
            self.coach,
            doc_ids,
        )
