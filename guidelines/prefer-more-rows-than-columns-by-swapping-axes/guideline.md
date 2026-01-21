---
id: prefer-more-rows-than-columns-by-swapping-axes
title: Reshape Tables to Have More Rows Than Columns
bibliography: references.bib
description: Swap rows and columns when it makes the table taller than it is wide
  to support faster vertical scanning.
labels:
- chart:table
- task:scan
- visual:layout
- impact:clarity
- data:categorical
- audience:general
- complexity:basic
---

## The Rule <!-- role: advice -->

If a table is wide, swap rows and columns so information is primarily vertically aligned and the table has more rows than columns.

## The Logic <!-- role: reason -->

People skim vertically aligned, sorted information more easily than horizontally aligned information; [@muth_tables_2019] notes that columns are better for skimming (like dictionaries).

- **The Principle:** Favor vertical scanning over horizontal scanning
- **The Evidence:** [@muth_tables_2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Skimming and comparing entries quickly
- **Data Type:** Wide tables where many attributes are spread across numerous columns
- **Audience:** General readers who scan rather than read sequentially [@muth_tables_2019]

## When to Break It <!-- role: exceptions -->

- **Scenario:** The current orientation is essential for the story (e.g., the “entity” must be a row for sorting or recognition)
- **Reason:** Swapping can make the table less intuitive or harder to sort/read in the intended way [@muth_tables_2019]

## The Price <!-- role: costs -->

- **The Sacrifice:** Potentially longer tables that require scrolling
- **The Risk:** The table may become too tall and interrupt the flow of an article [@muth_tables_2019]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping a very wide table and relying on readers to scroll sideways
- **Why it fails:** Horizontal skimming is harder and increases the chance readers miss values [@muth_tables_2019]

## How to Check <!-- role: check -->

- **Visual Sign:** Many columns are squeezed, and readers must track across long rows
- **The Test:** If comparing across columns requires frequent eye-jumps, try a transposed version and see if scanning improves [@muth_tables_2019]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Move secondary fields into headers or abbreviate to reduce width [@muth_tables_2019]
- **Best Fix:** Transpose the table so categories/entries run down the page in rows and can be skimmed vertically [@muth_tables_2019]
