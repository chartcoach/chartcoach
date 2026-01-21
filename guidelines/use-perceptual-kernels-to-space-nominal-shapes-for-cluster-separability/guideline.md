---
id: use-perceptual-kernels-to-space-nominal-shapes-for-cluster-separability
title: Use Perceptual Kernels to Space Nominal Shapes for Clustering
bibliography: references.bib
description: When clustering categorical groups, choose shape symbols whose perceptual
  distances are maximized using a perceptual kernel.
labels:
- chart:scatter
- task:cluster
- visual:shape
- impact:discriminability
- data:categorical
- audience:general
- method:perceptual-kernel
- source:paper
---

## The Rule <!-- role: advice -->

For clustering tasks with nominal categories, assign shapes using a perceptual-kernel distance matrix so the chosen shapes are as perceptually distinct as possible.

## The Logic <!-- role: reason -->

- **The Principle:** Perceptual distance matching (maximize between-category separability).
- **The Evidence:** Perceptual kernels quantify perceived distances among shapes and can be used to optimize symbol selection/ordering for discriminability [@demiralpLearningPerceptualKernels2014]; this study is collated as actionable graphical-perception knowledge for recommendation systems [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Cluster categories (see whether points form distinct groups).
- **Data Type:** Nominal (categorical) groups encoded with shape marks (points).
- **Audience:** General viewers who must visually separate categories quickly.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot rely on shape because the medium cannot render symbols clearly (e.g., extremely small marks).
- **Reason:** The kernel-based separability assumes viewers can actually perceive the symbol differences; if symbols are not legible, the distances no longer help [@demiralpLearningPerceptualKernels2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires collecting, storing, or using an existing perceptual-kernel matrix rather than default shape palettes.
- **The Risk:** If you use a kernel learned for a different shape set than the one you deploy, the “optimized” selection may not generalize [@demiralpLearningPerceptualKernels2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a tool’s default shape palette order and assuming all symbols are equally distinct.
- **Why it fails:** The kernel results show shape sets contain clusters of similar symbols; naive selection can pick multiple symbols from the same perceptual cluster [@demiralpLearningPerceptualKernels2014], a gap the collation highlights for recommendation systems to address [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Two or more categories look “nearly the same” even though the legend lists different shapes.
- **The Test:** Compare all assigned shapes pairwise and look for obvious near-duplicates; if many seem confusable, your selection likely ignored perceptual distances [@demiralpLearningPerceptualKernels2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the most-confusable shape(s) with ones farther away in the kernel distance matrix.
- **Best Fix:** Recompute the full shape assignment using the perceptual-kernel distances to maximize minimum pairwise distance among the shapes used [@demiralpLearningPerceptualKernels2014; @zengReviewCollationGraphical2023].
