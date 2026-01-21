---
id: repeat-category-colors-in-tooltips-to-clarify-what-is-hovered
title: Show Category Colors in Tooltips
bibliography: references.bib
description: "Use category colors inside tooltips so readers can identify and remember\
  \ the hovered item\u2019s category without consulting the legend."
labels:
- chart:interactive
- task:lookup
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- component:tooltip
- interaction:hover
---

## The Rule <!-- role: advice -->

Include the hovered item’s category color inside the tooltip (e.g., colored text, a colored shape, or a colored background) to restate what the color represents.

## The Logic <!-- role: reason -->

Tooltips appear right next to the data point and may be used before a reader ever consults the legend; they can also cover the legend. Putting the category color inside the tooltip reinforces the mapping at the moment of interaction and avoids confusion when the legend is distant or obscured.

- **The Principle:** Contextual reinforcement of color-category mapping at the point of interaction
- **The Evidence:** [@muth_remind_colors_2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify the category and exact values for a hovered mark
- **Data Type:** Interactive charts/maps with categorical color encoding; especially where regions/marks are small and ambiguity is high
- **Audience:** Digital readers exploring via hover [@muth_remind_colors_2023]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The tooltip already states the category clearly and the chart uses minimal colors (so color repetition adds noise).
- **Reason:** The post frames tooltip color as a way to teach/remind and disambiguate; if neither problem exists, extra color can be unnecessary. [@muth_remind_colors_2023]

## The Price <!-- role: costs -->

- **The Sacrifice:** More tooltip styling work and potential for busy tooltips.
- **The Risk:** Over-styled tooltips can distract from the value readout or reduce readability if color contrast is poor. [@muth_remind_colors_2023]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Relying on the legend alone while tooltips obscure it.
- **Why it fails:** Readers can’t cross-check the mapping while interacting, causing uncertainty about what category they’re seeing. [@muth_remind_colors_2023]

## How to Check <!-- role: check -->

- **Visual Sign:** Tooltip shows numbers but provides no color cue, and the legend is far away or covered.
- **The Test:** Hover a mark without looking at the legend: can you tell which category it belongs to from the tooltip alone? [@muth_remind_colors_2023]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a small colored dot/swatch next to the category name in the tooltip.
- **Best Fix:** Use tooltip styling that clearly ties category name and color (e.g., colored underline/background for the category text, and consistent use of the same category colors across tooltip elements). [@muth_remind_colors_2023]
