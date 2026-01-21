---
id: use-small-multiples-to-avoid-many-category-colors
title: Use Small Multiples Instead of Coloring Many Categories in One Plot
bibliography: references.bib
description: "Split many categories into separate small charts so each category doesn\u2019\
  t require its own color."
labels:
- chart:small-multiples
- task:compare
- visual:position
- impact:clarity
- data:categorical
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

When a single chart becomes unreadable with many colored categories, split it into small multiples—one panel per category.

## The Logic <!-- role: reason -->

Small multiples give each category its own space instead of layering categories together, reducing the need to distinguish them by many colors. Muth notes this improves readability for within-category patterns, while changing how cross-category comparison works ([@muth_fewer_colors_2022]).

- **The Principle:** Separation by faceting reduces encoding load.
- **The Evidence:** [@muth_fewer_colors_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Seeing trends/patterns within each category clearly.
- **Data Type:** Many-category line/area/scatter/stacked visuals that become crowded.
- **Audience:** Readers who benefit from scanning category-by-category.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The main task is comparing precise values across categories at the same point.
- **Reason:** Muth notes small multiples make cross-category comparisons harder than putting categories in one shared plot ([@muth_fewer_colors_2022]).

## The Price <!-- role: costs -->

- **The Sacrifice:** Direct side-by-side comparison across categories in a single shared coordinate space.
- **The Risk:** Too many panels can still overwhelm or require scrolling, depending on layout (tradeoff implied in [@muth_fewer_colors_2022]).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping everything in one chart and trying to solve overlap with more colors.
- **Why it fails:** Color does not solve density and tracking problems when many marks overlap ([@muth_fewer_colors_2022]).

## How to Check <!-- role: check -->

- **Visual Sign:** Overplotted lines/areas; legend decoding dominates the reading experience.
- **The Test:** Ask whether the key questions are within-category (“What’s the trend for Iran?”) rather than between-category; if yes, small multiples fit ([@muth_fewer_colors_2022]).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Create a small-multiple version with one panel per category using a consistent scale.
- **Best Fix:** Decide explicitly which comparison matters (within vs. across categories) and choose between small multiples or a combined chart accordingly ([@muth_fewer_colors_2022]).
