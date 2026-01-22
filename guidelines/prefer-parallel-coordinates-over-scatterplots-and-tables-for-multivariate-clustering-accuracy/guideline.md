---
id: prefer-parallel-coordinates-over-scatterplots-and-tables-for-multivariate-clustering-accuracy
title: Prefer parallel coordinates over scatterplots and tables for multivariate clustering
  accuracy
bibliography: references.bib
description: For identifying clusters in multivariate data, parallel coordinates improved
  accuracy over scatterplots and data tables.
labels:
- chart:parallel-coordinates
- chart:scatter
- chart:table
- task:cluster
- visual:position
- impact:accuracy
- data:multivariate
- data:quantitative
- audience:general
- complexity:intermediate
---

## Use parallel coordinates to improve clustering accuracy <!-- role: advice -->

Use a parallel coordinates plot (PCP) when users must identify clusters in multivariate data and accuracy is the priority. Prefer it over scatterplots and data tables for this clustering task.

## Why parallel coordinates help cluster judgments in multivariate data <!-- role: reason -->

Clustering in multivariate data requires integrating similarity across multiple attributes. Parallel coordinates provide a single integrated view where a record is a polyline across axes, supporting similarity judgments by comparing polyline proximity and shape across all dimensions at once.

**Mechanism:** A unified multi-axis representation reduces the need to mentally integrate clusters across multiple pairwise scatterplot panels and avoids the heavy serial comparison required by tables.

**Evidence:** For the clustering task, accuracy ranked parallel coordinates highest, followed by scatterplots, then data tables, with significant differences between each pair in the extracted results [@kanjanaboseMultitaskComparativeStudy2015]. This task-linked ranking is part of the collated graphical perception knowledge intended for visualization recommendation rules [@zengReviewCollationGraphical2023].

**Notes:** Response time for clustering did not distinguish parallel coordinates from scatterplots in the extracted ranking (they were grouped together as faster than tables).

## When clustering is the primary analysis task <!-- role: context -->

- **User Goal:** Identify which records form a coherent cluster based on similarity across multiple variables.
- **Task:** cluster.
- **Data:** Multivariate quantitative records where cluster structure depends on more than two variables.
- **Chart Setting:** Static view used for selecting or verifying a cluster membership answer.
- **Audience:** General audiences; may include users with limited prior exposure to parallel coordinates.
- **Success Criterion:** Higher clustering accuracy.

## When not to use parallel coordinates for clustering <!-- role: exceptions -->

**Break it when:** The task is exact value retrieval rather than clustering. **Why:** Tables were faster for value retrieval than both scatterplots and parallel coordinates in the same evidence base.

## Tradeoffs of parallel coordinates for clustering <!-- role: costs -->

**Sacrifice:** Parallel coordinates can be less familiar than scatterplots, which may increase initial learning effort.\
**Risk:** Users may misread polylines if visual clutter or crossings dominate the display.\
**Mitigation:** Keep the number of records and dimensions within a range where polylines remain distinguishable for the intended audience.

## Common failure modes in multivariate clustering views <!-- role: mistakes -->

**Mistake:** Using only a table for cluster identification in multivariate data. **Why it fails:** It performed worst in clustering accuracy compared with both scatterplots and parallel coordinates.

## Quick tests for choosing parallel coordinates <!-- role: check -->

**Failure Sign:** Users repeatedly switch between multiple scatterplot panels to decide cluster membership.\
**Quick Check:** If the cluster definition depends on 3+ variables at once, test parallel coordinates as the primary view.\
**Stronger Test:** Run a short task-based check: ask users to select cluster members and compare accuracy across candidate charts.

## What to do instead when parallel coordinates are not feasible <!-- role: fix -->

- Use scatterplots when you cannot deploy parallel coordinates and still need a visual clustering aid.
- Provide a table only as a supporting view for confirming exact values after clusters are identified.
- Reduce task scope by limiting the clustering decision to fewer variables if only scatterplots are available.
- Add clear visual identifiers for records so users can cross-reference selections across views more reliably.
