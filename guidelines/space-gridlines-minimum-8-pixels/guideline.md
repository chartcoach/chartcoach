---
id: space-gridlines-minimum-8-pixels
title: Space Gridlines at Least 8 Pixels Apart
bibliography: references.bib
description: A specific pixel density rule for gridlines to prevent visual interference
  and reading error.
labels:
- chart:bar
- chart:line
- visual:gridlines
- visual:density
- impact:legibility
---

## The Rule <!-- role: advice -->
Ensure that gridlines are separated by at least 8 pixels of screen space.

## The Logic <!-- role: reason -->
While gridlines generally improve judgment accuracy, packing them too densely impedes the viewer's ability to trace data points to labels. Error rates increase steeply when the spacing drops below this threshold (e.g., 40px high charts with 10 unit spacing resulted in massive error) [@heer_crowdsourcing_2010].
*   **The Principle:** Visual Interference
*   **The Evidence:** Experiment 3 in [@heer_crowdsourcing_2010] showed steep error increases when grid density exceeded 1 line per 8 pixels.

## Where to Apply <!-- role: context -->
*   **User Goal:** Tracing a value from a bar or line to its axis value.
*   **Data Type:** Small charts, sparklines, or mobile visualizations.
*   **Audience:** Web users.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Large Format Displays.
*   **Reason:** On very large displays where physical viewing distance is greater, pixel measurements may need to be adjusted for visual angle (though 8px is a good minimum for standard screens).

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may display fewer axis ticks/labels than theoretically possible.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Automatically generating gridlines based on data intervals (e.g., every 10 units) without checking the physical rendering height.
*   **Why it fails:** On small charts (e.g., 40px tall), this math results in lines every 4 pixels, which destroys legibility [@heer_crowdsourcing_2010].

## How to Check <!-- role: check -->
*   **Visual Sign:** The background looks like a solid or vibrating texture rather than distinct lines.
*   **The Test:** Divide the chart pixel height by the number of grid intervals. If the result is < 8, the grid is too dense.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Reduce the number of ticks/gridlines.
*   **Best Fix:** Implement adaptive tick generation that checks the available pixel height and enforces a minimum spacing constraint before drawing lines.
