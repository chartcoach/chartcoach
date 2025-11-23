---
id: describe-visually-apparent-features
title: Describe Visually Apparent Statistical Features
bibliography: references.bib
description: Explicitly describe trends, patterns, and outliers found in visualizations
  via text or alternative modalities to ensure non-visual access to insights.
labels:
- impact:accessibility
- impact:understanding
- visual:patterns
- task:summary
- audience:blind
- audience:low-vision
- category:assistive
---

## The Rule <!-- role: advice -->
Explicitly describe all visually apparent statistical features—such as trends, clusters, patterns, outliers, or significant findings—using text, sonification, or tactile means. Do not rely solely on the visual rendering to convey these relationships.

## The Logic <!-- role: reason -->
Visualizations allow sighted users to instantly perceive relationships using visual processing, but these insights are often lost when converted to simple data tables or basic alternative text.
*   **The Principle:** The **Assistive** principle of Chartability dictates that interfaces should be intelligent and multi-sensory to reduce the cognitive and functional labor required for access [@elavsky_how_2022].
*   **The Evidence:** Standard accessibility guidelines emphasize that structural information conveyed visually must be programmatically determinable [@w3c_understanding_info]. However, automated descriptions often fall short of capturing higher-level information like trends or outliers, necessitating manual or robust semantic descriptions [@elavsky_how_2022].

## Where to Apply <!-- role: context -->
This guideline applies to any data visualization where the primary insight is derived from the shape or distribution of the data.
*   **User Goal:** Understanding the "story" or statistical takeaways (e.g., "Sales are increasing") rather than just reading raw data points.
*   **Data Type:** Charts displaying relationships, such as scatter plots (clusters/outliers) or line charts (trends/volatility).
*   **Audience:** Users of screen readers (blind/low-vision) or those with cognitive disabilities who benefit from explicit summaries.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** When the visualization is purely exploratory and contains no pre-determined or statistically significant patterns.
*   **Reason:** If no features are "visually apparent" even to a sighted expert, forcing a description may introduce bias or false narratives. However, the raw data structure must still be accessible.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Implementing this requires significant manual authoring or advanced engineering. Building materials that semantically describe relationships are currently lacking, and "visually apparent" features are difficult to automate reliably [@elavsky_how_2022].
*   **The Risk:** Sonification and tactile experiences are often authored in parallel to, rather than integrated with, the visualization, potentially creating disjointed experiences if not managed carefully [@elavsky_how_2022].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying entirely on automated captioning tools.
*   **Why it fails:** Current research indicates that automated descriptions often lack the robustness required to interpret complex semantic layers of information effectively [@elavsky_how_2022].
*   **The Wrong Fix:** Providing only a raw data table.
*   **Why it fails:** A table provides the data but forces the user to mentally calculate the trends or outliers that are instantly visible to sighted users, failing the Assistive principle of reducing labor.

## How to Check <!-- role: check -->
*   **Visual Sign:** Look at the chart. specific trends (e.g., "upward slope"), clusters, or outliers are immediately obvious.
*   **The Test:** Close your eyes or turn off the monitor. Using only the text descriptions, captions, or audio (sonification) provided, can you identify those same trends, clusters, or outliers?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Manually write a text summary that explicitly states the visual findings (e.g., "The data shows a strong positive trend with one significant outlier in Q4") and place it in the figure caption or description.
*   **Best Fix:** Implement multi-sensory representations, such as sonification modules that map data values to pitch and duration, allowing users to perceive trends through audio [@highcharts_highcharts_accessibility].
