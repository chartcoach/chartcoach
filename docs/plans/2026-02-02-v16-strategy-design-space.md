# V16 Plan: Retrieval Strategy Design-Space Expansion (DSPy + LanceDB)

Date: 2026-02-02

This plan expands ChartCoach retrieval strategies to explore a broader research design space while keeping every strategy scenario-agnostic, composable, and runnable standalone.

## Goals

1) Implement multiple, clearly distinct strategy families inspired by the provided designs:
- ANN-only dense retrieval
- label-gated candidate pruning + vector rerank
- label-first deterministic filtering + abstract retrieval
- chart+intent decomposition with parallel facet retrieval + fusion
- section-role-aware retrieval (advice/context/exceptions/check/fix/...)
- neighborhood exploration to surface alternative “schools of thought”

2) Make “violation focus” a **strategy option** (not eval-time post-processing), with a consistent interface across strategies:
- `focus = violations | satisfied | all`

3) Ensure all strategies remain runnable **in isolation** and continue to run end-to-end through:
- `uv run chartcoach-retrieval run ...`
- eval artifacts generation
- eval-ui loading those artifacts

## Hard Constraints

- No strategy may hard-code anything about the eval specs/scenarios (IDs, titles, filenames, etc.).
- No scenario-specific heuristics or hard-coded “hints”.
- Any “intelligence” for decomposition, label routing, role routing, etc. must be via DSPy modules.
- Strategies must be usable outside the eval runner: no reliance on eval-only preprocessing.

## Assumptions (explicit; no questions asked)

- The guideline catalog’s label set is large (~1k unique labels), so label prediction must be robust to imperfect strings (canonicalization/fuzzy mapping required).
- Guideline sections have 8 roles: `advice, check, context, costs, exceptions, fix, mistakes, reason`.
- It is acceptable to build additional LanceDB tables / indices locally and reuse them across runs via stable digests.
- “Violation focus” can be approximated via a strategy-internal status scorer that predicts violated/satisfied/unclear/not_applicable; the scorer is used for reranking/selection, not as a global eval filter.

## Strategy Suite (V16 Additions)

Each strategy will accept a config including `focus`, `k`, and optional modules (LM/VLM).

### A) Dense ANN Baseline

`ann-dense@v1`:
- Dense vector search over an embedding index (ANN), minimal logic.
- Purpose: expose embedding-only strengths/weaknesses.

### B) Label-Gated ANN

`label-gated-ann@v1`:
- DSPy predicts a compact set of labels (high recall).
- Deterministically filters candidate guideline IDs by label match.
- Runs dense/hybrid retrieval within candidates + rerank.
- Purpose: scalability + precision through upstream pruning.

### C) Label-First + Abstract Retrieval

`label-first-abstract@v1`:
- DSPy interprets request into label constraints.
- Searches an “abstract” index (title/description/labels/short section summaries) via FTS/hybrid.
- Optionally reranks with dense similarity.
- Purpose: interpretable and efficient structured retrieval.

### D) Decompose + Parallel Retrieval

`decompose-parallel@v1`:
- DSPy decomposes chart+intent into facets/entities (form, marks, tasks, audience, constraints, likely issues).
- Runs parallel retrieval per facet (optionally label-gated per facet).
- Fuses results (weighted RRF / score sum) + dedup.
- Purpose: divide-and-conquer coverage and controllable breadth.

### E) Role-Aware Section Retrieval

`role-aware-sections@v1`:
- DSPy selects section roles to search based on user intent + `focus`.
- Searches only those roles (e.g., `fix/mistakes/check/exceptions` under violations).
- Aggregates section hits back to guideline cards.
- Purpose: precision through role-restricted retrieval.

### F) Neighborhood Explorer (Schools of Thought)

`neighborhood-explorer@v1`:
- Stage 1: produce anchors via a base retriever (configurable: label-gated or decompose-parallel).
- Stage 2: explore neighbors in section embedding space:
  - same-role similarity (“similar advice”)
  - same-context / different-advice (“schools of thought”)
  - context→exceptions boundary exploration
- Emits a diversified set and writes structured meta about discovered alternatives.

## Indexing / LanceDB

Add or reuse LanceDB-backed indices via `CatalogVectorIndex` caches:
- **Main**: sections + title + description + labels (already used).
- **Abstracts**: per-guideline synthesized “abstract” text rows (new).
- **Sections**: section-only index (optional; role filtering on main index may suffice).

Strategy implementations will choose the appropriate index/searcher rather than relying on eval runner behavior.

## DSPy Modules

New DSPy modules (composable; usable by multiple strategies):
- Chart+intent decomposition (VLM-aware; uses chart image when available).
- Label preselection + canonicalization.
- Section-role router (focus-aware).
- Schools-of-thought analyzer (optional summarization of divergent advice clusters).

## Evaluation Protocol (V16)

Run all strategies (existing + new) with k=16 against the scenarios spec and regenerate artifacts:
- Quantitative metrics must be spec-agnostic (latency, cost, diversity, redundancy, role distribution, internal focus/status distribution).
- Qualitative analysis will be written in IEEE VIS-style “Evaluation” prose, grounded by manual inspection of top-k outputs.

Outputs:
- `nogit/eval-artifacts/v16/`
- `nogit/strat-eval/v16-top16.md` and `nogit/strat-eval/v16-top16-lean.md`
- `nogit/strat-eval/report.md` extended with v16 results and research-strengthening recommendations.

