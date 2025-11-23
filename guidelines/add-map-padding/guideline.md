---
id: add-map-padding
title: Add Padding to Map Borders
bibliography: references.bib
description: Add padding around map borders to reduce clutter and let the visualization
  breathe.
labels:
- chart:map
- visual:layout
- visual:whitespace
- impact:aesthetics
- task:cleanup
---

## The Rule <!-- role: advice -->
Add approximately 5% padding around the borders of your map.

## The Logic <!-- role: reason -->
Cluttered visualizations often suffer from elements being cramped. Adding padding gives the "whole map more space to breathe" [@mintzer_map_annotations_2024]. This whitespace acts as a buffer, making the density of the actual data and annotations feel less overwhelming.

## Where to Apply <!-- role: context -->
*   **User Goal:** Improving the visual appeal of a dense or detailed map.
*   **Data Type:** Geographic maps where the landmass touches the edges of the canvas.
*   **Audience:** General audiences on web or mobile screens.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Small sparkline maps or thumbnails.
*   **Reason:** Space is at a premium and padding would render the map features too small to see.

## The Price <!-- role: costs -->
*   **The Sacrifice:** The map scale becomes slightly smaller to accommodate the margins.
*   **The Risk:** If the map is already small, details might become harder to resolve.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Cropping the map tightly to the landmass to maximize size.
*   **Why it fails:** It creates tension at the edges and contributes to a feeling of clutter.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the map edges or annotations touch the boundary of the image or container?
*   **The Test:** Check if there is consistent white space framing the content.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Increase the margin or padding settings in your visualization tool.
*   **Best Fix:** Calculate a ~5% buffer around the bounding box of your map geometry.
