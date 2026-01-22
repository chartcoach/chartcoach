---
id: use-small-multiple-line-charts-to-untangle-overlapping-series
title: Use small multiple line charts to untangle overlapping time-series lines
bibliography: references.bib
description: "Use small multiples to reduce overlap and make each category\u2019s\
  \ time trend readable."
labels:
- chart:line
- task:compare
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- complexity:intermediate
---

## Use small multiple line charts to untangle overlapping time-series lines <!-- role: advice -->

Use small multiple line charts when multiple time-series lines overlap so much that individual trends are hard to follow. Put each category in its own panel so each line has space to be read on its own.

## Small multiples reduce line interference and parsing load <!-- role: reason -->

Overlapping lines create visual interference: crossings, near-parallel segments, and occlusion make it harder to trace any one series and understand its shape. Separating series into panels preserves the same time axis while lowering clutter, so readers can more reliably perceive each trend as a distinct “shape” rather than a tangle.

**Mechanism:** Spatial separation reduces occlusion and accidental comparisons, letting viewers trace one series without continually re-identifying it among others.

**Evidence:** Small multiple line charts are recommended when overlapping lines in a single plot overwhelm readers and make it difficult to parse individual series; separating lines into panels makes trends easier to read [@muth_small_multiple_line_charts_2024].

**Notes:** This guideline is about readability of individual trends, not about comparing exact values between categories at a specific time.

## When overlapping makes multi-line charts hard to read <!-- role: context -->

- **User Goal:** Understand how each category changes over time without confusion from other categories.
- **Task:** Identify trend direction, turning points, volatility, or sustained increases/decreases per category.
- **Data:** Temporal series for multiple categories; even a small number of categories can qualify if lines intersect or crowd.
- **Chart Setting:** Static or lightly interactive; limited space where a legend and many colored lines would add clutter.
- **Audience:** Broad audiences who need quick, low-effort trend reading.
- **Success Criterion:** Readers can accurately describe the trend of a chosen category without losing the line.

## When not to use small multiples for this purpose <!-- role: exceptions -->

**Break it when:** The primary question is “Which category is higher/lower at a specific date?” **Why:** Small multiples make point-by-point cross-category comparisons at the same time difficult because values sit in separate panels [@muth_small_multiple_line_charts_2024].

## Tradeoffs of separating lines into panels <!-- role: costs -->

**Sacrifice:** You spend more space and may reduce the ability to see all categories at once in a single frame. **Risk:** Readers may miss relative ranking at specific dates because comparisons require scanning across panels. **Mitigation:** Treat small multiples as a trend-reading view, and use other devices (like added context lines) when ranking is important [@muth_small_multiple_line_charts_2024].

## Common ways this goes wrong <!-- role: mistakes -->

- **Mistake:** Keeping a crowded multi-line chart even though lines cross and overlap heavily. **Why it fails:** Readers cannot reliably trace individual series, so trend interpretation becomes error-prone [@muth_small_multiple_line_charts_2024].
- **Mistake:** Using small multiples while expecting readers to compare which category is higher in a given year. **Why it fails:** Separate panels make direct value comparisons at the same time point hard [@muth_small_multiple_line_charts_2024].

## Quick ways to tell if overlap is the real problem <!-- role: check -->

**Failure Sign:** Viewers have to repeatedly search for “their” line or lose it when lines cross. **Quick Check:** If you can’t quickly trace one category from start to end without confusion in a single combined chart, overlap is likely too high. **Stronger Test:** Ask a colleague to describe the trend of a randomly chosen category from the combined chart; if they struggle, switch to small multiples [@muth_small_multiple_line_charts_2024].

## What to do instead or in addition <!-- role: fix -->

- Split the chart into small multiple panels with one line per category.
- If you must keep one chart, reduce the number of shown categories to those that support the key takeaway.
- If point-in-time comparison is the main need, use a normal multi-line chart instead of small multiples.
- If you still want some cross-category context in small multiples, add other categories as faint background lines in each panel [@muth_small_multiple_line_charts_2024].
