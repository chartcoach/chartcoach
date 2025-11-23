---
id: animate-for-delta-identification
title: Animate Transitions to Highlight Value Changes
bibliography: references.bib
description: Use animated transitions between two datasets to help users instantly
  identify the largest value change.
labels:
- chart:bar
- chart:donut
- task:compare
- visual:motion
- impact:efficiency
- data:temporal
---

## The Rule <!-- role: advice -->
Use animated transitions (morphing) when asking users to identify which specific data point changed the most between two datasets in bar or donut charts.

## The Logic <!-- role: reason -->
Animation converts the difference in value (delta) into velocity. The human visual system processes motion speed as a primitive, direct feature. When marks transition over the same duration, the object with the largest change moves the fastest, creating an emergent signal that is pre-attentively detected [@ondov_face_2019].

*   **The Principle:** Motion Sensitivity / Velocity Encoding
*   **The Evidence:** In experiments, animated charts consistently outperformed all small multiple arrangements (stacked, adjacent, mirrored) and even overlaid charts for identifying the "biggest mover" in bar and donut charts [@ondov_face_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Rapidly identifying individual items with the largest increase or decrease (MaxDelta task).
*   **Data Type:** Two states of categorical data represented as Bar charts or Donut charts.
*   **Audience:** Users interacting with digital displays where attention can be focused on the transition.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Slope Charts.
*   **Reason:** Animation did not provide significant benefits over static overlaid views for slope charts, likely because the motion is simple vertical translation [@ondov_face_2019].
*   **Scenario:** Analyzing Correlation.
*   **Reason:** Animation failed to help users judge the overall correlation between two datasets; static comparisons were superior for this task [@ondov_face_2019].
*   **Scenario:** More than 2-4 distinct moving objects.
*   **Reason:** While not tested in this specific paper, the authors note that perceptual tracking capacity is limited to roughly 4 objects, so animation may fail if the user must track many complex changes simultaneously [@ondov_face_2019].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Comparison is ephemeral; the user must be looking at the screen at the exact moment of transition.
*   **The Risk:** Disorientation. In complex charts (like Sunbursts), large changes can shift adjacent elements, potentially confusing the user's spatial map [@ondov_face_2019].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using side-by-side (adjacent) small multiples for detecting magnitude changes.
*   **Why it fails:** This forces the user to saccade back and forth, relying on working memory rather than direct visual processing of motion [@ondov_face_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the two states displayed statically side-by-side?
*   **The Test:** If the user clicks a "toggle" or "play" button, do the bars smooth-interpolate to their new positions?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Implement a toggle switch that interpolates between the two data states using cubic interpolation.
*   **Best Fix:** Design the interaction so the transition duration is fixed (e.g., 1.5 seconds), ensuring velocity directly corresponds to the magnitude of change.
