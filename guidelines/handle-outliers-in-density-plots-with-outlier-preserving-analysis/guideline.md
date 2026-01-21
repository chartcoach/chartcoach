---
id: handle-outliers-in-density-plots-with-outlier-preserving-analysis
title: Add an Outlier-Preserving Strategy When Using Density Plots
bibliography: references.bib
description: Because PDFs de-emphasize rare points, pair density plots with explicit
  outlier detection and distinct rendering.
labels:
- chart:parallel-coordinates
- task:detect-outliers
- visual:layering
- impact:discoverability
- data:uncertainty
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

When using density/PDF plots, explicitly detect and separately render outliers so rare but meaningful structures are not lost in the density summary.

## The Logic <!-- role: reason -->

Density emphasizes likely regions and can hide small populations; large-uncertainty “apparent outliers” should also be discounted because their distributions cover wide ranges. Histogram/PDF-based outlier detection on pairwise variable bins can preserve small isolated islands while naturally accounting for uncertainty.

- **The Principle:** Focus+context: density for context, explicit outliers for focus
- **The Evidence:** [@fengMatchingVisualSaliency2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Find rare cases or subpopulations without being misled by uncertainty
- **Data Type:** Large multivariate datasets displayed as scatter/PC density where over-plotting and masking are likely
- **Audience:** Experts performing exploratory analysis who need both trends and exceptions

## When to Break It <!-- role: exceptions -->

- **Scenario:** The analysis goal is strictly central tendency and typical behavior, and outliers are known to be irrelevant
- **Reason:** Outlier emphasis adds complexity and may distract from the main density structure [@fengMatchingVisualSaliency2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional computation and visual layering decisions
- **The Risk:** Poor outlier criteria can surface noise, or miss meaningful rare points [@fengMatchingVisualSaliency2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assume outliers will be obvious in the PDF because they are “different”
- **Why it fails:** Outliers may be dim or fully absorbed by dominant density, especially in large datasets [@fengMatchingVisualSaliency2010].

## How to Check <!-- role: check -->

- **Visual Sign:** Known rare points disappear in density-only views, or only show as faint speckles indistinguishable from noise
- **The Test:** Compare discrete rendering vs density; if discrete shows isolated points that density obscures, you need an outlier-preserving layer [@fengMatchingVisualSaliency2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Run pairwise histogram/PDF connectivity analysis to find small isolated islands and mark contributing distributions as outliers
- **Best Fix:** Render detected outliers with distinct discrete glyphs/lines atop the density for combined focus+context [@fengMatchingVisualSaliency2010].
