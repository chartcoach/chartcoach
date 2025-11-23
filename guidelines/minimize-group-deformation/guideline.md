---
id: minimize-group-deformation
title: Minimize Geometric Deformation of Tracked Groups
bibliography: references.bib
description: Maintain the relative spatial arrangement of target groups during transitions
  to aid tracking.
labels:
- visual:shape
- visual:animation
- task:track
- impact:recognizability
- complexity:advanced
---

## The Rule <!-- role: advice -->
When a user is tracking a group of objects, ensure the shape formed by that group distorts as little as possible during the movement.

## The Logic <!-- role: reason -->
Users track groups of objects more easily when they move as a rigid structure (like a polygon translating or rotating) rather than an amorphous blob that changes shape. High "deformation"—changes in the relative distances between targets—negatively impacts tracking accuracy.
*   **The Principle:** Perceptual Grouping / Rigid Motion Bias
*   **The Evidence:** [@chevalier_not-so-staggering_2014] found that "deformation" was a statistically significant factor in tracking difficulty; tasks were harder when the triangle formed by three targets underwent severe distortion.

## Where to Apply <!-- role: context -->
*   **User Goal:** Tracking a cluster or subset of data points (NoID task).
*   **Data Type:** Moving clusters in scatterplots.
*   **Audience:** Users looking for macro-trends or cluster movements.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the data itself changes relationships (e.g., points within a cluster drift apart in the new projection).
*   **Reason:** The visualization must accurately represent the data change. Artificial rigidity would be misleading (a lie).

## The Price <!-- role: costs -->
*   **The Sacrifice:** You cannot use "staggering" techniques, as they inherently increase deformation by moving points at different times.
*   **The Risk:** If the data naturally deforms significantly, the user will struggle to track it regardless of the technique used.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Staggering the movement of a cluster.
*   **Why it fails:** Staggering breaks the rigid structure of the group, increasing the calculated deformation and making the group harder to track [@chevalier_not-so-staggering_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the group of points look like a "jellyfish" expanding and contracting, or a "plate" sliding across the table?
*   **The Test:** Compute the change in length of all segments connecting the target points over time.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Ensure all points in the group start and stop at the same time (simultaneous motion).
*   **Best Fix:** If possible, translate the group as a single unit first, then apply internal position adjustments (though this requires multi-stage animation).
