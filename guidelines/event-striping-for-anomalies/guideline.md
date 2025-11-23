---
id: event-striping-for-anomalies
title: Use Event Striping to Highlight Anomalies
bibliography: references.bib
description: For tasks specifically focused on outlier detection, event striping significantly
  outperforms standard charts.
labels:
- chart:event-striping
- task:find-anomalies
- visual:color-saturation
- data:outliers
- impact:efficiency
---

## The Rule <!-- role: advice -->
When the primary task is detecting outliers, use "Event Striping"—rendering specific vertical bands or distinct marks for values exceeding a threshold—instead of relying on the user to scan a line or box plot.

## The Logic <!-- role: reason -->
Pre-attentive processing allows distinct visual bands to "pop out," whereas scanning a line graph for peaks requires serial processing.
*   **The Evidence:** In the study reviewed by [@zeng_review_2023], the "Event Striping" design (E-7) ranked #1 for the "find-anomalies" task.
*   **The Stats:** E-7 was significantly better than all other designs tested, including the standard Line Graph (E-1) and the Composite Graph (E-4) [@albers_task-driven_2014].

## Where to Apply <!-- role: context -->
*   **User Goal:** Rapidly identifying moments where a system went out of bounds or a metric spiked unusually.
*   **Data Type:** Time-series data with defined thresholds for "normal" behavior.
*   **Audience:** System monitors, network administrators, or QA analysts.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the user also needs to characterize the distribution (spread) of the data.
*   **Reason:** While E-7 dominates anomaly detection, it performed poorly (ranked low) for "characterize-distribution" and "find-extremum" (magnitude) tasks [@albers_task-driven_2014]. It sacrifices detail for binary detection.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Context and precision for non-outlier data. The striping technique often simplifies the underlying signal (e.g., using a moving mean) to make the stripes visible.
*   **The Risk:** False sense of security if the threshold for "striping" is set incorrectly; users may ignore non-highlighted trends.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a Box Plot (E-3) for anomaly detection.
*   **Why it fails:** While Box Plots technically show outliers, the experiment showed E-3 was not included in the top rank for finding anomalies compared to the high-contrast Event Striping [@zeng_review_2023].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the user have to scan the y-axis height of every point to find the problem?
*   **The Test:** Can you identify the problem area in under 200 milliseconds (preattentive processing speed)?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a reference band or line; color any data point that crosses it distinctively.
*   **Best Fix:** Implement Event Striping (E-7), where vertical colored bands are rendered specifically where data violates statistical thresholds.
