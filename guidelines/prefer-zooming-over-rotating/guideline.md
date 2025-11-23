---
id: prefer-zooming-over-rotating
title: Prefer Zooming Over Rotating for Inspection
bibliography: references.bib
description: To preserve feature binding (memory of which part is which color), allow
  users to scale/zoom rather than rotate.
labels:
- chart:3D-model
- task:explore
- task:zoom
- interaction:navigation
- impact:accuracy
- audience:general
---

## The Rule <!-- role: advice -->
When designing interactions for exploring multi-part visual structures, prioritize **scaling** (expanding/contracting or zooming) over rotation. If the user needs to inspect details, allow them to magnify the view rather than forcing them to turn the object.

## The Logic <!-- role: reason -->
Rotation imposes a severe attentional bottleneck that scaling does not. In Experiment 1C of [@xu_capacity_2015], participants performed a scaling task (imagining an object expanding/shrinking) and maintained high capacity for feature binding, statistically identical to static views. Unlike rotation, which requires a singular focus to update spatial coordinates, scaling allows attention to remain distributed over the entire object, preserving the links between parts and their colors.

## Where to Apply <!-- role: context -->
*   **User Goal:** Checking details or verifying the identity of multiple parts in a complex assembly.
*   **Interaction Design:** Choosing the primary mouse-action or gesture for a 3D viewer.
*   **Data Type:** Dense clusters or multi-colored 3D models.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The structure is occluded (parts hiding behind other parts).
*   **Reason:** Scaling cannot reveal hidden surfaces; rotation is geometrically necessary to see the "back" of an object. In this case, rotation is unavoidable, but the design should acknowledge the memory cost.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Depth perception. Rotation provides "structure-from-motion" cues that help users understand 3D shape; scaling provides fewer 3D shape cues.
*   **The Risk:** Users may lose context of where they are in the overall structure if zooming is too aggressive (loss of global context).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Auto-rotating a model to "show it off."
*   **Why it fails:** This consumes the user's attentional resources, making it harder for them to actually read or remember the data encoded on the model surfaces.
*   **The Wrong Fix:** Coupling zoom and rotate simultaneously.
*   **Why it fails:** This introduces the high cognitive cost of rotation into an interaction (zooming) that would otherwise be low-cost.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the user interface default to a "spin" tool rather than a "magnify" tool?
*   **The Test:** Observe if users struggle to answer questions about the properties of the object after manipulating it. Compare error rates between a zoom-only trial and a rotate-only trial.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Set the default mouse interaction to Zoom/Pan instead of Orbit.
*   **Best Fix:** Provide "exploded views" or distinct static projections that allow inspection of components without requiring continuous mental transformation.
