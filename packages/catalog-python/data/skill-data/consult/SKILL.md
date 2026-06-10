---
name: consult
description: Use this to consult the ChartCoach Guideline Catalog. Teaches agents how to read MANIFEST.md, answer design questions with citations, compare viewpoints, and use optional indexed analysis without hard-coding section roles.
---

# ChartCoach Consult

Use ChartCoach primitives and catalog records to consult the Guideline Catalog with citations. Use this skill for design questions, chart-choice comparisons, tradeoff explanations, topic searches, source tracing, teaching, related guidance, conflicting guidance, boundary cases, and related-record exploration.

Load `core` first when catalog source, index setup, package extras, or output formats are unclear. This skill assumes the `chartcoach` command already points at the intended Catalog Instance.

## Start With The Live Catalog

Read the catalog shape before filtering or citing:

```sh
chartcoach catalog overview --format json
chartcoach catalog manifest --format markdown
chartcoach catalog roles --format jsonl
chartcoach catalog labels --format jsonl
```

Use the overview for counts and source context. Use the manifest to learn what the Catalog Instance means by its section roles, label families, tables, and vocabulary. Use roles and labels as the machine-readable inventory for deterministic filtering.

Do not assume a role named advice, context, mistakes, exceptions, fix, check, reason, or costs exists. Read the manifest, map role semantics, then use the catalog's own role names.

## Map Role Semantics

Build a role map before role-scoped retrieval:

1. Read the manifest.
2. Read roles and labels.
3. Group roles by manifest semantics.
4. Choose retrieval commands from those groups.
5. Use indexed role search only after mapping roles.
6. Verify candidates with exact reads.

| Semantic group | Manifest clues                                                                            |
| -------------- | ----------------------------------------------------------------------------------------- |
| Recommendation | Says what to do, choose, prefer, avoid, encode, use, show, label, or aggregate.           |
| Context        | Says when it applies, data situation, chart situation, reader task, audience, or scope.   |
| Boundary       | Says exceptions, limitations, caveats, costs, tradeoffs, constraints, or when not to use. |
| Failure        | Says mistakes, risks, warnings, anti-patterns, failure modes, or misleading cases.        |
| Repair         | Says fix, revise, change, replace, check, validate, or remediate.                         |
| Rationale      | Says why, evidence, reason, mechanism, perceptual basis, or empirical support.            |
| Source         | Gives citation context, bibliography, research grounding, or source detail.               |

One manifest role can belong to more than one group. Some Catalog Instances may not define every group.

## No-Index Consultation

Use base CLI commands first:

```sh
chartcoach catalog query --contains "<concept>" --format jsonl
chartcoach catalog query --section-contains "<concept>" --show-matches --format jsonl
chartcoach catalog query --body-contains "<concept>" --show-matches --format jsonl
chartcoach catalog labels --contains "<concept>" --format jsonl
chartcoach catalog query --label <exact-label-from-labels> --format jsonl
chartcoach catalog query --any-label <label-a> --any-label <label-b> --format jsonl
chartcoach catalog sql "select guideline_id, role, title from sections where content ilike '%<concept>%'" --format jsonl
chartcoach catalog read <guideline-id> --section <role-from-manifest> --source-detail minimal --format markdown
chartcoach catalog cite <guideline-id> <another-guideline-id> --format markdown
```

For compare questions, retrieve each option separately and then search for shared contexts, boundaries, and failure modes:

```sh
chartcoach catalog query --section-contains "<option-a>" --show-matches --format jsonl
chartcoach catalog query --section-contains "<option-b>" --show-matches --format jsonl
chartcoach catalog sql "select g.id, g.title, s.role, s.content from guidelines g join sections s on s.guideline_id = g.id where s.content ilike '%<concept>%'" --format jsonl
```

For source tracing:

```sh
chartcoach catalog read <guideline-id> --source-detail minimal --format markdown
chartcoach catalog cite <guideline-id> --format markdown
```

Discovery commands produce candidates. `catalog read` produces the exact guideline text needed for evidence. `catalog cite` produces live guideline URLs and every formatted source reference associated with the verified ids.

## Recover From Empty Results

| Empty result                                 | Next move                                                               |
| -------------------------------------------- | ----------------------------------------------------------------------- |
| No labels match                              | Try a broader term, inspect label families, or use section text search. |
| `list` or `query --contains` returns nothing | Use `query --body-contains` or `query --section-contains`.              |
| All-of labels are too strict                 | Remove one `--label` or use repeated `--any-label`.                     |
| Exact text fails                             | Search with a broader concept or a role-specific section term.          |
| SQL returns no rows                          | Inspect schema, then simplify the predicate.                            |

## Optional Indexed Discovery

Indexed discovery requires `chartcoach[index]` and a configured index. Use `core` for setup, custom catalog paths, and custom index paths.

Use role-scoped discovery only after mapping roles:

```sh
chartcoach catalog find --mode fts --candidate-limit 80 --limit 10 --format compact "<query>"
chartcoach catalog find --mode vector --where "role = 'overview'" --format compact "<query>"
chartcoach catalog find --mode hybrid --where "role = 'section.<manifest-role>'" --format compact "<query>"
```

Indexed discovery improves recall, but it can return plausible false positives. Read exact guideline sections before presenting a result as evidence.

## Advanced Analysis Tiers

Use three tiers for knowledge-space questions:

| Tier                     | Use                                                                                                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Base CLI              | Use manifest, roles, labels, query, SQL, and read. No index required.                                                                                         |
| 2. CLI indexed discovery | Use `catalog find` with `--mode fts`, `--mode vector`, or `--mode hybrid`. Use `--where "role = 'section.<role>'"` after deriving `<role>` from the manifest. |
| 3. Analysis environment  | Use a notebook, DuckDB, LanceDB, or equivalent vector table to compute pairwise operators over role-specific embeddings.                                      |

Tier 2 returns candidate guideline ids. Tier 3 can score pairwise relationships such as similar recommendation with different context. Current CLI `catalog find` does not expose built-in pairwise cosine operator commands. Pairwise operators require an analysis table or notebook environment.

Every tier still requires exact `catalog read` checks before claims. Use `catalog cite` only after verification.

## Operator Meta-Method

Derive operators from manifest semantics:

1. Identify role groups from `MANIFEST.md`.
2. Decide the relationship the user wants to inspect.
3. Choose two role groups to compare.
4. Decide whether similarity or distance should be high.
5. Generate candidates.
6. Read the exact guidelines.
7. Explain the relationship in catalog terms.
8. Mark false positives and uncertainty.

Use this operator schema:

```text
Operator name:
Question it answers:
Role group A:
Role group B:
Similarity condition:
Distance condition:
Candidate command or analysis query:
Exact-read validation:
Answer shape:
Failure mode:
```

Operator patterns that adapt to any role map:

| Operator             | Question                                                                  | Role relationship                                                       |
| -------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Transfer             | Where does the same principle apply in a different setting?               | Similar recommendation roles, different context roles.                  |
| Conflict             | Where do records address the same situation with different interventions? | Similar context roles, less similar recommendation roles.               |
| Divergence           | Where does one record recommend what another warns against?               | Recommendation roles similar to failure roles.                          |
| Boundary             | Where does one rule hand off to another?                                  | Context roles similar to boundary roles.                                |
| Convergence          | Where do different problems share a repair move?                          | Similar repair roles, different failure roles.                          |
| Remediation Distance | How large is the change implied by a guideline?                           | Distance between failure roles and repair roles within the same record. |
| Source Trail         | Which records share evidence roots or literature neighborhoods?           | Similar recommendations or contexts, then compare source records.       |
| Projection           | What clusters exist in the knowledge space?                               | Project role-specific embeddings and inspect neighborhoods.             |

If a catalog manifest defines roles like the current default catalog, these operators become concrete examples. For another catalog, remap roles from that catalog's manifest.

| Example operator     | Example role formula                                    |
| -------------------- | ------------------------------------------------------- |
| Analogical Transfer  | Similar `section.advice`, different `section.context`.  |
| Solution Convergence | Similar `section.fix`, different `section.mistakes`.    |
| Boundary Detection   | `section.context` similar to `section.exceptions`.      |
| Conflict Detection   | Similar `section.context`, lower `overview` similarity. |
| Remediation Distance | Distance between `section.fix` and `section.mistakes`.  |
| Viewpoint Divergence | `section.advice` similar to `section.mistakes`.         |
| Projection           | UMAP or atlas view over role-specific embeddings.       |

Treat these examples as current-catalog examples, not ChartCoach contracts. Dense embeddings can return topical overlap before logical fit, polarity, or strict conditionality.

## Answer Format

```text
Short answer:
Relevant guideline records:
Tradeoffs and boundaries:
Multiple viewpoints:
Source trail:
Uncertainty:
```

For each cited record, include the guideline id, title, relevant section, exact-read command, source detail when available, and the uncertainty or boundary around the claim.
