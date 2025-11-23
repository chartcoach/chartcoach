---
id: chartability-appropriate-spacing
title: Balance White Space and Padding
bibliography: references.bib
description: Use appropriate structural spacing to ensure content is perceivable and
  understandable, avoiding extremes of clutter or disconnection.
labels:
- chart:bar
- chart:column
- visual:layout
- impact:accessibility
- impact:readability
- visual:whitespace
---

## The Rule <!-- role: advice -->

Structure your visualization with appropriate white space and padding. Ensure spacing between data intervals (such as gaps between bars) is neither too narrow nor too wide.

## The Logic <!-- role: reason -->

White space is not wasted background; it is a critical design element that improves readability and aesthetics.

*   **The Principle:** **Perceivability and Grouping.** Proper usage of white space defines boundaries and groups related items, guiding the viewer's eye through the design [@calliaweb_whitespace_not]. It creates a balance between "macro" and "micro" space that allows users to distinguish content easily [@towardsdatascience_data_visualisation].
*   **The Evidence:** Within the Chartability framework, "Spacing is inappropriate" is identified as a failure of the **Perceivable** and **Understandable** principles. Research indicates that improper intervals (e.g., thin bars with large gaps) create barriers to interpreting data relationships [@elavsky_how_2022].

## Where to Apply <!-- role: context -->

*   **User Goal:** Identifying distinct data values and understanding the structure of the visualization.
*   **Data Type:** Discrete data or charts with intervals, such as bar charts, column charts, or grouped layouts.
*   **Audience:** All users, but particularly critical for accessibility to ensure content is not visual noise.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Histograms or continuous data distributions.
*   **Reason:** In a histogram, the lack of gap between bars implies continuity of the numerical range. Introducing white space here would incorrectly imply discrete categories.

## The Price <!-- role: costs -->

*   **The Sacrifice:** Screen real estate and data density. Increasing white space reduces the area available for the data marks themselves.
*   **The Risk:** Overusing white space can lead to disconnection. If gaps are too large, the eye struggles to compare values across the chart, or the data may feel sparse and unrelated [@elavsky_how_2022].

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Increasing chart size without adjusting element width.
*   **Why it fails:** This often results in extremely thin bars with massive gaps, making the data hard to see and compare.
*   **The Clutter Trap:** Eliminating white space to fit more data.
*   **Why it fails:** This creates a "wall of ink" where boundaries blur, causing perceivability issues.

## How to Check <!-- role: check -->

*   **Visual Sign:** Does the chart look like a "barcode" (too tight) or floating islands (too loose)?
*   **The Test:** Check for the specific Chartability heuristic: "Spacing is inappropriate." Ensure that interval gaps distinctively separate items without breaking the visual flow [@elavsky_how_2022].

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Adjust the `gap` or `padding` settings in your visualization tool to a moderate ratio (e.g., bar width > gap width).
*   **Best Fix:** Re-evaluate the density of the data. If the white space balance cannot be fixed by resizing, filter the data or break the chart into small multiples to maintain readability.
