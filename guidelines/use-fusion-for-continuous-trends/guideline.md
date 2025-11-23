---
id: use-fusion-for-continuous-trends
title: Use Fusion for Continuous Trends
bibliography: references.bib
description: Map continuous trend data using the Fusion pattern rather than discrete
  Tokens to emphasize overall direction over specific values.
labels:
- chart:area
- task:trend-analysis
- visual:shape
- impact:continuity
- data:temporal
- audience:analyst
---

## The Rule <!-- role: advice -->
When the goal is to communicate continuous trends or overall patterns over time, map data items using the "Fusion" pattern (e.g., area charts) rather than the "Token" pattern (e.g., discrete points or bars).

## The Logic <!-- role: reason -->
The Fusion pattern maps multiple data items into a single visualization in a continuous fashion, fused together. According to [@ola_beyond_2016], using Fusion allows users to "understand overall trends... as opposed to distinct values for each year." In contrast, Tokens emphasize the uniqueness of individual data points, which can distract from the macro-level temporal movement.

## Where to Apply <!-- role: context -->
*   **User Goal:** Assessing trends across a timeline (e.g., mortality rates from 1990-2010).
*   **Data Type:** Longitudinal or time-series data where the shape of the change is more important than specific daily/yearly values.
*   **Audience:** Analysts looking for patterns of increase or decrease across regions.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Precision Reading.
*   **Reason:** If the user needs to read the exact value for a specific year (e.g., "What was the exact rate in 1995?"), discrete Tokens (points/bars) are clearer than a fused area shape [@ola_beyond_2016].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Granularity. You lose the immediate distinctness of the individual data points (e.g., the exact value for 2004 is harder to isolate in a smooth area chart).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using discrete shapes (like dots) for general trend analysis.
*   **Why it fails:** This forces the user to mentally connect the dots to perceive the trend, increasing cognitive load.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is your time series represented by a sequence of unconnected shapes?
*   **The Test:** Ask if the "uniqueness" of a specific time point is important. If not, fuse them.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Connect discrete points with a line (Link pattern) or fill the area below the line (Fusion pattern) to create a unified shape [@ola_beyond_2016].
