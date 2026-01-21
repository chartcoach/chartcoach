---
id: use-tooltips-only-when-direct-labels-dont-fit
title: Use Tooltips for Secondary Categories, Not as a Replacement for Direct Labels
bibliography: references.bib
description: Rely on tooltips and hover effects to reveal minor categories when space
  prevents labeling, while labeling key categories directly.
labels:
- chart:interactive
- task:identify
- visual:interaction
- impact:clarity
- data:categorical
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use tooltips and hover effects to reveal less important categories when you lack space—but directly label the most important categories.

## The Logic <!-- role: reason -->

Tooltips show one label at a time, which makes scanning, searching, and comparing categories harder than with direct labels. Muth frames tooltips as a helpful addition for crowded charts, but not a substitute for labeling the key categories ([@muth_fewer_colors_2022]).

- **The Principle:** On-demand labels reduce clutter but slow comparison.
- **The Evidence:** [@muth_fewer_colors_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Identifying an unlabeled category on demand without adding permanent clutter.
- **Data Type:** Many small/secondary categories where direct labeling doesn’t fit.
- **Audience:** Interactive chart readers who can hover to explore.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The highlighted/most important categories are not directly labeled.
- **Reason:** Muth advises against relying on tooltips for the most important categories; they should always be labeled directly ([@muth_fewer_colors_2022]).

## The Price <!-- role: costs -->

- **The Sacrifice:** Quick scanning and side-by-side comparison of categories.
- **The Risk:** Readers may miss key context if they don’t hover, or can’t hover (e.g., limited interaction), making understanding slower (limitations implied in [@muth_fewer_colors_2022]).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using tooltips instead of direct labels for the main message categories.
- **Why it fails:** It hides the key information behind interaction and undermines immediate comprehension ([@muth_fewer_colors_2022]).

## How to Check <!-- role: check -->

- **Visual Sign:** You can’t tell what the key categories are without hovering.
- **The Test:** Look at the chart without interacting: are the most important categories still clearly identified? If not, the tooltip strategy is misapplied ([@muth_fewer_colors_2022]).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add direct labels for the key categories and keep tooltips for the rest.
- **Best Fix:** Combine selective emphasis, direct labels for the story-critical categories, and tooltips/hover fading for minor categories to reduce the need for many colors ([@muth_fewer_colors_2022]).
