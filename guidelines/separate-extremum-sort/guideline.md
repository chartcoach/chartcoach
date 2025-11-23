---
id: separate-extremum-sort
title: Distinguish Extremum Search from Sorting
bibliography: references.bib
description: Provide direct access to top/bottom values without forcing a full sort.
labels:
- task:find-extremum
- task:sort
- impact:efficiency
- visual:position
---

## The Rule <!-- role: advice -->
Provide specific functionality to identify top or bottom values (extrema) without relying solely on global sorting mechanisms.

## The Logic <!-- role: reason -->
Finding data cases with extreme values (e.g., "What car has the highest MPG?") is a distinct analytic task from sorting. While sorting is often used as a substrate to find extrema, the user's goal is typically to identify the "Top N" cases, not to reorder the entire dataset. A complete sort is not always necessary or desired to answer an extremum question [@amar_low-level_2005].

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying the "best," "worst," "most," or "least" of an attribute.
*   **Data Type:** Large datasets where reordering the entire view might be computationally expensive or visually disruptive.
*   **Audience:** Users focused on outliers, winners, or high-performance metrics.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user explicitly wants to see the ranking of *all* items (e.g., a leaderboard).
*   **Reason:** In this case, the "Sort" task is the primary goal, not just a means to find the extremum.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Additional UI controls specifically for "Find Top/Bottom N."
*   **The Risk:** Visual clutter if both sorting and filtering-by-extremum are prominent.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Assuming a "Sort Ascending/Descending" button is sufficient for all high/low value queries.
*   **Why it fails:** It forces a global change to the view layout when the user only wanted to isolate a few specific data points.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does finding the "highest value" require changing the order of every other data point in the visualization?
*   **The Test:** Ask "Who won the most awards?" If the only way to answer is to re-sort the whole list, the rule is broken.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Highlight the minimum and maximum values visually (e.g., distinct colors or labels).
*   **Best Fix:** Provide a "Top/Bottom N" filter or a specific query tool to retrieve extrema independent of the list order.
