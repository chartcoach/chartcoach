---
id: table-sorting-by-relevance
title: Sort Tables by Data Value, Not Alphabet
bibliography: references.bib
description: Sort table rows by the most important metrics rather than using alphabetical
  order as a default.
labels:
- chart:table
- task:sort
- task:rank
- impact:engagement
- data:quantitative
---

## The Rule <!-- role: advice -->
Do not default to sorting the first column alphabetically. Instead, sort the table by the most important data value (e.g., the biggest number, the worst performance) or an "invisible" logic column.

## The Logic <!-- role: reason -->
Alphabetical sorting often buries the most interesting data in the middle of the table. Sorting by value brings the most critical information to the top, where readers are most likely to see it. This is especially important for paginated tables where interesting data might otherwise be hidden on page 2 or 3 [@muth_tables_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Finding the "best," "worst," or "biggest" items quickly.
*   **Data Type:** Lists of entities (cities, companies, teams) associated with quantitative metrics.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The table functions strictly as a directory or dictionary where the user knows the specific name they are looking for.
*   **Reason:** In a pure lookup task without a search bar, alphabetical order is the expected convention.

## The Price <!-- role: costs -->
*   **The Risk:** Users looking for a specific entity by name (e.g., "Alabama") will take longer to find it if the list is sorted by value (e.g., "Population").

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Sorting alphabetically because it looks "neutral."
*   **Why it fails:** It fails to tell a story or highlight the most significant data points.

## How to Check <!-- role: check -->
*   **The Test:** Look at the first three rows of your table. Do they represent the most significant or interesting data points? If not, change the sort order.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Click the header of your main metric column to set the default sort to descending.
*   **Best Fix:** If "importance" is complex (e.g., major cities vs. small towns), sort by an "invisible" column (e.g., population) while displaying the city names.
