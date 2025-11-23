---
id: linear-layout-for-narrative
title: Arrange Sequential Panels in a Single Row
bibliography: references.bib
description: Use a horizontal row layout for small multiples to mimic a comic strip
  and guide the reader's eye.
labels:
- chart:small-multiples
- chart:line
- task:storytelling
- visual:layout
- impact:narrative
- audience:general
---

## The Rule <!-- role: advice -->
When telling a sequential story with small multiple charts, arrange the panels in a single horizontal row rather than a grid or wrapped lines.

## The Logic <!-- role: reason -->
Placing panels in a single row allows the visualization to function "like the panels of a comic strip" [@mintzer_sequential_storytelling_2024]. This linear layout establishes a clear reading order (left to right), signaling to the reader that the charts represent an "unfolding story" rather than a collection of isolated statistics.

## Where to Apply <!-- role: context -->
*   **User Goal:** Guiding the reader through a "deliberate sequence" of information [@mintzer_sequential_storytelling_2024].
*   **Data Type:** Interrelated trends or metrics where one leads to another.
*   **Audience:** Readers who need to understand the relationship between multiple metrics, not just the values.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** At-a-glance monitoring or dashboards.
*   **Reason:** If the goal is rapid information retrieval rather than narrative guidance, a grid or compact layout may be more efficient as it requires less eye travel.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate width. A single row requires significant horizontal space or forces individual charts to be smaller.
*   **The Risk:** On narrow screens (mobile), a single row may force scrolling or become illegible, whereas a grid adapts more easily.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a default 2x2 grid for a sequential story.
*   **Why it fails:** A grid structure implies "two numbers up, two done" rather than a connected narrative flow [@mintzer_sequential_storytelling_2024].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are your charts stacked vertically or wrapped onto a second line?
*   **The Test:** Does the layout look like a dashboard (grid) or a timeline/comic strip (row)?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the chart settings to display "1 row" or maximize the column count to equal the number of charts.
*   **Best Fix:** Reformat the canvas to be wide and short, placing all panels side-by-side to enforce linear reading.
