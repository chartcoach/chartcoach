---
id: optimize-categorical-palettes-with-perceptual-kernels-for-cluster-tasks
title: Optimize categorical color, shape, and size palettes using perceptual kernels
  for cluster tasks
bibliography: references.bib
description: Use perceptual distance kernels to choose or order discrete palette entries
  so categories are more perceptually separable in clustering.
labels:
- chart:scatter
- task:cluster
- visual:color
- visual:shape
- visual:size
- impact:clarity
- data:categorical
- complexity:advanced
---

## Use perceptual-kernel-optimized palettes for categorical clustering <!-- role: advice -->

Optimize discrete palette entries (for color hue, shape, and/or size) using a perceptual kernel so categories are as perceptually separated as possible for clustering.

## Perceptual-distance-driven separability in categorical encodings <!-- role: reason -->

When categorical values are mapped to visual tokens that are far apart in perceptual space, viewers can more reliably group similar items and separate different groups during clustering.

**Mechanism:** A perceptual kernel provides a data-driven distance matrix over palette items; choosing/ordering items to maximize these distances increases perceived separability among categories.

**Evidence:** Perceptual kernels (distance matrices from aggregate similarity judgments) were learned for nominal encodings of shape, color hue, size, and their pairwise combinations, enabling palette re-ordering to maximize perceptual discriminability for clustering-relevant separability judgments [@demiralpLearningPerceptualKernels2014; @zengReviewCollationGraphical2023].

**Notes:** This guideline is about *which palette entries to use and how to order them* within the same encoding channel(s), not about choosing between channels.

## When perceptual-kernel palette optimization applies <!-- role: context -->

- **User Goal:** Identify groups of points/marks that belong together and distinguish groups from one another.
- **Task:** cluster.
- **Data:** Nominal categories (one or two categorical fields) mapped to shape, color hue, size, or their combinations.
- **Chart Setting:** Discrete-mark charts where categories are distinguished by legendable symbols (e.g., points/circles).
- **Audience:** Any audience that needs reliable category separation (including mixed expertise).
- **Success Criterion:** Higher perceptual separability of categories (clear grouping and reduced confusion between categories).

## When not to follow perceptual-kernel palette optimization <!-- role: exceptions -->

**Break it when:** You do not have (or cannot derive) a perceptual kernel for the exact palette items you intend to use. **Why:** The optimization depends on measured distances among the specific stimuli; without those distances, the “optimized” ordering has no empirical basis.

## Tradeoffs of perceptual-kernel palette optimization <!-- role: costs -->

**Sacrifice:** Additional implementation and maintenance effort to store kernels and run the optimization. **Risk:** Overfitting palette choices to the tested stimulus set (e.g., a specific tool’s default palette) rather than your actual symbol set. **Mitigation:** Treat the kernel as a reusable asset tied to a specific palette definition and version it alongside design tokens.

## Common failure modes in kernel-based palette optimization <!-- role: mistakes -->

**Mistake:** Re-ordering or selecting palette entries “by intuition” while calling it perceptual optimization. **Why it fails:** The approach requires measured perceptual distances; intuition can reinforce hidden similarity clusters that hurt category separation.

## Quick checks for perceptual separability improvements <!-- role: check -->

**Failure Sign:** Multiple categories look interchangeable or form unintended visual groups. **Quick Check:** Hide the legend and see if you can still separate clusters by the intended category within a few seconds. **Stronger Test:** Run a small clustering identification task with users comparing the default palette vs. the kernel-optimized palette.

## What to do instead if you can’t use kernels <!-- role: fix -->

- Use fewer categories per view so separability demands are reduced.
- Split categories into multiple panels (faceting) so each panel uses a smaller palette.
- Switch to a single encoding channel (only color hue or only shape) instead of combining multiple channels if you cannot validate their combined palette items.
- Collect similarity judgments for your actual symbol set to build a kernel before optimizing palette assignments.
