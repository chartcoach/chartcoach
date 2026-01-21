---
id: use-tables-for-retrieve-value-in-small-tabular-data
title: Use Tables for Retrieve-Value Questions
bibliography: references.bib
description: For exact value lookup in small datasets, tables ranked highest in accuracy,
  time, and user preference among the tested visualizations.
labels:
- chart:table
- task:retrieve-value
- visual:text
- impact:accuracy
- data:tabular
- audience:general-public
- source:empirical
---

## The Rule <!-- role: advice -->

Use a table when the user needs to retrieve exact values.

## The Logic <!-- role: reason -->

- **The Principle:** Direct text presentation supports exact lookup without perceptual estimation.
- **The Evidence:** For **retrieve-value**, table designs ranked highest in **accuracy**, highest in **time performance** (fastest), and highest in **user preference** relative to bar, pie, scatter, and line designs in the experiment [@saketTaskBasedEffectivenessBasic2019]. This task-specific ranking is captured for recommendation in the collation [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify the value of a specified attribute for given items.
- **Data Type:** Small tabular datasets (5–34 displayed entries/marks as summarized in the study conditions).
- **Audience:** General public / mixed-expertise users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user goal is to judge correlation or detect global patterns (not look up exact values).
- **Reason:** The same study shows tables are low-ranked for correlation tasks [@saketTaskBasedEffectivenessBasic2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Tables provide weaker support for rapid pattern recognition compared to spatial encodings.
- **The Risk:** Users may miss outliers or trends unless they compute them manually.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a line chart because it “looks analytical,” even when the task is exact value lookup.
- **Why it fails:** Line designs ranked lowest for retrieve-value in the experiment [@saketTaskBasedEffectivenessBasic2019], as recorded in the collation [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users ask “what exactly is that value?” or need to estimate from axes/marks.
- **The Test:** If the question has a single correct numeric answer and users must estimate visually, prefer a table (supported by the study’s retrieve-value rankings) [@saketTaskBasedEffectivenessBasic2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide a table view for the relevant attributes and sort/filter to the requested item(s).
- **Best Fix:** Make the table the primary view for retrieve-value tasks and keep charts as optional summaries, consistent with the experiment’s best-performing design for retrieve-value [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].
