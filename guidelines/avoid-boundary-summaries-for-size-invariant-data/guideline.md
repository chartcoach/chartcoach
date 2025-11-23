---
id: avoid-boundary-summaries-for-size-invariant-data
title: Avoid Expanding Boundaries for Constant-Size Phenomena
bibliography: references.bib
description: Summary displays with expanding boundaries (like cones of uncertainty)
  cause users to misinterpret uncertainty as physical growth.
labels:
- chart:map
- chart:summary-display
- visual:size
- visual:area
- impact:accuracy
- data:geospatial
- data:uncertainty
- audience:novice
---

## The Rule <!-- role: advice -->
Do not use summary displays with expanding boundaries (such as "cones of uncertainty") to represent uncertainty for phenomena that do not physically grow in size over time.

## The Logic <!-- role: reason -->
Summary displays often rely on boundaries (like the edge of a cone) to denote confidence intervals. These boundaries are visually salient features that attract bottom-up attention. When the uncertainty grows over time, the visual area of the display expands.
*   **The Principle:** Visual Salience and Attribute Mapping. Novice viewers map the salient feature of "expanding visual area" to the physical attribute of "size," rather than the abstract concept of "uncertainty" [@padilla_effects_2017].
*   **The Evidence:** In Experiment 1, participants viewing a cone of uncertainty were significantly more likely to incorrectly report that a hurricane would get physically larger and more intense over time compared to those viewing ensemble displays [@padilla_effects_2017].

## Where to Apply <!-- role: context -->
This advice applies to geospatial visualizations where the goal is to show the potential path or value of an object that maintains a relatively stable physical size.
*   **User Goal:** Understanding the future path or value of a distinct entity (e.g., a storm, a vehicle, a particle).
*   **Data Type:** Uncertainty data projected over time or space (forecasts).
*   **Audience:** Novice audiences or the general public who may lack training in statistical probability distributions.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The phenomenon actually expands physically over time (e.g., a spreading oil spill or forest fire).
*   **Reason:** In this case, the visual expansion of the summary boundary matches the physical reality of the phenomenon, making the intuitive mapping correct.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Summary displays (like cones) are often cleaner and reduce visual clutter compared to showing all data points.
*   **The Risk:** By removing the boundary, you may need to use more complex visualizations (like ensembles) that can suffer from visual crowding or "spaghetti" effects.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding a text disclaimer (e.g., "The cone shows uncertainty, not size").
*   **Why it fails:** Visual salience often overrides textual instructions. Viewers process the "growing shape" pre-attentively before reading or comprehending the legend [@padilla_effects_2017].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the visualization get visually larger as you move along the x-axis (time) or space?
*   **The Test:** Ask a user, "Does the object shown here get bigger or smaller at the end of the path?" If they say "bigger" but the object size is constant, the design has failed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove the hard boundary lines and use a gradient or fuzzy edge to represent the probability distribution.
*   **Best Fix:** Replace the summary display with an **ensemble display** (showing individual potential paths), which decouples visual spread from physical size [@padilla_effects_2017].
