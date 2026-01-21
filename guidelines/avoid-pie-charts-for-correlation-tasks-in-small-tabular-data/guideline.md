---
id: avoid-pie-charts-for-correlation-tasks-in-small-tabular-data
title: Avoid Pie Charts for Correlation Tasks
bibliography: references.bib
description: Do not use pie charts to support correlation judgments; they ranked worst
  for correlation performance and preference in the study.
labels:
- chart:pie
- task:correlate
- visual:angle
- impact:accuracy
- data:quantitative
- audience:general-public
- source:empirical
---

## The Rule <!-- role: advice -->

Do not use a pie chart when the user’s task is to judge correlation.

## The Logic <!-- role: reason -->

- **The Principle:** Correlation requires judging relationships between two variables; angle-based part-to-whole encodings do not provide a clear relational structure for that judgment.
- **The Evidence:** Pie-chart designs were ranked at the bottom for the **correlate** task in **accuracy**, **time**, and **user preference** relative to the other tested visualization types [@saketTaskBasedEffectivenessBasic2019], and these findings are incorporated into the collation for recommendation contexts [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide whether two attributes increase/decrease together (strong correlation).
- **Data Type:** Small tabular datasets where users would otherwise be tempted to show category shares.
- **Audience:** General public / mixed-expertise users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The “correlation” question is actually a part-to-whole question (e.g., composition comparisons), not a relationship between two quantitative variables.
- **Reason:** The evidence here is explicitly about correlation tasks; it does not claim pies are always bad, only that they were poor for correlation in this experiment [@saketTaskBasedEffectivenessBasic2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** You lose a familiar part-to-whole look that some stakeholders expect.
- **The Risk:** Switching chart types may require rethinking the question (from composition to relationship).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encoding the “second variable” in pie slice color while keeping slice angle as the first.
- **Why it fails:** In the study’s pie designs, adding categorical color did not make pies competitive for correlation judgments; they still ranked lowest for correlation [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The viewer cannot point to an overall upward/downward relationship because slices do not form an ordered relational pattern.
- **The Test:** Ask users to describe the relationship direction without reading numeric labels; if they cannot, the pie is not supporting correlation (consistent with the experiment’s outcomes) [@saketTaskBasedEffectivenessBasic2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the pie chart with a line chart (or scatterplot) using x–y position encodings for the two quantitative variables.
- **Best Fix:** Re-map the two variables onto x and y position so correlation can be judged spatially, aligning with top-ranked designs for correlate in the study [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].
