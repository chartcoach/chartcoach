---
id: prefer-length-over-area-for-sorting-when-position-is-not-possible
title: Use length before area when sorting without shared position
bibliography: references.bib
description: If you cannot use a shared position scale for sorting, use length-based
  bars before area-based marks.
labels:
- chart:bar
- task:sort
- visual:length
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

If position-aligned comparisons are not possible for sorting, use length-based bars rather than area-based marks.

## The Logic <!-- role: reason -->

In the reported sort accuracy ranking, length-based bar designs appear above area-based designs, indicating better ordering performance than area (though still worse than top position-based conditions).

- **The Principle:** One-dimensional extent comparisons are more accurate for ordering than area comparisons.
- **The Evidence:** Length-based designs (E-4, E-5) rank above all area designs (E-8, E-9, E-7) for sort accuracy in the reported results [@heerCrowdsourcingGraphicalPerception2010]. This relationship is part of the collated guidelines dataset described in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Sort values, but the design cannot maintain the best position-aligned setup.
- **Data Type:** Quantitative values.
- **Audience:** General audiences in web/crowdsourced viewing contexts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must show hierarchical containment (a treemap-like requirement) and cannot switch chart families.
- **Reason:** The study evidence here only ranks accuracy for sorting judgments; it does not provide a hierarchy-task alternative that preserves containment semantics [@heerCrowdsourcingGraphicalPerception2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** Length encodings may require more space or a less compact layout than area-filling designs.
- **The Risk:** If length marks are arranged in a way that disrupts comparability (e.g., stacking segments), accuracy may still be worse than position-aligned designs (which rank higher) [@heerCrowdsourcingGraphicalPerception2010].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Replacing a bar chart with bubbles/treemap rectangles to keep a compact layout while still expecting accurate sorting.
- **Why it fails:** Area designs are ranked below the length designs for sort accuracy in the study results [@heerCrowdsourcingGraphicalPerception2010], as recorded in [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The ordering depends on comparing circle/rectangle areas rather than bar extents.
- **The Test:** Mock up an equivalent bar-length view; if users sort more accurately, your area encoding is likely the limiting factor (consistent with the ranking) [@zengReviewCollationGraphical2023; @heerCrowdsourcingGraphicalPerception2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch from area marks (bubbles/rectangles) to bars whose primary cue is length.
- **Best Fix:** Restructure to a position-aligned bar design when possible (top-ranked for sort accuracy), using the length-before-area fallback only when position alignment can’t be achieved [@heerCrowdsourcingGraphicalPerception2010; @zengReviewCollationGraphical2023].
