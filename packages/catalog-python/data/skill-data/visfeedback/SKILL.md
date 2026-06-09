---
name: visfeedback
description: Use this for visualization feedback with ChartCoach. Teaches agents how to inspect a chart, translate visible evidence into search signals, query the catalog, and cite guideline ids without hard-coding catalog vocabulary.
---

# ChartCoach Visfeedback

Use ChartCoach primitives to ground visualization feedback in the current Guideline Catalog. This skill defines the workflow. It does not encode a fixed manifest or assume any one visualization source.

## Start With The Live Catalog

Read the catalog contract before filtering or citing:

```sh
chartcoach catalog manifest --format json
chartcoach catalog roles --format jsonl
chartcoach catalog labels --format jsonl
```

Use the manifest and table output to learn valid section roles, label families, and table names for the current catalog. Do not guess old role names.

Omit `--source` to use the package-pinned default catalog. Use `--source` only when the user provides a custom catalog locator.

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

When an embedded chart blocks useful DOM inspection, switch to screenshot-led evidence. Capture the default state, the relevant hover or selected state, and an accessibility snapshot if the browser tool can provide one. Treat missing accessible text as an observed access gap only when the test actually covered that state.

When working from saved browser artifacts, treat screenshots and saved Markdown visual notes as chart evidence. Treat snapshots, DOM excerpts, and code snippets as supporting evidence about labels, interaction states, and data fields.

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

When a library term is too internal, translate it. For example, a pointer demo may need terms such as hover identity, exact value lookup, tooltip, keyboard access, and target visibility.

## Query And Retrieve

Start with base catalog queries:

```sh
chartcoach catalog query --contains "<observed text>" --format jsonl
chartcoach catalog query --label <exact-label> --label-prefix <prefix> --format jsonl
chartcoach catalog sql "select id, title from guidelines limit 10" --format jsonl
```

If a query returns no JSONL rows, relax one observed signal at a time. Inspect labels with `catalog labels --contains TEXT`, try a broader visual term in `--body-contains` or `--section-contains`, or use `catalog sql` when you need explicit boolean grouping. Do not jump to indexed discovery until the base path has had a reasonable pass.

Then inspect selected records with exact ids and manifest roles:

```sh
chartcoach catalog read <guideline-id>
chartcoach catalog read <guideline-id> --section <role-from-manifest> --source-detail minimal --format markdown
```

Use indexed discovery only after base navigation is too broad:

```sh
chartcoach catalog index create --index ./chartcoach-index
chartcoach catalog find --index ./chartcoach-index --mode fts --candidate-limit 80 --limit 10 --format compact "<query>"
```

Use `--mode hybrid` only after building the index with a LanceDB-native embedding function:

```sh
chartcoach catalog index create --index ./chartcoach-index --embedding sentence-transformers --embedding-option name=all-MiniLM-L6-v2
chartcoach catalog find --index ./chartcoach-index --mode hybrid --format compact "<query>"
```

Use section roles from the live manifest. If `catalog read` rejects a role, inspect valid roles and retry with current names.

Compact search output names indexed document roles. A match such as `section.<role>` points to an indexed section. Retrieve the manifest role after checking that it exists.

Copy guideline ids exactly from compact search output. Do not construct ids from titles, snippets, or nearby wording.

## Write Feedback

For each cited guideline, include:

- guideline id and title
- why it applies to the observed chart
- whether it is satisfied, violated, adjacent, or out of scope
- the visible evidence that supports the judgment
- uncertainty when the screenshot or interaction state is incomplete

Keep the critique grounded in the chart and the catalog. Do not let retrieval false positives drive the feedback. If a result is close but scoped to a different chart family or task, say so and choose a better citation.

## Applicability Boundaries

- Reject adjacent hits when the top result is scoped to another chart family, reader task, data type, or interaction state.
- If search results are adjacent but not exact, state the boundary and run a narrower query before citing.
- For synthetic demos, library demos, or visualizations without a clear communication task, keep feedback bounded to visible evidence. Do not invent a redesign objective.
- Tooltip and interaction claims need observed interaction evidence.
- Missing legends and hidden category identity often require visual inspection in addition to retrieval.
- Dense plots need terms for overplotting, density, lookup, and label availability.
- Map, projection, contour, density, and geometry examples often retrieve adjacent guidance. Preserve the applicability boundary.
- Small multiples and dense demos often retrieve guidance for one visible subchart. State which panel, repeated mark, or interaction state the citation covers.
- Specialized statistical charts may be valid for expert readers while still needing extra explanation for general audiences.
