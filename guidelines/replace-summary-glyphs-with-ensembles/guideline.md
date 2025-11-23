---
id: replace-summary-glyphs-with-ensembles
title: Replace Summary Uncertainty Glyphs with Representative Ensembles
bibliography: references.bib
description: Use discrete ensemble paths instead of summary cones to avoid confusing
  uncertainty with event size.
labels:
- chart:map
- chart:flow
- visual:position
- impact:clarity
- data:geospatial
- data:uncertainty
- audience:general-public
---

## The Rule <!-- role: advice -->
Visualize prediction uncertainty by displaying a representative set of discrete outcome paths (ensembles) rather than a single summary glyph, such as a cone or error band.

## The Logic <!-- role: reason -->
Summary visualizations, particularly the "Cone of Uncertainty" used in hurricane forecasting, suffer from a "glyph size" bias. Users frequently misinterpret the expanding width of the cone as an increase in the storm's physical size or intensity, rather than an increase in spatial uncertainty over time. By displaying discrete tracks, the visualization uses an **implicit uncertainty** representation. This allows the viewer to infer probability from the spatial distribution of the lines, dissociating the concept of "uncertainty" from the physical attributes of the phenomenon [@liu_visualizing_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Communicating the potential path and strike probability of a dynamic phenomenon (e.g., a hurricane).
*   **Data Type:** Spatiotemporal prediction ensembles (e.g., Monte Carlo simulations of storm tracks).
*   **Audience:** Non-expert users who may misinterpret abstract statistical summaries.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The dataset contains thousands of raw ensemble members without a filtering or clustering algorithm.
*   **Reason:** Displaying all raw data results in "spaghetti plots" with severe overdrawing and clutter, making individual paths indistinguishable and the display illegible [@liu_visualizing_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the clean, simplified aesthetic of a single summary polygon.
*   **The Risk:** Without careful selection (representative sampling), the visualization may appear chaotic or cluttered (the "spaghetti plot" effect).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Overplotting thousands of raw simulation lines.
*   **Why it fails:** It creates visual noise that obscures the underlying spatial distribution and makes it impossible to encode additional variables like intensity [@liu_visualizing_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the uncertainty represented by a solid filled shape or a single bounding outline?
*   **The Test:** Ask a user if the storm is getting "bigger" or "more uncertain" as time progresses. If they say "bigger" solely because the graphic gets wider, the design has failed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Draw a random subset of the simulation lines (though this may be irregular).
*   **Best Fix:** Use an algorithm to extract a "representative sample" (e.g., recursively finding median tracks) to ensure the subset accurately preserves the spatial distribution of the full ensemble without clutter [@liu_visualizing_2019].
