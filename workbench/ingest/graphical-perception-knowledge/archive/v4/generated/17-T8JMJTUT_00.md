---
id: cartogram-for-locating
title: "Use contiguous or non-contiguous cartograms for locating regions"
tags:
  - impact:perceptual
  - impact:cognitive
  - chart:map
  - chart:map.cartogram
  - chart:map.cartogram.contiguous
  - chart:map.cartogram.non-contiguous
  - task:lookup
  - task:spatial-lookup
  - data:spatial
  - data:quantitative
  - visual:position
  - visual:shape
  - medium:static

sources:
  - type: research
    ref: Nusrat, Alam, & Kobourov, 2018
    url: https://doi.org/10.1109/TVCG.2016.2642109
    note: "Compared four cartogram types on a 'locate' task. Found contiguous and non-contiguous types were significantly more accurate and faster than rectangular cartograms. Non-contiguous was fastest overall, while contiguous was most accurate."

---

## Guidance

For tasks that require users to find or locate specific geographic regions on a map, prefer contiguous or non-contiguous cartograms. Avoid rectangular and Dorling cartograms for this purpose.

## Why

Contiguous and non-contiguous cartograms are more effective because they better preserve the relative positions of regions compared to other types. Non-contiguous cartograms also preserve the original region shape, providing an additional strong cue for identification. Research shows that rectangular cartograms are the least accurate and slowest for location tasks, as they heavily distort both shape and relative position.

## When it applies

- When a key task for the viewer is to identify the location of a specific country, state, or region within the cartogram.
- When the audience has some familiarity with the underlying geography.

## Exceptions

- If the exact location is not important and the goal is purely schematic (e.g., showing adjacencies in a diagram), a rectangular cartogram might be used, but be aware that it will perform poorly for any location task.

## Trade-offs

- **Non-contiguous cartograms** are fastest for location but sacrifice the display of adjacency (topology).
- **Contiguous cartograms** preserve adjacency but are slightly slower for location tasks and distort shapes.
- **Rectangular and Dorling cartograms** are significantly less effective for location, making them a poor choice if this task is important.

## Signs of Trouble

- **The "Where's Waldo?" Effect:** Users spend a long time scanning the map to find a familiar region.
- **Frequent Misidentification:** Users consistently point to the wrong area when asked to locate a region.
- **Over-reliance on Labels:** The visualization is incomprehensible without every single region being labeled.

## How to Improve

- **Quick Fix: Add an Inset Map.** Include a small, standard geographic map for reference. Interactive link-and-brush highlighting between the inset map and the cartogram can further aid location.
- **Moderate Redesign: Switch Cartogram Type.** If using a rectangular or Dorling cartogram, switch to a **non-contiguous cartogram** for the best balance of speed and accuracy, or a **contiguous cartogram** if preserving adjacency is also critical.
- **Comprehensive Redesign: Re-evaluate the Chart Choice.** If locating regions is the primary task, a cartogram may not be the best choice. Consider a standard choropleth map or a non-geographic chart like a sorted bar chart if the main goal is to compare the data values.
