---
id: indicate-axis-scale-units-caption
title: State Axis Range Units in Captions
bibliography: references.bib
description: Explicitly mention the standard deviation units used for axis ranges
  in figure captions to aid comparison.
labels:
- chart:bar
- chart:line
- task:communicate
- visual:text
- impact:clarity
- data:statistical
- source:witt_2019
---

## The Rule <!-- role: advice -->
When you manipulate the y-axis range to match a specific statistical spread (like 1.5 Standard Deviations), explicitly state the range in SD units in the figure caption.

## The Logic <!-- role: reason -->
Since the exact numerical range will vary from plot to plot based on the data's variance, indicating the range in Standard Deviation units provides a consistent scale for comparison across different graphs.
*   **The Principle:** Graph Fluency.
*   **The Evidence:** [@witt_graph_2019] notes that because the specific numerical range changes based on the error bars or effect size, stating the range in SD units helps the reader understand the scale, particularly when error bars are not included.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing multiple graphs with different variables or scales.
*   **Data Type:** Statistical data plotted using the "1.5 SD" rule or similar variance-based scaling.
*   **Audience:** Readers reviewing multiple figures within a single report or paper.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When using a fixed, absolute scale across all charts (e.g., all charts are 0-100%).
*   **Reason:** The consistency is already visually apparent; the caption would be redundant.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Increases the length and technical density of the figure caption.
*   **The Risk:** Readers unfamiliar with "SD units" may find the caption confusing.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Changing the axis scale to 1.5 SDs without telling the reader.
*   **Why it fails:** The reader may assume a standard "min-max" or "full" scale, leading to confusion about why the axis limits seem arbitrary numerical values [@witt_graph_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** Look at the figure caption.
*   **The Test:** Does it explain *why* the axis starts and ends where it does? (e.g., "Range of the y-axis is 1.5 standard deviations.")

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a sentence to the caption: "The y-axis range represents 1.5 standard deviations."
*   **Best Fix:** Standardize this disclosure across all figures in the document to help readers learn the convention.
