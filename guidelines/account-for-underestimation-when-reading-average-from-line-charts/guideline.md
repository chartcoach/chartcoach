---
id: account-for-underestimation-when-reading-average-from-line-charts
title: Account for systematic underestimation when estimating an average from a line
  chart
bibliography: references.bib
description: Average positions read from line charts can be systematically underestimated
  in aggregate judgments.
labels:
- chart:line
- task:aggregate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- bias:underestimate
- complexity:advanced
---

## Account for line-average underestimation in aggregate judgments <!-- role: advice -->

When viewers estimate an average from a line chart, assume the perceived average position will be biased downward relative to the true average. Treat line-based average judgments as potentially systematically underestimated rather than only noisy.

## Why line averages skew downward <!-- role: reason -->

Average judgments can be systematically biased even when the encoding is position, meaning the perceived average does not center on the true average. This creates directional error (underestimation) rather than symmetric random error.

**Mechanism:** The perceived average vertical position of a line can shift downward relative to the true average, producing a consistent signed bias in aggregate judgments.

**Evidence:** In an aggregate task using a line chart (quantitative data on positionY with a nominal x-axis), average position estimates were significantly underestimated using a linear mixed-effects analysis. [@xiongBiasedAveragePosition2020; @zengReviewCollationGraphical2023]

**Notes:** This guideline concerns bias direction (systematic underestimation), not which chart is “best” overall.

## When this applies to your chart and task <!-- role: context -->

- **User Goal:** Estimate or recall an average level from a plotted series.
- **Task:** Aggregate (average position estimation).
- **Data:** Quantitative values distributed across a categorical/nominal x-axis.
- **Chart Setting:** A single line series shown in one plot.
- **Audience:** Any audience making quick visual average judgments.
- **Success Criterion:** Minimizing directional bias in the perceived average.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The user is not making an average/aggregate judgment from the line’s vertical position. **Why:** The evidence summarized here is specific to aggregate (average position) estimation.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Emphasizing bias awareness can reduce confidence in quick “read off the chart” interpretations. **Risk:** Overcorrecting can cause users to distrust accurate line-based readings when the task is not averaging. **Mitigation:** Keep the concern scoped to aggregate judgments of average position.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Assuming position encodings in line charts are unbiased and only vary by random noise. **Why it fails:** The observed error is directional (systematic underestimation) in aggregate judgments, not purely random.

## Quick tests <!-- role: check -->

**Failure Sign:** People consistently report the average level of a line lower than the true average. **Quick Check:** Ask a few users to estimate the series’ average level from the line and compare the sign of errors. **Stronger Test:** Run a small structured pilot and test whether mean signed error is below zero.

## What to do instead <!-- role: fix -->

- Add a direct representation of the average (e.g., a reference average indicator) so users do not rely solely on mental averaging.
- Provide the numeric average alongside the line when the decision hinges on the mean value.
- Use separated views for comparisons that require recalling averages across series rather than relying on memory of the line’s average position.
- Validate the final design with a brief task-focused check for signed error in average judgments.
