---
id: use-lit-surfaces-for-anomalies
title: Use Lit Surfaces to Reveal Local Anomalies
bibliography: references.bib
description: Employ 3D surfaces with lighting models to highlight subtle variations
  and global shape in continuous bivariate data.
labels:
- chart:surface
- visual:shading
- task:identify
- data:continuous
- data:multivariate
- impact:insight
---

## The Rule <!-- role: advice -->
Represent continuous measures across two variables as a 3D surface with a lighting model (shading and specular highlights), rather than as a 2D heatmap or grid of bars.

## The Logic <!-- role: reason -->
Lighting models inherent to 3D rendering reveal surface shape through shading, making subtle local variations visible that are lost in 2D color mapping.
*   **The Principle:** **Shape-from-shading**. Specular highlights and gradients indicate curvature and rate of change more effectively than discrete hue steps.
*   **The Evidence:** [@brath_3d_2014] demonstrates that in financial interest rate visualizations, a lit surface reveals "noisy trends" and "subtle local shifts" in day-to-day movements that are difficult to perceive in a 2D hue/brightness heatmap or a uniform 3D bar chart.

## Where to Apply <!-- role: context -->
*   **User Goal:** Detecting both macro structure (global curvature) and micro anomalies (local bumps/noise).
*   **Data Type:** Bivariate distributions, volatility surfaces, or functions (e.g., periodicity surfaces).
*   **Audience:** Analysts looking for deviations in continuous fields.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The data is discrete and categorical, not continuous.
*   **Reason:** A surface implies continuity. If the data consists of independent, unrelated categories, a surface creates false relationships between neighbors.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Precise reading of specific values on the Y-axis (height) can be harder than on a 2D chart with a grid.
*   **The Risk:** Bad lighting (e.g., a single headlight) can flatten the image or obscure data.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a grid of 3D bars for continuous data.
*   **Why it fails:** Bars break the surface continuity, and without a continuous mesh, the lighting model cannot effectively show curvature or gradients across the data [@brath_3d_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the visualization "flat" or does it look like a blocky city?
*   **The Test:** Can you see the "texture" of the data? If it looks like a flat color ramp, you are missing the benefit of 3D lighting.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Enable a lighting source (e.g., directional light) in your renderer.
*   **Best Fix:** Convert discrete bars into a continuous mesh or surface plot and apply specular highlights to accentuate changes in slope.
