---
id: avoid-rainbow-colormaps
title: Jettison the Rainbow Colormap
bibliography: references.bib
description: Avoid rainbow (Jet) colormaps as they reduce speed and accuracy in quantitative
  data comparison.
labels:
- visual:color
- impact:clarity
- task:compare
- data:quantitative
- chart:heatmap
---

## The Rule <!-- role: advice -->
Do not use the standard rainbow colormap (often called *Jet*) for encoding quantitative data.

## The Logic <!-- role: reason -->
The rainbow colormap creates false perceptual boundaries ("banding") and lacks natural perceptual ordering.
*   **The Principle:** Perceptual Uniformity and Ordering.
*   **The Evidence:** In empirical assessments, the *Jet* colormap was the slowest to read and the most error-prone among all tested colormaps. Even when users took more time, their accuracy did not improve [@liu_somewhere_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Any task involving the estimation of relative values or distances.
*   **Data Type:** Quantitative scalar data (interval or ratio).
*   **Audience:** All audiences (additionally, rainbow maps are often unfriendly to color-blind users, though this specific paper focused on general perceptual performance).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Isoluminant tasks where specific hue bands align exactly with meaningful categorical boundaries in the data (rare and risky).
*   **Reason:** The paper notes that "banding" can technically improve discrimination *if* the bands happen to align with the true value differences you want to highlight, but this is generally serendipitous and unreliable [@liu_somewhere_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the high saturation and familiarity that some legacy users or scientific communities may expect from older tools.
*   **The Risk:** Users accustomed to "red = hot, blue = cold" might initially complain about new encodings like *Viridis*.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Keeping the rainbow map but adding more distinct bands.
*   **Why it fails:** It does not solve the fundamental lack of perceptual ordering (e.g., yellow often appears brighter than red or green, confusing the "magnitude" signal).

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the visualization look like a spectrum of arbitrary stripes (cyan, yellow, magenta) rather than a smooth gradient?
*   **The Test:** Convert the image to grayscale. If the gradient no longer looks monotonic (steadily increasing or decreasing), it is likely a rainbow map failing to convey order.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Replace *Jet* with *Viridis* or a diverging *Blue-Orange* scheme depending on the data.
*   **Best Fix:** Use a colormap that ramps primarily in luminance while using hue for additional separation.
