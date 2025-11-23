---
id: use-maps-for-spatial-context
title: Use Maps for Spatial Context
bibliography: references.bib
description: Leverage map visualizations when data possesses a relevant geographical
  component to improve viewer familiarity and engagement.
labels:
- chart:map
- task:locate
- visual:position
- impact:engagement
- data:spatial
- audience:general
---

## The Rule <!-- role: advice -->

When your data has a relevant geographical component, use maps or geo-referencing to anchor the information. Do not rely solely on abstract lists or charts if the "where" is central to understanding the "what."

## The Logic <!-- role: reason -->

Maps leverage a viewer's existing mental model of the world, making abstract data instantly relatable. Because the format is familiar, it lowers the cognitive load required to understand the scope of the data.

*   **The Principle:** Spatial Familiarity. Viewers inherently understand geographical layouts, which helps them grasp relationships between data points and known locations.
*   **The Evidence:** Research indicates that viewers use maps to successfully contemplate crisis scenarios and establish geographical overviews [@koesten_encountering_2025]. Furthermore, practitioners report that audiences prioritize maps over other chart types, with country comparisons driving high engagement metrics [@schuster_who_2023].

## Where to Apply <!-- role: context -->

Use this approach when the location itself drives the insight.

*   **User Goal:** To see regional patterns, understand geographical scope, or relate data to specific crises or events.
*   **Data Type:** Datasets containing coordinates, country codes, or regional identifiers.
*   **Audience:** General audiences who respond well to familiar formats, or officials using data for location-based decision-making.

## When to Break It <!-- role: exceptions -->

Maps are poor tools for precise numerical comparison.

*   **Scenario:** The primary goal is ranking or comparing exact values (e.g., "Is France's GDP slightly higher than the UK's?").
*   **Reason:** Human perception judges aligned lengths (bar charts) much better than color intensity or bubble size scattered across a spatial plane.
*   **Scenario:** The geography is irrelevant to the data pattern.
*   **Reason:** It wastes space and distracts the viewer with unnecessary spatial details.

## The Price <!-- role: costs -->

Visualizing geography requires significant screen real estate for low data density.

*   **The Sacrifice:** You lose layout efficiency. A map often requires a large canvas to show a few data points, leaving vast amounts of "empty" space (oceans, rural areas).
*   **The Risk:** You may inadvertently highlight land area rather than the data variable (the "Alaska looks important because it is big" problem).

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Using a map for a "Top 10" list.
*   **Why it fails:** It forces the user to hunt for values across the canvas rather than scanning an ordered list.
*   **The Wrong Fix:** Mapping raw counts (e.g., number of customers) without normalizing for population.
*   **Why it fails:** You simply create a population density map, telling the viewer nothing new about your specific variable.

## How to Check <!-- role: check -->

*   **Visual Sign:** If you remove the map borders/background, does the data shape (the scatter or distribution) still make sense? If not, the map is essential. If yes, the map might be decorative.
*   **The Test:** Ask a viewer, "Where is the highest value?" If they have to scan the whole image to find a slightly darker shade of blue, a bar chart would have been faster.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Add a supplementary bar chart or table alongside the map to provide precise ranking.
*   **Best Fix:** If the geography obscures the data (e.g., small countries are invisible), switch to a cartogram or a tile map to equalize the visual weight of regions.
