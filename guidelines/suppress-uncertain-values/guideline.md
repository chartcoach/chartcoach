---
id: suppress-uncertain-values
title: Suppress Value Resolution in High-Uncertainty Data
bibliography: references.bib
description: Reduce the visual distinction between data values as uncertainty increases
  to promote risk-averse decision-making.
labels:
- chart:bivariate-map
- chart:heatmap
- task:decision-making
- visual:color
- impact:uncertainty-awareness
- data:uncertainty
- audience:general
- complexity:intermediate
---

## The Rule <!-- role: advice -->
When visualizing data with associated uncertainty, allocate fewer distinct color bins to values as their uncertainty increases. Merge highly uncertain values into a single visual category regardless of their nominal value.

## The Logic <!-- role: reason -->
There is a limited budget for perceptual discriminability in bivariate maps (maps showing value + uncertainty). By using a tree-like quantization structure (a Value-Suppressing Uncertainty Palette or VSUP), you preserve discriminability where it matters (high certainty) and remove it where it is likely noise (high uncertainty).
*   **The Principle:** Non-uniform budgeting of visual channels.
*   **The Evidence:** Experiments in [@correll_value-suppressing_2018] showed that this technique encourages "risk-averse" behavior, preventing users from making strong predictions based on unreliable data, while traditional maps failed to discourage risky guesses.

## Where to Apply <!-- role: context -->
*   **User Goal:** Making decisions where acting on uncertain data carries risk (e.g., "Where is it safest to intervene?").
*   **Data Type:** Bivariate data consisting of a quantitative value and a quantitative measure of uncertainty (e.g., polling leads and margins of error).
*   **Audience:** Users who need to weigh confidence against effect size.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** "Black Swan" or Long-Tail Risk Analysis.
*   **Reason:** If the user explicitly needs to identify high-risk events regardless of how uncertain they are (e.g., a low-probability but catastrophic failure), suppressing these values hides critical threats [@correll_value-suppressing_2018].
*   **Scenario:** Outlier detection/filtering.
*   **Reason:** If the task involves finding noisy signals specifically, you need to see the variation in high-uncertainty regions.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Loss of data fidelity. You literally cannot read the specific data value if the uncertainty crosses a certain threshold.
*   **The Risk:** Users might assume data is missing rather than just uncertain if the "fog" effect is not clearly explained in the legend.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using transparency (opacity) for uncertainty on a continuous scale.
*   **Why it fails:** This is "ad hoc" aliasing. While it makes uncertain data harder to see, it provides no guarantee of discriminability and creates perceptual interference with the underlying color value [@correll_value-suppressing_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Look at the legend. Is it a square grid (traditional) or a wedge/arc shape?
*   **The Test:** Pick a color representing "High Uncertainty." Can you distinguish between a "High Value" and a "Low Value" with that same uncertainty? If yes, you are not suppressing values.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reduce the number of color bins used for the highest uncertainty row/column in your legend.
*   **Best Fix:** Implement a VSUP (Value-Suppressing Uncertainty Palette) that uses a quantization tree: map all high-uncertainty values to one color (the root), and branch out to more colors only as uncertainty decreases.
