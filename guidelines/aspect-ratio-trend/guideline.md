---
id: aspect-ratio-trend
title: Maintain Standard Aspect Ratios for Trends
bibliography: references.bib
description: Prevents manipulation of the perceived rate of change in line charts.
labels:
- chart:line
- visual:shape
- visual:angle
- task:estimate-rate
- impact:integrity
---

## The Rule <!-- role: advice -->
Avoid manipulating the width-to-height ratio of line charts to artificially flatten or steepen a slope.

## The Logic <!-- role: reason -->
Changing the aspect ratio directly alters the angle of the line. This leads to **Message Exaggeration or Understatement** regarding the rate of change. Widening the scales makes a rapid increase appear slow; narrowing them makes a slow increase appear rapid.
*   **The Principle:** Angle Perception / Slope Estimation
*   **The Evidence:** @pandey_how_2015 found that aspect ratio manipulation significantly affected participants' responses to "How much better" a quantity became over time. The deceptive (manipulated) charts led to significantly higher or lower estimates compared to the control.

## Where to Apply <!-- role: context -->
*   **User Goal:** Estimating the rate of increase or decrease (e.g., "Is this growing effectively?").
*   **Data Type:** Time-series data.
*   **Audience:** General public and decision makers.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Banking to 45 degrees.
*   **Reason:** There are mathematical techniques (like banking to 45 degrees) meant to optimize the discriminability of line segments, which is a valid perception-based reason to alter aspect ratio, distinct from deceptive manipulation.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may have less flexibility in fitting charts into arbitrary layout spaces (e.g., wide banners or tall sidebars).
*   **The Risk:** A "standard" aspect ratio might make a very slow trend look flat, which is accurate but might be deemed "boring."

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Stretching a chart to fit a wide column in a dashboard without adjusting the time range.
*   **Why it fails:** It visually flattens the slope, potentially understating the volatility or growth rate of the data.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart look unusually "squashed" (very wide) or "tall"?
*   **The Test:** Compare the visual angle of the slope to the mathematical rate of change. Is the visual drama proportional to the data change?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Adjust the canvas size to a more square or standard rectangular (e.g., 4:3 or 16:9) ratio.
*   **Best Fix:** Select an aspect ratio that maximizes the readability of the slopes (banking to 45 degrees) rather than fitting the chart to available white space.
