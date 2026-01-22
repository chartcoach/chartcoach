---
id: do-not-assume-bar-height-range-removes-mean-underestimation-in-bar-charts
title: Do not rely on bar height range (high vs low bars) to eliminate mean-underestimation
  bias
bibliography: references.bib
description: Mean underestimation in bar charts persisted across both higher and lower
  bar-height ranges in mean judgment tasks.
labels:
- chart:bar
- task:aggregate
- visual:length
- impact:accuracy
- data:quantitative
- audience:general
- factor:scale-range
---

## Do not treat “high vs low bars” as a fix for mean bias <!-- role: advice -->

Do not assume that using smaller (low) bars instead of larger (high) bars will remove mean-underestimation bias when viewers estimate the grand average from a bar chart.

## Why bar-height range is not a reliable control for mean bias <!-- role: reason -->

Changing the overall bar-height range did not remove the systematic direction of bias in mean estimation, so “making bars shorter” is not a dependable mitigation.

**Mechanism:** The bias appears to be tied to how viewers aggregate across bar marks rather than simply the absolute height range of the bars.

**Evidence:** In aggregate mean-judgment tasks, mean underestimation occurred for both “high bars” and “low bars,” with no significant difference between these conditions in the reported tests [@godauPerceptionBarGraphs2016]. This condition-level finding is included as structured, reusable evidence in a broader collation of graphical perception knowledge for recommendation systems [@zengReviewCollationGraphical2023].

**Notes:** This guideline only covers the tested “high vs low” manipulation as captured in the structured results.

## When this guideline applies <!-- role: context -->

- **User Goal:** Estimate the overall mean of multiple values from a bar chart.
- **Task:** Aggregate (mean estimation).
- **Data:** Quantitative values displayed as bars across categories.
- **Chart Setting:** Static bar chart where designers consider rescaling or changing bar magnitudes to “reduce bias.”
- **Audience:** General audiences.
- **Success Criterion:** Reduce systematic directional error in mean estimation.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chart is not intended to support mean estimation from the bars (for example, users only need relative category comparisons). **Why:** The evidence concerns aggregate mean estimation, not other bar-chart tasks.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may spend effort on rescaling/redesign that does not improve mean-estimation accuracy. **Risk:** Viewers may still produce biased mean judgments despite “reasonable-looking” bar magnitudes. **Mitigation:** Validate with a quick mean-estimation check instead of assuming rescaling solves the issue.

## Common failure modes <!-- role: mistakes -->

**Mistake:** “Make the bars smaller” (or change the y-range) as the primary strategy to remove mean bias. **Why it fails:** Mean underestimation was observed for both higher and lower bar-height conditions.

## Quick tests <!-- role: check -->

**Failure Sign:** Mean judgments remain systematically below the true mean after rescaling. **Quick Check:** Compare user judgments on two versions of the same bar chart (rescaled vs original) and check whether the direction of bias changes. **Stronger Test:** Quantify directional errors across multiple samples of charts using the same yes/no “mean should be higher/lower” prompt.

## What to do instead <!-- role: fix -->

- Use a point-based display for mean estimation tasks when bias-free aggregation is required.
- Avoid presenting mean estimation as an inference task from bars; instead provide an explicit mean value intended to be read.
- If you are evaluating design alternatives, test bias directly rather than using bar-height range as a proxy for bias reduction.
