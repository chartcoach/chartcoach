---
id: use-multi-hue-for-value-retrieval
title: Use Multi-Hue Colormaps for Value Retrieval
bibliography: references.bib
description: When users need to read specific values from continuous maps, high hue
  variation (like Rainbow or Spectral) outperforms monotonic scales.
labels:
- chart:continuous-map
- chart:scalar-field
- task:retrieve-value
- visual:color-hue
- impact:accuracy
- data:quantitative
---

## The Rule <!-- role: advice -->
Use multi-hue colormaps (such as Rainbow or Spectral) rather than single-hue or monotonic luminance scales when the primary user task is reading specific quantitative values from a continuous map.

## The Logic <!-- role: reason -->
While often criticized in visualization design, high hue variation provides distinct perceptual advantages for specific tasks.
*   **The Principle:** Simultaneous Contrast Mitigation. Strong variations in hue help the human eye resist the influence of background colors, which often distort perceived values in luminance-based scales.
*   **The Evidence:** In a collation of graphical perception knowledge, Zeng and Battle [@zeng_review_2023] highlight experimental results from Reda et al. [@reda_graphical_2018]. The data shows that for "retrieve value" tasks, the Rainbow (E-9) and Spectral (E-7) colormaps yielded significantly higher accuracy than single-hue or spiral layouts (like Cubehelix), regardless of the data's spatial frequency.

## Where to Apply <!-- role: context -->
*   **User Goal:** Precise quantity estimation (e.g., "What is the temperature at this specific coordinate?").
*   **Data Type:** Continuous quantitative maps (scalar fields) with smooth gradients.
*   **Audience:** Specialists or general users performing lookup tasks on heatmaps or geological maps.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The users have Color Vision Deficiency (CVD).
*   **Reason:** The "Rainbow" colormap is notoriously difficult for colorblind users to interpret; a CVD-safe multi-hue scale (like Viridis or a distinct Spectral variation) should be substituted.
*   **Scenario:** The task involves identifying shapes or gradients in noisy data.
*   **Reason:** Reda et al. [@reda_graphical_2018] found that while Rainbow is good for point-reading, it performs worse than diverging scales for pattern recognition in high-frequency data.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Aesthetics and potentially intuitive ordering. Rainbow scales lack a natural perceptual ordering compared to luminance ramps.
*   **The Risk:** Users may perceive "false boundaries" where the hue shifts sharply (e.g., the yellow band in a rainbow), though the specific study suggests this does not impede value retrieval accuracy.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Forcing a single-hue linear scale (e.g., light blue to dark blue) for complex value-lookup tasks.
*   **Why it fails:** Users struggle to distinguish subtle saturation/luminance differences at specific points without the aid of hue variation.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the map look "smooth" but make it hard to match a specific point to the legend?
*   **The Test:** Pick a point on the map and try to guess its value using the legend. If you are off by more than 5-10% of the range, the color differentiation may be too low.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch from a Single-Hue scale to a Spectral or Viridis scale.
*   **Best Fix:** Use a "Spectral" scale, which Reda et al. [@reda_graphical_2018] found performed nearly as well as Rainbow for values but offers better properties for other tasks.
