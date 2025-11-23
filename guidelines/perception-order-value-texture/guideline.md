---
id: perception-order-value-texture
title: Use Luminance or Texture to Convey Order
bibliography: references.bib
description: Prioritize luminance or texture over hue or orientation when users must
  perceive the order of a sequence.
labels:
- chart:scatter
- chart:glyph
- task:correlate
- task:sort
- visual:color-saturation
- visual:texture
- impact:accuracy
- data:quantitative
- data:ordered
---

## The Rule <!-- role: advice -->
Map quantitative variables to color value (luminance/saturation) or texture when the user needs to perceive the overall order or correlation of a data sequence. Avoid using color hue for this purpose.

## The Logic <!-- role: reason -->
Users perceive "orderedness" most accurately when data is encoded with channels that have a natural perceptual hierarchy. Experimental data shows that luminance and texture allow users to detect the degree of order in a sequence significantly better than other channels.
*   **The Principle:** Perceptual Orderability
*   **The Evidence:** In the collation by [@zeng_review_2023] of the study by [@chung_how_2016], Color Saturation (Value) and Texture ranked 1st and 2nd respectively for accuracy in correlation tasks, significantly outperforming Color Hue, which ranked last.

## Where to Apply <!-- role: context -->
*   **User Goal:** The user needs to assess how sorted a dataset is or identify correlations between an ordered axis and a data variable.
*   **Data Type:** Ordered quantitative sequences.
*   **Audience:** General analytical audiences.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Rapid scanning is the only priority, and accuracy is secondary.
*   **Reason:** While Value is most accurate, the data indicates that Size encodings resulted in faster response times for correlation tasks [@chung_how_2016].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Using texture can introduce high visual frequency or "noise" if not carefully designed, and luminance consumes the color channel, limiting the use of color for categories.
*   **The Risk:** Texture is rarely supported by standard BI tools, making implementation difficult.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a rainbow (multi-hue) colormap to show order.
*   **Why it fails:** Hue ranked lowest (6th) in accuracy for perceiving order in the referenced study [@chung_how_2016]; users struggle to perceive a natural order in hue changes.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the visualization use different colors (e.g., Blue vs. Red) to imply that one value is "higher" than another?
*   **The Test:** Convert the visualization to grayscale. If the order becomes difficult to distinguish, the encoding relies too heavily on hue.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch the color scale to a single-hue sequential ramp (varying saturation/luminance).
*   **Best Fix:** If the tool supports it, map the magnitude to a texture density or grain size for high perceptual accuracy.
