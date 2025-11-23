---
id: use-color-hue-for-aggregate-time-series
title: Use Color Hue for Aggregate Time-Series Judgments
bibliography: references.bib
description: Prioritize color encodings over line charts when the user task involves
  estimating averages or aggregates in time series data.
labels:
- chart:heatmap
- chart:colorfield
- task:aggregate
- visual:color-hue
- data:temporal
- impact:accuracy
---

## The Rule <!-- role: advice -->
Visualize time-series data using color hue encodings (such as colorfields or heatmaps) instead of vertical position (line charts) when the primary task is to identify aggregate properties, such as determining regions with the highest average value.

## The Logic <!-- role: reason -->
Experimental evidence demonstrates that users are significantly more accurate at performing aggregate tasks—specifically identifying the month with the highest average value—when using color encodings compared to standard line charts. The visual system appears to aggregate color information over a region more effectively than it calculates the average vertical position of a fluctuating line.
*   **The Evidence:** In a study collated by [@zeng_review_2023], comparisons showed that colorfield designs (E-2) outperformed line charts (E-1) for aggregate tasks with high statistical significance (p < 0.001) [@correll_comparing_2012].

## Where to Apply <!-- role: context -->
This advice applies to visualization scenarios focused on summarization or overview tasks.
*   **User Goal:** The user needs to assess the "big picture" or find an average value over a specific time window (e.g., "Which month had the best performance on average?").
*   **Data Type:** Quantitative time-series data, particularly where the density or variance might make a line chart "noisy."
*   **Audience:** Analysts or general users performing summary analysis rather than precise point reading.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to read specific, precise values (Retrieve Value tasks).
*   **Reason:** While the cited evidence [@correll_comparing_2012] proves color is superior for *aggregation*, positional encodings (line charts) are generally understood to be superior for retrieving exact quantitative values.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the familiarity of the standard line chart, which is the convention for time-series data.
*   **The Risk:** Users unfamiliar with colorfields may initially struggle to interpret the encoding without a clear legend, although their performance on the specific task of averaging will likely be higher.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a line chart with a smoothing algorithm (like a moving average) to help users see the average.
*   **Why it fails:** While smoothing helps, the raw evidence suggests that simply changing the encoding to color hue is a perceptually robust method for aggregation tasks without necessarily altering the data geometry [@correll_comparing_2012].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the data displayed as a jagged line (Position Y) even though the question asked is about the "overall" or "average" behavior of a region?
*   **The Test:** Ask the user to identify the period with the highest average. If they have to mentally trace and "balance" the peaks and valleys of a line, the design is suboptimal.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Apply a color encoding to the points or area of the line chart to reinforce the value magnitude.
*   **Best Fix:** Convert the visualization to a 1D heatmap or "colorfield" where time is on the X-axis and the quantitative value is encoded purely by color hue or saturation.
