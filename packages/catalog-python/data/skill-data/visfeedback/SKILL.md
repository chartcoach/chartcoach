---
name: visfeedback
description: Use this for visualization feedback with ChartCoach. Teaches agents how to inspect a chart, translate visible evidence into catalog queries, retrieve matching guideline records, and cite exact guideline ids without hard-coding catalog vocabulary.
---

# ChartCoach Visfeedback

Use ChartCoach primitives to ground visualization feedback in the current Guideline Catalog. This skill defines the feedback steps. It does not assume fixed labels, fixed section roles, or any one visualization source.

Load `core` first when catalog source, index setup, package extras, or output formats are unclear. This skill assumes the `chartcoach` command already points at the intended Catalog Instance.

## Start With The Live Catalog

Read the catalog shape before filtering or citing:

```sh
chartcoach catalog overview --format json
chartcoach catalog roles --format jsonl
chartcoach catalog labels --format jsonl
chartcoach catalog manifest --format markdown
```

Use these commands to learn valid section roles, label families, and table names for the current catalog. Do not guess role names or labels from memory.

## Inspect The Visualization First

Record what is visible before searching:

- chart family or mark family
- variables and units
- encodings such as position, length, color, size, shape, text, facet, and order
- reader task such as overview, lookup, comparison, distribution, trend, anomaly, or relation
- interaction state such as default, hover, selected, toggled, animated, or keyboard access
- visible support such as title, legend, axis labels, annotations, gridlines, tooltips, source notes, and labels
- failure signs such as missing legend, ambiguous units, overplotting, hidden identity, clipped text, or unstable screenshot state

If the visualization is interactive, capture the relevant state. Do not claim hover-only content is available until you have observed it.

When an embedded chart blocks DOM inspection, switch to screenshot-led evidence. Capture the default state, the relevant hover or selected state, and an accessibility snapshot if the browser tool can provide one. Treat missing accessible text as an observed access gap only when the test actually covered that state.

When working from saved browser artifacts, treat screenshots and saved Markdown visual notes as chart evidence. Treat snapshots, DOM excerpts, and code snippets as supporting evidence about labels, interaction states, and data fields.

Use this evidence record before retrieval:

| Field                | Record                                                                                    |
| -------------------- | ----------------------------------------------------------------------------------------- |
| Visible evidence     | What the chart shows in the observed state.                                               |
| Data and task        | Data type, scale, variables, and reader task.                                             |
| Encoding and support | Channels, labels, legends, axes, annotations, tooltips, source notes, and layout support. |
| Failure mode         | The visible risk, ambiguity, or missing support.                                          |
| Interaction state    | Default, hover, selected, toggled, animated, keyboard state, or unavailable.              |
| Evidence boundary    | Screenshot, DOM, accessibility snapshot, source snippet, or inference.                    |

## Translate Evidence Into Search Signals

Build queries from observed signals rather than page titles. Include the task and failure mode:

```text
line chart direct labels many series color legend exact lookup
tooltip category context hover value units dense scatterplot identity
choropleth map region names values color key unfamiliar geography
histogram bin width frequency distribution novice exact lookup
```

Decompose the visual evidence into separate searches when one query mixes too many concerns:

- chart family or mark family
- reader task
- data type and scale
- encoding channel
- failure mode
- interaction state

When an implementation term is too internal, translate it into the reader task, encoding channel, interaction state, visible support, or failure mode it creates.

Run broad-to-narrow searches:

1. Start with chart facts and reader tasks.
2. Add the visible support or failure mode.
3. Inspect labels, roles, and values before using exact catalog vocabulary.
4. Use `--show-matches` when text-filtered candidates need match evidence.
5. Relax one predicate when results are empty.

## Query And Retrieve

Start with base catalog navigation. These commands do not require LanceDB:

```sh
chartcoach catalog list --contains "<observed text>" --format jsonl
chartcoach catalog labels --contains "<observed term>" --format jsonl
chartcoach catalog query --contains "<observed text>" --section-contains "<observed term>" --format jsonl
chartcoach catalog query --label <exact-label> --format jsonl
chartcoach catalog query --any-label <exact-label> --any-label <another-label> --format jsonl
chartcoach catalog query --label-prefix <prefix> --format jsonl
chartcoach catalog sql "select id, title from guidelines limit 10" --format jsonl
```

Use schema and values commands only for catalog structure and catalog vocabulary:

```sh
chartcoach catalog schema --tables --row-counts
chartcoach catalog schema
chartcoach catalog values labels --contains "<term>" --format jsonl
chartcoach catalog values roles --format jsonl
chartcoach catalog values label.family --format jsonl
```

For `catalog values`, pass a field alias or `TABLE.COLUMN` as the first argument. Do not pass an observed chart term, label family, or audience word as the field. Put search text in `--contains`, inspect label families with `catalog values label.family`, and inspect labels inside one family with `catalog labels --family <family>`.

If a query returns no JSONL rows, relax one observed signal at a time. Inspect labels with `catalog labels --contains TEXT`, try a broader visual term in `--body-contains` or `--section-contains`, or use `catalog sql` when you need explicit boolean grouping. Do not jump to indexed discovery until the base path has had a reasonable pass.

Then inspect selected records with exact ids and manifest roles:

```sh
chartcoach catalog read <guideline-id>
chartcoach catalog read <guideline-id> --section <role-from-manifest> --source-detail minimal --format markdown
chartcoach catalog cite <guideline-id> <another-guideline-id> --format markdown
```

Do not cite a guideline from `catalog list`, `catalog query`, `catalog sql`, or `catalog find` alone. These commands produce candidates. `catalog read` produces the exact guideline text to verify. `catalog cite` formats guideline URLs and source references for verified ids.

Use indexed discovery only after base navigation is too broad:

```sh
chartcoach catalog find --mode fts --candidate-limit 80 --limit 10 --format compact "<query>"
chartcoach catalog find --mode vector --where "role = 'overview'" --format compact "<query>"
chartcoach catalog find --mode hybrid --where "role = 'section.<manifest-role>'" --format compact "<query>"
```

Use `--mode vector` or `--mode hybrid` only when the configured index supports vector search. Use `core` for index setup.

Use section roles from the live catalog. If `catalog read` rejects a role, inspect valid roles and retry with current names.

Compact search output names indexed document roles. A match such as `section.<role>` points to an indexed section. Retrieve the manifest role after checking that it exists.

Copy guideline ids exactly from compact search output. Do not construct ids from titles, snippets, or nearby wording.

## Write Feedback

Classify retrieved guidance before writing the response:

- respected
- violated
- adjacent
- uncertain
- rejected

Use `rejected` as an internal trail for candidates that failed exact-read validation, had the wrong scope, or were retrieval false positives. Do not include rejected guidelines in the user-facing response by default. Include them only when the user asks for retrieval provenance, audit detail, or a list of excluded candidates.

For each user-facing guideline, include:

- guideline id and title
- why it applies to the observed chart
- whether it is respected, violated, adjacent, or uncertain
- the visible evidence that supports the judgment
- the discovery command that found the candidate
- the exact `catalog read` command used before citation
- the `catalog cite` command used when final output needs formatted references
- uncertainty from missing screenshot detail, incomplete interaction state, ambiguous task or audience, unknown data semantics, unclear chart intent, or conflicting catalog evidence

Keep the critique grounded in the chart and the catalog. Do not let retrieval false positives drive the feedback. If a result is close but scoped to a different chart family or task, say so and choose a better citation.

Use this retrieval template in notes or final feedback when provenance matters:

```text
Visible evidence:
Search signals:
Commands tried:
Exact reads:
Respected:
Violated:
Adjacent:
Rejected:
Uncertainty:
```

## Applicability Boundaries

- Reject adjacent hits when the top result is scoped to another chart family, reader task, data type, or interaction state.
- If search results are adjacent but not exact, state the boundary and run a narrower query before citing.
- For synthetic demos, library demos, or visualizations without a clear communication task, keep feedback bounded to visible evidence. Do not invent a redesign objective.
- Tooltip and interaction claims need observed interaction evidence.
- Screenshot-only review can support visible layout and labeling claims, but not hidden hover, keyboard, or animation claims.
- DOM and source snippets can support field names and interaction wiring, but not final visual appearance without rendered evidence.
- Accessibility snapshots can support accessible naming and structure only for the captured state.
- Missing legends and hidden category identity often require visual inspection in addition to retrieval.
- Dense plots need terms for overplotting, density, lookup, and label availability.
- Map, projection, contour, density, and geometry examples often retrieve adjacent guidance. Preserve the applicability boundary.
- Small multiples and dense demos often retrieve guidance for one visible subchart. State which panel, repeated mark, or interaction state the citation covers.
