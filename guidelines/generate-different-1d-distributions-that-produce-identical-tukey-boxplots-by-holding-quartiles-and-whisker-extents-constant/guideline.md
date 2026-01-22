---
id: generate-different-1d-distributions-that-produce-identical-tukey-boxplots-by-holding-quartiles-and-whisker-extents-constant
title: Generate different 1D distributions that produce identical Tukey boxplots by
  holding quartiles and whisker extents constant
bibliography: references.bib
description: "Create multiple distinct-looking 1D datasets that share the same Tukey\
  \ boxplot by constraining quartiles and the 1.5\xD7IQR whisker limits."
labels:
- chart:boxplot
- task:teach
- visual:position
- impact:insight
- data:distribution
- audience:novice
- custom:summary-statistics
- complexity:intermediate
---

## Create distinct 1D datasets that keep the same Tukey boxplot statistics <!-- role: advice -->

If you want different 1D data distributions to render as the same Tukey boxplot, constrain the first quartile, median, third quartile, and the furthest points within 1.5 interquartile ranges (IQR) of the quartiles while perturbing the data.

## Why identical boxplot summaries can hide very different distributions <!-- role: reason -->

A Tukey boxplot encodes only a small set of quantile-based summaries and whisker limits, so many different point configurations can satisfy those same values while varying substantially in distributional shape.

**Mechanism:** By holding quartiles and whisker-extreme locations fixed, the optimization can rearrange mass elsewhere (for example, shifting points inward or outward) without changing the rendered boxplot.

**Evidence:** Multiple 1D datasets were generated that shared the same first quartile, median, third quartile, and 1.5×IQR whisker-related locations, producing identical boxplots despite different underlying distributions [@matejkaSameStatsDifferent2017].

**Notes:** The perturbation direction can be biased (for example, toward edges or toward one side) while still preserving the boxplot-defining statistics [@matejkaSameStatsDifferent2017].

## When you need to show limits of boxplot summaries <!-- role: context -->

- **User Goal:** Demonstrate that identical boxplots can correspond to different underlying distributions.
- **Task:** Construct counterexamples or teaching datasets for summary-statistic reliance.
- **Data:** 1D quantitative samples suitable for quartiles and whisker computation.
- **Chart Setting:** Static instruction, exercises, or dataset generation for demos.
- **Audience:** Readers learning exploratory data analysis concepts.
- **Success Criterion:** Boxplots are identical while the underlying distributions differ visibly (for example, in histograms or dotplots).

## When not to use boxplot-equivalence as a notion of “same distribution” <!-- role: exceptions -->

**Break it when:** You need outputs that are similar in distributional shape rather than only in quartiles and whisker limits. **Why:** Identical boxplot summaries do not constrain many distributional features that may matter [@matejkaSameStatsDifferent2017].

## Tradeoffs of generating boxplot-identical distributions <!-- role: costs -->

**Sacrifice:** The construction can create distributions that satisfy the boxplot but may look contrived for some applications. **Risk:** Viewers may incorrectly infer that identical boxplots imply similar distributions if the underlying samples are not also shown. **Mitigation:** Pair the boxplot with a view of the raw points or another distribution view when teaching the lesson [@matejkaSameStatsDifferent2017].

## Common mistakes with boxplot-based comparisons <!-- role: mistakes -->

**Mistake:** Treating identical boxplots as evidence that datasets are similar. **Why it fails:** Very different distributions can share the same quartiles and whisker limits and therefore the same boxplot [@matejkaSameStatsDifferent2017].

## Quick tests for boxplot identity under constraints <!-- role: check -->

**Failure Sign:** The boxplot differs after perturbations (quartiles shift or whiskers move). **Quick Check:** Recompute quartiles and whisker-extreme locations after each accepted change and confirm they match the seed’s values. **Stronger Test:** Render boxplots for all generated datasets and verify they are visually indistinguishable while the raw distributions differ [@matejkaSameStatsDifferent2017].

## What to do instead when the boxplot changes unexpectedly <!-- role: fix -->

- Reduce the perturbation step size to avoid moving points across quantile boundaries.
- Constrain additional quantiles if you need tighter control than a standard Tukey boxplot provides.
- Increase iterations so the optimization can find alternative configurations that satisfy the quartile constraints.
- Start from a seed distribution whose quartiles and whisker extents make your intended variations feasible [@matejkaSameStatsDifferent2017].
