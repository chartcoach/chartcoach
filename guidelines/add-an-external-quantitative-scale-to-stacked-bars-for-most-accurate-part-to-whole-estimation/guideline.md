---
id: add-an-external-quantitative-scale-to-stacked-bars-for-most-accurate-part-to-whole-estimation
title: Add an external quantitative scale to stacked bar charts for the most accurate
  part-to-whole estimation
bibliography: references.bib
description: In one experiment, a stacked bar with an external scale yielded lower
  estimation error than both the baseline bar and a decile-ticked bar.
labels:
- chart:bar
- task:estimate
- visual:length
- visual:scale
- impact:accuracy
- data:categorical
- data:quantitative
- audience:general
- study:experiment
---

## Add an external scale to stacked bars for part-to-whole percent estimation <!-- role: advice -->

If you use a stacked bar for part-to-whole estimation, include an external quantitative scale to improve estimation accuracy beyond internal tick cues.

## Why an explicit scale can outperform internal anchors for estimation <!-- role: reason -->

A quantitative scale provides an explicit mapping from position/length to numeric value, reducing reliance on approximate perceptual interpolation. In the tested variants, the bar with an external scale outperformed both the decile-ticked bar and the baseline bar, indicating the scale improved accuracy for this estimation task.

**Mechanism:** An explicit numeric reference system reduces judgment noise in translating perceived length into a percentage estimate.

**Evidence:** For a part-to-whole estimation task, the bar with an external scale ranked higher (lower error) than the bar with decile ticks and higher than the baseline bar, with significant pairwise differences recorded for scale vs decile and scale vs baseline [@redmondVisualCuesEstimation2019; @zengReviewCollationGraphical2023].

**Notes:** This evidence compares a specific “bar with scale” variant to other bar variants within the same experimental setup.

## When your bar chart must support accurate percent readout/estimation <!-- role: context -->

- **User Goal:** Estimate (or closely read) a highlighted segment’s share of a whole as an integer percentage.
- **Task:** Characterize distribution (part-to-whole segment estimation).
- **Data:** One quantitative proportion per segment (sums to 100%); two segments shown (highlighted segment vs remainder).
- **Chart Setting:** Static stacked bar; segment distinguished via color saturation; axis-like scale shown externally.
- **Audience:** General audience (crowdsourced participants).
- **Success Criterion:** Lower estimation error (higher accuracy).

## When not to add an external scale <!-- role: exceptions -->

**Break it when:** The chart must be ultra-minimal (for example, very tight space) and a scale would not fit without harming legibility. **Why:** The scale consumes space and can visually dominate the small part-to-whole display.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You spend layout space and add visual elements that can reduce the “at-a-glance” simplicity of a two-segment bar.
**Risk:** A scale can encourage over-precision in interpretation if the underlying values are approximate or rounded.
**Mitigation:** Keep tick density and labeling aligned with the precision you want readers to use.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Adding internal ticks but omitting any external scale when high accuracy is required. **Why it fails:** In the extracted results, the external scale variant outperformed the internal tick variants for this task.

## Quick tests <!-- role: check -->

**Failure Sign:** Users’ percent estimates cluster around “nice” numbers that miss the true value by several points.
**Quick Check:** Compare mean absolute error on a handful of sample judgments with and without a scale.
**Stronger Test:** A/B test the bar-with-scale vs bar-with-ticks designs using the same target percentages and measure absolute error.

## What to do instead if you cannot show a scale <!-- role: fix -->

- Use internal reference cues that increase anchoring precision (for example, denser ticks) when a full scale is not feasible.
- Place a numeric label for the highlighted segment near the mark if the task can shift from estimation to reading.
- Switch to an alternative part-to-whole chart design and validate estimation accuracy with a small user check.
