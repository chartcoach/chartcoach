---
id: map-light-to-low-and-dark-to-high-in-sequential-scales
title: Map Low Values to Light Colors and High Values to Dark Colors
bibliography: references.bib
description: In sequential gradients, use light colors for low values and dark colors
  for high values to match reader expectations.
labels:
- chart:choropleth
- task:rank
- visual:color
- impact:interpretability
- data:quantitative
- audience:general
- scale:sequential
---

## The Rule <!-- role: advice -->

In sequential color gradients, assign low values to light colors and high values to dark colors.

## The Logic <!-- role: reason -->

Muth notes this mapping is most intuitive for most readers, reducing interpretation errors when scanning a gradient [@muth_colors_2018].

- **The Principle:** Match common perceptual expectations for magnitude.
- **The Evidence:** [@muth_colors_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify higher vs. lower values quickly on a gradient scale.
- **Data Type:** Quantitative data shown with a single-ended (sequential) gradient.
- **Audience:** General readers.

## When to Break It <!-- role: exceptions -->

- **Scenario:** None provided in the post.
- **Reason:** The post presents this as the intuitive default [@muth_colors_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less flexibility if you want a specific aesthetic or brand-driven direction.
- **The Risk:** If reversed, readers may systematically misread highs as lows (and vice versa) [@muth_colors_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using dark-to-light where dark implies “less” without explicitly justifying it.
- **Why it fails:** It conflicts with the intuitive mapping Muth recommends [@muth_colors_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** The map/chart “feels” inverted—dark areas appear like “more” but represent “less,” or vice versa.
- **The Test:** Confirm the legend runs from light (low) to dark (high) [@muth_colors_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reverse the gradient direction.
- **Best Fix:** Redesign the scale so lightness increases monotonically from low to high while preserving hue choices [@muth_colors_2018].
