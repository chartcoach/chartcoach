---
id: check-colormap-legend-based-order-with-minimum-speed
title: Check Legend-Based Colormap Order via Minimum Speed
bibliography: references.bib
description: Verify that a continuous colormap remains orderable (with a legend) by
  ensuring its minimum local/global speed is greater than zero.
labels:
- chart:colormap
- task:validate
- visual:color
- impact:clarity
- data:quantitative
- audience:expert
- scope:continuous-colormap
---

## The Rule <!-- role: advice -->

To ensure legend-based order in a continuous colormap, require **minimum local speed > 0** for local legend-based order and **minimum global speed > 0** for global legend-based order.

## The Logic <!-- role: reason -->

- **The Principle:** Legend-based order corresponds to invertibility: if two distinct values can map to the same (or indistinguishably close) color, users cannot reliably order them even with a legend. Minimum speed detects these collapses.
- **The Evidence:** The framework links legend-based order to (local/global) invertibility and evaluates it using minimum local/global speed, where zero indicates failure (non-invertibility) [@bujackGoodBadUgly2018]. This type of theoretical rule is part of the collated knowledge for recommendation systems [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Being able to read/order values using the legend (not necessarily intuitively without it).
- **Data Type:** Quantitative data encoded by a continuous colormap.
- **Audience:** Designers and automated systems that must reject colormaps with “flat” segments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intentionally want a flat region (multiple values mapping to the same color) as part of the design.
- **Reason:** The framework treats this as a failure of invertibility/order (minimum speed becomes 0), so it violates legend-based order by definition [@bujackGoodBadUgly2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may exclude colormaps that are acceptable for some specialized purposes but contain deliberate plateaus.
- **The Risk:** If sampling is too coarse, you may miss very small flat regions or over/underestimate the minimum speed [@bujackGoodBadUgly2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Only checking whether endpoints differ (start color ≠ end color).
- **Why it fails:** Global legend-based order requires all colors to be mutually distinct (injective); local order requires adjacent steps not to collapse—endpoint checks miss interior collapses [@bujackGoodBadUgly2018].

## How to Check <!-- role: check -->

- **Visual Sign:** A segment of the gradient looks unchanged (“stuck”) across a portion of the legend.
- **The Test:** Compute minimum local speed and minimum global speed; if either is 0, the corresponding legend-based order fails [@bujackGoodBadUgly2018; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the colormap with one whose minimum speeds are non-zero under the same metric and sampling.
- **Best Fix:** Add minimum-speed constraints to your colormap selection/recommendation rules to automatically filter non-invertible continuous colormaps [@zengReviewCollationGraphical2023; @bujackGoodBadUgly2018].
