---
id: explicitly-visualize-state-changes
title: Explicitly Visualize State Changes
bibliography: references.bib
description: Use distinct visual changes (color, shape) to signal reactions or state
  changes, rather than relying on contact alone.
labels:
- visual:color
- visual:shape
- task:identify
- impact:comprehension
---

## The Rule <!-- role: advice -->
When two objects interact or combine, visually alter their properties (color, shape, or size) to signify that a reaction has occurred. Do not rely solely on them touching.

## The Logic <!-- role: reason -->
Simply animating objects to touch or overlap is often insufficient for users to understand that a functional change has occurred. In recall tests, users frequently missed "reactions" when they were shown only as motion/contact. Re-authoring designs to include explicit changes—such as a "flash" or a change in color/shape of the combined object—significantly improved comprehension of the causal event [@faraday_designing_1997].

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding cause-and-effect or chemical/mechanical processes.
*   **Data Type:** Simulations, flowcharts, or state-transition diagrams.
*   **Audience:** Novices who do not inherently know that contact implies a reaction (e.g., chemistry students).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Physical stacking or grouping tasks.
*   **Reason:** If the objects are merely being collected and do not change state, altering their appearance would be misleading.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Requires creating additional assets (the "combined" state graphic).
*   **The Risk:** Over-dramatizing minor interactions (like simple collisions) can create false importance.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Just playing a sound effect when objects touch.
*   **Why it fails:** Visual attention is dominant; if the visual state doesn't change, the user may miss the implication of the sound.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do objects touch and remain looking exactly the same?
*   **The Test:** Show the animation without sound. Can the user tell that a transformation or reaction took place?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a brief "flash" or "pulse" animation at the moment of contact.
*   **Best Fix:** Replace the separate objects with a new, distinct "combined" object that has different visual properties (color/shape) to represent the new state.
