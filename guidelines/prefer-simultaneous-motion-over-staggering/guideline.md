---
id: prefer-simultaneous-motion-over-staggering
title: Prefer Simultaneous Motion Over Staggering
bibliography: references.bib
description: Use direct, simultaneous animations rather than staggered start times
  for visual tracking tasks.
labels:
- chart:scatterplot
- visual:animation
- task:track
- impact:clarity
- audience:general
- complexity:intermediate
---

## The Rule <!-- role: advice -->
When animating changes in dot plots or scatterplots, move all objects at the same time. Do not stagger the start times of individual elements.

## The Logic <!-- role: reason -->
While intuition suggests that staggering (introducing incremental delays) might reduce visual clutter, empirical evidence shows it generally fails to improve tracking performance. Staggering breaks "common motion" grouping, which helps users track sets of objects as a coherent whole. It also introduces unpredictability regarding when specific objects will begin to move, increasing cognitive load.
*   **The Principle:** Common Fate / Common Motion
*   **The Evidence:** [@chevalier_not-so-staggering_2014] demonstrate that staggering has a negligible or even negative impact on multiple object tracking compared to direct animation.

## Where to Apply <!-- role: context -->
This applies to interactive visualizations where the user must follow specific data points across a transition.
*   **User Goal:** Tracking the position or identity of specific data points (targets) among many others (distractors).
*   **Data Type:** 2D point clouds, scatterplots, or particle systems.
*   **Audience:** Users analyzing data changes between states (e.g., changing axis projections).

## When to Break It <!-- role: exceptions -->
There are extremely rare configurations where staggering might help, but they are difficult to predict.
*   **Scenario:** Highly specific spatial arrangements where direct movement causes extreme occlusion that staggering coincidentally solves.
*   **Reason:** The authors found staggering beneficial in only the top 0.01% of randomly generated cases designed to favor it, and even then, gains were modest [@chevalier_not-so-staggering_2014].

## The Price <!-- role: costs -->
Using simultaneous motion generally results in higher instantaneous crowding (objects getting close to each other).
*   **The Sacrifice:** You accept momentary higher density/occlusion during the transition.
*   **The Risk:** Users might briefly lose sight of a point if it is perfectly occluded, though the brain handles occlusion reasonably well if motion is predictable.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Applying a "wave" or random delay to all points to make the animation look "less overwhelming."
*   **Why it fails:** This destroys the temporal grouping that helps the eye track multiple items simultaneously.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do points start moving one by one or in waves?
*   **The Test:** Pause the animation at the very start. If some points have moved while others are still frozen, you are using staggering.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Set the start time delay ($dt$) to 0 for all elements.
*   **Best Fix:** Use a "slow-in/slow-out" pacing for the entire group moving simultaneously.
