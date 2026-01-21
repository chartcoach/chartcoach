---
id: use-density-plots-to-map-saliency-to-uncertainty
title: Replace Discrete Glyph Plots with Density Plots for Uncertain Data
bibliography: references.bib
description: Use KDE-based density plots so uncertain values become visually diffuse
  and less salient, while certain values remain crisp and prominent.
labels:
- chart:scatter
- chart:parallel-coordinates
- task:explore
- visual:luminance
- visual:blur
- impact:trust
- data:uncertainty
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

Render uncertain multivariate data as a kernel density estimate (PDF image) instead of plotting discrete points/lines.

## The Logic <!-- role: reason -->

Density estimation superimposes each sample’s uncertainty distribution; high-variance samples spread out and overlap into low-contrast “blur,” while low-variance samples stay compact and high-contrast. This disengages preattentive feature detection for uncertain values and makes visual saliency proportional to confidence.

- **The Principle:** Match saliency (contrast/blur) to confidence via KDE
- **The Evidence:** [@fengMatchingVisualSaliency2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Avoid false positives/false negatives when spotting clusters, trends, and relationships under uncertainty
- **Data Type:** Multivariate data with per-sample uncertainty represented as statistical distributions (e.g., normal with per-variable σ; optionally ρ)
- **Audience:** Analysts and domain experts doing exploratory multivariate analysis

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task requires tracking specific individual records end-to-end (e.g., following one polyline across many axes)
- **Reason:** Full density representations can remove the ability to uniquely identify and trace individual items [@fengMatchingVisualSaliency2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced identifiability of individual samples; outliers may be deemphasized
- **The Risk:** Viewers may miss rare-but-important points unless you add an outlier strategy [@fengMatchingVisualSaliency2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Plot uncertain points with discrete glyphs plus a legend encoding uncertainty (e.g., hue)
- **Why it fails:** Discrete marks can still trigger attention and create misleading clusters before the legend is consulted; the uncertainty scale is arbitrary and can confuse selection and interpretation [@fengMatchingVisualSaliency2010].

## How to Check <!-- role: check -->

- **Visual Sign:** Uncertain regions still look like crisp clusters or sharp polylines that “pop” like reliable features
- **The Test:** Compare a discrete plot to its density/PDF rendering; if the discrete plot shows apparent clusters that vanish into diffuse density, the discrete plot is likely overstating certainty [@fengMatchingVisualSaliency2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace glyph opacity stacking with explicit KDE using each sample’s uncertainty distribution as the kernel
- **Best Fix:** Use direct PDF visualization (pixel/grid bins) and link it with uncertainty-aware interaction (brushing by integrating distributions) [@fengMatchingVisualSaliency2010].
