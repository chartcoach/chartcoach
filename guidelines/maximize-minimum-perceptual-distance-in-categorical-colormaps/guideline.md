---
id: maximize-minimum-perceptual-distance-in-categorical-colormaps
title: Maximize the minimum perceptual distance between category colors (in CIEDE2000
  space)
bibliography: references.bib
description: Improve categorical color discriminability by optimizing the palette
  to increase the smallest pairwise color difference.
labels:
- chart:general
- task:distinguish
- visual:color
- impact:clarity
- data:categorical
- audience:general
- method:optimization
---

## Optimize categorical palettes for maximum minimum distance <!-- role: advice -->

Maximize the smallest pairwise perceptual difference among category colors rather than optimizing average separation.

## Minimum-distance optimization reduces the worst confusable pair <!-- role: reason -->

Optimizing the minimum pairwise distance targets the “weakest link” in a categorical palette: the pair of colors most likely to be confused. Raising that minimum increases the chance that every category remains distinguishable, even if some other pairs were already far apart.

**Mechanism:** Increasing the minimum pairwise distance reduces the most severe color confusability, which often dominates categorization errors when viewers must discriminate multiple classes.

**Evidence:** A categorical colormap optimization approach is formulated to maximize the minimal pairwise perceptual distance (Dmin) among colors, explicitly preferring improvements to the closest (most confusable) pairs over maximizing average distance [@fangCategoricalColormapOptimization2017; @zengReviewCollationGraphical2023].

**Notes:** This guidance concerns categorical (nominal) color sets, not sequential or diverging colormaps.

## Context for minimum-distance palette optimization <!-- role: context -->

- **User Goal:** Reliably tell categories apart using color.
- **Task:** Discriminate/identify categories (legend-based lookup or direct recognition).
- **Data:** Nominal categories mapped to distinct colors; moderate-to-high category count where confusion risk rises.
- **Chart Setting:** Any chart where color is the primary category key (e.g., maps, multi-class plots, categorical overlays), including repeated daily use where memorability matters.
- **Audience:** General audiences or domain experts who still need fast, accurate discrimination.
- **Success Criterion:** Fewer ambiguous/near-identical category colors; improved category separability.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The palette must prioritize semantic or conventional color meanings over discriminability. **Why:** Unconstrained distance maximization can shift hues enough to break intended associations.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose some palette “style” uniformity or aesthetic harmony when prioritizing the minimum distance. **Risk:** Distance-only optimization can produce colors that are perceptually distinct but semantically inappropriate for the domain. **Mitigation:** Constrain optimization to preserve required semantics.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Maximizing average pairwise distance while ignoring the closest pair. **Why it fails:** A single very-close pair can still dominate confusion even if most other pairs are far apart.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Two categories repeatedly get confused because their colors look “almost the same.” **Quick Check:** Compute all pairwise CIEDE2000 distances and identify the minimum; if one pair is notably smaller than the rest, you have a weak link. **Stronger Test:** Run a short forced-choice discrimination check where viewers must match swatches to category labels under time pressure.

## Fix: What to do instead <!-- role: fix -->

- Compute pairwise perceptual distances and directly target the closest pairs for improvement.
- Re-run palette optimization using an objective that increases the minimum distance (minimax objective).
- Reduce the number of categories shown at once (e.g., filtering or grouping) if the palette cannot be separated enough.
- Add a secondary redundant encoding (e.g., shape or line style) when color-only separability remains insufficient.
