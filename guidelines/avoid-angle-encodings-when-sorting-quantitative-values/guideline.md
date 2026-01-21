---
id: avoid-angle-encodings-when-sorting-quantitative-values
title: Avoid Angle Encodings When Sorting Quantitative Values
bibliography: references.bib
description: For sorting, do not use pie-slice angle judgments when a position-on-scale
  alternative is available.
labels:
- chart:pie
- chart:bar
- task:sort
- visual:angle
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception
---

## The Rule <!-- role: advice -->

Do not use **angle** judgments (e.g., pie slice angles) for sorting quantitative values when you can use **position on a common scale** (e.g., an aligned bar/dot chart).

## The Logic <!-- role: reason -->

In the reported sorting comparison, the position-based chart outperforms the angle-based chart, with a significant difference reported between the two designs [@clevelandGraphicalPerceptionTheory1984]. The review collates this as evidence supporting position channels as top choices for quantitative judgment tasks [@zengReviewCollationGraphical2023].

- **The Principle:** Angle judgments yield less accurate quantitative comparisons than position on a shared scale.
- **The Evidence:** Sorting results show a significant advantage for the position-based design over the angle-based design [@clevelandGraphicalPerceptionTheory1984], summarized and collated in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Rank/sort items by value (e.g., ordering categories).
- **Data Type:** Quantitative comparisons across categories.
- **Audience:** General audiences performing quick analytic comparisons.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are not asking users to sort; you are presenting a simple categorical breakdown and sorting is irrelevant to the task.
- **Reason:** The evidence cited is specifically for sorting accuracy, not for all possible pie-chart uses [@clevelandGraphicalPerceptionTheory1984; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Switching away from angle encodings may reduce the immediate “part-of-whole” visual metaphor.
- **The Risk:** A bar/dot alternative may require more space than a compact pie.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping a pie chart and adding labels, assuming labeling eliminates the need for angle judgment in sorting.
- **Why it fails:** The underlying perceptual comparison the chart invites is still angle-based; the experiment’s comparison is about judgment performance between encodings [@clevelandGraphicalPerceptionTheory1984; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users must compare wedge sizes/angles to decide order.
- **The Test:** If you removed the numeric labels, would the viewer still be sorting by wedge angle? If yes, you’re relying on angle judgments.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the pie with an aligned bar chart for sorting.
- **Best Fix:** Use a position-on-common-scale design (dot plot or aligned bars) and explicitly order the marks to match the sorting task [@clevelandGraphicalPerceptionTheory1984; @zengReviewCollationGraphical2023].
