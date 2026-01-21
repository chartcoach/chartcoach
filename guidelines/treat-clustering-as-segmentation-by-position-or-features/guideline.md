---
id: treat-clustering-as-segmentation-by-position-or-features
title: Treat Clustering As Segmentation By Position Or Features
bibliography: references.bib
description: Model clustering as a segmentation task where users partition marks into
  groups using spatial proximity or featural similarity.
labels:
- task:cluster
- task:segment
- visual:position
- visual:color
- visual:orientation
- impact:clarity
- data:quantitative
- audience:designer
---

## The Rule <!-- role: advice -->

When users need to cluster, design and evaluate the view as a **segmentation task**—partitioning marks into subsets by spatial position or by feature similarity.

## The Logic <!-- role: reason -->

Segmentation tasks require organizing data points into subsets based on similarity (often position or a visual feature), which leverages distributional information and grouping operations distinct from summarization or single-value lookup.

- **The Principle:** Visual Segmentation for Group Formation
- **The Evidence:** [@szafirFourTypesEnsemble2016], and its relevance for recommendation task taxonomies as compiled in [@zengReviewCollationGraphical2023]

## Where to Apply <!-- role: context -->

- **User Goal:** “Are there groups?” “How many clusters?” “Which points belong together?”
- **Data Type:** Many marks (e.g., scatterplot-like point clouds) with potential group structure.
- **Audience:** Designers and recommendation systems selecting encodings for cluster-oriented exploration.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Clusters are predefined categories the user already knows (pure categorical legend lookup).
- **Reason:** That becomes identification of known labels rather than discovering structure via segmentation [@szafirFourTypesEnsemble2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** Optimizing for segmentation may reduce support for precise value reading.
- **The Risk:** If multiple features encode multiple variables, segmentation along one feature may become harder to perceive.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming clustering performance will follow the same design rules as correlation or aggregate estimation.
- **Why it fails:** Clustering is segmentation (group formation), not structure estimation (trend/correlation) or summarization (mean/variance) [@szafirFourTypesEnsemble2016].

## How to Check <!-- role: check -->

- **Visual Sign:** Users disagree about how many clusters exist or which points belong to which group.
- **The Test:** Ask multiple users to mark clusters on the same plot; high disagreement signals weak segmentation support.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce competing encodings so one segmentation cue (position or a single feature) dominates.
- **Best Fix:** In recommendation workflows, tag “cluster” as segmentation and score candidate designs on their ability to support partitioning rather than averaging or precise reading, consistent with the task-centric use of perception knowledge advocated in [@zengReviewCollationGraphical2023].
