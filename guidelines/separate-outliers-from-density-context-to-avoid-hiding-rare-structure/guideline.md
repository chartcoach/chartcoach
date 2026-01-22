---
id: separate-outliers-from-density-context-to-avoid-hiding-rare-structure
title: Preserve outliers in density-based multivariate plots by identifying them in
  histogram/PDF space and drawing them separately
bibliography: references.bib
description: "Counteract density plots\u2019 tendency to deemphasize rare points by\
  \ explicitly detecting and overlaying outliers."
labels:
- chart:parallel-coordinates
- chart:scatter
- task:detect
- visual:layering
- impact:clarity
- data:multivariate
- data:uncertain
- audience:expert
- complexity:advanced
---

## Add an outlier layer on top of PDF context in density-based plots <!-- role: advice -->

In density-based plots, identify outliers using PDF- or histogram-based analysis and render them as a separate overlay distinct from the density context. Treat outliers as distributions so that highly uncertain “apparent outliers” are not promoted as meaningful.

## Density views summarize likelihood but can suppress rare events without an explicit focus channel <!-- role: reason -->

A PDF emphasizes the most likely values, which is valuable for overview, but it can make low-probability structure hard to notice, especially as dataset size grows and density concentrates. Outlier detection in histogram/PDF space finds isolated “islands” of low support, and rendering those separately restores focus+context while respecting uncertainty.

**Mechanism:** Separating rare structures into a distinct mark layer prevents them from being washed out by normalization and blending used to show the main density mass.

**Evidence:** PDF-based representations can hide outliers and increasingly deemphasize them in large datasets, and histogram-based outlier detection methods can be applied directly because histograms closely relate to PDFs [@fengMatchingVisualSaliency2010]. Rendering detected outliers separately provides focus (outliers) with context (PDF) while naturally handling uncertainty by ignoring clusters whose distributions are too large [@fengMatchingVisualSaliency2010].

**Notes:** The paper discusses applying connectivity-based analysis of pairwise histograms (islands) to the computed density representations.

## When to add an outlier layer to density plots <!-- role: context -->

- **User Goal:** Notice rare but potentially important cases while still understanding the dominant distribution.
- **Task:** Outlier detection and investigation in multivariate uncertain data.
- **Data:** Large or moderate-size datasets where PDFs summarize well but rare cases exist.
- **Chart Setting:** Density-based scatter plots or density-based parallel coordinates used as the main view.
- **Audience:** Analysts who must not miss unusual cases (for example, clinical investigation).
- **Success Criterion:** Outliers remain discoverable without making uncertain noise look like meaningful structure.

## When not to split outliers into a separate layer <!-- role: exceptions -->

**Break it when:** The analysis goal is strictly to summarize typical behavior and outliers are intentionally out of scope. **Why:** Outlier overlays can distract from the main distribution summary that the PDF is designed to communicate [@fengMatchingVisualSaliency2010].

## Tradeoffs of explicit outlier overlays <!-- role: costs -->

**Sacrifice:** Additional computation and visual complexity are introduced. **Risk:** Poor outlier criteria can over-highlight noise or under-highlight meaningful rare cases. **Mitigation:** Base outlier detection on PDF/histogram structure so uncertainty is incorporated into whether something is truly isolated.

## Common mistakes in outlier handling for density plots <!-- role: mistakes -->

- **Mistake:** Assume the PDF alone will reveal outliers reliably. **Why it fails:** Low-probability regions can be too faint to notice, especially as dataset size increases [@fengMatchingVisualSaliency2010].
- **Mistake:** Mark any visually isolated mean as an outlier without considering distribution variance. **Why it fails:** Large-variance distributions can look spatially isolated by mean but are not confidently distinguishable from the bulk distribution [@fengMatchingVisualSaliency2010].

## Quick checks for whether outliers are being suppressed <!-- role: check -->

**Failure Sign:** Rare cases known from the data are not visible or are nearly indistinguishable from background density. **Quick Check:** Temporarily raise contrast; if outliers only appear under extreme contrast changes, they are likely being suppressed by the density summary [@fengMatchingVisualSaliency2010]. **Stronger Test:** Run histogram/PDF island detection and confirm whether the view shows the flagged regions distinctly.

## What to do instead if you cannot implement outlier detection <!-- role: fix -->

- Use an animated probabilistic plot so rare events flicker and become attention-grabbing without explicit detection [@fengMatchingVisualSaliency2010].
- Provide interactive brushing linked across views so users can isolate sparse regions even when they are faint in the density image [@fengMatchingVisualSaliency2010].
- Reduce the density normalization or use a separate rendering pass for low-density tails to increase their visibility as a temporary investigative mode [@fengMatchingVisualSaliency2010].
- Show discrete marks only for candidate outliers while keeping the PDF as the default context layer [@fengMatchingVisualSaliency2010].
