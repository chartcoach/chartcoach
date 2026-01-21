---
id: compute-parallel-coordinates-density-by-transforming-distributions
title: Render Uncertain Parallel Coordinates as Density by Transforming Distributions
  into PC Space
bibliography: references.bib
description: Convert uncertainty distributions into parallel coordinates density rather
  than drawing discrete polylines.
labels:
- chart:parallel-coordinates
- task:explore
- visual:luminance
- impact:trust
- data:uncertainty
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

For uncertain multivariate data, generate parallel coordinates plots as a density (PDF) in PC space by transforming each sample’s distribution between adjacent axes, instead of drawing one polyline per sample.

## The Logic <!-- role: reason -->

A PC density plot makes uncertain values spread and overlap, reducing preattentive saliency of unreliable structures and preventing misleading line-tracing. Transforming distributions preserves probabilistic meaning (unit integral) and makes the visible structure reflect likelihood.

- **The Principle:** Probability-density representation in PC space to suppress false structure
- **The Evidence:** [@fengMatchingVisualSaliency2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify credible multivariate trends and correlations while avoiding false clusters caused by uncertainty
- **Data Type:** Multivariate samples with modeled uncertainty per variable (notably normal distributions; optional correlation ρ)
- **Audience:** Expert users using PC plots for hypothesis generation and variable relationship discovery

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must preserve the ability to follow individual lines across many axes as a primary task
- **Reason:** Density PC plots intentionally discourage line-following because it can lead to false inferences from uncertain trajectories [@fengMatchingVisualSaliency2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less direct “record-level” traceability
- **The Risk:** Axis reordering becomes more expensive because density between many axis pairs may need recomputation [@fengMatchingVisualSaliency2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keep standard line PC plots and only annotate uncertainty separately
- **Why it fails:** The sharp polylines remain preattentively salient and can create false positives/negatives under uncertainty [@fengMatchingVisualSaliency2010].

## How to Check <!-- role: check -->

- **Visual Sign:** The PC view is dominated by crisp line crossings even where uncertainty is high
- **The Test:** Compare to the PC density rendering; if apparent line “bundles” dissolve into diffuse density, the line plot is overstating structure [@fengMatchingVisualSaliency2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace line rendering with PC-space density computed from transformed distributions between adjacent axes
- **Best Fix:** Add uncertainty-proportional mean emphasis and link brushing to distribution-aware selection (integrate probability within brush bounds) [@fengMatchingVisualSaliency2010].
