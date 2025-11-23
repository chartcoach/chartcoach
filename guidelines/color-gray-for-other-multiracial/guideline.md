---
id: color-gray-for-other-multiracial
title: Use Distinct Colors for 'Other' Categories
bibliography: references.bib
description: Avoid using gray for 'Other' or 'Multiracial' categories to prevent diminishing
  the people in those groups.
labels:
- visual:color
- impact:ethics
- data:categorical
---

## The Rule <!-- role: advice -->
Assign a distinct, non-gray hue to "Other" or "Multiracial" categories. Do not use gray.

## The Logic <!-- role: reason -->
In data visualization, gray signals "background," "context," or "less importance." When visualizing people, using gray for the "Other" or "Multiracial" bucket implies those humans are not as important as the named categories. This violates the "Do No Harm" principle of ensuring data subjects feel respected [@muth_race_ethnicity_colors_2024].

## Where to Apply <!-- role: context -->
*   **User Goal:** Visualizing census data or demographics with a catch-all category.
*   **Data Type:** Categorical data including "Multiracial," "Mixed," or "Other."

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Missing data or "Unknown."
*   **Reason:** If the category represents a lack of data rather than a group of people (e.g., "Data not available"), gray is appropriate to signal absence.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to visually recede the smallest category to clean up the chart.
*   **The Risk:** The chart becomes more colorful and potentially busier.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a very faint version of another color.
*   **Why it fails:** It still visually deprioritizes the group.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the "Other" bar look like gridlines or background elements?
*   **The Test:** Ask, "If I were in the 'Multiracial' category, would I feel like a full participant in this chart?"

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Assign a color like purple, orange, or teal to the "Other" category.
*   **Best Fix:** Treat "Multiracial" as a primary category with equal visual weight to all others.
