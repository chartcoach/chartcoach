---
id: prefer-grouped-color-layouts-for-target-search-in-high-density-grids-and-scatterplots
title: Group Same-Color Marks to Speed Up Target Search
bibliography: references.bib
description: When users must find a unique target among many marks, spatially grouping
  same-color marks reduces search time versus random color placement.
labels:
- chart:scatter
- chart:heatmap
- chart:waffle
- task:find-anomalies
- visual:color-hue
- visual:position
- impact:speed
- data:categorical
- audience:general
- design:layout
---

## The Rule <!-- role: advice -->

Spatially group marks by color (same-color marks adjacent) instead of randomly intermixing colors when the user needs to find a unique colored target.

## The Logic <!-- role: reason -->

Grouping by color reduces the amount of searching needed because similarly colored marks form larger coherent regions that are faster to scan than randomly distributed colors.

- **The Principle:** Perceptual grouping reduces visual search effort.
- **The Evidence:** Grouped color layouts produced faster target-search times than random layouts in both grid-like displays and scatterplot-like displays [@gramazioRelationVisualizationSize2014], as collated for visualization recommendation use [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly locate a single distinct item/target (“find anomalies” / find a unique mark).
- **Data Type:** Categorical color encoding (nominal color-hue) over many marks; high mark counts (e.g., ~196–484 marks tested).
- **Audience:** Any audience doing rapid scanning (novice or expert).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot rearrange mark positions without changing meaning (e.g., positions are fixed by data mapping).
- **Reason:** Grouping requires spatial reordering; if position encodes data, reordering can invalidate the visualization’s meaning.

## The Price <!-- role: costs -->

- **The Sacrifice:** You may have to change the layout/order of marks.
- **The Risk:** Grouping could conflict with other design constraints that depend on the original spatial arrangement.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keep colors random but increase the number of colors or tweak the palette.
- **Why it fails:** The measured performance difference was driven by layout (grouped vs random), not by adding more categorical variety within these tested conditions [@gramazioRelationVisualizationSize2014]; the collation emphasizes layout as the factor tied to speed here [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Same-color marks are scattered evenly across the view, producing a “confetti” look.
- **The Test:** Ask a user (or yourself) to point to the target color as fast as possible; if you must serially scan many marks, you likely need stronger grouping.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reorder marks (or bin into regions) so same-color items cluster spatially.
- **Best Fix:** Redesign the view so categorical groups occupy distinct regions (clear spatial clusters) while preserving the meaning of position for the task at hand [@gramazioRelationVisualizationSize2014; @zengReviewCollationGraphical2023].
