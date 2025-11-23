---
id: reinforce-static-elements-during-motion
title: Reinforce Static Elements During Motion
bibliography: references.bib
description: Use reveals or highlights to draw attention to static elements if other
  parts of the screen are moving.
labels:
- visual:attention
- visual:hierarchy
- task:monitor
- impact:balance
---

## The Rule <!-- role: advice -->
If you need the user to notice a static object while other animation is happening, you must actively highlight or "reveal" that static object.

## The Logic <!-- role: reason -->
Static presentation elements are often neglected in favor of elements that are revealed or in motion. The human visual system prioritizes motion (attentional capture). In study data, static labels received far fewer fixations than moving objects or labels that were dynamically revealed [@faraday_designing_1997]. To compete with motion, static elements need a "state change" (appearing, highlighting) to trigger attention.

## Where to Apply <!-- role: context -->
*   **User Goal:** Reading a legend, axis label, or reference value while data is animating.
*   **Data Type:** Dashboards with live updates or animated charts.
*   **Audience:** All users (attentional capture by motion is a low-level biological reflex).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The static elements are background context (e.g., gridlines).
*   **Reason:** You generally want these to remain in the background and not compete for attention.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Increases visual noise if too many things are flashing or highlighting.
*   **The Risk:** "Pop-out" fatigue where the user stops reacting to highlights.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Making the static label larger or bold at the start, then starting animation elsewhere.
*   **Why it fails:** Once the animation starts, the eye is drawn away from the large static text.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there important labels that sit quietly on screen while the main action happens elsewhere?
*   **The Test:** Ask a user to recall the static label after watching the animation.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Blink or highlight the static element briefly when it becomes relevant to the moving action.
*   **Best Fix:** Do not reveal the static element until the moment it is needed, using its appearance (onset) to grab attention.
