---
id: prefer-parallel-coordinates-over-scatter-and-tables-for-multivariate-change-detection
title: Use Parallel Coordinates to Detect Changes Across Ordered Multivariate Dimensions
bibliography: references.bib
description: Prefer parallel coordinates for change detection across ordered dimensions
  compared with scatterplots or data tables.
labels:
- chart:parallel-coordinates
- chart:scatter
- chart:table
- task:correlate
- task:trend
- task:change-detection
- visual:position
- impact:accuracy
- impact:speed
- data:multivariate
- data:ordered
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use a parallel coordinates plot (PCP) to identify which records change the most across an ordered set of dimensions, instead of using a scatterplot-based view or a data table.

## The Logic <!-- role: reason -->

A PCP represents each record as a single polyline across ordered axes, making within-record variation across dimensions directly observable without repeatedly re-identifying the same record across multiple bivariate plots or scanning across columns in a table.

- **The Principle:** A single continuous trace across ordered axes supports judging within-item change across dimensions.
- **The Evidence:** In the experiment’s “change detection” task (ordered axes like Q1–Q4), PCPs outperformed scatterplots and tables on both accuracy and response time overall (PCP > SP > DT for time; accuracy favored PCP over both) [@kanjanaboseMultitaskComparativeStudy2015]. This ranking is part of the collated knowledge base for recommendation in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Find which 1–2 data points exhibit the most change across ordered variables.
- **Data Type:** Multivariate quantitative data with an explicit order on dimensions (e.g., sequential quarters), as used in the study [@kanjanaboseMultitaskComparativeStudy2015].
- **Audience:** Users monitoring change patterns across multiple measures.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is exact value retrieval between two variables.
- **Reason:** The study suggests tables are better suited for value retrieval (especially in response time), while PCP/SP did not show strong advantages for that task [@kanjanaboseMultitaskComparativeStudy2015].

## The Price <!-- role: costs -->

- **The Sacrifice:** PCP introduces a less familiar representation for some users.
- **The Risk:** Users unfamiliar with PCP may need onboarding; the study notes PCP is often perceived as less intuitive, even though performance favored it for these tasks [@kanjanaboseMultitaskComparativeStudy2015].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using multiple scatterplots and trying to “track” the same point across them to infer change.
- **Why it fails:** This forces repeated identification and cross-panel matching; PCP encodes all dimensions per record in one trace and performed better in accuracy and time for change detection in the experiment [@kanjanaboseMultitaskComparativeStudy2015], as collated in [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users lose track of which marks correspond to the same record across plots and make inconsistent “most changed” selections.
- **The Test:** Ask users to identify the most-changing record within a fixed time limit; if error rates are high with scatter/table, test PCP on the same question set.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the multi-scatter view with a PCP when the goal is change detection across ordered dimensions.
- **Best Fix:** Use PCP as the primary change-detection view and keep tables available only for follow-up confirmation of exact values.
