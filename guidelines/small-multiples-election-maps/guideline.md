---
id: small-multiples-election-maps
title: Use Small Multiples for Multi-Party Maps
bibliography: references.bib
description: Display regional vote shares for multiple parties using side-by-side
  maps rather than a single complex map.
labels:
- chart:map
- task:compare
- visual:layout
- impact:clarity
- data:geospatial
- audience:general
---

## The Rule <!-- role: advice -->
Place multiple choropleth maps next to each other (small multiples) when visualizing the vote shares of different parties across the same regions.

## The Logic <!-- role: reason -->
A standard choropleth map can effectively show the density of only one variable (one party) at a time. To compare where different parties are strong, you cannot layer them easily. By using small multiples, you allow the eye to scan across maps to "reveal interesting patterns," which is "especially apparent for smaller parties" that might otherwise be invisible on a winner-take-all map [@muth_german_election_2021].

*   **The Principle:** Small Multiples / Faceting
*   **The Evidence:** [@muth_german_election_2021]

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the geographic strongholds of rival parties (e.g., "Where do the Greens win vs. the FDP?").
*   **Data Type:** Regional vote shares for 3+ distinct parties.
*   **Audience:** Readers analyzing the geographic distribution of political support.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Determining the absolute winner per district ("First Vote").
*   **Reason:** If the goal is simply to show who won each district, a single map with categorical coloring is more efficient than separate density maps.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate. Small multiples require space for multiple maps.
*   **The Risk:** If the maps are too small, individual districts become difficult to see or interact with.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Trying to color-mix or use complex patterns to show multiple party strengths in a single map view.
*   **Why it fails:** The resulting map becomes muddy and unreadable.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you toggling heavily between layers, or trying to interpret a legend with mixed colors?
*   **The Test:** Can you instantly see where the "Green" party is strongest without clicking anything? If not, use small multiples.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Create separate maps for each major party and stack them vertically.
*   **Best Fix:** Arrange the maps in a grid (side-by-side) with a shared color scale (0-100% or similar) to allow for direct visual comparison of density [@muth_german_election_2021].
