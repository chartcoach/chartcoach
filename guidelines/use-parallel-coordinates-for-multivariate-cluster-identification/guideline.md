---
id: use-parallel-coordinates-for-multivariate-cluster-identification
title: Use Parallel Coordinates to Identify Clusters in Multivariate Data
bibliography: references.bib
description: Prefer parallel coordinates over scatterplots or data tables for clustering
  tasks on multivariate datasets.
labels:
- chart:parallel-coordinates
- chart:scatter
- chart:table
- task:cluster
- visual:position
- impact:accuracy
- impact:speed
- data:multivariate
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use a parallel coordinates plot (PCP) instead of a scatterplot or a data table when the task is to identify clusters in multivariate data.

## The Logic <!-- role: reason -->

PCPs enable users to judge similarity across multiple variables by comparing polyline proximity across shared axes, which supports cluster identification more effectively than scanning cells in a table or reconciling multiple scatterplots.

- **The Principle:** Multivariate similarity is easier to assess via consistent cross-dimension traces than via repeated lookups or separate bivariate views.
- **The Evidence:** In a multi-task experiment comparing data tables, scatterplots, and PCPs, PCPs ranked best for clustering accuracy, ahead of scatterplots and then tables (PCP > SP > DT), with significant differences between all pairs for accuracy [@kanjanaboseMultitaskComparativeStudy2015]. This result is collated for visualization recommendation use in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Detect which points form a cluster (membership) in multivariate data.
- **Data Type:** Multivariate quantitative records (the study used 4 quantitative dimensions and 8 data points) displayed as table vs scatterplot vs PCP [@kanjanaboseMultitaskComparativeStudy2015].
- **Audience:** Analysts or general users doing exploratory multivariate clustering.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user’s goal is value retrieval (look up an exact value given another value).
- **Reason:** In the same experiment, value retrieval was not a strength for the visual representations relative to the table baseline [@kanjanaboseMultitaskComparativeStudy2015].

## The Price <!-- role: costs -->

- **The Sacrifice:** PCPs may not provide the fastest completion time advantage over scatterplots for clustering.
- **The Risk:** For clustering time, PCP and scatterplot were grouped together (similar), with both faster than tables; choosing PCP may not improve speed compared to scatterplots even if it improves accuracy [@kanjanaboseMultitaskComparativeStudy2015].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a data table because it “shows exact numbers,” even when the task is clustering.
- **Why it fails:** Table scanning does not support perceptual grouping across multiple dimensions as well as PCPs, and performed worst on clustering accuracy and time in the study [@kanjanaboseMultitaskComparativeStudy2015], as summarized in [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users repeatedly bounce between columns/plots and still disagree on which points belong together.
- **The Test:** Run a quick pilot: ask users to pick cluster membership; if many responses are incorrect or timeouts occur with a table/scatter approach, switch to PCP and re-test.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the multivariate table (or the row-of-scatterplots view) with a PCP for the clustering step.
- **Best Fix:** Use PCP as the primary view for cluster identification and reserve other representations for follow-on tasks (e.g., exact lookups).
