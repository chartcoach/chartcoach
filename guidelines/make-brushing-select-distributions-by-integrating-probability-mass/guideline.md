---
id: make-brushing-select-distributions-by-integrating-probability-mass
title: Select Uncertain Data by Integrating Distribution Mass Inside the Brush
bibliography: references.bib
description: Replace inside/outside selection with probability-mass selection so uncertain
  values require larger brushes.
labels:
- chart:scatter
- chart:parallel-coordinates
- task:select
- visual:interaction
- impact:trust
- data:uncertainty
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

When brushing uncertain data, select a point only if the brush region contains at least a chosen fraction of its distribution’s probability mass (e.g., 95%), not merely its mean.

## The Logic <!-- role: reason -->

Uncertain points are distributions with infinite extent, so binary inclusion is ill-defined. Integrating the PDF within the brush yields the likelihood that a sample would fall inside; using a high threshold forces the user to acknowledge uncertainty by requiring a larger brush for high-variance points.

- **The Principle:** Probabilistic selection via definite integration
- **The Evidence:** [@fengMatchingVisualSaliency2010]

## Where to Apply <!-- role: context -->

- **User Goal:** Interactive filtering/selection in uncertain scatter plots and parallel coordinates without over-trusting noisy values
- **Data Type:** Per-sample statistical distributions (notably uncorrelated normals where erf-based integrals are fast)
- **Audience:** Expert users doing linked brushing and exploratory hypothesis generation

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intentionally want to include “maybe relevant” uncertain values for recall-heavy exploration
- **Reason:** High mass thresholds (like 95%) bias toward precision and can exclude uncertain-but-interesting cases [@fengMatchingVisualSaliency2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** More computation than simple hit-testing; requires integration (analytical or numerical)
- **The Risk:** Threshold choice changes interaction feel and selection size; too strict can frustrate users [@fengMatchingVisualSaliency2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Select based on whether the mean falls inside the brush
- **Why it fails:** It lets large-uncertainty distributions be selected too easily, contradicting the goal of discouraging attention to unreliable values [@fengMatchingVisualSaliency2010].

## How to Check <!-- role: check -->

- **Visual Sign:** Very uncertain points get selected with tiny brushes just because their mean is inside
- **The Test:** Try selecting a known high-σ point with a small brush; it should fail unless the brush expands enough to cover most mass [@fengMatchingVisualSaliency2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Implement axis-aligned box selection by integrating separable normals inside [a,b]×[c,d] using error functions
- **Best Fix:** Use probabilistic selection consistently across interval queries, angular brushing, and linear function brushing by integrating mass under the brush geometry [@fengMatchingVisualSaliency2010].
