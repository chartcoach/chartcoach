---
id: avoid-hops-for-high-variance-mean-estimation
title: Avoid HOPs for High-Variance Mean Estimation
bibliography: references.bib
description: Prefer static summaries over HOPs when the primary task is estimating
  a single-variable mean under high variance.
labels:
- chart:animation
- task:estimate
- visual:position
- impact:accuracy
- data:univariate
- audience:novice
- uncertainty:high-variance
---

## The Rule <!-- role: advice -->

Do not rely on HOPs as the primary view when users must estimate the mean of a single variable with high variance; use a static depiction that directly supports mean reading.

## The Logic <!-- role: reason -->

Mean estimation from HOPs requires integrating across many frames; with high variance, frame-to-frame jumps are larger and sampling imprecision is higher, increasing error. The study found significantly higher error for HOPs than error bars or violin plots in estimating μ when variance was high.

- **The Principle:** Integration burden and finite-sample imprecision in animated draws
- **The Evidence:** [@hullmanHypotheticalOutcomePlots2015]

## Where to Apply <!-- role: context -->

- **User Goal:** Reading/estimating μ accurately for a single distribution.
- **Data Type:** Univariate distributions with high dispersion (large σ).
- **Audience:** Viewers who won’t spend long watching many frames.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The key goal is not μ but comparative reliability (ordering) across variables.
- **Reason:** HOPs substantially improved ordering judgments in multi-variable tasks, even though it can be worse for high-variance mean estimation. [@hullmanHypotheticalOutcomePlots2015]

## The Price <!-- role: costs -->

- **The Sacrifice:** Less intuitive “outcome-by-outcome” feel for uncertainty if you switch away from HOPs.
- **The Risk:** Static depictions may still be misread for other tasks (e.g., ordering reliability), so you may need multiple complementary views. [@hullmanHypotheticalOutcomePlots2015]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming viewers will “average visually” across a small number of HOP frames to get an accurate mean when variability is large.
- **Why it fails:** With high σ, fewer viewed frames plus large jumps raise error; the study shows HOPs lagging static alternatives for this specific task. [@hullmanHypotheticalOutcomePlots2015]

## How to Check <!-- role: check -->

- **Visual Sign:** Users’ mean estimates vary widely across repeated viewers for the same high-variance distribution.
- **The Test:** Ask users to estimate μ; if mean absolute error is materially larger than with a static mean-indicating depiction, HOPs is the wrong primary tool for this task. [@hullmanHypotheticalOutcomePlots2015]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a clear static mean indicator alongside/over HOPs when σ is high.
- **Best Fix:** Use a static uncertainty depiction for μ tasks (e.g., one that explicitly marks the mean) and reserve HOPs for tasks where outcome-by-outcome comparison is central. [@hullmanHypotheticalOutcomePlots2015]
