---
id: use-colorfields-instead-of-line-graphs-for-max-average-subrange-judgments
title: Use a colorfield instead of a line graph for finding the sub-range with the
  maximum average
bibliography: references.bib
description: Colorfields support more accurate identification of the highest-average
  segment in dense time series than standard line graphs.
labels:
- chart:heatmap
- task:compare
- visual:color
- impact:accuracy
- data:temporal
- audience:novice
- task:aggregate
---

## Prefer colorfields for maximum-average segment selection <!-- role: advice -->

Use a colorfield (value encoded by color in an aligned time-by-value grid) rather than a line graph when users must pick which time segment has the highest average. Keep the segment boundaries explicit so people can compare averages across the same partitions.

## Why colorfields improve average judgments <!-- role: reason -->

Colorfields make the judgment depend on summarizing a region’s overall color, which aligns with efficient visual summary processing for averaged appearance across a spatial area, instead of requiring integrating many point heights along a complex line shape.

**Mechanism:** Regional color can be pooled perceptually, enabling rapid approximate averaging across many samples; line graphs require integrating position over time and interpreting global shape, which is less directly available as a perceptual “average.”

**Evidence:** In a forced-choice task to choose the month with the highest average from a 360-point series, accuracy was significantly higher with colorfields than with line graphs across difficulty levels [@correllComparingAveragesTime2012a]. The line graph condition was also more sensitive to small differences between the best month and close distracter months than the colorfield condition [@correllComparingAveragesTime2012a].

**Notes:** This guidance targets average-based decisions over predefined ranges, not precise reading of individual values.

## When maximum-average comparisons are the goal <!-- role: context -->

- **User Goal:** Identify which segment (e.g., month) has the highest average value.
- **Task:** Compare averages across multiple equal-length sub-ranges within one time series.
- **Data:** Dense ordered sequence (hundreds of points) with noise where the peak value may not occur in the highest-average segment.
- **Chart Setting:** Static view or brief exposure where measuring or computing exact averages is impractical.
- **Audience:** General audiences with basic chart literacy; exclude viewers with color vision deficiency if the palette is not designed for it.
- **Success Criterion:** Higher accuracy (and robustness under noise and close competitors) in selecting the correct segment.

## When not to rely on a colorfield for this task <!-- role: exceptions -->

**Break it when:** The viewer must read exact values or precise point-to-point changes from the series. **Why:** The colorfield encoding is designed for summary judgments and is less suited to precise value extraction than position encodings in the studied setup [@correllComparingAveragesTime2012a].

## Tradeoffs of switching to colorfields <!-- role: costs -->

**Sacrifice:** Some precision for individual values compared to position-based charts. **Risk:** Users may misinterpret the display as showing only categories or may over-trust fine-grained differences in color. **Mitigation:** Treat the view as a summary-first display and ensure boundaries and legend are clear.

## Common ways this goes wrong <!-- role: mistakes -->

**Mistake:** Using a colorfield without a clear legend and explicit segment boundaries. **Why it fails:** The task depends on comparing average color by segment; unclear mapping or partitions weakens comparability and can shift users back to guesswork [@correllComparingAveragesTime2012a].

## Quick tests for whether a colorfield is warranted <!-- role: check -->

**Failure Sign:** Users frequently choose the segment containing the maximum spike rather than the segment with the highest average. **Quick Check:** Ask a few people to pick the highest-average segment; if they talk about “the tallest peak,” the design is not supporting average comparison. **Stronger Test:** Run a small accuracy test with representative series and compare correctness between your line graph and colorfield versions.

## Alternatives if you cannot use a colorfield <!-- role: fix -->

- Use a line graph only if you can add an explicit per-segment average summary elsewhere in the workflow.
- Reduce the decision to fewer points per segment by aggregating or downsampling before plotting in a line graph.
- Provide interaction that directly supports selecting and comparing segment averages rather than forcing visual integration.
