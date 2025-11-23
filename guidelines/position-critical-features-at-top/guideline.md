---
id: position-critical-features-at-top
title: Position Critical Features at the Object's Top
bibliography: references.bib
description: Users preferentially track the top part of an object during mental rotation;
  place the most important data there.
labels:
- chart:3D-model
- visual:position
- visual:layout
- task:rotate
- impact:attention
- audience:general
---

## The Rule <!-- role: advice -->
If a 3D object must be mentally rotated, ensure the most critical visual feature (or the specific part the user must track) is positioned at the **top** of the object or the topmost quadrant of the screen before the rotation begins.

## The Logic <!-- role: reason -->
Eye-tracking experiments in [@xu_capacity_2015] reveal a strong bias: participants spontaneously select the topmost part of an object to track during rotation. This top part serves as an attentional "handle" or "arrowhead" to drive the transformation. Consequently, change detection rates for feature swaps were significantly higher (approx. 80%) when the swap involved the top part, compared to near-chance levels when it did not.

## Where to Apply <!-- role: context -->
*   **User Goal:** Tracking a specific component through a spatial transformation.
*   **Data Type:** 3D objects with multiple distinct colored or labeled parts.
*   **Audience:** General users, as this appears to be a default biological heuristic (related to "top" biases in spatial descriptions).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Highly trained experts (e.g., organic chemists).
*   **Reason:** Experts may have developed analytical strategies (like verbal coding or distinct axis manipulation) that override the default visual spotlight limitations [@xu_capacity_2015].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Layout flexibility. You are forced to prioritize vertical hierarchy based on importance rather than other logical ordering schemes.
*   **The Risk:** Neglecting the "bottom" data. Information located in the bottom quadrants is significantly more likely to be ignored or forgotten during the transformation.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Placing key legends or reference markers at the bottom of the screen during a rotation task.
*   **Why it fails:** The user's gaze is "locked" to the top of the rotating structure to maintain spatial reference.
*   **The Wrong Fix:** Assuming center-fixation.
*   **Why it fails:** Even when initial fixation starts at the center, saccades almost immediately jump to the top part to begin the rotation process.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the "hero" data point or the primary outlier located at the bottom or periphery of the 3D cluster?
*   **The Test:** Eye-tracking or simply asking the user "which part did you look at while turning it?"

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Re-orient the default view of the model so the critical component is at the 12 o'clock position.
*   **Best Fix:** Add explicit visual markers (like an axis arrow or a "front" label) to the top of the object to aid the user's attentional tracking mechanism [@xu_capacity_2015].
