---
id: treat-scatterplot-design-methods-as-equivalent-for-correlation-accuracy-and-time
title: Do Not Over-Optimize Scatterplot Presets for Correlation Estimation
bibliography: references.bib
description: For correlation estimation in scatterplots, multiple tested design methods
  performed equivalently in accuracy and time.
labels:
- chart:scatter
- task:correlate
- visual:position
- impact:robustness
- data:quantitative
- audience:novice
- source:literature-collation
- complexity:basic
---

## The Rule <!-- role: advice -->

For correlation estimation tasks using scatterplots, treat the tested scatterplot design methods as equivalent; do not expect a reliable accuracy or time gain from switching between them.

## The Logic <!-- role: reason -->

When empirical evidence shows no significant performance differences, optimization effort is unlikely to produce user-perceivable benefits for that task (within the tested conditions).

- **The Principle:** If performance is statistically indistinguishable across presets, design choice among those presets is not a primary lever for that task’s performance.
- **The Evidence:** For *correlate* (accuracy and time), the algorithm-generated scatterplot (E-1), MATLAB (E-2), R (E-3), and the prior-study design (E-4) were ranked together with no significant pairwise differences reported [@micallefPerceptualOptimizationVisual2017]. This is recorded as a flat ranking in the collation dataset described by [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating correlation from a scatterplot.
- **Data Type:** Two quantitative variables plotted with position encodings (linear scales).
- **Audience:** Anyone choosing between common scatterplot presets for correlation estimation.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your correlation task is coupled with another objective (e.g., you must also detect outliers).
- **Reason:** For *find-anomalies*, the same presets are not equivalent (they show significant differences in both accuracy and time) [@micallefPerceptualOptimizationVisual2017], as organized in [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You might miss small, context-specific advantages not captured by the tested metrics.
- **The Risk:** Overconfidence in equivalence outside the tested setting; this guideline is limited to the reported correlate accuracy/time outcomes.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Investing effort into swapping presets or implementing complex optimization specifically to improve correlation estimation.
- **Why it fails:** The reported comparison found no significant accuracy or time differences among the tested methods for *correlate* [@micallefPerceptualOptimizationVisual2017; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** You see no consistent change in users’ correctness or speed when switching presets for correlation tasks.
- **The Test:** A/B test correlation estimation time and accuracy across presets; if differences are not statistically meaningful, treat them as equivalent (mirroring the reported outcome) [@micallefPerceptualOptimizationVisual2017; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Keep your existing correlation scatterplot preset (among the tested types) and focus effort elsewhere.
- **Best Fix:** Reallocate optimization to tasks where the collation shows sensitivity (e.g., outlier detection) rather than correlation estimation [@zengReviewCollationGraphical2023], grounded in the task results from [@micallefPerceptualOptimizationVisual2017].
