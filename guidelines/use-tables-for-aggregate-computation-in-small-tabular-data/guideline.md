---
id: use-tables-for-aggregate-computation-in-small-tabular-data
title: Use Tables for Aggregate Computation
bibliography: references.bib
description: For computing aggregate/derived values from small datasets, tables ranked
  highest across accuracy, time, and user preference in the experiment.
labels:
- chart:table
- task:aggregate
- visual:text
- impact:accuracy
- data:tabular
- audience:general-public
- source:empirical
---

## The Rule <!-- role: advice -->

Use a table when the task is to compute an aggregate/derived value from the displayed items.

## The Logic <!-- role: reason -->

- **The Principle:** Aggregation from displayed values is easier when values are directly readable rather than estimated from marks.
- **The Evidence:** For the **aggregate** task, table designs ranked highest in **accuracy**, ranked fastest in **time**, and ranked highest in **user preference** relative to bar, pie, scatter, and line designs [@saketTaskBasedEffectivenessBasic2019]. This outcome is part of the collated guidance for recommendation systems [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Compute/compare aggregate values (e.g., sum across categories) from the shown numbers.
- **Data Type:** Small tabular datasets (5–34 marks/entries per view as in the study).
- **Audience:** General public / mixed-expertise users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The aggregate task is intended to be perceptual (e.g., “which group is larger overall?”) rather than numeric computation.
- **Reason:** The evidence is for computation of derived values as operationalized in the experiment, not for all possible “aggregate-like” questions [@saketTaskBasedEffectivenessBasic2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less immediate visual summarization than charts.
- **The Risk:** Users may experience higher cognitive load if many values must be combined without calculator support.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a line chart and expecting users to add/interpolate values from the axis.
- **Why it fails:** Line designs were lowest-ranked for aggregate accuracy and time compared with table designs in the experiment [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users pause to estimate values from marks before doing arithmetic.
- **The Test:** If users cannot state the addends confidently before summing, switch to a representation that shows the numbers directly (as in the table condition that ranked highest) [@saketTaskBasedEffectivenessBasic2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide a table with the relevant values visible for the rows/columns being aggregated.
- **Best Fix:** Use a table as the primary view for aggregate computation and optionally add a chart only as a secondary summary, following the experiment’s top-ranked design for aggregate tasks [@saketTaskBasedEffectivenessBasic2019; @zengReviewCollationGraphical2023].
