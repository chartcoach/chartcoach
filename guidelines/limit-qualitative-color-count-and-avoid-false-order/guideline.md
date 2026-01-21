---
id: limit-qualitative-color-count-and-avoid-false-order
title: Limit Qualitative Colors and Avoid Implied Order
bibliography: references.bib
description: Use as few category colors as possible and avoid palettes that look sequential/diverging
  when categories are unordered.
labels:
- chart:choropleth
- task:categorize
- visual:color
- impact:clarity
- data:categorical
- audience:general
- custom:qualitative-palette
---

## The Rule <!-- role: advice -->

For qualitative choropleths, use as few hues as possible (aim for ~3 when feasible) and avoid color sets that imply a low-to-high or two-sided scale.

## The Logic <!-- role: reason -->

More category colors increase memory load because readers must repeatedly consult the key; and ordered-looking palettes falsely suggest ranking. Muth recommends using as few colors as possible in qualitative schemes, notes three colors reduce legend-checking, and warns against giving the idea of sequential/diverging order when data isn’t ordered [@muth_choroplethmaps_2018].

- **The Principle:** Reduce legend dependency and prevent false semantics
- **The Evidence:** [@muth_choroplethmaps_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify which category each region belongs to
- **Data Type:** Unordered categories (e.g., party winner per region)
- **Audience:** General readers, especially when categories are unfamiliar

## When to Break It <!-- role: exceptions -->

- **Scenario:** Readers already know the category color encoding (e.g., political party colors)
- **Reason:** The post notes it can be acceptable to use more hues when the encoding is already familiar [@muth_choroplethmaps_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may not be able to show many categories distinctly.
- **The Risk:** Collapsing categories to reduce colors can hide meaningful distinctions [@muth_choroplethmaps_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using many category colors and expecting the legend to carry comprehension
- **Why it fails:** Readers can’t remember mappings and repeatedly look back and forth [@muth_choroplethmaps_2018].
- **The Wrong Fix:** Using a rainbow-like ordered palette for categories
- **Why it fails:** It suggests a progression that doesn’t exist [@muth_choroplethmaps_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users must constantly consult the legend to interpret categories.
- **The Test:** Hide the legend and see if you can still correctly identify categories for a few regions; if not, reduce hues or use more familiar encoding [@muth_choroplethmaps_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of category colors and choose clearly distinct hues [@muth_choroplethmaps_2018].
- **Best Fix:** Use known/familiar colors when applicable (e.g., established party colors) and keep the legend simple [@muth_choroplethmaps_2018].
