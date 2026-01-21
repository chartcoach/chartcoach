---
id: demonstrate-boxplot-non-uniqueness-by-creating-different-1d-distributions-with-identical-boxplots
title: Show Multiple Distributions That Produce the Same Boxplot
bibliography: references.bib
description: Reveal that identical boxplots can hide different underlying 1D distributions
  by displaying alternative point distributions with the same boxplot statistics.
labels:
- chart:boxplot
- task:educate
- visual:position
- impact:trust
- data:univariate
- audience:novice
- custom:distribution-shape
---

## The Rule <!-- role: advice -->

When using boxplots to summarize data, show alternative underlying 1D distributions (or raw points) that share the same boxplot statistics to demonstrate what the boxplot cannot reveal.

## The Logic <!-- role: reason -->

- **The Principle:** Many different point arrangements can share identical quartiles and whisker extents; the summary graphic is not uniquely determined by the data.
- **The Evidence:** The paper generates multiple distinct 1D datasets that keep Tukey boxplot-defining values constant (quartiles and 1.5 IQR whisker limits), yielding identical boxplots despite different distributions [@matejkaSameStatsDifferent2017].

## Where to Apply <!-- role: context -->

- **User Goal:** Learn the limits of boxplots as summaries (shape, modality, clustering).
- **Data Type:** Univariate data being presented primarily as a Tukey boxplot.
- **Audience:** Anyone interpreting boxplots as “the distribution.”

## When to Break It <!-- role: exceptions -->

- **Scenario:** The goal is compact reporting with minimal ink/space and distribution shape is not relevant.
- **Reason:** Adding underlying distributions increases space and detail beyond the reporting requirement.

## The Price <!-- role: costs -->

- **The Sacrifice:** More visual real estate and potentially more noise if raw points are shown.
- **The Risk:** Viewers might over-index on one shown alternative distribution as “the truth,” rather than as an illustration of ambiguity.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating identical boxplots as evidence that datasets are “the same.”
- **Why it fails:** The paper shows markedly different distributions can map to the same boxplot summary [@matejkaSameStatsDifferent2017].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers make claims about skewness/modality from the box alone without seeing underlying values.
- **The Test:** Compare quartiles and whisker-defining points across datasets; if they match but the raw distributions differ, the boxplot is hiding structure as intended [@matejkaSameStatsDifferent2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Overlay jittered points or a 1D strip of observations alongside the boxplot.
- **Best Fix:** Pair the boxplot with an explicit depiction of the underlying distribution (e.g., multiple example distributions or a point-based view) when distribution shape matters to interpretation [@matejkaSameStatsDifferent2017].
