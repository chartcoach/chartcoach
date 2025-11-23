---
id: label-directly-avoid-legends
title: Label Data Lines Directly
bibliography: references.bib
description: Place labels next to data elements rather than using a separate legend
  to reduce cognitive load.
labels:
- chart:line
- chart:pie
- visual:position
- impact:usability
- task:identify
---

## The Rule <!-- role: advice -->
Place the words that explain your chart elements as close to those elements as possible. Remove separate color keys (legends) and directly label your categories, lines, or segments.

## The Logic <!-- role: reason -->
Separating labels from data forces the reader's eye to travel back and forth, similar to walking between a museum exhibit and a label by the door. By the time the reader returns to the data, they may have forgotten the explanation. Direct labeling minimizes "eye-travel" and makes understanding the visualization more convenient [@muth_text_in_data_visualizations_2022].

## Where to Apply <!-- role: context -->
*   **User Goal:** Quick identification of categories in multi-series charts.
*   **Data Type:** Line charts, pie charts, and donut charts.
*   **Audience:** All audiences, particularly those on mobile devices where screen real estate is limited.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Extremely high-density charts (spaghetti charts) where lines overlap significantly at the label point.
*   **Reason:** There may not be enough physical space to place legible text next to every line without obscuring data.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose white space immediately adjacent to the data visualization.
*   **The Risk:** On small screens or with many data points, labels might overlap or look cluttered if not managed dynamically.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a legend box at the bottom or top of the chart.
*   **Why it fails:** It forces the reader to memorize colors and scan back and forth to decode the chart.

## How to Check <!-- role: check -->
*   **Visual Sign:** Is there a box containing colored circles/squares and text separate from the chart area?
*   **The Test:** Look at a specific line or slice. Do you have to move your eyes to a different part of the screen to know what it represents?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Move the text from the legend to the end of the lines or next to the pie slices.
*   **Best Fix:** Use annotation tools or software defaults (like in Datawrapper) that automatically attach labels to the corresponding data elements.
