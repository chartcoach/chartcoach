---
id: delineate-same-color-regions
title: Delineate Adjacent Regions with Borders
bibliography: references.bib
description: Draw boundary lines between adjacent areas in a tree-map, especially
  when they share the same color.
labels:
- chart:treemap
- visual:border
- visual:separation
- impact:clarity
---

## The Rule <!-- role: advice -->
Draw boundary lines between rectangles if adjacent areas have the same color.

## The Logic <!-- role: reason -->
When color is used to encode categories, adjacent nodes of the same category will visually merge into a single shape without explicit boundaries, destroying the perception of individual node size.
*   **The Principle:** Visual Separation.
*   **The Evidence:** [@shneiderman_tree_1992] explicitly states: "If adjacent areas have the same color, then a boundary line will be necessary."

## Where to Apply <!-- role: context -->
This advice is designed for colored tree-maps.
*   **User Goal:** Distinguishing individual items (files/nodes) within a cluster of similar items.
*   **Data Type:** Categorical data where clusters of the same type are common.
*   **Audience:** General users.

## When to Break It <!-- role: exceptions -->
No rule is absolute. When is this advice actually WRONG?
*   **Scenario:** Every adjacent node is guaranteed to be a different color.
*   **Reason:** The contrast provides natural separation (though this is rare in practice).

## The Price <!-- role: costs -->
Every design choice has a cost.
*   **The Sacrifice:** Borders consume pixels.
*   **The Risk:** In extremely dense maps, borders might dominate the view, obscuring the color coding of very small nodes.

## Common Mistakes <!-- role: mistakes -->
How do people usually screw this up?
*   **The Wrong Fix:** Removing borders to save space.
*   **Why it fails:** Users cannot distinguish if a large blue area is one giant file or one hundred small files.

## How to Check <!-- role: check -->
How can I tell if I've broken this rule?
*   **Visual Sign:** Do clusters of same-colored data look like single, irregular polygons?
*   **The Test:** Can you count the number of nodes in a single-color block?

## How to Fix <!-- role: fix -->
I've broken the rule. How do I solve it?
*   **Quick Fix:** Add a 1-pixel black or contrasting outline to every rectangle.
*   **Best Fix:** Implement logic to draw lines specifically when color contrast is insufficient to separate regions.
