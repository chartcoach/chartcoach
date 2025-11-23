---
id: encode-averages-with-color
title: Use Color to Visualize Averages Over Time
bibliography: references.bib
description: When users need to estimate averages over ranges of time, colorfields
  outperform line graphs.
labels:
- chart:colorfield
- chart:heatmap
- task:summary
- task:aggregate
- visual:color
- impact:efficiency
- data:temporal
- audience:analyst
---

## The Rule <!-- role: advice -->
When the primary user task is to estimate or compare average values over specific time ranges (aggregates), encode the data values using color intensity or hue rather than vertical position (line graphs).

## The Logic <!-- role: reason -->
The human visual system can "average" optical parameters like color and intensity across a spatial region efficiently and pre-attentively. This is known as the theory of perceptual averaging.
*   **The Principle:** Visual Averaging vs. Shape Perception.
*   **The Evidence:** [@correll_comparing_2012] demonstrates that participants were significantly more accurate at identifying the month with the maximum average value when using colorfields compared to line graphs. The complex shapes of line graphs are processed in higher-level visual areas that cannot average across multiple instances as efficiently as the low-level visual system processes pooled color.

## Where to Apply <!-- role: context -->
This advice applies to "big picture" tasks where the goal is summarization rather than precise point extraction.
*   **User Goal:** Identifying sub-ranges (e.g., months) with the maximum or minimum average value.
*   **Data Type:** Noisy time series data or 1D signal data (e.g., sales data, genomics).
*   **Audience:** Users needing rapid assessments of statistical properties over large amounts of data.

## When to Break It <!-- role: exceptions -->
Do not use this rule if the user needs to read exact values or analyze specific local trends.
*   **Scenario:** The user needs to find the specific date of a peak value or read an exact y-axis value.
*   **Reason:** Positional encodings (line graphs) are more precise for retrieving specific values than color encodings [@correll_comparing_2012].

## The Price <!-- role: costs -->
Using colorfields trades precision for summarization power.
*   **The Sacrifice:** You lose the ability to easily detect high-frequency details, such as specific peaks or "needle in the haystack" values within the aggregate block.
*   **The Risk:** Users may struggle to determine the exact numerical value of a data point due to the limitations of color perception compared to position.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** using a standard line graph for tasks requiring the user to mentally average noisy data.
*   **Why it fails:** Users cannot effectively "average out" the shape of a noisy line graph visually; they struggle to ignore the high-frequency spikes to see the underlying mean [@correll_comparing_2012].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you asking users to look at a jagged line and tell you which section is "generally higher"?
*   **The Test:** If the line graph has significant noise or variance (high frequency changes), try converting it to a color strip. If the "hot" regions become immediately obvious without mental calculation, the colorfield is superior.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Keep the line graph but add a colored background strip or heatmap below it that encodes the same values.
*   **Best Fix:** Replace the line graph with a "colorfield" or heatmap strip where time is on the X-axis and the value is encoded entirely by color saturation or hue.
