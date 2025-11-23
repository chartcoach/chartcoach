---
id: fallback-to-reference-maps
title: Revert to reference maps when data relevance is low
bibliography: references.bib
description: If no thematic data strongly matches the text, display a simple locator
  map instead of a weak thematic map.
labels:
- chart:map
- task:contextualize
- impact:clarity
- data:geospatial
- audience:general
---

## The Rule <!-- role: advice -->
If the semantic match between your available data variables and the article text falls below a specific confidence threshold, do not force a thematic map. Instead, display a "reference map" (locator map) showing only the relevant locations.

## The Logic <!-- role: reason -->
Showing a data variable that is only tangentially related to the text confuses the reader. The NewsViews system calculates the Pointwise Mutual Information (PMI) between article text and data headers. If no variable surpasses a threshold (e.g., 2.5), the system defaults to a reference map to ensure the visualization remains useful for context without being misleading or irrelevant [@gao_newsviews_2014].

## Where to Apply <!-- role: context -->
*   **User Goal:** Providing geographic context for a news story.
*   **Data Type:** Automated pipelines with large repositories of "found" data tables.
*   **Audience:** Readers attempting to understand the "where" of a story.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user explicitly queries for a specific dataset.
*   **Reason:** Explicit user intent overrides automated relevance matching.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the richness of data-driven context (trends, comparisons).
*   **The Risk:** The visualization becomes purely locational, which is less informative than a well-matched thematic map.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Displaying the "least bad" variable just to have a data visualization.
*   **Why it fails:** Users perceive the relevance of the map as low, which degrades the overall quality of the reading experience.

## How to Check <!-- role: check -->
*   **Visual Sign:** The map title (data variable) feels disconnected from the article headline or lead paragraphs.
*   **The Test:** Ask, "Does the data variable name appear conceptually in the first three sentences of the text?"

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove the data layer and simply place markers on the mentioned locations.
*   **Best Fix:** Implement a relevance scoring system (like PMI) and set a hard threshold below which thematic generation is disabled.
