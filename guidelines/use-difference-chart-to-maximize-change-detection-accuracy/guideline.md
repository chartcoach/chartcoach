---
id: use-difference-chart-to-maximize-change-detection-accuracy
title: Use a difference chart to maximize accuracy for finding the maximum absolute
  change
bibliography: references.bib
description: To identify the category with the largest absolute change between two
  series, a difference chart is the most accurate design among the tested variants.
labels:
- chart:bar
- task:aggregate
- visual:position
- impact:accuracy
- data:categorical
- audience:general
- comparison:multi-series
- derived:difference
---

## The Rule <!-- role: advice -->

When users must identify the category with the **largest absolute change** between two series, use a **difference chart**.

## The Logic <!-- role: reason -->

A difference chart directly encodes the derived differences, supporting more accurate comparisons than making users compare bar pairs.

- **The Principle:** Explicitly encode the derived comparison target (difference) for fastest/most accurate change judgments.
- **The Evidence:** For the “maximum absolute change” task, accuracy ranks **Difference chart (E-2) > SB+D (E-4) > GB+D (E-3) > GB (E-1)**, with significant pairs indicating multiple designs outperform the plain grouped bar chart and the difference chart at the top of the ranking [@srinivasanWhatsDifferenceEvaluating2018]. This ranking is part of the structured collation described in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Identify which category changed the most (largest absolute difference across two series).
- **Data Type:** Two-series categorical/ordinal data where derived change is meaningful.
- **Audience:** Dashboard users doing quick “what changed most?” checks.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users also need to read the original values in either series within the same chart.
- **Reason:** The difference chart design shown in the extracted designs encodes differences (derived values) rather than both original series’ values, so it may not meet a “read raw values” need [@srinivasanWhatsDifferenceEvaluating2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Loss of direct access to original series values within the same view.
- **The Risk:** Viewers may lack context for whether a large difference is large relative to the absolute baseline.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a grouped bar chart and expecting viewers to mentally compute differences reliably.
- **Why it fails:** The plain grouped bar chart is ranked worst for accuracy for maximum-change identification in the reported results [@srinivasanWhatsDifferenceEvaluating2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers misidentify the “biggest change” category or take too long comparing pairs.
- **The Test:** Ask “Which category changed most?”; if the answer varies across viewers on a grouped bar chart, try a difference chart.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the grouped bar chart with a difference chart for this specific task view.
- **Best Fix:** Offer a difference chart as the default for “maximum change” tasks and provide a separate view (or toggle) for raw values if needed [@srinivasanWhatsDifferenceEvaluating2018; @zengReviewCollationGraphical2023].
