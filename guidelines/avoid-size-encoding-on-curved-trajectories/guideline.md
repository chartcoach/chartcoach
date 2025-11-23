---
id: avoid-size-encoding-on-curved-trajectories
title: Avoid Size Encoding on Curved Trajectories
bibliography: references.bib
description: Do not use line width (size) to encode data on curved paths due to perceptual
  distortion.
labels:
- chart:trajectory
- chart:line
- visual:size
- visual:width
- visual:shape
- impact:accuracy
- data:spatiotemporal
---

## The Rule <!-- role: advice -->
Do not map quantitative data (like speed or time) to line width (size) if the trajectory contains curves. Use size only for strictly straight paths, or prefer other channels like color.

## The Logic <!-- role: reason -->
Curvature introduces geometric distortion that interferes with the perception of width.
*   **The Principle:** Shape-Size Interference. Perin et al. [@perin_assessing_2018] demonstrated that the accuracy of size encodings degrades significantly when the path bends.
*   **The Evidence:** As collated by Zeng and Battle [@zeng_review_2023], the rankings for `find-extremum` tasks showed that while size (E-14) performed moderately on straight lines, its performance dropped (E-13) on curved lines. Color saturation (E-7) remained robust regardless of curvature [@perin_assessing_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing values (magnitude) along a path.
*   **Data Type:** Geospatial trajectories, route maps, or any path-based visualization that is not perfectly linear.
*   **Audience:** General purpose.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The path is schematic and strictly rectilinear (e.g., a simplified subway map with only 90-degree turns).
*   **Reason:** If curves are eliminated, the perceptual distortion of width is minimized.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the "Flow" metaphor (where thicker often intuitively implies "more" or "heavier" flow).
*   **The Risk:** You must rely on color (which requires a legend/key) or texture, which might be less intuitive than size for magnitude.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a "tadpole" or "comet" tail effect (tapering size) to show movement direction and speed on a winding road map.
*   **Why it fails:** On the curves, the tapering gets lost or distorted, making it impossible to judge the actual speed or time value accurately [@perin_assessing_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the line vary in thickness while also turning corners?
*   **The Test:** Find a curve where the line is thick. Is it thick because of the data, or does it just look thick because of the rendering of the curve? If you are unsure, the encoding is flawed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Normalize the line width to be constant.
*   **Best Fix:** Move the quantitative variable to the Color Saturation channel.
