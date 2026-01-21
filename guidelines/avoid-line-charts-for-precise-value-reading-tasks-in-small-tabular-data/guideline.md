---
id: avoid-line-charts-for-precise-value-reading-tasks-in-small-tabular-data
title: Avoid Line Charts for Precise Value Reading Tasks
bibliography: references.bib
description: Line charts ranked poorly for tasks requiring precise reading (e.g.,
  retrieve-value and aggregate) compared with tables and bars in the experiment.
labels:
- chart:line
- task:retrieve-value
- task:aggregate
- visual:position
- impact:accuracy
- data:tabular
- audience:general-public
- source:empirical
---

## The Rule <!-- role: advice -->

Avoid line charts for tasks that require precise identification of individual values or computed totals from exact values.

## The Logic <!-- role: reason -->

- **The Principle:** When exact values matter, designs that present values discretely (e.g., in text cells) reduce ambiguity compared with reading along a continuous line path.
- **The Evidence:** In the experiment, line-chart designs ranked lowest for **retrieve-value** accuracy and lowest for **aggregate** accuracy compared with table and bar designs [@saketTaskBasedEffectivenessBasic2019]. These rankings are recorded as reusable guidance in the collation [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Read an exact value for a specific item (retrieve-value) or compute an aggregate/derived value from the displayed numbers (aggregate).
- **Data Type:** Small tabular datasets where exact reading is feasible (5–34 marks) and the question demands precision.
- **Audience:** General public / mixed-expertise users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary goal is correlation (trend judgment), not precision.
- **Reason:** Line charts ranked highest for correlate tasks in the same experiment [@saketTaskBasedEffectivenessBasic2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Avoiding line charts may reduce perceived “trend” readability for some audiences who expect a connected series.
- **The Risk:** Switching away from lines can make it harder to communicate continuity if that continuity is semantically important.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the line chart and relying on viewers to infer exact values from axis ticks.
- **Why it fails:** The empirical ranking indicates line designs underperform for precision-oriented tasks relative to table/bar designs [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users repeatedly move their gaze between the line and axes trying to interpolate values.
- **The Test:** Ask users to report a specific value quickly; if they require repeated interpolation steps, the line chart is likely mismatched for the task (consistent with the study’s retrieve/aggregate rankings) [@saketTaskBasedEffectivenessBasic2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the line chart with a table for exact lookup, or a bar chart for reading magnitudes by length.
- **Best Fix:** Use a table as the primary view for retrieve-value and (in this experiment) for aggregate tasks, matching the top-ranked designs for those tasks [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].
