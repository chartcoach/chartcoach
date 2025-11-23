---
id: minimize-target-crowding
title: Minimize Target Crowding in Trajectories
bibliography: references.bib
description: Prioritize trajectory paths that keep target objects away from distractors
  to reduce tracking difficulty.
labels:
- visual:position
- visual:animation
- task:track
- impact:accuracy
- chart:scatterplot
---

## The Rule <!-- role: advice -->
Design animation trajectories so that tracked objects (targets) stay as far away from other moving objects (distractors) as possible.

## The Logic <!-- role: reason -->
The primary predictor of difficulty in tracking multiple objects is "crowding"—the proximity of distractors to the targets. When a target gets too close to a distractor, the user risks swapping them or losing the target entirely.
*   **The Principle:** Visual Crowding
*   **The Evidence:** [@chevalier_not-so-staggering_2014] validated that "target crowding" (how often distractors cross or come near the target's path) is heavily correlated with lower tracking accuracy.

## Where to Apply <!-- role: context -->
This applies when you have control over the specific path or ordering of elements in a transition.
*   **User Goal:** Accurately following specific data points from a start state to an end state.
*   **Data Type:** Dense visualizations with many moving parts.
*   **Audience:** Analytical users requiring high precision.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When maintaining the "mental map" of the coordinate system is more important than tracking specific points.
*   **Reason:** Warping trajectories to avoid crowding might confuse the user about the spatial relationship between the two views (e.g., curving a path might look like a data value change).

## The Price <!-- role: costs -->
*   **The Sacrifice:** Calculating optimal paths to minimize crowding is computationally expensive and complex.
*   **The Risk:** Non-linear paths might be misinterpreted as data attributes rather than just transition artifacts.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Simply slowing down the animation without changing the paths.
*   **Why it fails:** While speed matters at extremes, crowding (proximity) is the stronger factor. If objects overlap, slow speed won't prevent confusion.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do moving points frequently clump together or cross over each other "tightly"?
*   **The Test:** Calculate the average distance between targets and their nearest neighbors throughout the animation frames.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use linear interpolation (straight lines), as complex paths often introduce more accidental crowding.
*   **Best Fix:** If generating paths algorithmically, use a cost function that penalizes proximity between targets and distractors.
