---
id: use-parallel-coordinates-for-multivariate-anomaly-detection
title: Use Parallel Coordinates to Find Anomalies in Multivariate Data
bibliography: references.bib
description: Prefer parallel coordinates over scatterplots or data tables when detecting
  outliers/anomalies in multivariate datasets.
labels:
- chart:parallel-coordinates
- chart:scatter
- chart:table
- task:find-anomalies
- visual:position
- impact:accuracy
- impact:speed
- data:multivariate
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use a parallel coordinates plot (PCP) rather than a scatterplot or data table to detect anomalies/outliers in multivariate data.

## The Logic <!-- role: reason -->

Outliers in multivariate data can manifest as unusual patterns across multiple dimensions; PCPs make these deviations visible as polylines that diverge from the main bundle across axes, enabling faster and more accurate identification than scanning a table or reconciling multiple scatterplots.

- **The Principle:** Cross-dimension deviations are easier to spot as a holistic trace than as separate bivariate projections or raw cells.
- **The Evidence:** In the experiment, anomaly (outlier) detection accuracy ranked PCP > SP > DT, with significant differences across all pairs; completion time grouped PCP and SP together (faster than DT) [@kanjanaboseMultitaskComparativeStudy2015]. These outcomes are collated as recommendation-ready knowledge in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify 1–2 anomalous points/outliers in multivariate data.
- **Data Type:** Multivariate quantitative data (4 dimensions; 8 points) where outliers may be based on different value ranges or inconsistent relationships across dimensions [@kanjanaboseMultitaskComparativeStudy2015].
- **Audience:** Users performing exploratory analysis or QA on multivariate records.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary user goal is exact value lookup (retrieve a precise number given another).
- **Reason:** The same study indicates value retrieval is not where the visual representations excel relative to the table baseline [@kanjanaboseMultitaskComparativeStudy2015].

## The Price <!-- role: costs -->

- **The Sacrifice:** Switching to PCP may not reduce time compared to scatterplots for anomaly detection.
- **The Risk:** For time, PCP and scatterplot were in the same top group (PCP ≈ SP) and both were better than tables; you may gain accuracy without gaining speed over scatterplots [@kanjanaboseMultitaskComparativeStudy2015].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Defaulting to a data table for outlier detection because anomalies are “just extreme numbers.”
- **Why it fails:** Tables performed worst for anomaly detection accuracy and time, while PCP performed best, in the controlled study [@kanjanaboseMultitaskComparativeStudy2015], as captured in the collation [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users miss outliers unless they painstakingly inspect many cells or multiple plots.
- **The Test:** Time-box an outlier identification task; if users frequently time out or disagree, try the same task with a PCP and compare correctness rates.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap the table view to a PCP for the anomaly detection step.
- **Best Fix:** Use PCP as the default multivariate anomaly view; use other representations only after anomalies are flagged (e.g., for reporting exact values).
