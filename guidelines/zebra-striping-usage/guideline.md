---
id: zebra-striping-usage
title: Stripe Rows Only in Wide, Long Tables
bibliography: references.bib
description: Guidelines for using alternating background colors (zebra shading) to
  aid row tracking.
labels:
- chart:table
- visual:color
- visual:style
- impact:readability
---

## The Rule <!-- role: advice -->
Apply grey stripes (zebra shading) to every second row only if the table is long and has many columns. Do not use striping for small tables with few columns.

## The Logic <!-- role: reason -->
Zebra shading reduces the risk of readers accidentally jumping between rows while trying to read a value in a distant column (e.g., looking from column 1 to column 5). However, in simple tables with few columns, the gaps between data are small enough for the eye to track easily, making the striping unnecessary visual noise [@muth_tables_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Reading across a wide row to find corresponding data points.
*   **Data Type:** Wide datasets with 5+ columns.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Tables with very few columns (e.g., 2-3 columns).
*   **Reason:** Striping becomes "confusing" or unnecessary clutter when the eye can easily track the row without assistance [@muth_tables_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Increases visual weight ("ink") on the page.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Applying zebra striping to every table by default.
*   **Why it fails:** It adds unnecessary design elements to simple tables where whitespace is sufficient.

## How to Check <!-- role: check -->
*   **The Test:** Remove the stripes. Can you still easily read the last column and map it to the first column? If yes, leave the stripes off.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Toggle zebra shading off for simple tables.
*   **Best Fix:** For complex tables, use a very light grey to ensure text contrast remains high.
