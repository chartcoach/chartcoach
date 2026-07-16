---
name: visfeedback
description: Use this for source-backed feedback on an observed visualization with chartcoach.
---

# chartcoach Visfeedback

Inspect the rendered visualization, retrieve candidate catalog records, and
connect each feedback claim to visible evidence. Load `core` for source and CLI
mechanics.

## Record Visible Evidence

Capture the state that the feedback covers:

| Field             | Record                                                                            |
| ----------------- | --------------------------------------------------------------------------------- |
| Chart             | Marks, encodings, variables, units, scales, and layout.                           |
| Reader task       | Overview, lookup, comparison, trend, distribution, relation, or anomaly.          |
| Support           | Title, labels, legend, axes, annotations, tooltips, and source notes.             |
| State             | Default, hover, selected, toggled, animated, or keyboard state.                   |
| Risk              | Ambiguity, overplotting, hidden identity, clipping, contrast, or missing context. |
| Evidence boundary | Screenshot, rendered DOM, accessibility snapshot, data, or inference.             |

Capture each interactive state before making a claim about it. Use rendered
evidence for appearance and accessibility evidence for accessible naming and
structure.

## Retrieve Candidates

Translate visible facts into reader-facing search terms:

```text
line chart direct labels many series exact lookup
dense scatterplot tooltip identity overplotting
choropleth region names unfamiliar geography color key
```

Inspect vocabulary, then search:

```sh
chartcoach catalog labels --contains "<visible concept>" --format json
chartcoach catalog list --contains "<task or risk>" --format json
```

Use SQL for section text and `find` for broader indexed recall:

```sh
chartcoach catalog find \
  --profile <profile> \
  --mode fts \
  --limit 10 \
  --format compact \
  "<chart> <task> <risk>"
```

## Verify And Classify

Read selected records before citing them:

```sh
chartcoach catalog read <guideline-id> \
  --source-detail minimal \
  --format markdown
chartcoach catalog cite <guideline-id> --format markdown
```

Classify each verified record as respected, violated, adjacent, or uncertain.
Keep rejected retrieval matches in private notes when provenance is required.

Reject a match whose chart family, reader task, data type, or interaction state
falls outside the observed case. Screenshot evidence supports visible layout
and labeling claims. Claims about hover, keyboard access, or animation require
evidence from that state.

## Write Feedback

For each point, include:

- the observed chart evidence
- guideline id and title
- respected, violated, adjacent, or uncertain status
- the applicable section and scope
- a concrete change or reason to preserve the current design
- uncertainty from missing state, data semantics, audience, or intent

Use this compact structure:

```text
Observed evidence:
Feedback:
Catalog record:
Suggested action:
Evidence boundary:
```
