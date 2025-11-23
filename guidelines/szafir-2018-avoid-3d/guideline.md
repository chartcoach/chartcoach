---
id: szafir-2018-avoid-3d
title: Avoid 3D Projections for Abstract Data
bibliography: references.bib
description: Use 2D representations for abstract data to avoid occlusion, projection
  distortion, and perceptual ambiguity.
labels:
- visual:3d
- visual:2d
- impact:clarity
- chart:pie
- chart:bar
- bias:occlusion
---

## The Rule <!-- role: advice -->
Do not use 3D effects or 3D coordinate systems for abstract data visualization unless the data possesses inherent spatial qualities.

## The Logic <!-- role: reason -->
Projecting 3D data onto a 2D screen causes three specific failures: occlusion (data hiding behind other data), projection distortion (perspective makes distant objects look smaller regardless of value), and the loss of binocular cues (depth perception) required to resolve spatial position.
*   **The Principle:** Monocular Depth Cues & Motion Parallax.
*   **The Evidence:** [@szafir_good_2018] highlights that tilting a pie chart in 3D distorts angles, making slices appear larger or smaller based on position rather than value.

## Where to Apply <!-- role: context -->
*   **User Goal:** Precise comparison of values or categories.
*   **Data Type:** Abstract statistical data (sales, demographics, performance metrics).
*   **Audience:** Any audience needing accurate analysis.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Visualizing inherently spatial structures.
*   **Reason:** Data such as molecular surfaces or architectural structures have real 3D shapes. In these cases, 3D provides necessary context, though 2D summaries should still accompany them [@szafir_good_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the "engaging, futuristic, and sophisticated" aesthetic that some presenters desire.
*   **The Risk:** The visualization may appear "flatter" or less "flashy" to non-expert stakeholders.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Allowing the user to rotate the 3D view manually.
*   **Why it fails:** Even with rotation, occlusion prevents seeing the whole dataset at once, and perspective distortion remains.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are there shadows, vanishing points, or z-axes in a chart representing non-spatial data?
*   **The Test:** If an object moves to the "back" of the chart, does it become visually smaller? If yes, the design is biased.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Flatten the chart to 2D (e.g., changing a 3D bar chart to a standard bar chart).
*   **Best Fix:** Map the third dimension to a different visual channel, such as Size or Color, or use small multiples (faceting) [@szafir_good_2018].
