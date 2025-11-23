---
id: avoid-broken-axis-glyphs
title: Avoid Relying on Broken Axis Glyphs
bibliography: references.bib
description: Visual indicators of axis truncation do not correct the viewer's perception
  of exaggerated magnitude.
labels:
- chart:bar
- visual:annotation
- visual:scale
- impact:deception
---

## The Rule <!-- role: advice -->
Do not use visual "broken axis" indicators (such as squiggle glyphs, torn paper metaphors, or axis gaps) with the expectation that they will "de-bias" the viewer's perception of a truncated chart.

## The Logic <!-- role: reason -->
Designers often use visual cues to signal that a chart does not start at zero, believing this transparency allows viewers to mentally correct for the missing data. However, empirical testing reveals that these signals fail to alter the immediate visual impression.
*   **The Principle:** Visual dominance. The visual magnification of the differences (the shape of the data) overrides the cognitive awareness of the axis manipulation.
*   **The Evidence:** [@correll_truncating_2020] tested standard bars against bars with broken axes and gradient bottoms. They found that "visual designs with non-zero axes that indicate y-axis breaks... were [not] perceived as having smaller effect sizes." The exaggeration persisted despite the explicit visual warnings.

## Where to Apply <!-- role: context -->
*   **User Goal:** Creating "honest" charts that require zooming in on small differences.
*   **Data Type:** Bar charts with non-zero baselines.
*   **Audience:** Viewers who are processing charts visually/preattentively rather than performing deep statistical analysis.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Adhering to strict style guides or scientific publication standards.
*   **Reason:** Some publication standards require these glyphs as a formality to indicate non-zero origins. You should include them to satisfy the standard, but do not expect them to fix the perceptual bias.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You cannot "have your cake and eat it too"—you cannot zoom in to show detail while simultaneously expecting the user to perceive the global context via a small icon.
*   **The Risk:** You may inadvertently deceive viewers who notice the break symbol but still subconsciously register the exaggerated difference as the primary takeaway.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding a "zigzag" on the y-axis of a highly zoomed-in bar chart to excuse the exaggeration.
*   **Why it fails:** The viewer sees the large difference in bar height first; the zigzag is ignored or discounted in the judgment of severity [@correll_truncating_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** A bar chart with a non-zero baseline and a break symbol.
*   **The Test:** Cover the break symbol. Does the chart look dramatic? If so, that dramatic impression is what the user will perceive, regardless of the symbol.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Accept that the chart emphasizes differences and ensure the text/caption contextualizes the small relative change.
*   **Best Fix:** Use an inset chart (Focus+Context) or show the full scale if the absolute magnitude is more important than the relative differences.
