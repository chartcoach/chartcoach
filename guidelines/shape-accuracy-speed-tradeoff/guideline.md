---
id: shape-accuracy-speed-tradeoff
title: Accept Slower Performance When Using Shape for Precision
bibliography: references.bib
description: Use complex shape encodings for high accuracy, but be aware they significantly
  slow down user response times.
labels:
- chart:glyph
- chart:scatterplot
- task:find-extremum
- task:correlate
- visual:shape
- impact:speed
- data:quantitative
---

## The Rule <!-- role: advice -->
Only use countable shape features (such as the number of spikes on a star) to encode quantitative data if high accuracy is required and slower reading speed is acceptable.

## The Logic <!-- role: reason -->
Shape encodings that rely on countable elements (like spikes) allow users to determine values and order with high precision because they can be explicitly counted or compared. However, this cognitive process is cognitively demanding and slow.
*   **The Principle:** Cognitive Load vs. Precision
*   **The Evidence:** In the results from [@chung_how_2016] presented by [@zeng_review_2023], Shape ranked highly for accuracy (2nd for finding extremums, 3rd for correlation) but consistently ranked last (6th) for completion time in both tasks.

## Where to Apply <!-- role: context -->
*   **User Goal:** Detailed comparison where precision matters more than "at-a-glance" speed.
*   **Data Type:** Discrete quantitative values or small-range integers.
*   **Audience:** Expert users or situations where the data density is low enough to allow inspection.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Dashboards requiring rapid monitoring or "glanceability."
*   **Reason:** The slow response time makes shape encodings unsuitable for time-critical decision-making [@chung_how_2016].

## The Price <!-- role: costs -->
*   **The Sacrifice:** User efficiency (time-on-task).
*   **The Risk:** Users may become fatigued if they are required to process many shape-encoded glyphs repeatedly.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using shape variations (like spikes) for a real-time monitoring display.
*   **Why it fails:** Users take significantly longer to process shape changes compared to pre-attentive attributes like Size or Value.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the visualization require the user to "count" features on a mark to understand its value?
*   **The Test:** Measure how long it takes to identify the maximum value. If it feels laborious, the shape encoding is introducing cognitive drag.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Switch to Color Value (Luminance) if speed is the priority.
*   **Best Fix:** Reserve shape encodings for secondary variables that do not require rapid scanning.
