---
id: prefer-position-aligned-bars-over-length-angle-and-area-encodings-for-sorting
title: Use position-aligned bars for sorting tasks
bibliography: references.bib
description: For sorting judgments, prioritize position-aligned bar comparisons over
  length, angle, and area encodings.
labels:
- chart:bar
- task:sort
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use position-aligned bar comparisons (bars that share a common baseline/scale) when users need to sort values.

## The Logic <!-- role: reason -->

Position along a common scale enables more accurate proportional judgments than alternatives like length (stacked segments), angle (pie slices), and area (circles/rectangles/treemaps) for sorting-style judgments.

- **The Principle:** Position on a common scale supports more precise ordering.
- **The Evidence:** The accuracy ranking for a sort task places position-based conditions first (E-1, E-2, E-3) ahead of length (E-4, E-5), angle (E-6), and area-based designs (E-8, E-9, E-7) in crowdsourced experiments [@heerCrowdsourcingGraphicalPerception2010]. This result is included as collated knowledge for recommendation in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Sort/order values by magnitude (rank items).
- **Data Type:** Quantitative values that must be ordered.
- **Audience:** General audiences (including crowdsourced/online viewers).

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot allocate enough horizontal space for a position-aligned bar chart (e.g., extreme layout constraints).
- **Reason:** The rule assumes you can present a shared scale; if you cannot, you may be forced into alternative encodings despite expected accuracy loss [@heerCrowdsourcingGraphicalPerception2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires a shared axis and sufficient space to place comparable marks.
- **The Risk:** If the shared scale is not visually clear, users may not get the benefit of position-based ordering.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to a pie chart (angle) or bubble/treemap (area) to “save space” while still expecting accurate sorting.
- **Why it fails:** These encodings rank below position-based approaches for sort accuracy in the reported results [@heerCrowdsourcingGraphicalPerception2010], as collated in [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users must compare slice angles or areas to determine order.
- **The Test:** Ask a reviewer to rank 5–10 items quickly; if they hesitate or misorder items, you likely left the position-aligned regime (consistent with the lower-ranked encodings) [@heerCrowdsourcingGraphicalPerception2010].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Convert the design to bars that share a common baseline/axis (a position-aligned comparison).
- **Best Fix:** Use the highest-ranked position-based arrangement for the comparison you need (choose a design that keeps the compared values aligned to the same scale), consistent with the top-ranked position conditions reported [@heerCrowdsourcingGraphicalPerception2010] and surfaced for recommendation in [@zengReviewCollationGraphical2023].
