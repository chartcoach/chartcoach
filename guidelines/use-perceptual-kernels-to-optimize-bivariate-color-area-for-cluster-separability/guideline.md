---
id: use-perceptual-kernels-to-optimize-bivariate-color-area-for-cluster-separability
title: "Optimize Color\u2013Size Pairings with Perceptual Kernels for Clustering"
bibliography: references.bib
description: When encoding categories with both color hue and marker size, use the
  combined perceptual kernel to choose combinations that maximize separability.
labels:
- chart:scatter
- task:cluster
- visual:color
- visual:area
- impact:discriminability
- data:categorical
- audience:general
- encoding:redundant
- method:perceptual-kernel
- source:paper
---

## The Rule <!-- role: advice -->

When you encode nominal categories using both color hue and marker area (size), choose the color–size combinations using a bivariate perceptual-kernel distance matrix to maximize perceptual separability.

## The Logic <!-- role: reason -->

- **The Principle:** Use measured distances in the joint (color, size) stimulus space.
- **The Evidence:** The study estimates bivariate kernels (including size–color) and presents them as reusable distance matrices for optimizing assignments and improving discriminability [@demiralpLearningPerceptualKernels2014]; the review incorporates this as structured knowledge meant for visualization recommendation decisions [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Cluster many nominal groups when a single channel is insufficient.
- **Data Type:** Nominal categories encoded with color hue + marker size.
- **Audience:** General viewers.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Size is needed to represent quantitative magnitude.
- **Reason:** Using size for nominal categories can imply ordering or magnitude; kernel-based separability does not resolve that semantic ambiguity [@demiralpLearningPerceptualKernels2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** More complex legend entries and increased cognitive load for decoding composite symbols.
- **The Risk:** Composite encodings can over-emphasize some categories if size differences are large, even if the intent is categorical separation [@demiralpLearningPerceptualKernels2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Spreading sizes uniformly and picking colors independently, then pairing without checking composite confusability.
- **Why it fails:** Separability in the joint space is what matters for category discrimination; bivariate kernels directly capture joint perceptual distances [@demiralpLearningPerceptualKernels2014], which collation work argues should be machine-actionable [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Two categories differ in both color and size but still appear similar as a combined mark.
- **The Test:** View the legend only (without data) and ask whether each composite symbol is clearly distinct from all others; if not, revisit the assignment [@demiralpLearningPerceptualKernels2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Adjust the most-confusable composites by swapping sizes or colors to increase bivariate kernel distances.
- **Best Fix:** Optimize the full assignment using the size–color perceptual kernel to maximize the minimum pairwise distance among composites [@demiralpLearningPerceptualKernels2014; @zengReviewCollationGraphical2023].
