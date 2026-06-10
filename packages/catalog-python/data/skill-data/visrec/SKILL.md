---
name: visrec
description: Use this for Visualization Recommendation with ChartCoach. Teaches agents how to turn a data task, audience, constraints, and output target into source-traced chart recommendations using manifest-driven catalog navigation and optional indexed discovery.
---

# ChartCoach Visrec

Use ChartCoach primitives to recommend visualization designs from a design brief. This skill starts from data, task, audience, constraints, and output target. Use `visfeedback` instead when the task starts from an existing chart and observed visual evidence.

Load `core` first when catalog source, index setup, package extras, or output formats are unclear. This workflow assumes the `chartcoach` command already points at the intended Catalog Instance.

## Start With The Live Catalog

Read the catalog shape before filtering or citing:

```sh
chartcoach catalog overview --format json
chartcoach catalog manifest --format markdown
chartcoach catalog roles --format jsonl
chartcoach catalog labels --format jsonl
```

Use the overview for counts and source context. Use the manifest to learn what the Catalog Instance means by its section roles, label families, tables, and vocabulary. Use roles and labels as the machine-readable inventory for deterministic filtering.

Do not guess role names or label values from memory. Exact labels in examples are patterns only. Inspect live labels before using exact values.

## Record The Design Brief

Capture the brief before retrieval:

| Field          | Record                                                                                                      |
| -------------- | ----------------------------------------------------------------------------------------------------------- |
| Data           | Fields, types, scales, units, aggregation, missingness, cardinality, time, and geography.                   |
| Reader task    | Compare, lookup, rank, trend, distribution, relationship, anomaly, part-to-whole, overview, or explanation. |
| Audience       | General public, analyst, domain expert, executive, learner, or internal reviewer.                           |
| Output         | Static chart, dashboard, paper figure, slide, notebook, web component, spec, or prose recommendation.       |
| Constraints    | Accessibility, color, layout, space, print, interaction, annotation, uncertainty, and toolchain.            |
| Target library | Vega-Lite, Observable Plot, Altair, ggplot, matplotlib, D3, React charting, or none.                        |

Ask for missing data shape, task, or output target only when the recommendation would otherwise be underdetermined. If a reasonable assumption lets the work proceed, state it and keep the caveat local to the recommendation.

## Translate Brief To Search Signals

Search with generic visualization concepts:

- data type and scale
- reader task
- audience literacy
- chart family or candidate encoding
- visible support such as labels, legends, axes, annotations, source notes, and tooltips
- constraints such as accessibility, small space, print, interaction, uncertainty, or color
- failure modes the design must avoid

Search broad first, then narrow with live labels, roles, sections, or SQL.

## No-Index Retrieval

Use base CLI commands first:

```sh
chartcoach catalog list --contains "<term>" --format jsonl
chartcoach catalog labels --contains "<term>" --format jsonl
chartcoach catalog query --contains "<term>" --format jsonl
chartcoach catalog query --section-contains "<term>" --show-matches --format jsonl
chartcoach catalog query --body-contains "<term>" --show-matches --format jsonl
chartcoach catalog query --label <exact-label-from-labels> --format jsonl
chartcoach catalog query --any-label <label-a> --any-label <label-b> --format jsonl
chartcoach catalog query --label-prefix <family-or-prefix> --format jsonl
chartcoach catalog schema --tables --row-counts
chartcoach catalog schema --format jsonl
chartcoach catalog values labels --contains "<term>" --format jsonl
chartcoach catalog values roles --format jsonl
chartcoach catalog sql "<read-only SELECT query>" --format jsonl
```

Use `--show-matches` when text-filtered candidates need match evidence. Use SQL when the relationship is clearer as table logic than as a keyword query.

For design choice questions, run separate searches for task fit, chart or encoding choice, audience needs, and constraints. Then read exact records before recommending.

## Recover From Empty Results

| Empty result                 | Next move                                                           |
| ---------------------------- | ------------------------------------------------------------------- |
| No labels match              | Try a broader term, inspect label families, or search section text. |
| `list` returns nothing       | Use `query --body-contains` or `query --section-contains`.          |
| All-of labels are too strict | Remove one `--label` or use repeated `--any-label`.                 |
| Exact text fails             | Search with a broader concept or a role-specific section term.      |
| SQL returns no rows          | Inspect schema, then simplify the predicate.                        |

Empty output is a retrieval signal. It is not evidence that the Guideline Catalog has no relevant design guidance.

## Optional Indexed Discovery

Indexed discovery requires `chartcoach[index]` and a configured index. Use `core` for setup, custom catalog paths, and custom index paths.

Use indexed discovery to broaden recall after base navigation:

```sh
chartcoach catalog find --mode fts --candidate-limit 80 --limit 10 --format compact "<query>"
chartcoach catalog find --mode vector --where "role = 'overview'" --format compact "<query>"
chartcoach catalog find --mode hybrid --where "role = 'section.<manifest-role>'" --format compact "<query>"
```

Choose `<manifest-role>` after reading the manifest and roles. Search output reports indexed document roles such as `overview` and `section.<role>`. `catalog read --section` uses the manifest role name without the `section.` prefix.

Indexed discovery returns candidates and can return plausible false positives. Verify each candidate with exact reads.

## Exact Reads And Evidence

Read exact guideline records before citing:

```sh
chartcoach catalog read <guideline-id> --section <role-from-manifest> --source-detail minimal --format markdown
chartcoach catalog cite <guideline-id> <another-guideline-id> --format markdown
```

For every recommendation, keep:

- design brief fact
- discovery command
- candidate id
- exact-read command
- citation command when final output needs formatted references
- guideline id and title
- section evidence
- applicability or caveat

## Answer Format

```text
Recommendation:
Why it fits:
Catalog evidence:
Alternatives:
Caveats:
Implementation notes:
Uncertainty:
```

Include implementation notes only when the target library or output format is known. Keep library-specific advice separate from catalog evidence.
