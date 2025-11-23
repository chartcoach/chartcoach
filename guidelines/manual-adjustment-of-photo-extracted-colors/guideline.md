---
id: manual-adjustment-of-photo-extracted-colors
title: Manually Adjust Colors Extracted from Images
bibliography: references.bib
description: Do not rely solely on automated color pickers from photos, as they often
  produce desaturated results.
labels:
- visual:color
- task:palettest-generation
- source:automation
---

## The Rule <!-- role: advice -->
Manually increase saturation or select colors by eye when creating palettes from photos or movie stills; do not rely purely on automated generators.

## The Logic <!-- role: reason -->
Automated tools calculate averages or exact pixel values, which often fail to capture the perceptual vibrancy of an image.
*   **The Principle:** Perceptual vs. Computed Color.
*   **The Evidence:** [@muth_colorguide_2018] notes that automated palettes "will turn out far less saturated than you 'see' the colors." An automated approach "won’t help you much... it will always look more greyish."

## Where to Apply <!-- role: context -->
*   **User Goal:** Creating a distinctive color palette inspired by a movie, painting, or photo.
*   **Tool:** Automated palette generators (e.g., DeGraeve’s generator).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Using photos of tropical fish.
*   **Reason:** @muth_colorguide_2018 notes a suggestion by Bill Hart-Davidson that tropical fish photos are naturally saturated enough to work as a basis.

## The Price <!-- role: costs -->
*   **The Sacrifice:** It requires more time and a "good eye" compared to one-click generation.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using the raw output of a generator and wondering why the visualization looks muddy.

## How to Check <!-- role: check -->
*   **The Test:** Compare the generated palette to the original image. Does the palette feel "greyer" than the mood of the image?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Pick the colors manually using a "color radius" tool (like *image-color.com*) rather than a single pixel picker [@muth_colorguide_2018].
