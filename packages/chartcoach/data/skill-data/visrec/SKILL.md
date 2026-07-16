---
name: visrec
description: Use this for source-backed visualization recommendations from a data task, audience, and constraints with chartcoach.
---

# chartcoach Visrec

Use catalog records to recommend a visualization from a design brief. Use
`visfeedback` for an observed chart. Load `core` for source and CLI mechanics.

## Record The Brief

| Field       | Record                                                                                    |
| ----------- | ----------------------------------------------------------------------------------------- |
| Data        | Fields, types, scales, units, aggregation, missingness, cardinality, time, and geography. |
| Reader task | Compare, lookup, rank, trend, distribution, relation, anomaly, or explanation.            |
| Audience    | General public, analyst, expert, executive, learner, or reviewer.                         |
| Output      | Static chart, dashboard, paper, slide, notebook, web component, or specification.         |
| Constraints | Accessibility, color, layout, print, interaction, annotation, and uncertainty.            |
| Toolchain   | Target chart library or rendering environment.                                            |

Ask for missing data shape, reader task, or output target when it changes the
recommendation. Otherwise state the assumption next to the affected choice.

## Retrieve Candidates

Search separately for task fit, encoding choice, audience needs, and
constraints:

```sh
chartcoach catalog labels --contains "<concept>" --format json
chartcoach catalog list --contains "<task or constraint>" --format json
```

Use SQL for role-specific content or label intersections. Use indexed discovery
when terms in the brief differ from catalog wording:

```sh
chartcoach catalog find \
  --profile <profile> \
  --mode fts \
  --limit 10 \
  --format compact \
  "<data> <task> <audience> <constraint>"
```

Broaden one term at a time when retrieval is empty. Inspect the live labels and
roles before introducing exact catalog vocabulary.

## Verify Evidence

Read exact records before recommending a design:

```sh
chartcoach catalog read <guideline-id> \
  --source-detail minimal \
  --format markdown
chartcoach catalog cite <guideline-id> --format markdown
```

For each recommendation, retain the brief fact, discovery command, exact-read
command, guideline id, applicable section, and scope boundary.

## Write The Recommendation

```text
Recommendation:
Why it fits:
Catalog evidence:
Alternatives:
Caveats:
Implementation notes:
Uncertainty:
```

Connect each recommendation to a brief fact and a verified catalog record.
Keep library-specific implementation advice separate from catalog evidence.
