---
id: nominal-effectiveness-ranking
title: Encode Categories Using Color Hue
bibliography: references.bib
description: Use color hue for nominal data; avoid using size or saturation which
  imply order.
labels:
- visual:color
- visual:texture
- visual:size
- data:nominal
- data:categorical
- impact:clarity
---

## The Rule <!-- role: advice -->
When encoding nominal (unordered) data, use **Color Hue** or **Texture**. Do not use Size or Color Saturation.

## The Logic <!-- role: reason -->
Effectiveness depends on the match between the perceptual task and the data type. While Color is poor for quantities, it is highly effective for distinguishing distinct, unordered items. Conversely, Size and Saturation are perceived as ordered, which creates confusion for nominal data.
*   **The Principle:** Accuracy Ranking of Nominal Perceptual Tasks
*   **The Evidence:** [@mackinlay_automating_1986] extends the accuracy ranking to nominal data: Position > Color Hue > Texture > Connection > Containment > Density > Color Saturation > Shape > Length > Angle > Slope > Area > Volume.

## Where to Apply <!-- role: context -->
*   **User Goal:** Distinguishing between different categories (e.g., Companies, Nations).
*   **Data Type:** Nominal (sets of unordered items).
*   **Audience:** General to expert.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Position is available.
*   **Reason:** Position is technically the most effective channel for *all* data types, including nominal (e.g., separating categories along an axis). Color Hue is the best non-positional choice.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You cannot use color to show intensity or magnitude if you are using it for categories.
*   **The Risk:** Using "Size" for categories (e.g., big circle = "Ford", small circle = "Honda") will cause users to perceive "Ford" as "more" or "better" than "Honda."

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using different sizes or color saturations (light vs dark) to represent different categories.
*   **Why it fails:** Size and Saturation are expressiveness violations for nominal data because they imply an ordinal relationship [@mackinlay_automating_1986].

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the categories look like they are "increasing" or "fading"?
*   **The Test:** Does the visual variable imply a "more/less" relationship? If yes, it is wrong for nominal data.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch from a sequential color palette (light-to-dark) to a categorical palette (distinct hues).
*   **Best Fix:** Use distinct Hues or Spatial Position to separate categories.
