---
id: use-optimizer-generated-scatterplots-to-reduce-anomaly-finding-time-when-speed-is-critical
title: Use optimizer-generated scatterplots to reduce anomaly-finding time when speed
  is critical
bibliography: references.bib
description: For anomaly finding, an optimizer-generated scatterplot can yield faster
  completion times than MATLAB, R, and a prior-study preset in the reported comparison.
labels:
- chart:scatter
- task:find-anomalies
- visual:position
- impact:speed
- data:quantitative
- audience:novice
- complexity:advanced
---

## Faster anomaly finding with an optimizer preset <!-- role: advice -->

Use an optimizer-generated scatterplot preset for anomaly finding when completion time is more important than maximizing accuracy.

## Why an optimizer preset can speed anomaly finding <!-- role: reason -->

Some design-parameter combinations can reduce the time needed to visually locate anomalous points, even if they do not produce the highest accuracy among compared presets.

**Mechanism:** Parameter settings can increase visual salience or reduce visual clutter enough to accelerate search and decision time.

**Evidence:** For anomaly-finding time, the optimizer-generated design was ranked faster than MATLAB, R, and the prior-study preset, with significant pairwise differences reported at the stated threshold [@micallefPerceptualOptimizationVisual2017; @zengReviewCollationGraphical2023].

**Notes:** This guideline is about speed benefits in the reported comparison, not about general anomaly-detection superiority.

## When the speed-first anomaly rule applies <!-- role: context -->

- **User Goal:** Triage potential anomalies quickly.
- **Task:** Find anomalies.
- **Data:** Two quantitative attributes with potential anomalies/outliers.
- **Chart Setting:** Static scatterplot with point marks and linear position scales.
- **Audience:** Analysts doing rapid scanning or time-bounded review.
- **Success Criterion:** Lower completion time.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Missing anomalies has high cost (e.g., safety-critical review). **Why:** Faster time does not imply higher accuracy in the reported results.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may give up some anomaly-detection accuracy compared to other presets. **Risk:** Users may feel confident because they finished quickly, even if correctness dropped. **Mitigation:** Pair fast presets with a second-pass review step using a more accurate preset.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using the fastest preset as the default for all audiences and all anomaly scenarios. **Why it fails:** Different presets can trade speed for accuracy, and the best choice depends on the success criterion.

## Quick tests <!-- role: check -->

**Failure Sign:** Users finish quickly but later discover missed anomalies. **Quick Check:** Track time-to-answer and correctness side-by-side for a small anomaly benchmark set. **Stronger Test:** Run a within-subjects evaluation that measures both completion time and accuracy across presets.

## What to do instead <!-- role: fix -->

- Use a speed-first preset only in triage workflows, and provide an accuracy-first preset for confirmation.
- Add a lightweight verification step (e.g., a second view or a second preset) for high-stakes anomaly decisions.
- If you cannot afford the accuracy drop, standardize on the more accurate preset and optimize the workflow around it.
