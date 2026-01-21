---
id: directly-label-categories-to-reduce-color-dependence
title: Directly Label Categories Instead of Relying on Many Colors
bibliography: references.bib
description: Use direct labels so categories can share similar colors while remaining
  distinguishable.
labels:
- chart:line
- task:identify
- visual:label
- impact:clarity
- data:categorical
- audience:novice
- source:datawrapper
---

## The Rule <!-- role: advice -->

Label categories directly on the marks so you can use the same or similar colors instead of assigning each category a distinct color.

## The Logic <!-- role: reason -->

Direct labels let readers identify series/categories at the point of interest without decoding a color key. This makes it feasible to reduce hue variety while still distinguishing categories ([@muth_fewer_colors_2022]).

- **The Principle:** Identification through proximity (labels near data).
- **The Evidence:** [@muth_fewer_colors_2022]

## Where to Apply <!-- role: context -->

- **User Goal:** Identifying which category a mark/line belongs to without legend lookups.
- **Data Type:** Multi-category charts where a legend would be slow or ambiguous (e.g., many lines).
- **Audience:** General audiences who need fast comprehension.

## When to Break It <!-- role: exceptions -->

- **Scenario:** There is not enough space to label categories without clutter.
- **Reason:** Labels can collide or overwhelm the plot area; Muth suggests tooltips only when direct labeling isn’t possible ([@muth_fewer_colors_2022]).

## The Price <!-- role: costs -->

- **The Sacrifice:** Labels consume space and can add visual clutter.
- **The Risk:** Poorly placed labels can obscure data or become unreadable ([@muth_fewer_colors_2022]).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a color key/legend for many similarly colored categories.
- **Why it fails:** Readers can’t reliably map similar colors to categories; direct labeling is what makes reduced colors workable ([@muth_fewer_colors_2022]).

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers must repeatedly jump between legend and marks to decode categories.
- **The Test:** Remove the legend mentally: can you still tell which category is which from labels placed on/near the marks? If not, labeling is insufficient ([@muth_fewer_colors_2022]).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Label at least the emphasized and most important categories directly.
- **Best Fix:** Replace legend dependence by placing labels adjacent to lines/segments and reduce category hues accordingly ([@muth_fewer_colors_2022]).
