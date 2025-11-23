---
id: use-rectangular-cartograms-for-adjacency
title: Use Rectangular Cartograms for Topology Tasks
bibliography: references.bib
description: Rectangular cartograms are most effective when users need to determine
  which regions are neighbors.
labels:
- chart:cartogram
- chart:rectangular-cartogram
- task:topology
- task:adjacency
- visual:topology
- data:geospatial
---

## The Rule <!-- role: advice -->
Select rectangular cartograms when the user's primary task is to identify neighboring regions or understand the topological structure of a map.

## The Logic <!-- role: reason -->
Rectangular cartograms schematize a map while strictly maintaining the "dual graph" of the topology (which country touches which). This abstraction makes it easier to trace borders compared to deformed polygons or separated shapes.
*   **The Principle:** Topological Preservation.
*   **The Evidence:** According to [@zeng_review_2023], citing [@nusrat_evaluating_2018], rectangular cartograms (E-2) ranked highest in accuracy for "filter" tasks related to finding adjacency, significantly outperforming non-contiguous and Dorling types.

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding geopolitical relationships or network connectivity between regions.
*   **Data Type:** Geospatial data where "neighboring" status is relevant analysis context.
*   **Audience:** Users needing a schematic overview of connectivity.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to recognize the geographic shape of a specific country.
*   **Reason:** Rectangular distortion makes shape recognition (Locate tasks) more difficult than contiguous or non-contiguous maps [@nusrat_evaluating_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Accurate area comparison and shape recognition.
*   **The Risk:** Users may misinterpret the statistical values (area sizes) due to aspect ratio issues.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using non-contiguous cartograms to show neighbors.
*   **Why it fails:** Non-contiguous cartograms separate regions, destroying the visual links required to determine adjacency instantly.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the regions share borders?
*   **The Test:** Ask, "Is Region A a neighbor of Region B?" If the user has to guess across whitespace (Non-contiguous) or gap (Dorling), the design has failed this task.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Ensure regions share borders (Contiguous or Rectangular).
*   **Best Fix:** Use a Rectangular cartogram, as it simplifies the borders into easy-to-trace straight lines.
