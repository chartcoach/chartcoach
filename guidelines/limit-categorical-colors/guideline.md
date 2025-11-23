---
id: limit-categorical-colors
title: Limit Categorical Colors to Seven
bibliography: references.bib
description: Restrict distinct color categories to a maximum of seven to ensure readability.
labels:
- visual:color
- impact:readability
- data:categorical
- audience:general
---

## The Rule <!-- role: advice -->
Do not use more than seven distinct colors to distinguish between categories in a single chart. If you have more than seven categories, group them or switch chart types.

## The Logic <!-- role: reason -->
Using too many colors increases the cognitive load on the reader. As the number of colors rises, it becomes harder to distinguish between them and "read it quickly" [@muth_colors_2018]. Readers are forced to constantly consult the color key to understand what is shown, disrupting the flow of information processing.

## Where to Apply <!-- role: context -->
*   **User Goal:** Rapid identification of different groups or categories.
*   **Data Type:** Nominal/Categorical data (e.g., countries, product lines, departments).
*   **Audience:** General audiences who need to scan the chart quickly.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Using a continuous gradient for sequential data.
*   **Reason:** This rule applies specifically to distinct *categories*, not quantitative gradients.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to show granular detail for every single category.
*   **The Risk:** Grouping categories (e.g., into "Others") might hide specific outliers in the smaller groups.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using 15 different colors for 15 countries.
*   **Why it fails:** Readers cannot remember the mapping and struggle to distinguish between similar hues (e.g., three different blues).

## How to Check <!-- role: check -->
*   **Visual Sign:** A legend that looks like a long list.
*   **The Test:** Count the distinct hues in your legend. Is the number greater than 7?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Group the smallest values into a single "Other" category appearing in grey.
*   **Best Fix:** Use another chart type (like a bar chart with labels) where colors aren't required to identify the category.
