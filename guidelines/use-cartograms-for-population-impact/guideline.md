---
id: use-cartograms-for-population-impact
title: Use Cartograms for Population Focus
bibliography: references.bib
description: Use population cartograms when the number of people affected is more
  important than the geographic land area.
labels:
- chart:map
- data:geospatial
- impact:fairness
- task:comparison
---

## The Rule <!-- role: advice -->
Consider using a cartogram instead of a standard geographic projection if the number of people affected is critical to the story.

## The Logic <!-- role: reason -->
Standard choropleth maps show how much *geographic area* is affected, which can be misleading if large regions have few people. Cartograms distort the geometry based on population, offering a "more honest view of the data" by driving attention to populated areas rather than empty land [@muth_choroplethmaps_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Visualizing demographic or social data (e.g., election votes, social services).
*   **Data Type:** Data highly correlated with population density.
*   **Audience:** Readers who are generally familiar with the geography of the region (as shapes will be distorted).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Unfamiliar Geography.
*   **Reason:** Cartograms make it harder for readers to recognize regions. If the audience is not familiar with the standard map, a cartogram will be unreadable [@muth_choroplethmaps_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Geographic accuracy and recognizability. Regions appear warped or simplified.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Sticking to a Mercator projection for election results.
*   **Why it fails:** It often visually over-represents rural parties because they hold more land area, even if they have fewer votes.

## How to Check <!-- role: check -->
*   **The Test:** Does your map show a massive sea of color for one category, but the actual data summary says the categories are split 50/50? You have a density bias.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Switch to a cartogram (e.g., Dorling or hexagonal cartogram) where region size represents population size.
