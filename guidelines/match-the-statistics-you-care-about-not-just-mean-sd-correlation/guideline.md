---
id: match-the-statistics-you-care-about-not-just-mean-sd-correlation
title: Lock the Specific Statistics You Intend to Teach or Preserve
bibliography: references.bib
description: Choose and enforce the exact statistical measures relevant to your message
  (parametric or non-parametric) when generating comparison datasets.
labels:
- chart:scatter
- task:compare
- visual:position
- impact:validity
- data:bivariate
- audience:expert
- custom:statistics-constraints
---

## The Rule <!-- role: advice -->

Constrain the datasets on the exact statistics you want to keep constant (including non-parametric choices), rather than defaulting to mean/SD/Pearson correlation.

## The Logic <!-- role: reason -->

- **The Principle:** Different statistical summaries preserve different aspects of the data; your constraint set determines what “same” means.
- **The Evidence:** The paper demonstrates generating datasets that match non-parametric measures (median, IQR, Spearman correlation) instead of parametric summaries [@matejkaSameStatsDifferent2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Demonstrate robustness/fragility of different summaries or tailor a “same stats” message to a specific metric.
- **Data Type:** 2D scatter data where rank-based or quantile-based summaries are more appropriate than moments.
- **Audience:** Stats/vis learners comparing parametric vs non-parametric summaries.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your communication goal is specifically about how mean/SD/Pearson can mislead.
- **Reason:** Switching constraints changes the lesson and may dilute that particular point.

## The Price <!-- role: costs -->

- **The Sacrifice:** More complex constraint checking (more statistics to compute/validate).
- **The Risk:** Viewers may assume other properties are also preserved when they are not.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Claiming two datasets are “the same statistically” without specifying which statistics were matched.
- **Why it fails:** The method is agnostic to measures; without explicit naming, the equivalence claim is ambiguous [@matejkaSameStatsDifferent2017].

## How to Check <!-- role: check -->

- **Visual Sign:** The plots differ in ways the audience finds “unfair” (e.g., different medians when you meant to preserve center).
- **The Test:** Recompute the stated statistics for both datasets and confirm equality to the declared tolerance (e.g., two decimal places) [@matejkaSameStatsDifferent2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add the missing statistic(s) to the constraint check used for accepting perturbations.
- **Best Fix:** Define a clear constraint set aligned to the lesson (e.g., median/IQR/Spearman for robust summaries) and state it directly in the figure caption or annotation [@matejkaSameStatsDifferent2017].
