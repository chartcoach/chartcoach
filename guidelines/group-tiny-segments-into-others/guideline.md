---
id: group-tiny-segments-into-others
title: Group Tiny Segments into an 'Other' Category
bibliography: references.bib
description: Improve chart readability by aggregating small, insignificant data slices
  into a single group.
labels:
- chart:stacked-column
- visual:clutter
- impact:simplification
- task:clean
---

## The Rule <!-- role: advice -->
Group tiny data parts together into one bigger part (e.g., "Others") rather than displaying many thin slivers.

## The Logic <!-- role: reason -->
Too many small segments create visual noise ("screaming cats") and require excessive labeling. Grouping them cleans up the overall look, reduces the number of colors required, and guides the reader's eye specifically to the important, larger parts of the chart [@muth_stacked_columns_2018].

## Where to Apply <!-- role: context -->
*   **Data Type:** Categorical data with a "long tail" of small values.
*   **User Goal:** Focusing on major contributors rather than granular detail.
*   **Visual limit:** Segments are too small to hold a label or be distinguished by color.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The "long tail" or the diversity of small options is the main insight.
*   **Reason:** If the story is "look how fragmented the market is," hiding the fragments destroys the narrative.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Loss of granular detail for the smallest categories.
*   **The Risk:** The "Other" category might become deceptively large, hiding potentially interesting outliers within it.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a legend with 20+ items to identify thin slivers.
*   **Why it fails:** Readers cannot easily map colors back and forth between the legend and the tiny segments.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there segments so thin they look like lines? Are you running out of distinguishable colors?
*   **The Test:** If a segment contributes less than 1-2% to the total and isn't individually critical to the story, it belongs in "Others."

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Create a new data category called "Other" and sum the smallest values into it.
*   **Best Fix:** Place this "Other" category at the top of the stack (in standard charts) or in a neutral color to de-emphasize it.
