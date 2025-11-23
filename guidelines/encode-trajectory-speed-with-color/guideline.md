---
id: encode-trajectory-speed-with-color
title: Encode Speed with Color Value on Trajectories
bibliography: references.bib
description: Use color saturation or value rather than size to represent speed along
  a 2D trajectory.
labels:
- chart:trajectory
- chart:line
- task:find-extremum
- visual:color-value
- visual:color-saturation
- impact:accuracy
- data:spatiotemporal
---

## The Rule <!-- role: advice -->
Use color value or saturation to encode speed changes along a 2D trajectory path. Do not use line width (size) or segment length to represent speed if color is available.

## The Logic <!-- role: reason -->
When users need to find minimum or maximum speed values (`find-extremum`) along a path, color encodings significantly outperform size and length encodings.
*   **The Principle:** Visual Interference and Shape Independence. As collated by Zeng and Battle [@zeng_review_2023], experiments by Perin et al. [@perin_assessing_2018] demonstrate that color value is distinct from the spatial properties of the path (curvature and length), whereas line width (size) is easily distorted by the path's shape.
*   **The Evidence:** In the experimental rankings, designs using color saturation for speed (e.g., design E-7) consistently ranked in the top tier for accuracy, while size-based speed encodings (e.g., E-13) performed significantly worse, particularly on curved paths [@perin_assessing_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying the fastest or slowest segments of a movement path (finding extrema).
*   **Data Type:** 2D + Time trajectories (e.g., vehicle movement, eye-tracking scanpaths).
*   **Audience:** Analysts needing to assess velocity changes geographically.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The visualization already uses color to encode a categorical variable (e.g., "Vehicle Type" or "Driver ID").
*   **Reason:** Overloading the color channel causes confusion. In this case, segment length (ticks) is a viable secondary alternative for speed, though less accurate than color [@perin_assessing_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to use color for nominal data (categories) or other quantitative metrics.
*   **The Risk:** Users with color vision deficiencies may struggle if the value ramp is not perceptually uniform or colorblind-safe.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Varying the thickness of the line (Size) to show speed.
*   **Why it fails:** On curved paths, the changing orientation and curvature make it difficult for the eye to judge relative thickness accurately, leading to higher error rates [@perin_assessing_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the path look like a "sausage" with varying thickness?
*   **The Test:** Look at a sharp curve in the path. Can you instantly tell if the speed is high or low without mentally correcting for the curve's distortion? If not, switch to color.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Apply a sequential color ramp (e.g., light to dark) to the line stroke based on the speed variable.
*   **Best Fix:** Use a perceptually uniform color scale (linear luminance change) mapped to the speed, keeping line width constant.
