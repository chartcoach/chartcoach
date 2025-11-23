---
id: do-not-rely-on-broken-axis-symbols
title: Do Not Rely on Broken Axis Symbols to Correct Perception
bibliography: references.bib
description: Visual cues like broken axes or gradients do not mitigate the exaggerated
  perception caused by truncation.
labels:
- chart:bar
- visual:glyph
- impact:interpretation
- task:estimate
- visual:axis
---

## The Rule <!-- role: advice -->

Do not rely on visual indicators—such as broken axis glyphs, torn paper effects, or gradient bottoms—to neutralize the exaggerated perception of differences caused by y-axis truncation.

## The Logic <!-- role: reason -->

Visual cues that signal a broken axis fail to "de-bias" the user's perception. Even when users notice the truncation, the visual magnitude dominates their subjective judgment.
*   **The Principle:** Visual Dominance. Visual effect size (the physical height difference) tends to override cognitive corrections (knowing the axis is broken).
*   **The Evidence:** In the review by Zeng and Battle [@zeng_review_2023], they collate findings from Correll et al. [@correll_truncating_2020] (specifically comparisons of designs E-3, E-4, and E-5). The study found that neither broken axis lines nor gradient fills significantly reduced the perceived severity of the effect compared to a standard truncated bar chart.

## Where to Apply <!-- role: context -->

*   **User Goal:** Attempting to display small differences clearly while "being honest" about the scale.
*   **Data Type:** Bar charts requiring truncation to show detail.
*   **Audience:** Any audience, as this effect was observed in crowd-sourced studies with varying graphical literacy.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** When strict adherence to editorial standards or style guides mandates the indication of non-zero baselines.
*   **Reason:** While these symbols do not fix the *perceptual* bias, they serve a *convention* role in signaling that the data has been manipulated, which helps with transparency even if it doesn't fix the immediate visual impression.

## The Price <!-- role: costs -->

*   **The Sacrifice:** You lose the "safety net" of believing your design is neutral.
*   **The Risk:** Designers may believe they have "solved" the truncation problem by adding a symbol, while the viewer is still subjectively interpreting the data as having massive fluctuations.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Adding a "squiggly line" or break mark to the y-axis and assuming the chart is now perfectly accurate.
*   **Why it fails:** Correll et al. [@correll_truncating_2020] demonstrated that these designs are perceived as having the same effect size severity as charts without the symbols.

## How to Check <!-- role: check -->

*   **Visual Sign:** A truncated chart with a visual break indicator.
*   **The Test:** Cover the numbers and the break symbol. Does the visual shape still look like a massive change? If so, that is how the user will perceive it, regardless of the symbol.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Use the symbols for transparency, but do not expect them to fix the perception of magnitude.
*   **Best Fix:** If the exaggeration is misleading, you must change the axis range (include zero) rather than just decorating the break. Alternatively, use an inset chart to show the full context alongside the zoomed-in view.
