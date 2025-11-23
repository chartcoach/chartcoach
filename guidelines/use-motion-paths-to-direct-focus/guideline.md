---
id: use-motion-paths-to-direct-focus
title: Use Motion to Direct Attention to End Points
bibliography: references.bib
description: Utilize the trajectory of moving objects to guide viewer fixation toward
  specific destination elements.
labels:
- visual:motion
- task:navigate
- impact:focus
- audience:novice
---

## The Rule <!-- role: advice -->
Use the movement of an object to physically drag the user's eye to a specific location. Ensure the motion ends exactly where you want the user to look next.

## The Logic <!-- role: reason -->
Visual attention locks onto moving objects. According to eye-tracking studies, the onset of motion triggers a rapid alignment of the eye to the object, and the eye subsequently tracks the path. Crucially, fixations tend to cluster at the **end point** of the motion path [@faraday_designing_1997]. If an object moves and stops next to a label or a new component, the eye is naturally deposited there.

## Where to Apply <!-- role: context -->
*   **User Goal:** Guiding the user through a linear process or narrative sequence.
*   **Data Type:** Animated diagrams, process flows, or dynamic visualizations.
*   **Audience:** Users unfamiliar with the spatial layout of the information.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The moving object is decorative or secondary.
*   **Reason:** If the motion is irrelevant, tracking it will distract the user from the actual primary content (e.g., reading a static label elsewhere).

## The Price <!-- role: costs -->
*   **The Sacrifice:** The user cannot attend to other parts of the screen while tracking the object.
*   **The Risk:** If the motion is too fast, the eye will shift rather than track, potentially causing the user to miss the intermediate path entirely [@faraday_designing_1997].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Moving an object past the target and then having it disappear.
*   **Why it fails:** The eye follows the object off-screen or into empty space, rather than landing on the relevant information.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the animation end at a blank space?
*   **The Test:** Watch the animation and note where your eye rests immediately after the movement stops. Is it the most important element?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the animation path so the object stops adjacent to the next label or element to be read.
*   **Best Fix:** Redesign the layout so that the logical flow of information matches the spatial trajectory of the animated elements.
