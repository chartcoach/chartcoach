---
id: place-labels-next-to-what-they-explain
title: Place Labels Next to What They Explain
bibliography: references.bib
description: Reduce eye-travel by putting explanations directly beside the lines,
  bars, or marks they describe.
labels:
- chart:line
- task:identify
- visual:position
- impact:readability
- data:temporal
- audience:novice
- custom:legendless
- source:muth_readers_time_2017
---

## The Rule <!-- role: advice -->

Put labels and explanations as close as possible to the visual elements they refer to; avoid making readers bounce between marks and a distant legend.

## The Logic <!-- role: reason -->

Long eye-travel (e.g., legend in a corner, lines elsewhere) forces readers to repeatedly search and remember mappings (“Wait, what did red represent?”), increasing effort and time; proximity makes decoding faster and more reliable [@muth_readers_time_2017].

- **The Principle:** Minimize eye-travel for decoding
- **The Evidence:** [@muth_readers_time_2017]

## Where to Apply <!-- role: context -->

- **User Goal:** Rapidly identify what each line/bar/category represents without back-and-forth scanning.
- **Data Type:** Multi-series charts where color/line style encodes categories (especially time series line charts).
- **Audience:** Readers skimming quickly or viewing on small screens, where back-and-forth is costly [@muth_readers_time_2017].

## When to Break It <!-- role: exceptions -->

- **Scenario:** There are too many series/categories to label legibly near the marks.
- **Reason:** On-chart labels may overlap or clutter so much that the mapping becomes less clear than a compact legend [@muth_readers_time_2017].

## The Price <!-- role: costs -->

- **The Sacrifice:** More layout effort; less free space for the data region.
- **The Risk:** Poorly placed labels can collide with marks or each other, creating clutter and reducing readability [@muth_readers_time_2017].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the legend and just enlarging it or moving it slightly.
- **Why it fails:** The reader still has to context-switch between legend and marks; the core eye-travel problem remains [@muth_readers_time_2017].

## How to Check <!-- role: check -->

- **Visual Sign:** You catch yourself repeatedly looking from the legend to the chart to decode a color/line.
- **The Test:** Track your gaze: if you must look away from the data region to identify categories more than once, labels are too far from their elements [@muth_readers_time_2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove the legend and add direct labels on or at the ends of lines/bars using matching colors (as shown in the post’s example) [@muth_readers_time_2017].
- **Best Fix:** Design the chart around in-place labeling: reserve space near marks, use consistent label placement, and color labels to match their corresponding elements [@muth_readers_time_2017].
