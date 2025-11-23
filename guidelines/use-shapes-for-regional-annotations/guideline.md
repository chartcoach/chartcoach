---
id: use-shapes-for-regional-annotations
title: Use Shapes To Annotate Regions
bibliography: references.bib
description: Use circles or shapes instead of arrows when annotating broad regional
  patterns on a map.
labels:
- chart:map
- visual:annotations
- visual:shape
- task:group
- impact:clarity
---

## The Rule <!-- role: advice -->
Use circles (or enclosing shapes) instead of arrows to connect annotations to the map when describing regional patterns.

## The Logic <!-- role: reason -->
Arrows imply a relationship to a specific, single data point. When the insight refers to a cluster or a general area, an arrow is misleading. Circles or shapes encompass the area, visually reinforcing that you are "describing regional patterns rather than labeling specific data points" [@mintzer_map_annotations_2024].

## Where to Apply <!-- role: context -->
*   **User Goal:** Highlighting a cluster of data (e.g., "Lots of solar plants in sunny California").
*   **Data Type:** Scatter maps or dot density maps where points aggregate into clouds.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Labeling a specific outlier or a single point of interest.
*   **Reason:** An arrow effectively points to a single coordinate; a circle implies a group.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Shapes take up more "ink" on the chart than thin lines.
*   **The Risk:** If the circles are too thick or opaque, they might obscure the underlying data points.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Drawing arrows that point generally into the middle of a cloud of points.
*   **Why it fails:** It suggests the annotation applies only to the specific dot the arrow touches, rather than the group.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using arrows that point to "areas" rather than "items"?
*   **The Test:** Ask a user what the annotation refers to. If they point to a single dot, but you meant the whole state, use a circle.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Replace lines/arrows with transparent circles outlining the region.
*   **Best Fix:** Design the annotation layer to use visual encodings (shapes) that match the semantic scope (regions vs. points).
