---
id: use-perceptual-kernels-to-optimize-bivariate-shape-area-for-cluster-separability
title: "Optimize Shape\u2013Size Pairings with Perceptual Kernels for Clustering"
bibliography: references.bib
description: When encoding categories with both shape and marker size, use the combined
  perceptual kernel to choose combinations that maximize separability.
labels:
- chart:scatter
- task:cluster
- visual:shape
- visual:area
- impact:discriminability
- data:categorical
- audience:general
- encoding:redundant
- method:perceptual-kernel
- source:paper
---

## The Rule <!-- role: advice -->

When you encode nominal categories using both shape and marker area (size), choose the shape–size combinations using a bivariate perceptual-kernel distance matrix to maximize perceptual separability.

## The Logic <!-- role: reason -->

- **The Principle:** Joint perceptual distance optimization for combined encodings.
- **The Evidence:** The paper reports bivariate perceptual kernels (including shape–size) that measure perceived distances among composite stimuli and demonstrates their use for optimized assignment [@demiralpLearningPerceptualKernels2014]; this is included as structured perceptual knowledge intended to inform recommendation systems [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Cluster nominal groups using composite encodings.
- **Data Type:** Nominal categories encoded jointly via shape + size.
- **Audience:** General viewers.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The plot must remain readable at very small mark sizes.
- **Reason:** If shapes are not legible at the required size, a kernel-based choice among shapes cannot help separation [@demiralpLearningPerceptualKernels2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Added decoding overhead (viewers must interpret two channels at once).
- **The Risk:** If size differences become too salient, viewers may overweight size over shape when judging categories [@demiralpLearningPerceptualKernels2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking “distinct” shapes and “distinct” sizes separately and assuming the combined set will be distinct.
- **Why it fails:** Interactions in multi-dimensional perceptual spaces mean distinctness must be evaluated in the combined space; bivariate kernels provide exactly that measurement [@demiralpLearningPerceptualKernels2014], aligning with the collation objective of producing machine-usable guidance [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Multiple categories share a “similar silhouette” overall despite differing in either shape or size.
- **The Test:** Compare all composite symbols in the legend; if any pair seems too close, your assignment likely didn’t maximize bivariate distances [@demiralpLearningPerceptualKernels2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap sizes among shapes to increase the distance between the most-confusable composites.
- **Best Fix:** Optimize the complete set of composite symbols using the shape–size perceptual kernel to maximize minimum pairwise distance [@demiralpLearningPerceptualKernels2014; @zengReviewCollationGraphical2023].
