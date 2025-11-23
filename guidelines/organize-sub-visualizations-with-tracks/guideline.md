---
id: organize-sub-visualizations-with-tracks
title: Organize Sub-Visualizations with Tracks
bibliography: references.bib
description: Use concentric tracks or lanes to arrange related sub-visualizations,
  allowing simultaneous exploration of independent facets.
labels:
- chart:radial
- task:correlation
- visual:layout
- impact:organization
- data:hierarchical
- audience:analyst
---

## The Rule <!-- role: advice -->
Use the "Track" pattern (concentric lanes or parallel tracks) to organize multiple sub-visualizations that share a common coordinate system but represent different facets of data (e.g., Cause, Risk, Location).

## The Logic <!-- role: reason -->
The Track pattern allows designers to place visualizations in a lane-like fashion. This spatial organization highlights the "individual nature of each sub-visualization" while simultaneously allowing the user to see "relationships across the four sub-visualizations" (co-occurrence) [@ola_beyond_2016]. It provides a structure where users can explore different perspectives (e.g., demography vs. geography) independently without losing the context of the whole.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing different aspects of the same entities (e.g., exploring Age Groups alongside Risk Factors and Geographic Location).
*   **Data Type:** High-dimensional data that can be aligned along a shared axis (such as a circular/polar axis for age groups).
*   **Audience:** Users needing to generate hypotheses about relationships between disparate data categories.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Linear comparison of time.
*   **Reason:** If the shared axis is time, a standard stacked linear layout (like a timeline) might be more intuitive than concentric rings, which can distort time perception.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Space and Simplicity. Concentric tracks create a "dense lens" that requires interaction (filtering/selection) to manage visual overload.
*   **The Risk:** Misalignment. If the coordinate systems of the tracks do not align perfectly (e.g., different sorting orders), the "stacking" effect for comparison is lost.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Separate charts side-by-side.
*   **Why it fails:** Separation makes it difficult to scan across dimensions to find correlations (e.g., matching a specific age group to its specific risk factors) [@ola_beyond_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are your facets (Age, Risk, Cause) scattered across the screen in different boxes?
*   **The Test:** Can you draw a straight line (or ray) through the visualization and intersect all related attributes for a single data entity?

## How to Fix <!-- role: fix -->
*   **Best Fix:** Adopt a polar coordinate system and layer the facets as concentric rings (Tracks), moving from the most granular entity (e.g., Age) outward to broader categories (e.g., Location) [@ola_beyond_2016].
