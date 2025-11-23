---
id: use-shades-for-subcategories
title: Use Shades to Distinguish Sub-categories
bibliography: references.bib
description: Use hue for parent categories and shades for their sub-categories.
labels:
- visual:color
- data:hierarchical
- chart:stacked-bar
- chart:area
- task:part-to-whole
---

## The Rule <!-- role: advice -->
Use distinct hues to represent main categories, and use shades (light to dark variations of those hues) to distinguish the sub-categories within them.

## The Logic <!-- role: reason -->
This technique leverages the brain's ability to group similar colors. Readers intuitively understand that shades of blue belong to the "Blue" category and shades of green belong to the "Green" category. It helps distinguish sub-groups (like specific territories within a religious group, or specific age terms within a generation) without needing a chaotic legend of unrelated colors [@muth_quantitative_vs_qualitative_2021].

## Where to Apply <!-- role: context -->
*   **Data Type:** Hierarchical data (Category > Sub-category).
*   **Chart Types:** Stacked area charts, stacked bar charts.
*   **User Goal:** Comparing the composition of major groups while maintaining detail.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The sub-categories have no relationship to the parent category logic.
*   **Reason:** If the sub-groups are totally distinct entities that don't belong to the "parent," grouping them by color might mislead the reader about their relationship.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You cannot use the shades to imply value or rank (e.g., lightest is not necessarily smallest) if you are using them strictly for differentiation.
*   **The Risk:** Users might expect the shades to represent an order (lightest = least important) even if you just meant to differentiate the blocks.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using random, distinct hues for every single slice in a hierarchical chart.
*   **Why it fails:** The reader loses track of which slices belong to which major group.

## How to Check <!-- role: check -->
*   **The Test:** Can you identify which sub-sectors belong to "Group A" just by looking at the color?
*   **Visual Sign:** If Group A contains a red, a blue, and a green slice, you have failed. If Group A contains dark blue, medium blue, and light blue, you have succeeded.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Assign a base hue to each parent category.
*   **Best Fix:** Adjust the lightness of that base hue to create distinct steps for each sub-category, ensuring contrast between adjacent areas.
