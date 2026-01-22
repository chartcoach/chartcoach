---
id: use-difference-chart-or-difference-overlays-for-maximum-change-identification
title: Use explicit differences (difference chart or difference overlays) to improve
  accuracy when identifying the maximum absolute change
bibliography: references.bib
description: For finding the category with the largest absolute change between two
  series, designs that explicitly encode differences are more accurate than a grouped
  bar chart.
labels:
- chart:bar
- task:aggregate
- task:compare
- visual:position
- impact:accuracy
- impact:speed
- data:categorical
- audience:novice
- comparison:multi-series
---

## Use explicit differences for max-change tasks <!-- role: advice -->

When people must identify which category changed the most between two series, use a design that explicitly encodes the difference (a difference chart or bar charts with difference overlays). Avoid relying on a grouped bar chart alone.

## Why explicit differences improve max-change judgments <!-- role: reason -->

Explicitly encoding the difference reduces the need to mentally subtract two values for every category, which otherwise increases mistakes and slows scanning.

**Mechanism:** Difference encodings externalize the computation (change between series) into a directly comparable visual mark, reducing mental arithmetic across many categories.

**Evidence:** For identifying the maximum absolute change, the difference chart and both difference-overlay designs outperformed the grouped bar chart in accuracy with significant differences reported between each explicit-difference design and the grouped bar chart; task time also ranked the grouped bar chart slowest with significant differences indicating explicit-difference designs were faster in key pairwise comparisons [@srinivasanWhatsDifferenceEvaluating2018; @zengReviewCollationGraphical2023].

**Notes:** This guideline is about the “maximum absolute change” comparison task, not about reading original per-series values.

## When max-change identification applies <!-- role: context -->

- **User Goal:** Find which category has the largest absolute change from source to target.
- **Task:** Identify maximum absolute change.
- **Data:** Two-series categorical/ordinal categories with per-category numeric values (may include missing categories depending on the scenario).
- **Chart Setting:** Dashboard comparison where space is limited and users need to compare many categories quickly.
- **Audience:** General dashboard readers.
- **Success Criterion:** Higher correctness and/or faster completion for selecting the category with the largest change.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Users must primarily read and compare original values for each series and differences are secondary. **Why:** A difference chart focuses attention on derived values rather than the original series values.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Explicit difference marks add visual elements and may reduce simplicity. **Risk:** Viewers may over-focus on differences and miss the magnitude of the underlying baseline values. **Mitigation:** Ensure the chart design still provides a clear pathway to the original values when that is needed.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Asking users to identify the largest change using only a grouped bar chart without explicit difference encoding. **Why it fails:** Users must repeatedly compare and compute differences across categories, increasing error and time.

## Quick tests <!-- role: check -->

**Failure Sign:** Users scan back and forth between paired bars for many categories before answering. **Quick Check:** Time yourself answering “Which category changed the most?”; if you must mentally subtract repeatedly, explicit differences are likely needed. **Stronger Test:** A/B test grouped bars versus explicit-difference encodings on correctness for max-change selection.

## What to do instead <!-- role: fix -->

- Use a difference chart when the primary question is “what changed” rather than “what are the values.”
- Use grouped bars with difference overlays when both original values and changes are important to see together.
- Use a single bar chart with difference overlays only when source-series values are not directly queried and the design is clearly explained.
