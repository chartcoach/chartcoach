---
id: prioritize-task-over-precision
title: Prioritize Task Fit Over Perceptual Precision
bibliography: references.bib
description: Choose visual encodings based on the specific analytical task (e.g.,
  spotting trends, shapes) rather than defaulting to the most precise channel for
  value reading.
labels:
- chart:heatmap
- chart:line
- task:overview
- task:trend-analysis
- visual:position
- visual:color
- impact:efficiency
---

## The Rule <!-- role: advice -->
Do not default to position-based encodings (like scatter plots or dot plots) simply because they are the most precise for reading individual values. Instead, select encodings that best support the specific perceptual task required, such as identifying shapes, trends, or the "big picture."

## The Logic <!-- role: reason -->
While position on a common axis is the most precise channel for extracting individual values (ratio judgments), it is often inferior for other fundamental analytics tasks.
*   **The Principle:** **Task-Encoding Congruence**. Different tasks rely on different perceptual operations. For example, spotting the "big picture" or distinct "shapes" in data is often easier with encodings that are theoretically less precise for single values (like heatmaps or line charts) because they support holistic pattern recognition [@bertini_why_2020].
*   **The Evidence:** In comparing grid visualizations, [@bertini_why_2020] note that a heatmap (imprecise for values) is superior for seeing the overall dataset structure, while a line chart adds an emergent encoding of local deltas (orientation) that dots lack.

## Where to Apply <!-- role: context -->
*   **User Goal:** The user needs to identify high-level patterns, trends, rising/falling shapes, or the overall density of a dataset.
*   **Data Type:** Large grids of values, time series, or dense multidimensional data.
*   **Audience:** Analysts looking for "motifs" or broad behaviors rather than exact numbers.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Precise Value Retrieval.
*   **Reason:** If the primary task is indeed comparing two specific points to calculate an exact ratio (e.g., "Is A exactly twice as large as B?"), then position-based charts (dot plots, scatter plots) remain the gold standard [@bertini_why_2020].

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to read individual values with high accuracy.
*   **The Risk:** Users may misinterpret specific data points if they try to read them as exact numbers rather than patterns.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Converting a dense heatmap or line chart into a massive dot plot or scatter plot to "increase precision."
*   **Why it fails:** This destroys the emergent shapes and "big picture" view, forcing the user to mentally reconstruct trends from discrete points [@bertini_why_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does your chart look like a cloud of disconnected points when the user is asking about "trends" or "shapes"?
*   **The Test:** Ask: "If I squint, do I see the pattern the user cares about?" If you see only dust, you have prioritized precision over task fit.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a connecting line to dot plots to introduce orientation cues for trends.
*   **Best Fix:** Switch to a chart type optimized for the task (e.g., a heatmap for density/overview, lines for trends), even if the channel (color, orientation) is "less precise" [@bertini_why_2020].
