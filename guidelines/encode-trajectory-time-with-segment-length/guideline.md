---
id: encode-trajectory-time-with-segment-length
title: Encode Time with Segment Lengths on Trajectories
bibliography: references.bib
description: Use segment lengths (ticks) rather than color or size to represent time
  progression on 2D paths.
labels:
- chart:trajectory
- chart:line
- task:aggregate
- task:locate
- visual:length
- visual:texture
- impact:accuracy
- data:temporal
---

## The Rule <!-- role: advice -->
Use divided segment lengths (ticks) to encode the passage of time along a trajectory. Avoid using color gradients or line thickness (tapering) for time.

## The Logic <!-- role: reason -->
For tasks requiring the identification of specific time points or duration (`aggregate` tasks), spatial segmentation allows users to "count" or visually estimate geometry more accurately than decoding a continuous gradient.
*   **The Principle:** Spatial Discretization. Zeng and Battle [@zeng_review_2023] highlight findings from Perin et al. [@perin_assessing_2018] showing that finding a specific time value (e.g., "where is the 50% mark?") is difficult with color value because detecting specific luminance levels is perceptually imprecise.
*   **The Evidence:** Designs using segment length (e.g., E-1, E-3) ranked highest for time-based aggregation tasks. Conversely, designs relying on color saturation for time (e.g., E-17) performed significantly worse in accuracy rankings [@perin_assessing_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Estimating duration, locating specific timestamps, or comparing travel times across different path segments.
*   **Data Type:** 2D + Time trajectories where the temporal dimension is critical.
*   **Audience:** Users needing to correlate spatial position with specific moments in time.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The trajectory is extremely long or the data is very dense.
*   **Reason:** High data density can cause "tick" marks to alias or clutter the visual field, creating a moiré effect that hinders readability.

## The Price <!-- role: costs -->
*   **The Sacrifice:** The visual "smoothness" of the path. The line will appear dashed, textured, or interrupted by ticks.
*   **The Risk:** If the segments are too small (due to high speed or long duration), they may become indistinguishable.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a gradient that fades from light to dark (Color Value) to show the start and end of the path.
*   **Why it fails:** Users can easily identify the start and end, but cannot accurately pinpoint intermediate values (e.g., "the halfway point") within the gradient [@perin_assessing_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the path a smooth, continuous gradient?
*   **The Test:** Ask a user to point to the exact moment where 50% of the travel time elapsed. If they hesitate or guess widely, the encoding is failing.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Overlay ticks or divide the line into segments corresponding to fixed time intervals (e.g., every minute).
*   **Best Fix:** Use a "beaded" or segmented line style where the length of each segment corresponds to the distance traveled in a fixed unit of time (longer segments = faster speed, shorter segments = slower speed).
