---
id: use-horizontal-bars-on-mobile
title: Use Horizontal Bars for Small Screens
bibliography: references.bib
description: On mobile devices, vertical column charts crowd labels; horizontal bar
  charts adapt better by growing vertically.
labels:
- chart:bar
- chart:column
- visual:orientation
- impact:mobile-optimization
- impact:readability
- audience:general
---

## The Rule <!-- role: advice -->
Prioritize horizontal bar charts over vertical column charts when designing for small screens or mobile devices, especially if you have many categories.

## The Logic <!-- role: reason -->
Column charts have a fixed horizontal width. When "squished down to smartphone size," labels often overlap or must be turned sideways, making them hard to read. Horizontal bar charts, conversely, grow vertically; they can be as tall as necessary to accommodate all labels legibly without horizontal constraint [@muth_chart_types_guide_2025].

## Where to Apply <!-- role: context -->
*   **User Goal:** Reading labels and values clearly on a phone.
*   **Data Type:** Categorical data with many items (e.g., 30 items) or long labels.
*   **Audience:** Mobile users or responsive web designs.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Time series data with few points (e.g., "wildfires in the past five years").
*   **Reason:** Time is conventionally plotted on the horizontal axis (left to right). A column chart is usually a good fit for a few points in time [@muth_chart_types_guide_2025].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the conventional "y-axis is value" orientation that some readers expect for specific data types.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Rotating axis labels 90 degrees on a column chart.
*   **Why it fails:** It forces the user to tilt their head or strain to read, creating an "awkward" experience [@muth_chart_types_guide_2025].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are your x-axis labels diagonal, vertical, or overlapping?
*   **The Test:** Resize your browser window to narrow (mobile width). If the chart labels break, switch to bars.

## How to Fix <!-- role: fix -->
*   **Best Fix:** Transpose the chart so categories are on the y-axis (horizontal bars).
