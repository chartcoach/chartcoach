---
id: use-line-charts-for-correlation-judgments-in-small-tabular-data
title: Use Line Charts for Correlation Judgments
bibliography: references.bib
description: For correlation tasks in small datasets, prefer line charts over bars,
  pies, and tables based on measured accuracy, time, and preference rankings.
labels:
- chart:line
- task:correlate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general-public
- source:empirical
---

## The Rule <!-- role: advice -->

Use a line chart when the user’s primary task is to judge correlation between two quantitative variables.

## The Logic <!-- role: reason -->

- **The Principle:** Correlation judgments can be supported by visually assessing overall trend structure across ordered x–y positions.
- **The Evidence:** Line-chart designs ranked highest for the **correlate** task by both **accuracy** and **time**, and also ranked highest in **user preference** compared with bar, pie, and table designs in the experiment [@saketTaskBasedEffectivenessBasic2019]. These results are part of the knowledge base collated for recommendation use [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Determine whether two quantitative attributes are strongly correlated.
- **Data Type:** Small datasets (5–34 marks) where the relationship can be shown as a 2D series of connected points (quantitative x and quantitative y).
- **Audience:** General public / mixed-expertise users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task requires precise reading of individual point values (not correlation).
- **Reason:** In the same experiment, line charts are not top-ranked for tasks emphasizing precise value identification (e.g., retrieve-value rankings favor table-like designs) [@saketTaskBasedEffectivenessBasic2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Using a line implies an ordering/continuity that may not be semantically meaningful for all quantitative x variables in a tabular dataset.
- **The Risk:** If users interpret the connection as a meaningful temporal or sequential process when none exists, they may over-trust trend continuity.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a table to “let users compute correlation themselves.”
- **Why it fails:** Tables were among the lowest-ranked designs for correlation in accuracy/time/preference in the experiment [@saketTaskBasedEffectivenessBasic2019], as recorded in the collation [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users stop to compute or compare many individual values rather than making a quick trend judgment.
- **The Test:** Ask users “Is the relationship strongly positive/negative?” If they respond by reading multiple exact values, your encoding may be working against the correlation task (consistent with the experiment’s low correlation performance for tables/pies) [@saketTaskBasedEffectivenessBasic2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch from table/pie/bar to a line chart with quantitative x–y position encodings.
- **Best Fix:** Ensure the correlation question is expressed over two quantitative attributes and render as a line chart (top-ranked for correlate by accuracy/time and preference) [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].
