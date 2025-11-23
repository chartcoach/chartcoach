---
id: annotate-area-charts
title: Use Annotations in Area Charts
bibliography: references.bib
description: Utilize the ample space in area charts to add explanatory annotations
  and highlight ranges.
labels:
- chart:area
- visual:text
- visual:highlight
- impact:storytelling
- task:explain
---

## The Rule <!-- role: advice -->
Use annotations and highlight ranges to add explanations to your area charts.

## The Logic <!-- role: reason -->
Area charts create large blocks of color that serve as excellent backgrounds for text, unlike line charts which are mostly whitespace.
*   **The Principle:** Contextual Layering.
*   **The Evidence:** Area charts offer "enough space" for annotations, making the chart more interesting and helping readers figure out what is going on [@muth_area_charts_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** Storytelling and explaining *why* changes occurred.
*   **Data Type:** Time series data with notable events (peaks, valleys, sudden shifts).
*   **Audience:** Readers who need context, not just raw numbers.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Highly volatile, "noisy" data.
*   **Reason:** If the chart is extremely jagged, the background color is unstable and text may become hard to read or overlapping.

## The Price <!-- role: costs -->
*   **The Sacrifice:** "Clean" minimalism.
*   **The Risk:** Over-annotating can clutter the chart and distract from the overall trend.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Putting explanations in a caption below the chart.
*   **Why it fails:** It disconnects the explanation from the visual event.

## How to Check <!-- role: check -->
*   **Visual Sign:** Large empty fields of color with no context.
*   **The Test:** Does the chart explain *why* a spike happened in 2015? If not, add an annotation.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a text box pointing to a specific peak or valley.
*   **Best Fix:** Use background shading (highlight ranges) for time periods and direct text labels for specific events.
