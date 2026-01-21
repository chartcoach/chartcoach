---
id: prefer-dorling-cartograms-for-aggregate-accuracy
title: Prefer Dorling Cartograms for Accurate Aggregation
bibliography: references.bib
description: For aggregate judgments, Dorling cartograms produced higher accuracy
  than non-contiguous, contiguous, and rectangular cartograms in the reported results.
labels:
- chart:cartogram
- task:aggregate
- visual:area
- visual:position
- impact:accuracy
- data:geospatial
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use a **Dorling cartogram** when the user’s goal is to make an **aggregate** judgment (aggregate task) as accurately as possible.

## The Logic <!-- role: reason -->

Aggregate judgments (as represented in the dataset) benefit from the cartogram type that minimizes aggregate-task errors; Dorling ranks highest in the reported accuracy ordering.

- **The Principle:** Match cartogram type to the task’s empirically best-performing design.
- **The Evidence:** For the aggregate task, accuracy rank is **E-4 (Dorling) > E-3 (non-contiguous) > E-1 (contiguous) > E-2 (rectangular)**, with at least Dorling and non-contiguous significantly better than rectangular (pairs include E-4 > E-2 and E-3 > E-2) [@nusratEvaluatingCartogramEffectiveness2018]. This rule is produced in the spirit of turning collated study outcomes into actionable guidance [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Make an aggregate judgment over regions (aggregate task as captured in the evidence).
- **Data Type:** Geo regions with quantitative values encoded via area; geographic placement via position.
- **Audience:** General audiences summarizing overall magnitude.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is primarily sorting, filtering, or correlation, where Dorling may not be top-ranked in accuracy for those tasks.
- **Reason:** The same evidence base reports different rankings for other tasks, so optimizing for aggregate accuracy can reduce performance elsewhere [@nusratEvaluatingCartogramEffectiveness2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose accuracy for tasks where contiguous ranks highest (e.g., some filtering/correlation entries).
- **The Risk:** A single cartogram type may not serve mixed-task dashboards well without task-aware switching.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using **rectangular cartograms** for aggregation because they are easy to tile/fit.
- **Why it fails:** Rectangular cartograms are the lowest-ranked design for aggregate accuracy in the reported aggregate ranking [@nusratEvaluatingCartogramEffectiveness2018], a mismatch that the collation process aims to prevent [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users’ aggregate answers are frequently wrong or inconsistent.
- **The Test:** Compare aggregate-task accuracy on Dorling vs. contiguous vs. rectangular using the same prompt set.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch the aggregation view to a **Dorling cartogram**.
- **Best Fix:** Implement a task selector (aggregate vs. filter/sort/correlate) and swap cartogram type accordingly, guided by the collated rankings approach in [@zengReviewCollationGraphical2023; @nusratEvaluatingCartogramEffectiveness2018].
