---
id: annotate-context-and-outliers
title: Annotate Outliers and Context
bibliography: references.bib
description: Use text annotations to explain highlights, outliers, and the 'why' behind
  the data.
labels:
- visual:text
- impact:storytelling
- task:explain
- audience:general
---

## The Rule <!-- role: advice -->
Use text annotations to highlight specific data points, explain outliers, or provide context on why data looks the way it does (e.g., "The latest recession happened here").

## The Logic <!-- role: reason -->
Annotations are powerful for explanatory visualizations. They help readers understand *why* values are high or low without requiring them to guess. Furthermore, annotations make charts more visually appealing; readers get "intrigued by little notes that promise something interesting" [@muth_text_in_data_visualizations_2022].

## Where to Apply <!-- role: context -->
*   **User Goal:** Storytelling or explaining specific trends (explanatory vs. exploratory).
*   **Data Type:** Time series with events, scatterplots with outliers, or maps with specific regions of interest.
*   **Audience:** General audiences who may not know the historical context of the data.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Strictly exploratory dashboards intended for expert analysis.
*   **Reason:** Experts may want to discover insights themselves without being led by a pre-written narrative.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Cleanliness and minimalism.
*   **The Risk:** Over-annotating can clutter the chart and obscure the overall trend.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Putting all context in a paragraph of text below the chart.
*   **Why it fails:** Readers might skip the long text or fail to connect the written context to the specific visual peak or trough it describes.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is there a spike, dip, or outlier in the chart that is visually prominent but unexplained?
*   **The Test:** Ask "Why is this point so high?" If the chart doesn't answer it directly with a label, you need an annotation.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a small text note with a line pointing to the interesting data point.
*   **Best Fix:** Integrate the explanation into the visual layer, ensuring the text hierarchy distinguishes it from axis labels.
