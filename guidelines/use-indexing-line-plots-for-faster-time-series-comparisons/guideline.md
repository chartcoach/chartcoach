---
id: use-indexing-line-plots-for-faster-time-series-comparisons
title: Use indexed (percent-based) line plots instead of juxtaposed linear line plots
  for faster multivariate time-series comparison tasks
bibliography: references.bib
description: Indexed (percent-based) line plots can reduce completion time versus
  juxtaposed linear line plots for comparison-oriented time-series tasks.
labels:
- chart:line
- task:compare
- visual:position
- impact:speed
- data:temporal
- audience:general
- transformation:indexing
---

## Prefer indexed line plots over juxtaposed linear line plots for speed <!-- role: advice -->

Use indexed (percent-based) line plots instead of juxtaposed line plots on a linear y-scale when you want people to complete multivariate time-series comparison tasks faster.

## Why indexing can be faster here <!-- role: reason -->

Indexing converts values into a common percent-based scale so multiple series can be compared directly within one shared y-axis, reducing the work of mentally reconciling different value domains across separate panels.

**Mechanism:** A shared comparison scale reduces cross-panel matching and re-scaling effort during comparison-oriented judgments.

**Evidence:** In extracted results for time-series comparison tasks, indexed (percent-based) line plots ranked faster than juxtaposed linear line plots, with a significant pairwise difference reported for time (E-2 better than E-1). [@aignerBertinWasRight2011; @zengReviewCollationGraphical2023]

**Notes:** This guideline is about completion time, not accuracy.

## When this applies to your visualization <!-- role: context -->

- **User Goal:** Compare multiple time-series efficiently.
- **Task:** Correlate; Aggregate.
- **Data:** Temporal sequences with multiple series (multivariate time-series).
- **Chart Setting:** Static line plots (or static snapshots of interactive views).
- **Audience:** General audiences doing analytical comparisons.
- **Success Criterion:** Faster task completion time.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Accuracy is the primary constraint and you cannot tolerate any potential accuracy tradeoffs. **Why:** The extracted accuracy rankings did not report significant pairwise differences for correlate/aggregate/overall in this comparison, so speed gains should not be assumed to also improve correctness.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Percent-based indexing can reduce direct readability of absolute values. **Risk:** Viewers may misinterpret indexed values as raw units if labeling is unclear. **Mitigation:** Make the percent/indexed nature explicit in axis labeling and captions.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Switching to an indexed view but leaving the y-axis labeling ambiguous about being percent-based. **Why it fails:** Readers may apply an absolute-value interpretation to a transformed scale.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers hesitate or re-check values repeatedly when comparing series across time. **Quick Check:** Ask a colleague to complete one correlate or aggregate comparison; if they repeatedly “translate” between series before answering, try indexing. **Stronger Test:** Run a small timed task trial comparing your current design vs. an indexed version.

## What to do instead <!-- role: fix -->

- Use indexed (percent-based) line plots that place all series on a single shared y-axis.
- If absolute values must remain primary, keep linear scaling but provide a separate indexed comparison view as an alternative.
- If the task is dominated by absolute value reading, keep juxtaposed linear views and avoid transforming the y-axis into percent.
