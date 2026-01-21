---
id: reorder-categorical-palettes-by-maximin-perceptual-distance
title: Reorder Palettes to Maximize Perceptual Discriminability
bibliography: references.bib
description: Reorder categorical palette items so early selections maximize minimum
  perceptual distance using a perceptual kernel.
labels:
- chart:any
- task:select
- visual:color
- visual:shape
- impact:clarity
- data:categorical
- audience:designer
- method:palette-optimization
- source:demiralp-2014
---

## The Rule <!-- role: advice -->

Reorder a categorical palette by repeatedly choosing the next item that **maximizes its minimum perceptual distance** to the items already chosen (a maximin/Hausdorff-style selection), using a perceptual kernel.

## The Logic <!-- role: reason -->

A perceptual kernel exposes clusters of similar marks; selecting representatives from different clusters early increases discriminability for small-n subsets and produces a stable ordering that extends by addition without reshuffling prior assignments [@demiralpLearningPerceptualKernels2014a].

- **The Principle:** Maximize minimum distance to avoid early picks from the same perceptual cluster.
- **The Evidence:** The paper demonstrates re-ordered shape/color/size palettes derived from triplet-matching kernels using a procedure that starts with the farthest pair and then adds items maximizing minimum distance to the existing set [@demiralpLearningPerceptualKernels2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Ensure the first k categories are as distinguishable as possible (especially when k varies over time).
- **Data Type:** Categorical labels where the number of categories shown may grow.
- **Audience:** Designers building palette defaults for tools, templates, or style guides.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must preserve a conventional or semantic ordering (e.g., pre-established category-color mappings).
- **Reason:** The optimized order may conflict with existing conventions or label associations; the paper focuses on perceptual discriminability, not semantics [@demiralpLearningPerceptualKernels2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** The resulting order may appear “random” with respect to hue families or shape themes.
- **The Risk:** If the kernel is learned for a specific rendering context (size, stroke, background), reordering based on it may not transfer perfectly to different contexts [@demiralpLearningPerceptualKernels2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Spacing items evenly in an arbitrary parameter space (e.g., palette index) and assuming equal perceptual spacing.
- **Why it fails:** The learned kernels show non-uniform perceptual structure and clustering that arbitrary spacing doesn’t address [@demiralpLearningPerceptualKernels2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** The first few palette entries still contain near-duplicates (e.g., two very similar shapes/hues).
- **The Test:** For the first k items, compute the minimum pairwise distance from the kernel; it should be relatively high compared to other k-subsets [@demiralpLearningPerceptualKernels2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the palette order with the kernel-derived maximin order.
- **Best Fix:** Maintain a stable, extendable ordering built from the farthest-pair seed and iterative maximin additions, as shown in the paper [@demiralpLearningPerceptualKernels2014a].
