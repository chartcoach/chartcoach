---
id: use-scatterplots-for-finding-anomalies-in-small-tabular-data
title: Use Scatterplots for Finding Anomalies
bibliography: references.bib
description: For anomaly-finding tasks in small tabular datasets, prefer scatterplots
  over bars, lines, tables, and pies based on measured accuracy and preference.
labels:
- chart:scatter
- task:find-anomalies
- visual:position
- impact:accuracy
- data:quantitative
- audience:general-public
- source:empirical
---

## The Rule <!-- role: advice -->

Use a scatterplot when the user’s task is to find anomalies.

## The Logic <!-- role: reason -->

- **The Principle:** Anomaly detection benefits from spatial position encodings that make outliers visually distinct from the rest of the marks.
- **The Evidence:** In the collated study results, scatterplot designs ranked highest for anomaly tasks by **accuracy** and **user preference** relative to bar, line, table, and pie designs [@saketTaskBasedEffectivenessBasic2019]. This study is included as structured evidence for recommendation in the collation work [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify outliers / anomalies in the data.
- **Data Type:** Small tabular datasets (the study used 5–34 marks per view) with quantitative relationships (including quantitative–quantitative and categorical–quantitative pairings rendered as points).
- **Audience:** General public / mixed-expertise users (crowdsourced participants).

## When to Break It <!-- role: exceptions -->

- **Scenario:** The anomaly is defined as “an unusual category proportion” rather than an unusual numeric relationship.
- **Reason:** The evidence here is task-based and does not establish scatterplots as best for proportion-based anomaly definitions; it only supports anomaly finding as operationalized in the experiment [@saketTaskBasedEffectivenessBasic2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose the directness of exact numeric lookup compared with a table.
- **The Risk:** If anomalies depend on precise values rather than visual deviation, users may still need labels or a different representation.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a pie chart to “spot the odd slice” for anomaly finding.
- **Why it fails:** In the experiment’s anomaly task, pie designs were lowest-ranked by accuracy and preference compared with scatterplots [@saketTaskBasedEffectivenessBasic2019], as recorded in the collation [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users must scan labels/legends to decide what is “weird,” rather than seeing it immediately as a spatial outlier.
- **The Test:** Ask a user to point to the anomaly in under ~5 seconds; if they must compute from text, the chart is likely mis-specified for this task (per the study’s relative performance patterns) [@saketTaskBasedEffectivenessBasic2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch from pie/line/table to a scatterplot with point marks using x–y position encodings.
- **Best Fix:** Re-express the anomaly definition in the same two quantitative dimensions and use a scatterplot so anomalous points separate spatially (aligned with the study’s top-ranked designs) [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].
