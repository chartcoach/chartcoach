---
id: use-small-multiple-line-charts-to-show-per-category-trends
title: "Use small multiple line charts to emphasize each category\u2019s trend shape\
  \ over time"
bibliography: references.bib
description: Use small multiples when the main message is the within-category trend,
  not precise cross-category comparison.
labels:
- chart:line
- task:trend
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- complexity:beginner
---

## Use small multiple line charts to emphasize each category’s trend shape over time <!-- role: advice -->

Use small multiple line charts when you want readers to focus on the shape of each category’s line over time (rises, falls, and turning points). Present each category in a separate panel so the trend is read as a clear individual pattern.

## Isolating series makes “trend reading” the default task <!-- role: reason -->

When multiple series share a single plotting area, attention often shifts from understanding each series’ trajectory to decoding the crowd: identifying colors, tracing lines through crossings, and resolving confusion. Small multiples make each panel a single-subject view, encouraging readers to perceive the time pattern within that category first.

**Mechanism:** One-series-per-panel reduces competing visual signals, so the viewer’s perceptual work goes into judging direction and change rather than disentangling identity.

**Evidence:** Small multiple line charts are positioned as especially good for letting readers see the trend in each individual category—how quickly and how much a line goes up and down—because each line is separated into its own panel [@muth_small_multiple_line_charts_2024].

**Notes:** This is most useful when the narrative is about “how each category behaves,” not “which category wins at time t.”

## When the question is about within-category change <!-- role: context -->

- **User Goal:** Understand how each category changes over time on its own terms.
- **Task:** Describe direction, acceleration/slowdown, variability, and notable peaks/dips per category.
- **Data:** Multiple temporal series; categories are meaningful units (regions, products, cohorts).
- **Chart Setting:** Reports or articles where readers can scan multiple panels like a set of mini-stories.
- **Audience:** Mixed literacy; readers who benefit from simplified decoding.
- **Success Criterion:** Readers can summarize each category’s trajectory quickly and consistently.

## When a single combined line chart is better <!-- role: exceptions -->

**Break it when:** The key task is comparing categories against each other at the same time point. **Why:** Small multiples make “which is higher in 2022?” style questions hard because the values are separated into different panels [@muth_small_multiple_line_charts_2024].

## Tradeoffs of prioritizing trend shape <!-- role: costs -->

**Sacrifice:** You reduce immediate cross-category comparability at specific dates. **Risk:** Readers may infer comparisons that the layout doesn’t support well. **Mitigation:** Pair small multiples with clear labeling or an alternative view when exact cross-category comparisons are essential [@muth_small_multiple_line_charts_2024].

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using small multiples but writing takeaways that require precise across-panel value comparison at a specific date. **Why it fails:** The chart form does not support that judgment efficiently [@muth_small_multiple_line_charts_2024].
- **Mistake:** Keeping everything in one multi-line chart when the story is mainly about each category’s trend. **Why it fails:** Readers spend effort disentangling instead of interpreting trajectories [@muth_small_multiple_line_charts_2024].

## Quick tests for fit <!-- role: check -->

**Failure Sign:** Readers’ first questions are “Which color is which?” or “Where does this line go next?” **Quick Check:** If your intended takeaway can be expressed per category (e.g., “most regions rise after 2015”), small multiples are a strong fit. **Stronger Test:** Remove the legend mentally—if the chart collapses without it, small multiples likely improve comprehension [@muth_small_multiple_line_charts_2024].

## What to do instead <!-- role: fix -->

- Use a standard multi-line chart when the story depends on direct cross-category comparison at a given time.
- Reduce the number of categories shown if you keep a combined chart but want trend readability.
- Use small multiples as the primary view and provide a combined view as a secondary “comparison” view when needed [@muth_small_multiple_line_charts_2024].
- Consider a searchable table with sparklines if you need to show many categories compactly [@muth_small_multiple_line_charts_2024].
