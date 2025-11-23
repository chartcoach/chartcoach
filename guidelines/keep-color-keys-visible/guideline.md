---
id: keep-color-keys-visible
title: Keep Color Keys Visible via Sticky Positioning or Repetition
bibliography: references.bib
description: Ensure readers never scroll away from the legend by making it sticky
  or repeating it.
labels:
- visual:color
- visual:layout
- impact:usability
- audience:general
- chart:general
---

## The Rule <!-- role: advice -->
For long, scrolling visualizations, ensure the color key remains visible at all times. Either make the key "sticky" (fixing it to the top, bottom, or side of the viewport) or repeat the key multiple times throughout the scroll.

## The Logic <!-- role: reason -->
Readers forget color associations quickly. Even after reading a legend once, they often need to re-check it while scanning the data. If the legend disappears off-screen, the reader must scroll back and forth, disrupting the reading flow [@muth_remind_colors_2023].
*   **The Principle:** Working Memory Limits
*   **The Evidence:** [@muth_remind_colors_2023] notes that even the creator of a chart needs to check the key repeatedly.

## Where to Apply <!-- role: context -->
This rule applies to digital formats where the visualization height exceeds the screen height.
*   **User Goal:** Reading long-form data stories or tall charts.
*   **Data Type:** Vertical timelines, long tables, or scrollytelling maps.
*   **Audience:** Online readers on desktop or mobile devices.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Static Print Media.
*   **Reason:** In print, simply ensuring the visualization and key are on the same page is sufficient [@muth_remind_colors_2023].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate. A sticky header reduces the available vertical space for the chart itself.
*   **The Risk:** Repetition might feel redundant to some, though [@muth_remind_colors_2023] argues readers are rarely annoyed by clarity, only by confusion.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Placing a single legend at the very top of a long article.
*   **Why it fails:** Once the user scrolls past the first screen, the data becomes abstract shapes without meaning.

## How to Check <!-- role: check -->
*   **Visual Sign:** Scroll to the middle or bottom of your chart. Can you still see the legend?
*   **The Test:** If you have to scroll up more than "roughly the height of the screen" to identify a color, the key is too far away [@muth_remind_colors_2023].

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Duplicate the legend image and insert it periodically between chart sections.
*   **Best Fix:** Implement a CSS sticky position for the legend element or use a visualization tool that supports sticky keys.
