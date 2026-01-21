---
id: include-fixed-background-and-foreground-colors-in-categorical-optimization
title: Include Fixed Background and Foreground Colors in Categorical Palette Optimization
bibliography: references.bib
description: Treat background/foreground colors as fixed constraints during categorical
  palette optimization to ensure separation against the canvas and labels.
labels:
- chart:generic
- task:distinguish
- visual:color-hue
- impact:clarity
- data:categorical
- audience:general
- constraint:background
---

## The Rule <!-- role: advice -->

When optimizing a categorical palette, include any fixed **background and foreground** colors as constraints and optimize category colors against them as well as against each other.

## The Logic <!-- role: reason -->

Category colors must be distinguishable not only from each other but also from the canvas and common foreground elements; otherwise a “distinct” palette can still fail due to poor contrast against the background.

- **The Principle:** Context-aware separability (optimize in the full color set that appears together)
- **The Evidence:** The method explicitly supports “Fixed Colors” constraints (background/foreground) and shows that optimizing with a fixed white background produces noticeably different results and can converge more quickly, shifting colors to increase separation from both the background and other colors [@fangCategoricalColormapOptimization2017]. This operational constraint knowledge is part of what the collation paper aims to capture for recommendation systems [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Make colored categories readable on a known canvas (e.g., white background) and alongside typical label/line colors.
- **Data Type:** Nominal categories encoded with distinct colors.
- **Audience:** Any; especially dashboard/report contexts with fixed themes.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The background is unknown or changes dynamically across deployments.
- **Reason:** You cannot optimize “against” a background you can’t specify; a palette optimized for one background may not be optimal for another [@fangCategoricalColormapOptimization2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** Reduced freedom for the optimizer; some category-color separations may decrease to ensure separability against background/foreground.
- **The Risk:** Overfitting to a specific background can reduce robustness across other themes or display contexts [@fangCategoricalColormapOptimization2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Optimizing only category-to-category distances and ignoring the background/foreground.
- **Why it fails:** Colors that are well-separated from each other can still be too light/dark or too close to the background/labels, reducing visibility [@fangCategoricalColormapOptimization2017].

## How to Check <!-- role: check -->

- **Visual Sign:** One or more categories “wash out” into the background or compete with foreground elements.
- **The Test:** Add the background (and any fixed label/line color) into the set of colors considered during evaluation and see if any pairwise distances are small relative to others [@fangCategoricalColormapOptimization2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Re-run optimization including the background color as a fixed color.
- **Best Fix:** Model both background and foreground as fixed constraints and optimize the palette in that combined set, aligning with how perceptual knowledge is meant to be translated into actionable constraints [@zengReviewCollationGraphical2023; @fangCategoricalColormapOptimization2017].
