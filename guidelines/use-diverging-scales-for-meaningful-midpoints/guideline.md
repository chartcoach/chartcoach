---
id: use-diverging-scales-for-meaningful-midpoints
title: Use Diverging Scales for Meaningful Midpoints
bibliography: references.bib
description: Apply diverging color scales only when the data possesses a natural or
  mathematically significant center point.
labels:
- chart:heatmap
- chart:choropleth
- visual:color
- data:quantitative
- impact:accuracy
---

## The Rule <!-- role: advice -->
Use a diverging color scale (two hues diverging from a neutral center) if—and only if—your data has a meaningful middle value. If no natural center exists, use a sequential scale.

## The Logic <!-- role: reason -->
Diverging scales rely on a pivot point to separate values into two distinct categories (e.g., "positive" vs. "negative" or "above" vs. "below"). Without a genuine pivot, the color shift implies a categorical difference that does not exist in the data [@muth_diverging_vs_sequential_2021].
*   **The Principle:** Semantically Resonant Color.
*   **The Evidence:** The blog post illustrates that a "normal" exhaustion level serves as a valid center point for a diverging scale, whereas a dataset simply measuring "level of exhaustion" from zero to high should remain sequential [@muth_diverging_vs_sequential_2021].

## Where to Apply <!-- role: context -->
This advice applies when visualizing quantitative data that contains one of the following specific midpoints:
*   **User Goal:** Showing deviation from a norm or target.
*   **Data Type:**
    *   **Zero:** Positive and negative values (e.g., economic growth).
    *   **50%:** A binary split (e.g., vote share between two choices).
    *   **Average/Median:** Values above and below the population norm (e.g., age relative to median).
    *   **Thresholds:** Values relative to a specific line (e.g., poverty line).
    *   **Targets:** Performance relative to a goal (e.g., quarterly revenue targets) [@muth_diverging_vs_sequential_2021].

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The middle point is arbitrary.
*   **Reason:** If you force a middle point where none exists (e.g., arbitrarily deciding "sleeping" is zero exhaustion and "running" is high), you mislead the reader into seeing a qualitative shift where there is only magnitude [@muth_diverging_vs_sequential_2021].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the immediate, intuitive "darker equals more" logic of sequential scales.
*   **The Risk:** Readers may not immediately understand what the neutral color represents without clear labeling.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a diverging scale for purely positive data (0 to 100) just to add color variety.
*   **Why it fails:** It implies that values in the middle are "neutral" or distinct from the low values, confusing the narrative.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the point where the color changes (e.g., from blue to orange) represent a specific, namable concept (like "break-even" or "average")?
*   **The Test:** Ask, "What does white/grey represent in this chart?" If the answer is just a random number with no semantic meaning, the scale is wrong.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch to a single-hue sequential scale (e.g., light blue to dark blue).
*   **Best Fix:** Identify if a threshold actually exists in the data (like a target value) and recenter the diverging scale on that; otherwise, use sequential.
