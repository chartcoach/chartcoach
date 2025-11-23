---
id: visualize-error-explicitly
title: Visualize Error Estimates Directly on the Graph
bibliography: references.bib
description: Do not rely on text captions for error margins; visual integration is
  required for accurate judgment.
labels:
- chart:bar
- visual:text
- task:integration
- impact:confidence
- source:bad-practice
---

## The Rule <!-- role: advice -->
Always visualize margins of error or uncertainty directly on the chart glyphs. Do not relegate error information to text captions, legends, or subtitles while displaying only the means graphically.

## The Logic <!-- role: reason -->
Removing visual error bars and relying on text (e.g., "Margin of error +/- 3%") forces the user to mentally project the error onto the graph. This mental operation is highly prone to failure.
*   **The Principle:** Visual Integration.
*   **The Evidence:** When error bars were removed and replaced with text, participants' confidence in their judgments *increased* unjustifiably, while their accuracy became unpredictable. Visualizing the error acts as a necessary signal of uncertainty that tempers overconfidence [@correll_error_2014].

## Where to Apply <!-- role: context -->
*   **User Goal:** Any comparison between two values where statistical significance is a factor.
*   **Data Type:** Polling data, experimental results.
*   **Audience:** Lay audiences (who are prone to ignoring text caveats in favor of the strong visual signal of the mean).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The error is negligible.
*   **Reason:** If the uncertainty is smaller than the resolution of the display (e.g., less than a pixel), visual encoding adds noise without information.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual Simplicity. Adding error ranges adds "ink" and complexity to a clean chart.
*   **The Risk:** Clutter, especially in datasets with many data points.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Listing "Margin of Error: +/- 5%" in the footer of a bar chart.
*   **Why it fails:** Users generally fail to account for the error when making visual comparisons, leading to unjustified certainty in the difference between means [@correll_error_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** A chart containing only bars or points, with a text note about "significance" or "error" located elsewhere.
*   **The Test:** If you cover the text caption, does the chart look like definitive, exact data? If yes, it is misleading.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add standard error bars to the existing plot.
*   **Best Fix:** Integrate the error into the shape of the data using a Gradient Plot or Violin Plot to force the user to process the uncertainty simultaneously with the mean [@correll_error_2014].
