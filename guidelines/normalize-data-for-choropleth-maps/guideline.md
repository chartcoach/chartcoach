---
id: normalize-data-for-choropleth-maps
title: Normalize Data Before Mapping
bibliography: references.bib
description: Use relative data (rates or ratios) instead of absolute numbers to avoid
  population bias in choropleth maps.
labels:
- chart:map
- visual:color
- data:quantitative
- impact:accuracy
- task:compare
---

## The Rule <!-- role: advice -->
Map relative data (rates, percentages, or ratios) rather than absolute numbers. Calculate the number of occurrences per capita (e.g., per 100 citizens) or per area.

## The Logic <!-- role: reason -->
Absolute numbers are heavily influenced by population density; a map of absolute values often simply answers the question, "Where do most people live?" rather than revealing the phenomenon you intend to show. Using relative data allows for valid comparisons between regions with different population sizes [@muth_choroplethmaps_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the intensity or prevalence of a phenomenon across different regions.
*   **Data Type:** Quantitative totals (e.g., unemployment count, crime count) associated with geographic regions.
*   **Audience:** Readers attempting to understand regional severity independent of population size.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Symbol Maps.
*   **Reason:** If you must map absolute data (raw counts), use a symbol map (proportional circles) instead of a choropleth, as the size of the region should not conflate with the magnitude of the value [@muth_choroplethmaps_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the context of the total magnitude (e.g., a small county might have a high rate but very few actual cases).
*   **The Risk:** Readers may overinterpret a high rate in a statistically insignificant, sparsely populated area.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Mapping raw counts (e.g., "Total Unemployed People") directly onto a standard geographic map.
*   **Why it fails:** It visually emphasizes large cities or populous states regardless of the actual economic situation relative to the workforce [@muth_choroplethmaps_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does your map look almost identical to a population density map of the same region?
*   **The Test:** Check if the highest values align exclusively with major metropolitan areas.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Divide your value by the population of the region and multiply by a standard unit (e.g., `(unemployed / population) * 100`).
*   **Best Fix:** Use relative data for the choropleth coloring and include the absolute numbers in a tooltip for context [@muth_choroplethmaps_2018].
