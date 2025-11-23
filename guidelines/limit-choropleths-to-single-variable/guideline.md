---
id: limit-choropleths-to-single-variable
title: Limit Choropleths to Single Variables
bibliography: references.bib
description: Avoid using choropleth maps to show correlations; stick to one variable
  or a calculated difference.
labels:
- chart:map
- data:multivariate
- impact:clarity
- task:analysis
---

## The Rule <!-- role: advice -->
Use choropleth maps to display only one variable at a time, or the computed difference between two variables. Do not use them to show correlations between multiple values.

## The Logic <!-- role: reason -->
Choropleth maps are optimized for showing the distribution of a single metric across space. They are poor tools for correlation analysis because comparing two different color layers or patterns simultaneously is cognitively difficult. If the goal is correlation, standard statistical charts are superior [@muth_choroplethmaps_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Showing the "big picture" of a single dataset.
*   **Data Type:** Univariate data (e.g., Unemployment Rate) or a single derived metric (e.g., Change in rate from 2023 to 2024).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Bivariate Choropleth Maps (Advanced).
*   **Reason:** While not explicitly encouraged in the text, advanced designers sometimes overlap variables, but the text specifically advises against it for general clarity, suggesting other chart types instead [@muth_choroplethmaps_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You cannot see how Factor A relates to Factor B on the same visual plane.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Trying to map two distinct variables (e.g., "Income" and "Education") on the same choropleth map.
*   **Why it fails:** It confuses the reader about what the color intensity represents.

## How to Check <!-- role: check -->
*   **The Test:** Ask, "Am I trying to show how X influences Y?" If yes, the map is likely the wrong choice.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Use a dotplot or scatterplot to show the correlation between the two variables, rather than a map [@muth_choroplethmaps_2018].
