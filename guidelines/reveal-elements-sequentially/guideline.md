---
id: reveal-elements-sequentially
title: Reveal Elements Sequentially
bibliography: references.bib
description: Introduce visual elements one by one to control the viewer's scan path.
labels:
- visual:layout
- task:search
- impact:clarity
- visual:animation
---

## The Rule <!-- role: advice -->
Do not reveal multiple new objects or labels simultaneously. Display related elements one at a time in the desired order of processing.

## The Logic <!-- role: reason -->
When multiple items appear at once, the designer loses control over the viewer's attention. Eye-tracking reveals that simultaneous appearance results in "little order" in fixations, as the eye jumps randomly between new elements [@faraday_designing_1997]. Sequential revealing forces the eye to process information in a coherent, linear narrative structure.

## Where to Apply <!-- role: context -->
*   **User Goal:** Learning a complex structure or relationship between parts.
*   **Data Type:** Complex diagrams, charts with many annotations, or scene setups.
*   **Audience:** Users seeing the visualization for the first time.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Comparative views (small multiples) where the "Gestalt" or overall pattern is more important than individual details.
*   **Reason:** Simultaneous appearance allows for immediate pattern recognition across the set.

## The Price <!-- role: costs -->
*   **The Sacrifice:** It takes longer to establish the full scene.
*   **The Risk:** If the sequence is too slow, the user may lose the context of how the parts fit into the whole.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Showing a complex diagram all at once and using a mouse pointer to point at parts.
*   **Why it fails:** The user's eye may wander to other interesting parts of the complex diagram before the pointer gets there.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the screen go from blank to full complexity in one frame?
*   **The Test:** Ask a user what they looked at first. If users give different answers, the reveal is uncontrolled.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a slight time delay (e.g., 0.5s) between the appearance of related items.
*   **Best Fix:** Script the appearance of objects to match the causal or logical flow of the data (e.g., Input -> Process -> Output).
