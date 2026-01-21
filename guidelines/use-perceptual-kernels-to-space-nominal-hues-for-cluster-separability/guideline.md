---
id: use-perceptual-kernels-to-space-nominal-hues-for-cluster-separability
title: Use Perceptual Kernels to Space Nominal Hues for Clustering
bibliography: references.bib
description: When clustering categorical groups, choose color hues whose perceptual
  distances are maximized using a perceptual kernel.
labels:
- chart:scatter
- task:cluster
- visual:color
- impact:discriminability
- data:categorical
- audience:general
- method:perceptual-kernel
- source:paper
---

## The Rule <!-- role: advice -->

For clustering tasks with nominal categories, assign color hues using a perceptual-kernel distance matrix so the chosen hues are as perceptually distinct as possible.

## The Logic <!-- role: reason -->

- **The Principle:** Perceptual distance optimization for categorical separation.
- **The Evidence:** The color perceptual kernel captures how similar/dissimilar hues are perceived and supports re-ordering/selection to improve discriminability [@demiralpLearningPerceptualKernels2014]; the review frames this type of extracted knowledge as directly reusable in visualization recommendation workflows [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Cluster categories (spot grouping and separation).
- **Data Type:** Nominal categories encoded via color hue (points).
- **Audience:** General viewers.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must preserve a pre-existing semantic mapping (e.g., mandated brand colors).
- **Reason:** Kernel-optimized choices may alter which specific hues are used/assigned, conflicting with fixed mappings; the kernel only optimizes perception, not external semantics [@demiralpLearningPerceptualKernels2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less freedom to use arbitrary or stylistic color sets; you may need to swap to a different subset for separability.
- **The Risk:** A kernel learned from one palette may not apply to a different palette without re-measurement [@demiralpLearningPerceptualKernels2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Choosing colors evenly spaced “by eye” without any perceptual distance model.
- **Why it fails:** Perceived similarity is not uniform across a palette; kernels reveal structure and clustering that naive choices can miss [@demiralpLearningPerceptualKernels2014], which is exactly why collation into machine-usable rules is valuable [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Categories blend because multiple groups use hues that feel too close.
- **The Test:** If viewers confuse category colors in a quick glance, your palette likely doesn’t maximize perceptual distances implied by the kernel [@demiralpLearningPerceptualKernels2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap the closest-looking hues with alternatives that are farther apart in the kernel distance matrix.
- **Best Fix:** Re-run color assignment using kernel distances to maximize minimum pairwise distance across the set of hues in use [@demiralpLearningPerceptualKernels2014; @zengReviewCollationGraphical2023].
