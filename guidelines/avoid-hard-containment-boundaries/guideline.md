---
id: avoid-hard-containment-boundaries
title: Avoid Hard Boundaries for Probabilistic Areas
bibliography: references.bib
description: Use visual techniques that break the 'containment' heuristic to prevent
  users from viewing areas outside a shape as safe.
labels:
- chart:area
- visual:border
- task:safety-assessment
- impact:risk-communication
- audience:novice
- concept:heuristics
---

## The Rule <!-- role: advice -->
Avoid using solid, hard-edged shapes (like polygons with distinct borders) to represent uncertainty distributions. Use ensembles or gradients instead.

## The Logic <!-- role: reason -->
Hard boundaries trigger a "containment heuristic," where users view the region inside the line as "affected" and the region immediately outside as "safe." This binary thinking contradicts the continuous nature of probability.
*   **The Principle:** Containment Heuristic. Users categorize risk based on whether a point falls inside or outside a visual container.
*   **The Evidence:** Participants explicitly referenced "containment" (e.g., "it's in the blue area") significantly more often when viewing standard cones than when viewing ensemble visualizations. Ensembles encouraged a more distributed assessment of damage, even outside the primary cluster [@ruginski_non-expert_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** preventing users from feeling a false sense of security just outside the probable area.
*   **Data Type:** Geospatial risk, flood maps, or hurricane cones.
*   **Audience:** Non-experts prone to binary categorization.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the boundary represents a hard threshold (e.g., "Evacuation Zone A").
*   **Reason:** In administrative contexts, binary decisions (stay/go) are required, and hard boundaries map to these distinct actions.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to easily calculate "area" or define a simple perimeter.
*   **The Risk:** Gradients (fuzzy cones) resulted in lower overall damage ratings in the study, potentially leading to under-reaction if not calibrated correctly [@ruginski_non-expert_2016].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Just removing the outline stroke but keeping the solid fill.
*   **Why it fails:** The contrast edge between the fill and the background still creates a hard cognitive boundary.

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you trace the exact edge of the danger zone with a pen?
*   **The Test:** Place a point 1mm outside your shape. Does it look 100% safe compared to a point 1mm inside?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Feather the edges of the shape (fuzzy boundary).
*   **Best Fix:** Use an ensemble (spaghetti) visualization, which naturally disperses boundaries and reduces reliance on the containment heuristic.
