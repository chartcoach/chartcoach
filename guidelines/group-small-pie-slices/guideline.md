---
id: group-small-pie-slices
title: Group Small Slices into Others
bibliography: references.bib
description: Combine small slices into a single 'Others' section to clean up the chart
  and improve readability.
labels:
- chart:pie
- task:aggregation
- visual:simplification
- impact:readability
- data:categorical
---

## The Rule <!-- role: advice -->
Group small slices together into one bigger slice (labeled "others" or similar).

## The Logic <!-- role: reason -->
This cleans up the overall look of the chart. The fewer the labels and the bigger the slices, the easier the chart is to read. It prevents clutter caused by thin wedges [@muth_pie_charts_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Reducing noise and focusing on major contributors.
*   **Data Type:** Data with a "long tail" of insignificant categories.
*   **Audience:** General readers who don't need granular detail on minor categories.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The specific detail of a tiny slice is the critical insight (e.g., a small but growing political party).
*   **Reason:** Hiding it in "others" buries the lead.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Transparency regarding the composition of the "others" group.
*   **The Risk:** A large "others" slice can be ambiguous.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a pointer line for every single tiny slice.
*   **Why it fails:** It creates a "spider web" of lines that is hard to track.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there slices so thin they are barely visible?
*   **The Test:** Can you fit the label inside or directly next to the slice without overlap? If not, group it.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Aggregate the smallest 3-4 values into one category.
*   **Best Fix:** Aggregate and add a note in the text explaining what "others" contains if necessary [@muth_pie_charts_2018].
