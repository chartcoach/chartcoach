---
id: prioritize-spatial-proximity-for-grouping
title: Use Space for Primary Segmentation
bibliography: references.bib
description: Spatial proximity dominates color or shape when users try to identify
  clusters.
labels:
- visual:position
- visual:layout
- task:segment
- task:cluster
- impact:clarity
- principle:gestalt
---

## The Rule <!-- role: advice -->
Use spatial proximity as the primary method for defining groups (clusters); rely on feature cues (color, shape) only for secondary grouping or when spatial separation is impossible.

## The Logic <!-- role: reason -->
Spatial clustering is largely based on the Gestalt cue of proximity. It is a parallel, mandatory cue that tends to dominate over other grouping cues like color. While viewers *can* segment by feature (e.g., "all red dots"), spatial grouping happens faster and more automatically [@szafir_four_2016].
*   **The Principle:** Gestalt Proximity Dominance
*   **The Evidence:** Studies show proximity grouping is mandatory and often overrides color grouping (Oyama, 1961) [@szafir_four_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Quickly identifying distinct categories or clusters in data.
*   **Data Type:** Scatterplots, network graphs, or any positional mapping.
*   **Audience:** All users (relies on low-level vision).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** X/Y coordinates are strictly reserved for continuous quantitative variables (e.g., a geographical map).
*   **Reason:** You cannot move the points to create clusters without falsifying the data.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate.
*   **The Risk:** Creating white space to separate groups reduces the resolution available for data plotting.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Placing two distinct groups right next to each other and coloring one red and one blue to "separate" them.
*   **Why it fails:** Users will initially perceive one large "blob" of data, then require cognitive effort to separate the colors. Space splits them instantly.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are distinct groups touching or overlapping?
*   **The Test:** Squint your eyes until colors blur. Can you still see separate groups? If not, you are relying entirely on color, not space.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add white space/padding between groups.
*   **Best Fix:** Re-layout the visualization (e.g., force-directed layout) to prioritize cluster separation.
