---
id: avoid-overlaying-series-to-reduce-perceptual-pull-in-average-estimation
title: "Avoid co-plotting multiple series when users must estimate each series\u2019\
  \ average (to reduce perceptual pull)"
bibliography: references.bib
description: "When multiple series are shown together, perceived averages can be pulled\
  \ toward other series\u2019 positions."
labels:
- chart:line
- chart:bar
- task:aggregate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- bias:context-effects
- complexity:advanced
---

## Reduce perceptual pull by not co-plotting multiple series for average estimation <!-- role: advice -->

When users need to estimate the average of each series, do not place multiple plotted series in the same axes if you can avoid it. Co-plotted series can pull perceived averages toward each other.

## Why co-plotted series distort perceived averages <!-- role: reason -->

Context can bias perceived averages: the presence of another series provides an additional positional reference that shifts the perceived mean of the target series. This produces a systematic context effect (“pull”) rather than independent judgments per series.

**Mechanism:** Average position estimates for a target series can shift toward the position of another (irrelevant-to-the-target) series in the same plot, changing the direction and magnitude of bias depending on relative placement.

**Evidence:** In aggregate tasks with two lines, two bar sets, or a line with bars shown together, average position estimates exhibited a significant perceptual pull effect under linear mixed-effects analysis. [@xiongBiasedAveragePosition2020; @zengReviewCollationGraphical2023]

**Notes:** This guideline is about estimating each series’ average, not about all forms of multi-series comparison.

## When this applies to your chart and task <!-- role: context -->

- **User Goal:** Estimate the average of a specific series while other series are present.
- **Task:** Aggregate (average position estimation per series).
- **Data:** Quantitative series values across a categorical/nominal x-axis; at least two series to be judged separately.
- **Chart Setting:** Multiple lines, multiple bar groups, or line-plus-bars drawn together in the same plotting area.
- **Audience:** Any audience expected to judge per-series averages quickly.
- **Success Criterion:** Reduce context-driven shifts in perceived averages between series.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The purpose is explicitly to judge the combined/overall pattern from all series together rather than separate per-series averages. **Why:** The distortion is defined relative to separate target-series average judgments.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Separating series can cost space and can make direct point-by-point comparison harder. **Risk:** Users may need more time to switch attention between views when series are split. **Mitigation:** Use consistent scales and alignment so separated views remain comparable.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Overlaying multiple series and assuming viewers can accurately estimate each series’ average independently. **Why it fails:** Co-plotted series can introduce perceptual pull that shifts perceived averages toward other series’ positions.

## Quick tests <!-- role: check -->

**Failure Sign:** Average estimates for a series drift toward the other series when both are shown, compared to when the series is shown alone. **Quick Check:** Show users a single-series view and a multi-series view and compare signed error for the same target series. **Stronger Test:** A/B test co-plotted versus separated views and test for systematic changes in mean signed error.

## What to do instead <!-- role: fix -->

- Split the series into small multiples with a shared scale so each series’ average is estimated without interference.
- Provide explicit per-series average cues so viewers do not have to infer means from co-plotted marks.
- If co-plotting is required, add task scaffolding that directs attention to the target series during the average judgment.
- Verify with a small pilot that average estimates for each series do not shift when additional series are introduced.
