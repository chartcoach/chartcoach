---
id: use-two-hues-to-improve-gradient-discrimination
title: Use Two (or Three) Hues in Gradients to Improve Discrimination
bibliography: references.bib
description: Combine lightness with two or three carefully chosen hues so readers
  can distinguish steps in a gradient more easily.
labels:
- chart:choropleth
- task:distinguish
- visual:color
- impact:clarity
- data:quantitative
- audience:general
- scale:sequential
---

## The Rule <!-- role: advice -->

For sequential gradients, consider using two (or three) carefully selected hues in addition to lightness to make steps easier to distinguish.

## The Logic <!-- role: reason -->

Muth notes readers can better differentiate colors along a gradient when encoding uses both lightness and a small number of hues, improving decipherability [@muth_colors_2018].

- **The Principle:** Redundant encoding (lightness + limited hue change) improves discriminability.
- **The Evidence:** [@muth_colors_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Distinguish adjacent value ranges more easily on a gradient.
- **Data Type:** Quantitative data shown with a sequential gradient (often maps).
- **Audience:** General readers interpreting many small regions/areas.

## When to Break It <!-- role: exceptions -->

- **Scenario:** A single-hue lightness gradient is already sufficiently distinguishable for the number of steps shown.
- **Reason:** Adding hues can be unnecessary complexity if discrimination is already adequate [@muth_colors_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** More palette design work and a higher chance of unintended perceptual artifacts if hues are poorly chosen.
- **The Risk:** Too many hue changes can reintroduce confusion that Muth cautions against for complex gradients [@muth_colors_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding many hues across the scale to “help distinction.”
- **Why it fails:** Excessive hue variation can confuse ordering rather than clarify it [@muth_colors_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Neighboring regions with slightly different values look nearly identical.
- **The Test:** Pick several adjacent bins/values and verify they are visually separable without relying heavily on the legend [@muth_colors_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of steps/bins so each step has more perceptual distance.
- **Best Fix:** Redesign the gradient to use lightness plus two or three hues that change smoothly across the scale [@muth_colors_2018].
