---
id: optimize-color-class-assignment-for-multiclass-scatterplots
title: Optimize Color Assignment to Maximize Class Separability in Multiclass Scatterplots
bibliography: references.bib
description: Assign colors to classes in multiclass scatterplots using an optimization
  approach so classes are more visually separable for clustering.
labels:
- chart:scatter
- task:cluster
- visual:color
- visual:position
- impact:clarity
- data:categorical
- audience:general
- complexity:advanced
---

## The Rule <!-- role: advice -->

Optimize the mapping from class labels to color hues (not just the palette choice) to maximize perceived class separability in multiclass scatterplots.

## The Logic <!-- role: reason -->

This works because the same set of categorical colors can produce very different perceived separations depending on which specific class gets which specific color; choosing the assignment to emphasize separability helps users distinguish clusters.

- **The Principle:** Color assignment (label→color mapping) materially affects perceived cluster separability even when the palette is fixed.
- **The Evidence:** [@wangOptimizingColorAssignment2019] as collated for recommendation-oriented knowledge use in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Clustering—seeing how many classes/groups exist and how well they separate.
- **Data Type:** Two quantitative fields plotted on X/Y plus a nominal class label encoded by color hue.
- **Audience:** General users performing visual cluster separation judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot change class→color assignments because colors are semantically fixed (e.g., organizational standards).
- **Reason:** The rule requires freedom to reassign hues across categories; if assignments are fixed, you cannot apply the optimization implied by [@wangOptimizingColorAssignment2019] (as summarized in [@zengReviewCollationGraphical2023]).

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra computation/implementation complexity compared to using a default or sequential class ordering.
- **The Risk:** Inconsistency across views/sessions if the optimized assignment changes when data changes, potentially confusing users.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Selecting a “good” categorical palette and assuming any default class ordering is fine.
- **Why it fails:** The evidence indicates that assignment (which class gets which hue) strongly influences separability even with the same palette [@wangOptimizingColorAssignment2019], a point emphasized in the collation for recommendation settings [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Some classes visually “blend” or are hard to disentangle from neighboring clusters despite using distinct categorical hues.
- **The Test:** Reassign colors across classes (permute label→hue mapping) and see whether separability noticeably changes; if it does, your current assignment is likely suboptimal per the phenomenon documented in [@wangOptimizingColorAssignment2019] and collated in [@zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Try multiple permutations of class→hue assignment and pick the one that makes clusters easiest to distinguish.
- **Best Fix:** Implement an explicit optimization procedure for class→hue assignment targeting perceived class separability as described by [@wangOptimizingColorAssignment2019], leveraging the structured collation context from [@zengReviewCollationGraphical2023].
