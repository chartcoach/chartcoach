---
id: increase-color-separation-for-small-distant-marks
title: Use Stronger Color Separation for Small or Distant Marks
bibliography: references.bib
description: Make small points and thin lines more distinguishable by increasing hue
  or brightness contrast, especially when separated by distance.
labels:
- chart:scatter
- task:distinguish
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- mark:points-lines
---

## The Rule <!-- role: advice -->

When marks are small (points/lines) or far apart, increase their hue or brightness contrast; use more toned-down colors for large areas.

## The Logic <!-- role: reason -->

Muth notes that comparison becomes harder as areas get smaller and distance increases; stronger color contrast helps small marks remain distinguishable, while large areas can tolerate lower contrast without confusion [@muth_colors_2018].

- **The Principle:** Discriminability depends on mark size and adjacency.
- **The Evidence:** [@muth_colors_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Tell series/categories apart quickly.
- **Data Type:** Multi-series line charts, scatter plots, or any chart with small marks.
- **Audience:** Readers viewing on typical screens (not zoomed in).

## When to Break It <!-- role: exceptions -->

- **Scenario:** Large, adjacent areas (e.g., stacked/filled regions) where subtle differences are sufficient.
- **Reason:** Muth suggests big areas can handle toned-down colors with little contrast, especially without intervening background colors [@muth_colors_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Higher-contrast palettes can look more “colorful” and less subdued.
- **The Risk:** Over-contrasting many series can create visual noise [@muth_colors_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using similarly light/dark shades for multiple thin lines because it feels cohesive.
- **Why it fails:** Lines/points become hard to distinguish at normal viewing size [@muth_colors_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Lines/points blend together unless the reader zooms in or traces carefully.
- **The Test:** View the chart at intended display size; if you can’t reliably differentiate series without effort, contrast separation is too low [@muth_colors_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase brightness (lightness) differences between series colors.
- **Best Fix:** Redesign the palette so small marks differ clearly in hue and/or brightness, while keeping large-area fills more muted [@muth_colors_2018].
