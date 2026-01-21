---
id: use-imprecise-encodings-when-aggregate-judgments-dominate
title: "Use \u201CImprecise\u201D Encodings When Aggregate Judgments Dominate"
bibliography: references.bib
description: When users judge averages, distributions, or ensembles, consider encodings
  (including color) that support these tasks even if individual values are less readable.
labels:
- task:summarize
- task:detect
- visual:color
- impact:clarity
- data:temporal
- audience:analyst
- source:bertini-why-not-scatterplots
---

## The Rule <!-- role: advice -->

If users mainly make aggregate/ensemble judgments (mean, range, clusters, outliers), choose encodings that support those judgments—even if they are less precise for reading individual values.

## The Logic <!-- role: reason -->

The paper highlights evidence that “aggregate” perception differs from individual value extraction, and that encodings traditionally considered imprecise for individual values (notably color) can offer performance benefits for ensemble tasks compared to purely positional encodings [@bertiniWhyShouldntAll2020].

- **The Principle:** Ensemble/aggregate perception
- **The Evidence:** [@bertiniWhyShouldntAll2020]

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating averages, ranges, variability, clusters, or spotting outliers in a field of many values.
- **Data Type:** Time series collections, matrices, or any many-mark display where summary perception matters more than exact lookup.
- **Audience:** Analysts and readers performing overview judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task requires extracting exact numeric values for specific items.
- **Reason:** The paper positions these encodings as beneficial specifically when aggregate judgments dominate, not as a replacement for precise read-off [@bertiniWhyShouldntAll2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced precision for any single value.
- **The Risk:** Users may attempt value lookup from an aggregate-oriented view and fail or misread [@bertiniWhyShouldntAll2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Rejecting heatmaps or color encodings categorically because they are low-ranked for individual value precision.
- **Why it fails:** The paper argues that this ranking does not generalize to ensemble tasks and can lead to worse task support [@bertiniWhyShouldntAll2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Users can’t answer “which year is higher on average?” without painstaking point-by-point reading.
- **The Test:** Ask an aggregate question (mean/range/outliers). If the design forces serial value extraction, it likely underserves ensemble perception [@bertiniWhyShouldntAll2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Provide an aggregate-oriented view (e.g., a field-like encoding) alongside the precise view.
- **Best Fix:** Make the primary view match the dominant aggregate task, as urged by the paper’s critique of precision-first defaults [@bertiniWhyShouldntAll2020].
