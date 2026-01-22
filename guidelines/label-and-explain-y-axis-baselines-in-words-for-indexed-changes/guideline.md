---
id: label-and-explain-y-axis-baselines-in-words-for-indexed-changes
title: Label the y-axis baseline in words when showing indexed change from a reference
  period
bibliography: references.bib
description: Make indexed charts understandable by naming the reference point and
  expressing values as deviations from it.
labels:
- chart:line
- task:compare
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- custom:indexed-data
---

## Name the reference point on the y-axis, not just the number <!-- role: advice -->

Label the y-axis baseline in words (for example, “Employment as of Q3 2023”) when the chart shows values relative to a reference period. Also explain at least one tick label as a deviation from that baseline (for example, “−5% from 2023”).

## Why verbal baselines make indexes legible <!-- role: reason -->

Indexed differences are easy to misread as absolute levels unless the viewer can immediately identify what “zero” means and how distances relate to that reference. Turning the baseline and a representative tick into plain-language statements anchors interpretation so readers map positions to “change from reference” rather than “current level.”

**Mechanism:** Explicit verbal meaning for the zero line and ticks reduces ambiguity about what is being measured, helping viewers translate positions into “relative to reference” comparisons instead of assuming all series share the same current value.

**Evidence:** Adding a verbal baseline label (e.g., “Employment as of Q3 2023”) and an explanatory tick label (e.g., “−5% from 2023”) is presented as the primary fix to improve mainstream understanding of an indexed employment-rate chart whose readers otherwise misinterpreted the meaning of the lines [@mintzer_y_axis_2024].

**Notes:** The same approach supports terms that are commonly confused (like employment vs. unemployment) by repeating the exact measured concept at the point where readers decode the scale.

## Use this when the chart’s zero is a reference, not an absence <!-- role: context -->

- **User Goal:** Understand whether values are higher or lower than a reference period, and by how much.
- **Task:** Interpret deviations from a baseline across multiple series over time.
- **Data:** Temporal series expressed as an index or difference relative to a chosen reference time point.
- **Chart Setting:** Multi-series line chart (or similar) where the y-axis includes negative/positive values around a baseline.
- **Audience:** General or mainstream readers with limited familiarity with indexing.
- **Success Criterion:** Readers can accurately state what zero means and what a value like “−5” represents without extra explanation.

## When not to do this <!-- role: exceptions -->

**Break it when:** The y-axis already shows absolute units (not relative-to-reference values) and the baseline is a true zero (absence), not a chosen reference period. **Why:** A reference-style label can incorrectly imply the scale is indexed or relative when it is not.

## Tradeoffs of verbose y-axis labeling <!-- role: costs -->

**Sacrifice:** You spend axis space and may need to simplify other labels to avoid clutter. **Risk:** Over-specific wording can become incorrect if the reference period changes but the label is not updated. **Mitigation:** Treat baseline wording as data-linked text that gets reviewed whenever the reference period is edited.

## Common ways this goes wrong <!-- role: mistakes -->

- **Mistake:** Leaving the baseline as a bare “0” with no explanation of what it represents. **Why it fails:** Viewers can assume zero means “no employment” or interpret values as levels rather than deviations.
- **Mistake:** Explaining the index only in body text while keeping the y-axis purely numeric. **Why it fails:** Readers decode meaning at the axis first; missing meaning there causes misinterpretation before they reach the description.

## Quick tests for y-axis comprehensibility <!-- role: check -->

**Failure Sign:** A reader thinks every country has the same current level because the lines converge at zero. **Quick Check:** Ask someone to explain what “0” means on the y-axis using only the chart; if they can’t mention the reference period, the baseline is under-labeled. **Stronger Test:** Ask what a value like “−5” means; success requires an answer like “5% (or percentage points) lower than the reference period,” not “an employment rate of −5.”

## What to do instead when the axis still confuses people <!-- role: fix -->

- Replace the baseline tick label with a phrase that names the metric and reference period (e.g., “Employment as of Q3 2023”).
- Add an explanatory tick label that translates the scale into deviations (e.g., “−5% from 2023”).
- Ensure the chart subtitle repeats that the series are shown “relative to each country’s rate in [reference period]” so the axis meaning is reinforced.
- If space is tight, move less critical tick marks out and keep only the baseline plus a small set of clearly explained deviation ticks.
