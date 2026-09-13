---
name: visrec
description: Recommend a visualization from the data, reader task, audience, and constraints with chartcoach citations.
---

# chartcoach Visrec

Use guideline entry records to recommend a visualization from a design brief.
Use `visfeedback` for an existing rendered chart. Read `core` for catalog
selection, retrieval, and citation.

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

Preserve the measured quantity, units, aggregation, and meaning of uncertainty
when proposing a design. Distinguish facts supplied by the brief from
assumptions that still need confirmation.

## Find records

Follow `core` to search the reader task and each important constraint. Use
short terms such as `comparison`, `uncertainty`, or `labels` separately with
`contains`. Use full-text search for combined concepts when a profile is
available. Recover from empty matches before deciding that the catalog lacks
guidance for the brief.

## Check the records

Read and cite selected records together using the host's tools or the access
recipes in `core`.

Discard a record when its chart family, task, audience, data type, or
interaction state differs from the brief. Check its applicable situations and
exceptions, including what its quantities or intervals represent. A matching
title or retrieval score is a candidate for inspection, not proof that the
recommendation fits.

Separate the initial design from alternatives that solve a specific problem.
Use the brief's stated facts to support the initial choice. Field names and
category counts do not establish overlap, large scale differences, outliers, or
other patterns in the values. Keep recommendations for those conditions as
explicit contingencies until data or a rendered chart establishes them.
Preserve the reader task: comparing shapes over time and comparing values at
the same time are different requirements and can favor different layouts.

## Write the recommendation

Connect each decision to the brief and catalog evidence:

```text
recommended chart or encoding
  -> fact from the data, task, audience, or constraints
  -> guideline entry ID, title, and applicable section
  -> tradeoff or remaining uncertainty
  -> source citation
```

Keep library-specific implementation advice separate from statements supported
by the catalog record. Identify sources with `cite` and inspect a publication
before attributing a specific claim to it. When the catalog supports part of a
design, distinguish that guidance from your additional reasoning.

Lead with the recommended chart or encoding and explain which fact in the brief
supports it. Include an alternative when a named constraint changes the choice.
A design brief can support a recommendation before any chart exists. Assess
compliance with guidelines when the task asks to inspect an existing chart,
following `visfeedback`.
