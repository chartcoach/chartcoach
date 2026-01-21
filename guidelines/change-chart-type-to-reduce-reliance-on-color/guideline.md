---
id: change-chart-type-to-reduce-reliance-on-color
title: Switch Chart Types to Encode Categories by Position Instead of Color
bibliography: references.bib
description: Reduce the need for many colors by choosing a chart type that distinguishes
  categories through position rather than hue.
labels:
- chart:comparison
- task:compare
- visual:position
- impact:clarity
- data:categorical
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

If many categories force you to use many colors, change to a chart type that uses position (not color) to separate categories.

## The Logic <!-- role: reason -->

Some chart types inherently require color to distinguish stacked or overplotted categories; alternatives can “move” the category encoding to position, which reduces dependence on a large palette. Muth gives examples like choosing split bars over stacked bars, or transposing encodings so fewer categories need color ([@muth_fewer_colors_2022]).

- **The Principle:** Prefer position-based separation when color becomes overloaded.
- **The Evidence:** [@muth_fewer_colors_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Comparing categories without decoding many colors.
- **Data Type:** Many categories that are currently encoded primarily by color.
- **Audience:** Broad audiences who may struggle with many hues or legend lookups.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The alternative chart type prevents the comparisons your readers need.
- **Reason:** Muth notes suitability depends on what readers should see and compare; a type change can trade one comparison for another ([@muth_fewer_colors_2022]).

## The Price <!-- role: costs -->

- **The Sacrifice:** You may lose compactness or the ability to show part-to-whole in one view.
- **The Risk:** The new chart can make some comparisons harder even as it reduces color use ([@muth_fewer_colors_2022]).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Forcing a single chart type and compensating by adding more and more colors.
- **Why it fails:** The palette becomes the crutch; the chart remains hard to decipher ([@muth_fewer_colors_2022]).

## How to Check <!-- role: check -->

- **Visual Sign:** Many-category legend; readers must constantly map colors to categories.
- **The Test:** Ask: “Could position separate these categories instead?” If yes, prototype a positional alternative (split bars, transposed layout) and see if it reads faster ([@muth_fewer_colors_2022]).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Try a simple alternative that replaces stacking/overlay with separation (e.g., split bars).
- **Best Fix:** Redesign around the comparisons that matter most, potentially using two or three charts instead of one, as Muth suggests ([@muth_fewer_colors_2022]).
