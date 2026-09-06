---
name: visfeedback
description: Review a rendered visualization with chartcoach guidelines and source citations.
---

# chartcoach Visfeedback

Inspect the rendered chart, find relevant guideline entry records, and connect
each feedback claim to visible evidence. Read `core` first. It sets
`CHARTCOACH_SOURCE` and inspects the current roles and labels before this
workflow begins.

## Inspect the chart

Record the state being reviewed:

| Field             | Record                                                                           |
| ----------------- | -------------------------------------------------------------------------------- |
| Chart             | Marks, encodings, variables, units, scales, and layout                           |
| Reader task       | Overview, lookup, comparison, trend, distribution, relation, or anomaly          |
| Supporting text   | Title, labels, legend, axes, annotations, tooltips, and source notes             |
| Interaction state | Default, hover, selected, toggled, animated, or keyboard state                   |
| Risk              | Ambiguity, overplotting, hidden identity, clipping, contrast, or missing context |
| Evidence          | Screenshot, rendered page, accessibility snapshot, data, or inference            |

Inspect every state you discuss. Use the rendered chart for visual claims and
an accessibility snapshot for names and structure.

## Find records

Translate observed facts into ordinary search terms:

```text
line chart direct labels many series exact lookup
dense scatterplot tooltip identity overplotting
choropleth region names unfamiliar geography color key
```

Inspect the catalog labels, then search:

```sh
chartcoach catalog labels --contains "<visible concept>" --format json
chartcoach catalog list --contains "<task or risk>" --format json
```

Use SQL for section text or `catalog search` when an indexed profile is available
and ordinary filters leave too many matches:

```sh
chartcoach catalog search \
  --profile <profile-id> \
  --mode fts \
  --limit 10 \
  "<chart> <task> <risk>"
```

## Check each record

Read each selected record before citing it:

```sh
chartcoach catalog read <guideline-entry-id> \
  --source-detail minimal \
  --format markdown
chartcoach catalog cite <guideline-entry-id> --format markdown
```

For each record, decide whether it:

- applies and the chart follows it
- applies and the chart violates it
- is related but outside this case
- cannot be judged from the available evidence

Discard records whose chart family, reader task, data type, or interaction
state differs from the observed case. A screenshot can support layout and
labeling claims. Hover, keyboard, and animation claims need evidence from
those states.

## Write the feedback

For each point, connect:

```text
suggested change or decision to preserve the design
  -> visible chart evidence
  -> guideline entry ID, title, and applicable section
  -> tradeoff or missing evidence
  -> source citation
```
