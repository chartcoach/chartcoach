---
id: do-not-use-sequential-gradients-for-categories
title: Do Not Use Gradient Palettes for Categories
bibliography: references.bib
description: Use distinct hues for categories; sequential shades imply ordering and
  can mislead readers.
labels:
- chart:bar
- task:categorize
- visual:color
- impact:accuracy
- data:categorical
- audience:general
- scale:categorical
---

## The Rule <!-- role: advice -->

Use distinct hues to encode categories; do not use shades of one hue (a sequential gradient) for categorical data.

## The Logic <!-- role: reason -->

Muth explains that many readers interpret dark as “more/high” and light as “less/low,” so using a gradient for categories implies a ranking that may not exist [@muth_colors_2018].

- **The Principle:** Avoid accidental ordinal cues in nominal encodings.
- **The Evidence:** [@muth_colors_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify categories without inferring an order.
- **Data Type:** Nominal categories (no inherent ranking).
- **Audience:** General readers prone to applying common light/dark magnitude assumptions.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your categories are intentionally ordered (i.e., they are actually ordinal).
- **Reason:** Then a sequential scheme is encoding a real order rather than implying a false one [@muth_colors_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** More varied, potentially “colorful” appearance.
- **The Risk:** If too many hues are used, the chart can become harder to read; Muth suggests reconsidering chart type if it feels too colorful [@muth_colors_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using multiple blue shades for unrelated categories to make the chart look “clean.”
- **Why it fails:** It suggests a hierarchy and makes categories harder to name and discuss (“the medium blue one”) [@muth_colors_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Categories appear to have a “more/less” relationship purely from color darkness.
- **The Test:** Ask: “Would a reader assume the darkest category is the biggest/most important?” If yes and that’s untrue, the palette is misleading [@muth_colors_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace shades with distinct hues while keeping similar saturation.
- **Best Fix:** Use a true categorical palette (different hues) and, if the result is too colorful, switch chart type or regroup categories [@muth_colors_2018].
