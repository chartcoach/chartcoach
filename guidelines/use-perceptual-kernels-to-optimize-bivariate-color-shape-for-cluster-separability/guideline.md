---
id: use-perceptual-kernels-to-optimize-bivariate-color-shape-for-cluster-separability
title: "Optimize Color\u2013Shape Pairings with Perceptual Kernels for Clustering"
bibliography: references.bib
description: When encoding categories with both color hue and shape, use the combined
  perceptual kernel to choose pairings that maximize separability.
labels:
- chart:scatter
- task:cluster
- visual:color
- visual:shape
- impact:discriminability
- data:categorical
- audience:general
- encoding:redundant
- method:perceptual-kernel
- source:paper
---

## The Rule <!-- role: advice -->

When you encode nominal categories using both color hue and shape, select the specific color–shape combinations using a bivariate perceptual-kernel distance matrix to maximize perceptual separability.

## The Logic <!-- role: reason -->

- **The Principle:** Multi-channel perceptual distance optimization (treat combinations as stimuli with measurable distances).
- **The Evidence:** The paper estimates bivariate kernels (including shape–color) that quantify perceived distances for combined encodings and argues they can drive automated assignment for better discriminability [@demiralpLearningPerceptualKernels2014]; the review collates this into structured design knowledge intended to be translated into recommendation rules/constraints [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Cluster multiple nominal groups where one channel alone may not provide enough distinguishable categories.
- **Data Type:** Nominal categories encoded jointly with color hue + shape in point marks.
- **Audience:** General viewers.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must keep color and shape independently meaningful (e.g., color encodes category A and shape encodes category B, not a combined code).
- **Reason:** A bivariate kernel optimizes the combined symbol space; it may select combinations that are optimal jointly but not independently interpretable by channel [@demiralpLearningPerceptualKernels2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Added complexity in legend and mapping (more composite symbols to explain).
- **The Risk:** Kernel-optimized combinations may still visually cluster (e.g., by one dominant dimension) depending on the chosen stimuli set; you must validate the result visually for your specific palette [@demiralpLearningPerceptualKernels2014].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Independently picking a “good” color palette and a “good” shape palette and then pairing them arbitrarily.
- **Why it fails:** Perceptual interaction means separability in the combined space is not guaranteed by separability in each single channel; bivariate kernels explicitly measure the combined distances [@demiralpLearningPerceptualKernels2014], a nuance highlighted by collation efforts [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Some composite symbols (color+shape) are confused even though colors alone and shapes alone seem distinct.
- **The Test:** Inspect the set of composite symbols as a whole; if multiple composites feel “too close,” your pairing likely ignored bivariate distances [@demiralpLearningPerceptualKernels2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap pairings among existing colors/shapes to increase bivariate kernel distances between the most-confusable composites.
- **Best Fix:** Re-run assignment using the shape–color perceptual kernel to maximize minimum pairwise distance among all composites used [@demiralpLearningPerceptualKernels2014; @zengReviewCollationGraphical2023].
