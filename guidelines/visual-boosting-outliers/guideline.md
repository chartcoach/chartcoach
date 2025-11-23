---
id: visual-boosting-outliers
title: Visually Boost Outliers for Detection Tasks
bibliography: references.bib
description: Use explicit visual markers that occupy significant space (like striping)
  to make outlier detection accurate.
labels:
- chart:heatmap
- chart:strip-plot
- task:outlier-detection
- visual:highlight
- data:timeseries
---

## The Rule <!-- role: advice -->
When the primary task is identifying or counting outliers, explicitly map these values to a high-salience visual encoding, such as broad stripes or distinct glyphs, that overrides the context.

## The Logic <!-- role: reason -->
Standard encodings (like colorfields or line graphs) may hide brief outliers due to smoothing or lack of pixel space. "Visual boosting" ensures these signals are processed.
*   **The Principle:** Visual Boosting.
*   **The Evidence:** The "Event Striping" design (which mapped outliers to broad stripes over a smoothed colorfield) drastically outperformed all other designs for outlier counting tasks in [@albers_task-driven_2014].

## Where to Apply <!-- role: context -->
*   **User Goal:** Counting or locating unusual events (anomalies, errors, spikes).
*   **Data Type:** Large scale time series where normal data is high volume, and outliers are sparse.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to see the context *behind* the outlier.
*   **Reason:** Event striping often occludes the underlying data to make the outlier visible.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Context. The "boosting" technique (like widening a single pixel outlier to a 5-pixel stripe) distorts the temporal accuracy and hides local data.
*   **The Risk:** Users might overestimate the duration or frequency of outliers because they visually dominate the display.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying on a standard line chart where an outlier is just a single pixel spike.
*   **Why it fails:** In high-density displays, a single pixel spike is easily missed or rendered invisible by anti-aliasing.

## How to Check <!-- role: check -->
*   **Visual Sign:** Can you spot the outlier from 5 feet away?
*   **The Test:** If the outlier represents a critical failure, does it command attention, or does it blend into the noise?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Increase the stroke width or point size of data points that exceed a threshold.
*   **Best Fix:** Implement "Event Striping"—draw a distinct vertical band or overlay for any time step containing an outlier.
