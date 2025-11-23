---
id: visualize-ensembles-for-trajectory-uncertainty
title: Use Ensembles Instead of Expanding Cones
bibliography: references.bib
description: Use ensemble (spaghetti) plots rather than summary cones to prevent users
  from confusing increasing uncertainty with increasing object size.
labels:
- chart:ensemble
- chart:spaghetti-plot
- task:forecast
- visual:shape
- impact:comprehension
- data:geospatial
- audience:non-expert
- concept:uncertainty
---

## The Rule <!-- role: advice -->
When visualizing the uncertain path of a moving object (like a storm), display an ensemble of discrete potential tracks rather than a single solid "cone of uncertainty" or summary polygon.

## The Logic <!-- role: reason -->
Non-experts frequently misinterpret the visual widening of a summary cone as a change in the physical size or intensity of the object itself (the "size heuristic"), rather than an increase in positional uncertainty.
*   **The Principle:** Discrete Instance Visualization. By showing individual tracks, you explicitly communicate that the variance lies in the *position*, not the *magnitude* of the event.
*   **The Evidence:** Participants viewing ensemble displays were significantly less likely to believe a hurricane would get larger or more intense over time compared to those viewing standard cones, where the widening shape was conflated with storm growth [@ruginski_non-expert_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Communicating risk or trajectory forecasts where uncertainty increases over time.
*   **Data Type:** Predictive models generating multiple potential paths (e.g., weather forecasting, financial projections).
*   **Audience:** Non-experts or laypeople who may not understand statistical conventions like confidence intervals.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the display resolution is extremely low or the number of tracks is massive.
*   **Reason:** Too many lines can cause occlusion or "clutter," making the map unreadable, though the paper suggests even "spaghetti" plots perform better cognitively than cones for this specific misconception.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the clean, simplified aesthetic of a single polygon.
*   **The Risk:** Users might try to count the lines ("count heuristic") to calculate exact probabilities, which may be misleading if the ensemble selection isn't perfectly representative.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding a text legend explaining the cone.
*   **Why it fails:** Visual dominance often overrides textual instructions; users still intuitively process the large shape as a "large storm" despite legends [@ruginski_non-expert_2016].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the visualization look like a single object growing larger as it moves across the screen?
*   **The Test:** Ask a user, "Does the object get bigger or stronger later in the forecast?" If they say yes based solely on the graphic, switch to an ensemble.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove the solid fill of the cone and replace it with several representative lines.
*   **Best Fix:** Generate a robust ensemble visualization showing a distribution of specific possible tracks to dissociate position from size.
