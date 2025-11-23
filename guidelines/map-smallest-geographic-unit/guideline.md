---
id: map-smallest-geographic-unit
title: Map the Smallest Geographic Unit Possible
bibliography: references.bib
description: Use granular geographic units (like counties instead of states) to reveal
  detailed regional patterns.
labels:
- chart:map
- data:geospatial
- impact:clarity
- task:discovery
---

## The Rule <!-- role: advice -->
Choose the most granular geographic unit your data allows (e.g., counties instead of states, or NUTS2 regions instead of countries).

## The Logic <!-- role: reason -->
Using smaller units provides a "refined image of the data," allowing readers to spot detailed regional patterns that are obscured when data is aggregated into larger shapes. Large regions often hide the variation between cities and rural areas [@muth_choroplethmaps_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying localized clusters, trends, or "hot spots."
*   **Data Type:** Data available at multiple levels of administrative hierarchy.
*   **Audience:** Readers looking for nuance or finding their specific local area.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Winner-takes-all systems.
*   **Reason:** In contexts like US presidential elections where the state-level result determines the outcome, a state-level map is more informative regarding the political result than a county-level map [@muth_choroplethmaps_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Increased visual noise and data density; the map may become harder to read as a quick overview if the units are too small or the borders too thick.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Aggregating data to the state/country level when county/district data is available.
*   **Why it fails:** It creates a monolithic view that erases the contrast between neighboring sub-regions (e.g., urban vs. rural divides) [@muth_choroplethmaps_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the map consist of large, uniform blocks of color that hide internal variety?
*   **The Test:** Check if neighboring sub-regions usually have vastly different demographics. If yes, your map units are likely too large.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Switch the map geometry to the next level down in the administrative hierarchy (e.g., US States → US Counties).
