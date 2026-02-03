# 2026-02-03 Retrieval Operators Refactor (Slice 3)

## Motivation

The retrieval strategy pipelines are currently readable, but they duplicate a lot of boilerplate:
role-aware fallback, status-filter planning, and “search -> aggregate -> map to entries” scaffolding.
This repetition makes strategies harder to audit (for scenario leakage), harder to maintain, and
encourages subtle behavior drift when we change a shared convention.

## Goals

- Keep strategy implementations thin and composable by extracting shared mechanics into reusable
  “operators”.
- Preserve existing retrieval semantics (no behavior change): same role fallback behavior, same
  candidate-k logic for status filtering, and same meta fields.
- Make it easier for future work to add new strategy families without copy/pasting scaffolding.

## Non-Goals

- Changing scoring, fusion, reranking, or selection semantics.
- Changing artifact schemas or eval-ui behavior.
- Introducing scenario-specific heuristics (strictly forbidden).

## Proposed Operator Modules

`chartcoach.retrieval.operators.search`
- `search_dense_with_focus(...)`
- `search_fts_with_focus(...)`
- `search_hybrid_with_focus(...)`

Each helper applies:
1) primary role selection based on the configured focus mode,
2) optional fallback-role broadening when role-filtered retrieval returns empty results.

Return `(hits_df, roles_used)` so strategies can log which roles were active.

`chartcoach.retrieval.operators.status`
- `plan_status_filter(...) -> (use_status_filter, candidate_k)`
- `apply_status_filter(...) -> (ordered_entries, status_meta)`

This centralizes the (focus-mode, config, scorer-present) checks and the `candidate_multiplier`
logic while keeping the expensive filtering call opt-in (only invoked when enabled).

## Integration Plan

1) Add the operator modules + unit tests for their core contracts (role fallback, candidate_k).
2) Refactor the three baselines first (`ann-dense@v1`, `bm25-prf@v1`, `hybrid-rrf@v1`) to use
   operators while keeping their behavior identical.
3) Migrate remaining strategies opportunistically when they touch the same patterns.

## Testing Strategy

- Add operator-level contract tests with a stub `GuidelineSearcher` that returns empty/non-empty
  `polars.DataFrame`s to verify fallback behavior deterministically.
- Keep strategy tests focused on invariants (k handling, meta keys, role logging) rather than
  line/branch coverage.

