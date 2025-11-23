---
id: use-analog-representations
title: Use Analog or Spatial Representations Over Tables
bibliography: references.bib
description: For audiences with lower health numeracy, prefer spatial displays (like
  meters) over row-and-column tables.
labels:
- chart:meter
- chart:gauge
- task:monitor-status
- visual:spatial
- impact:accessibility
- data:categorical
- audience:elderly
- audience:low-numeracy
---

## The Rule <!-- role: advice -->
For patients with lower document literacy or representational fluency, display measurements using spatial or analog metaphors (such as meters or scales) rather than tabular grids of numbers.

## The Logic <!-- role: reason -->
Representational fluency—the ability to recognize the same quantity in different formats—is not inherent; it is learned. Some populations, such as the elderly or those with low numeracy, may struggle to map values in a row-and-column table to their real-world meaning. However, these same users often possess the skills to read spatial devices (like blood pressure meters) because the visual position correlates directly to the value [@ancker_rethinking_2007].

## Where to Apply <!-- role: context -->
*   **User Goal:** Monitoring personal health metrics (e.g., blood pressure, glucose).
*   **Data Type:** Single-point numerical measurements comparing a current value to a range.
*   **Audience:** Elderly patients, users with low "document literacy," or those unfamiliar with spreadsheet conventions.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to identify precise historical trends or exact values for calculation.
*   **Reason:** Analog scales are better for "gist" or status checks; tables are superior for precise extraction of historical data points.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Density. Tables can hold dozens of data points in a small space; meters require significant screen real estate for a single datum.
*   **The Risk:** Users might overestimate the precision of the reading if the graphic is poorly designed.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Presenting a log or history solely as a spreadsheet-style grid (Date | Time | Value).
*   **Why it fails:** Users who can read the device itself may fail to recognize the same data when stripped of its spatial context and placed in a grid structure [@ancker_rethinking_2007].

## How to Check <!-- role: check -->
*   **Visual Sign:** Is the primary display a grid of text?
*   **The Test:** Ask a user to identify if a specific value is "high" or "low." If they have to read the number and mentally compare it to a memorized threshold, the design has failed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add color-coding or icons to the table to indicate status (High/Low).
*   **Best Fix:** Implement a visual interface that mimics the physical collection device (e.g., a digital meter graphic) or uses position on a scale to indicate value.
