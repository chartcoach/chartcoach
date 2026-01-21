---
id: avoid-tables-for-correlation-tasks-in-small-tabular-data
title: Avoid Tables for Correlation Tasks
bibliography: references.bib
description: Tables performed poorly for correlation tasks relative to line and scatter
  designs in accuracy, time, and preference rankings.
labels:
- chart:table
- task:correlate
- visual:text
- impact:efficiency
- data:tabular
- audience:general-public
- source:empirical
---

## The Rule <!-- role: advice -->

Do not use a table as the primary view when the task is to judge correlation.

## The Logic <!-- role: reason -->

- **The Principle:** Correlation judgments require perceiving a global relational pattern; text grids force serial reading and mental integration.
- **The Evidence:** In the experiment, table designs were ranked lowest for the **correlate** task across **accuracy/time** and were least preferred relative to line (and other) designs [@saketTaskBasedEffectivenessBasic2019]. This evidence is part of the collated knowledge for visualization recommendation [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly decide if there is a strong correlation (positive/negative).
- **Data Type:** Two quantitative attributes drawn from a small dataset.
- **Audience:** General public / mixed-expertise users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The real user goal is to retrieve exact values for specific records, not to judge correlation.
- **Reason:** The evidence is specific to correlation tasks and does not claim tables are ineffective for precise lookup tasks [@saketTaskBasedEffectivenessBasic2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to reduce detail-on-demand (exact values in every cell) in the primary view.
- **The Risk:** Some users may distrust the chart without seeing raw numbers.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the table and adding a written “correlation” annotation computed by the designer.
- **Why it fails:** The guideline is about supporting user perception of correlation through visualization; the study’s results show tables themselves do not support the correlate task well compared to line/scatter designs [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users scroll/scan rows and columns to compare many pairs manually.
- **The Test:** If users need to compute trends by reading multiple cells, the table is acting against correlation perception (mirroring the experiment’s low table ranking for correlate) [@saketTaskBasedEffectivenessBasic2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a line chart (or scatterplot) as the primary correlation view.
- **Best Fix:** Replace the table-first design with a line chart for correlation judgments and keep the table only as a secondary lookup view (consistent with the study’s correlation rankings) [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].
