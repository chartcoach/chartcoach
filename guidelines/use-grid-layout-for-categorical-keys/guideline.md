---
id: use-grid-layout-for-categorical-keys
title: Arrange Categorical Keys in Grids
bibliography: references.bib
description: Organize long lists of categorical key items into grids rather than single
  vertical columns.
labels:
- visual:layout
- visual:legend
- data:categorical
- impact:scannability
---

## The Rule <!-- role: advice -->
When a categorical color key contains many items or long labels, arrange them in a grid layout rather than a single vertical list.

## The Logic <!-- role: reason -->
Trying to fit many items into as few lines as possible works for short lists, but becomes overwhelming with many items. A grid layout creates structure, making the list easier to skim and visually tidier compared to a chaotic wrap-around text or a tall, space-consuming list [@muth_color_keys_2023].

## Where to Apply <!-- role: context -->
*   **User Goal:** Finding a specific category definition in a crowded map or chart.
*   **Data Type:** Categorical data with many distinct classes (e.g., many political parties, multiple energy sources).
*   **Audience:** Readers scanning for specific information.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Very few, short items.
*   **Reason:** A single horizontal line or a concise vertical list is more space-efficient for small numbers of categories (e.g., just "Solar" and "Wind").

## The Price <!-- role: costs -->
*   **The Sacrifice:** Vertical space. A grid might take up more height than a tightly packed paragraph-style legend (though it is more readable).
*   **The Risk:** If labels are of vastly different lengths, the grid may look uneven or create trapped whitespace.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using all uppercase letters to make grid items look uniform.
*   **Why it fails:** Lowercase letters are easier to read; all-caps reduces legibility.

## How to Check <!-- role: check -->
*   **Visual Sign:** Your legend looks like a wall of text or a very tall tower pushing the chart to the side.
*   **The Test:** Glance at the key. Can you instantly distinguish where one item ends and the next begins?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Introduce line breaks to separate items onto their own lines.
*   **Best Fix:** Implement a structured grid (columns and rows) and group related items together if logical sub-groups exist.
