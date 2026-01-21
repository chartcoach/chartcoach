---
id: use-grid-and-grouping-for-categorical-color-keys
title: Lay Out Categorical Color Keys in Grids and Groups
bibliography: references.bib
description: Make categorical legends skimmable by arranging items in a tidy grid
  and grouping related categories.
labels:
- chart:multiple
- task:identify
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

For categorical color keys with many or long items, use a grid layout and group related items instead of packing everything into as few lines as possible.

## The Logic <!-- role: reason -->

Dense, wrapped, single-line legends are hard to scan; a grid creates consistent alignment and predictable reading paths, and grouping reduces search space by chunking related categories. Muth recommends grids and grouping specifically to make larger categorical keys easier to skim [@muth_color_keys_2023].

- **The Principle:** Improve skimmability through alignment and chunking
- **The Evidence:** [@muth_color_keys_2023]

## Where to Apply <!-- role: context -->

- **User Goal:** Fast matching of category names to colors
- **Data Type:** Categorical palettes with multiple categories and/or long labels
- **Audience:** General readers scanning quickly

## When to Break It <!-- role: exceptions -->

- **Scenario:** Only a few short legend items and ample horizontal space
- **Reason:** A simple single-row key can be sufficiently readable without the extra structure [@muth_color_keys_2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Potentially more vertical space (more rows)
- **The Risk:** Over-grouping can imply relationships that aren’t in the data if groups are not meaningful [@muth_color_keys_2023].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Squeezing many items into one or two tightly packed lines
- **Why it fails:** The key becomes visually overwhelming and hard to skim, defeating its purpose [@muth_color_keys_2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Legend items form an uneven “word soup” with inconsistent wrapping and weak alignment.
- **The Test:** Time yourself: if you can’t find a specific category-color pairing quickly, the layout needs grid/group structure [@muth_color_keys_2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Break the legend into multiple rows with consistent columns.
- **Best Fix:** Introduce explicit grouping (subheads or spacing) and a grid so items align cleanly and can be scanned line by line [@muth_color_keys_2023].
