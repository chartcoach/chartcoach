---
id: use-discriminable-categorical-colors
title: Use Discriminable Categorical Colors for Intensity Categories
bibliography: references.bib
description: Use distinct, recognizable colors for distinct categories rather than
  continuous gradients.
labels:
- chart:line
- visual:color
- impact:clarity
- data:categorical
- audience:general-public
---

## The Rule <!-- role: advice -->
When encoding distinct intensity categories (like the Saffir-Simpson scale), use a palette of highly discriminable, named colors rather than a continuous hue or saturation ramp.

## The Logic <!-- role: reason -->
Visualizing distinct categories requires colors that are easily distinguishable and memorable. Continuous ramps (e.g., light red to dark red) can be ambiguous when trying to identify specific categorical boundaries. By using a palette of distinct colors (e.g., Green, Pink, Gray, Orange, Brown, Purple, Red) derived from perceptual guidelines, users can more easily identify specific intensity levels along a track segment [@liu_visualizing_2019].

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying specific threat levels or categories (e.g., "Is this a Category 3 or 4?").
*   **Data Type:** Ordered categorical data (ordinal) mapped onto geometric paths.
*   **Audience:** General public or decision-makers who rely on standardized safety scales.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The data is truly continuous and has no meaningful categorical thresholds.
*   **Reason:** Using distinct colors for continuous data introduces artificial boundaries (binning artifacts) that may mislead the user.

## The Price <!-- role: costs -->
*   **The Sacrifice:** The intuitive ordering of a single-hue ramp (where darker = stronger).
*   **The Risk:** Users must learn the specific mapping (legend lookups) if the colors do not follow a natural perceptual order (though ordering by redness/alertness helps).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a "Rainbow" ramp or a subtle saturation scale.
*   **Why it fails:** Saturation scales are hard to read on thin lines over maps; Rainbow scales introduce perceptual artifacts.

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you name the colors easily (e.g., "That segment is Orange")?
*   **The Test:** Remove the legend. Can a user distinguish between Category 2 and Category 3 segments if they are not adjacent?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Increase the contrast between steps in your current color ramp.
*   **Best Fix:** Adopt a standard, discriminable palette (e.g., Ware’s color catalog), ensuring colors are sorted by a meaningful attribute (like the red channel) to maintain some sense of order while maximizing distinctness [@liu_visualizing_2019].
