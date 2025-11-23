---
id: normalize-choropleth-maps
title: Normalize Data for Choropleth Maps
bibliography: references.bib
description: Use densities rather than raw values to prevent area bias in colored
  maps.
labels:
- chart:map
- visual:color
- data:geospatial
- impact:fairness
- task:compare
---

## The Rule <!-- role: advice -->
Do not encode raw data values (like population counts) on a standard choropleth map. Always normalize values to produce a density (e.g., population per square mile) or a ratio.

## The Logic <!-- role: reason -->
Standard maps inevitably confound the geographic area with the data value.
*   **The Principle:** Visual Confounding
*   **The Evidence:** In a standard choropleth map, perception of the shaded value is affected by the underlying area of the geographic region. Large areas naturally dominate the visual field, distorting the interpretation of raw counts [@heer_tour_2010].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the prevalence or intensity of a phenomenon across geographic regions.
*   **Data Type:** Geospatial data aggregated by region (e.g., states, counties).
*   **Audience:** General audiences interpreting geographic trends.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Using a Cartogram.
*   **Reason:** Cartograms purposefully distort the shape of regions so that the area itself encodes the data variable, making normalization unnecessary for the area channel [@heer_tour_2010].

## The Price <!-- role: costs -->
*   **The Risk:** Normalization might hide the absolute scale of the data (e.g., a high rate in a tiny town vs. a high rate in a metropolis).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Coloring large states based on total population.
*   **Why it fails:** It essentially just highlights the largest shapes rather than the density of the population, telling the viewer nothing about the concentration of people.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the largest geographic regions (like Montana or Texas) dominate the visual attention regardless of the data context?
*   **The Test:** Check the legend. If the unit is a raw count (e.g., "Number of People") rather than a ratio (e.g., "People per Sq Mile" or "Percentage"), the rule is broken.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Divide the value by the geographic area or total population to create a ratio.
*   **Best Fix:** If raw counts are essential, switch to a "Graduated Symbol Map" where symbol size represents the raw count independent of the land mass [@heer_tour_2010].
