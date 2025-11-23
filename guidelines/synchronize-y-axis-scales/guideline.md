---
id: synchronize-y-axis-scales
title: Synchronize Y-Axis Scales Across Panels
bibliography: references.bib
description: Use the same Y-axis scale for all panels to prevent misleading comparisons,
  or explicitly signal when scales differ.
labels:
- chart:small-multiples
- visual:scale
- impact:accuracy
- task:compare
---

## The Rule <!-- role: advice -->
Avoid independent Y-axis scales for your panels. If you must use different scales to show trends of vastly different magnitudes, you must make the difference obvious through text or visual cues.

## The Logic <!-- role: reason -->
*   **The Principle:** Visual Consistency Bias.
*   **The Evidence:** Readers typically assume that side-by-side panels share the same scale. [@muth_small_multiple_line_charts_2024] warns that independent scales can provide false insights (e.g., making a small trend look identical to a large trend). However, independent scales are useful when magnitudes vary wildly and the *trend shape* is more important than absolute value.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing the magnitude or rate of change across categories.
*   **Data Type:** Categories with similar units of measure.
*   **Audience:** General audiences who may overlook axis labels.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Comparing trends where magnitudes are vastly different (e.g., one line ranges 0-100, another 0-1,000,000) and the goal is comparing *shape* (trend), not *volume*.
*   **Reason:** On a shared scale, the small line would appear flat. As per [@muth_small_multiple_line_charts_2024], use independent axes here to give each line "visual height," but warn the reader.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Independent axes sacrifice the ability to visually compare volume/magnitude.
*   **The Risk:** Misleading the audience into thinking a small increase is a massive spike.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Letting software auto-scale every panel without notification.
*   **Why it fails:** Readers rarely check every single Y-axis label.

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the gridlines look uniform, or do they align differently in each chart?
*   **The Test:** If you use independent scales, does the chart description explicitly say "Notice that y-axis scalings differ"?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Force all panels to use the same min/max range.
*   **Best Fix:** If using variable scales, add a subtitle note (e.g., "Note: Scales vary by panel") or use distinct gridlines to signal the difference.
