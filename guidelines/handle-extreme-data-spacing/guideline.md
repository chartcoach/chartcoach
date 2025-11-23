---
id: handle-extreme-data-spacing
title: Manage Space for Data Extremes and Similarities
bibliography: references.bib
description: Ensure chart layouts adapt to extreme data outliers or dense similarities
  to prevent unreadable, compressed displays.
labels:
- chart:line
- chart:scatter
- impact:accessibility
- impact:readability
- visual:position
- data:outliers
- data:high-density
---

## The Rule <!-- role: advice -->
Ensure your visualization layout automatically handles extreme differences (outliers) or extreme similarities (clustering) in the data. If automatic adaptation is not possible, you must provide clear annotations or user controls to filter, sort, and navigate the space.

## The Logic <!-- role: reason -->
Real-world data often contains extremes that break standard layout algorithms.
*   **The Principle:** Assistive Layout. When data containing outliers is plotted on standard linear scales, the majority of the data is often compressed into unreadable margins. Conversely, extreme similarity causes elements to overlap and merge.
*   **The Evidence:** Chartability identifies this as an "Assistive" heuristic failure because unmanaged space increases the cognitive and functional labor required to interpret the data [@elavsky_how_2022]. Proper management of macro and micro white space is critical for readability, as white space is an active design element, not wasted space [@towardsdatascience_data_visualisation_2].

## Where to Apply <!-- role: context -->
This applies specifically to environments where data is variable or user-generated.
*   **User Goal:** Exploratory analysis or monitoring where data ranges are not fixed.
*   **Data Type:** Data sets with potential outliers, heavy tails, or high-density clusters.
*   **Audience:** All users, but particularly critical for those using assistive technologies who rely on clear spatial separation or semantic descriptions of data density.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The goal is specifically to visualize the magnitude of the disparity between the outlier and the rest of the dataset.
*   **Reason:** If the compression of the majority data is the intended insight (e.g., "wealth inequality"), correcting the spacing might obscure the main message.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Implementation time. Building "intelligent" charts that detect collisions or outliers requires more complex code than standard plotting libraries provide by default.
*   **The Risk:** Automatic axis-breaking or log-scaling can sometimes confuse users who are unfamiliar with non-linear representations.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Allowing default auto-scaling to render all points, resulting in a chart where 90% of the data is a flat line against the x-axis.
*   **Why it fails:** The visualization becomes illegible because elements are "squished" into margins [@elavsky_how_2022].
*   **The Wrong Fix:** Plotting dense, similar lines without interactivity.
*   **Why it fails:** Users cannot distinguish individual series when differences are visually negligible.

## How to Check <!-- role: check -->
*   **Visual Sign:** Look for "pancaking," where most data points are flattened against an axis, or "hairballs," where lines merge into a solid block of color.
*   **The Test:** If two lines or points are so close together that it is almost impossible to see the difference between them visually, the design has failed this heuristic.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Provide clear annotations that explain what is happening in the dense or compressed areas.
*   **Best Fix:** Implement dynamic controls that allow the user to sort, divide, filter, or zoom into the chart space to resolve the extremes [@elavsky_how_2022]. Alternatively, use algorithmic approaches to switch chart types or scales when data density thresholds are met.
