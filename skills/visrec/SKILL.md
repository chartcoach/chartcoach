---
name: visrec
description: Recommend a visualization from the data, reader task, audience, and constraints with chartcoach citations.
---

# chartcoach Visrec

Use catalog records to recommend a visualization from a design brief. The
`visfeedback` instructions cover an existing rendered chart. The `core`
instructions must be read first. They set `CHARTCOACH_SOURCE` and inspect the
current roles and labels before this workflow begins.

## Describe the brief

| Field       | Record                                                                                               |
| ----------- | ---------------------------------------------------------------------------------------------------- |
| Data        | Fields, types, scales, units, aggregation, missing values, number of categories, time, and geography |
| Reader task | Compare, look up, rank, follow a trend, inspect a distribution, find a relation, or spot an anomaly  |
| Audience    | General public, analyst, expert, executive, learner, or reviewer                                     |
| Output      | Static chart, dashboard, paper, slide, notebook, web component, or specification                     |
| Constraints | Accessibility, color, layout, print, interaction, annotation, and uncertainty                        |
| Tool        | Target chart library or rendering environment                                                        |

Ask for the data fields, reader task, or output when missing information could
change the chart choice. Otherwise state the assumption beside the affected
recommendation.

## Find records

Search the task and each important constraint separately:

```sh
chartcoach catalog list \
  --contains "<reader task>" \
  --format json
chartcoach catalog list \
  --contains "<constraint>" \
  --format json
```

Check the current labels and roles before passing them as exact filters:

```sh
chartcoach catalog labels --contains "<concept>" --format json
chartcoach catalog roles --format json
```

If an indexed profile is available and ordinary filters leave too many
matches, use full-text search:

```sh
chartcoach catalog find \
  --profile <profile> \
  --mode fts \
  --limit 10 \
  --format compact \
  "<data> <task> <audience> <constraint>"
```

## Check the records

Read and cite every record used in the recommendation:

```sh
chartcoach catalog read <guideline-id> \
  --source-detail full \
  --format markdown
chartcoach catalog cite <guideline-id> --format markdown
```

Discard a record when its chart family, task, audience, data type, or
interaction state differs from the brief.

## Write the recommendation

Connect each decision to the brief and catalog evidence:

```text
recommended chart or encoding
  -> fact from the data, task, audience, or constraints
  -> guideline ID, title, and applicable section
  -> tradeoff or remaining uncertainty
  -> source citation
```

Keep library-specific implementation advice separate from statements supported
by the catalog record.
