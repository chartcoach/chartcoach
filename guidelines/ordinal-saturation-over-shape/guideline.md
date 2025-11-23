---
id: ordinal-saturation-over-shape
title: Encode Ordinal Data with Saturation Over Shape
bibliography: references.bib
description: For ordered categories, use color saturation or hue rather than shape
  or geometric size.
labels:
- chart:heatmap
- task:rank
- visual:saturation
- visual:shape
- impact:readability
- data:ordinal
---

## The Rule <!-- role: advice -->
When visualizing Ordinal data (ordered categories), prioritize **Color Saturation** or **Color Hue** over geometric channels like Length, Angle, or Shape, provided Position is not available.

## The Logic <!-- role: reason -->
Ordinal data possesses an inherent order but lacks precise numerical distance. According to the theoretical rankings in [@zeng_review_2023], which synthesize the framework of [@mackinlay_automating_1986], the effectiveness ranking for Ordinal data places retinal properties high:
1.  **Position**
2.  **Color Saturation** (Intensity)
3.  **Color Hue** (Note: usually for ordered spectra)
4.  **Texture**
5.  **Length**

This theoretical framework suggests that perceiving the "order" in saturation (light to dark) is more effective for ordinal categories than perceiving order in geometric shapes or angles.

## Where to Apply <!-- role: context -->
*   **User Goal:** Recognizing rank or intensity levels (e.g., Low, Medium, High).
*   **Data Type:** Ordinal (Likert scales, T-shirt sizes, Ratings).
*   **Audience:** Users scanning for trends or "hot spots."

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When precise comparison of the *magnitude* of the rank is required.
*   **Reason:** While Mackinlay ranks Saturation high for Ordinal data, modern empirical studies often suggest geometric channels (Length) are better if the user treats the ordinal data effectively as quantitative (e.g., comparing a 4-star vs 2-star rating).
*   **Scenario:** Printing in black and white.
*   **Reason:** Saturation relies on contrast; if reproduction quality is poor, steps become indistinguishable.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Quantitative precision. Saturation is poor for determining if "High" is twice as much as "Medium."
*   **The Risk:** Perceptual nonlinearity. Users perceive changes in saturation logarithmically, not linearly.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using Shape to denote order (e.g., Circle = Low, Square = Medium, Triangle = High).
*   **Why it fails:** Shapes have no inherent visual order. The user must constantly reference a legend.
*   **The Wrong Fix:** Using rainbow hues for ordered data.
*   **Why it fails:** While Hue is ranked relatively high for ordinal data in this specific theoretical set [@mackinlay_automating_1986], unordered hues do not intuitively convey "less" to "more."

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart use a random assortment of colors for "Low/Med/High"?
*   **The Test:** Remove the legend. Can a viewer guess which value is the highest and which is the lowest just by looking? (Saturation passes this test; Shape fails).

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Apply a sequential color palette (e.g., light blue to dark blue).
*   **Best Fix:** If the ordinal data represents clear steps (like survey responses), a diverging bar chart (Position/Length) is often superior, but for compact displays, use Saturation.
