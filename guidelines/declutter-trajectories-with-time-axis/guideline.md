---
id: declutter-trajectories-with-time-axis
title: Extrude 2D Trajectories into Space-Time Cubes
bibliography: references.bib
description: Use the vertical dimension to represent time in trajectory data to resolve
  overlapping 'hairballs'.
labels:
- chart:space-time-cube
- visual:position
- task:trace
- data:temporal
- data:spatiotemporal
- impact:clarity
---

## The Rule <!-- role: advice -->
When visualizing movement or temporal sequences that overlap heavily in 2D, map time to the vertical (3rd) axis to separate the paths.

## The Logic <!-- role: reason -->
The third dimension provides **spatial separation** for data that occupies the same 2D coordinates at different times.
*   **The Principle:** Disambiguation via expansion. 2D movement maps often result in "hairballs" or "wormplots" where determining sequence is impossible due to occlusion.
*   **The Evidence:** [@brath_3d_2014] cites the "GeoTime" application, noting that law enforcement officials successfully use space-time cubes to analyze geotemporal data and secure convictions, as the 3D view reveals oscillations and sequences invisible in overlapping 2D points.

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding the sequence of events or movement patterns over time.
*   **Data Type:** Spatio-temporal data (locations + timestamps).
*   **Audience:** Investigators or analysts tracking entities (e.g., logistics, surveillance).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Time is not a critical variable, or the paths do not overlap in 2D.
*   **Reason:** If there is no overlap, the 2D view is simpler and sufficient.

## The Price <!-- role: costs -->
*   **The Sacrifice:** The user loses the "standard" map view unless they view the cube explicitly from the top down.
*   **The Risk:** Navigating a 3D cube requires more complex interaction (rotation/zoom) than a static 2D map.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using animation or brightness/hue to encode time on a 2D map.
*   **Why it fails:** Even with brightness, overlapping points obscure the density and specific motion patterns (e.g., distinct oscillations) [@brath_3d_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does your 2D map look like a tangled knot of lines?
*   **The Test:** Pick a specific location where multiple paths cross. Can you instantly tell which path arrived first? If not, use a space-time cube.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Map the timestamp of each data point to the Z-axis (height).
*   **Best Fix:** Render the data as a continuous line or "worm" moving upward through a bounded 3D box, preserving the 2D map as the "floor" for context.
