---
id: orient-bars-by-data-type
title: Orient Bar Charts Based on Data Type
bibliography: references.bib
description: Choose vertical or horizontal orientation for bar charts based on whether
  the axis is nominal, time-based, or binned.
labels:
- chart:bar
- visual:orientation
- data:categorical
- data:temporal
- impact:readability
---

## The Rule <!-- role: advice -->
Use vertical bar charts (columns) when the independent variable is time or binned quantitative data. Use horizontal bar charts when the independent variable is nominal (categorical).

## The Logic <!-- role: reason -->
The orientation of a chart should support the readability of axis labels and the natural ordering of data types.
*   **The Principle:** Label Readability and Convention.
*   **The Evidence:** Compass (the engine behind Voyager) explicitly ranks horizontal bar charts higher for nominal data because "their axis labels are easier to read" (avoiding rotation or truncation). Conversely, it favors vertical bars for temporal or binned data to align with the convention of time/sequences flowing left-to-right [@wongsuphasawat_voyager_2016].

## Where to Apply <!-- role: context -->
*   **User Goal:** Reading labels clearly without tilting their head or interpreting abbreviated text.
*   **Data Type:** Nominal strings (often long) vs. Time units (Year, Month) or Bins.
*   **Chart Type:** Bar charts and histograms.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The nominal labels are extremely short (e.g., "A", "B", "C").
*   **Reason:** Vertical columns may be acceptable here as label rotation is unnecessary.
*   **Scenario:** Screen space constraints (e.g., a very wide but short aspect ratio).
*   **Reason:** The physical container might force a specific orientation.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Vertical space. Horizontal bar charts with many categories grow tall, potentially requiring vertical scrolling.
*   **The Risk:** If the time series has extremely long labels (e.g., full timestamps), vertical bars might still result in overlapping text.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using vertical bar charts for long categorical names and rotating the text 45 or 90 degrees.
*   **Why it fails:** This significantly reduces reading speed and legibility.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you tilting your head to read axis labels?
*   **The Test:** Check the data type of the axis. If it is "Category/Name" and the bars are vertical, check if labels are rotated. If it is "Time/Date" and bars are horizontal, ensure the flow feels natural.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Swap the x and y axes.
*   **Best Fix:** Automate the selection: If `type == nominal`, default to Horizontal. If `type == temporal` or `binned_quantitative`, default to Vertical.
