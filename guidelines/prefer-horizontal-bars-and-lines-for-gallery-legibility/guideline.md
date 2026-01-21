---
id: prefer-horizontal-bars-and-lines-for-gallery-legibility
title: Prefer Horizontal Bars and Lines for Gallery Legibility
bibliography: references.bib
description: In thumbnail galleries, favor orientations that make labels easier to
  read and charts easier to scan.
labels:
- chart:bar
- task:browse
- visual:orientation
- impact:legibility
- data:categorical
- audience:analyst
- system:recommendation
---

## The Rule <!-- role: advice -->

In a chart gallery, prefer horizontal bar charts (when not showing binned quantitative/temporal distributions) and favor horizontal orientations for line/area charts.

## The Logic <!-- role: reason -->

Compass explicitly ranks orientations with gallery reading in mind: horizontal bars are preferred because labels are easier to read, and horizontal line/area charts are favored over vertical ones to support scannability in a gallery layout [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

- **The Principle:** Optimize small-multiple legibility for rapid scanning
- **The Evidence:** [@wongsuphasawatVoyagerExploratoryAnalysis2016a]

## Where to Apply <!-- role: context -->

- **User Goal:** Browse many charts quickly and read labels without zooming
- **Data Type:** Nominal/ordinal categories with labels; time series lines/areas
- **Audience:** Analysts in a recommendation browser

## When to Break It <!-- role: exceptions -->

- **Scenario:** The x-axis is explicitly a binned quantitative or temporal variable (histograms).
- **Reason:** Compass prefers vertical bars/histograms in that specific case [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Some conventional default orientations (e.g., vertical bars) may be less common for users.
- **The Risk:** If users expect a different orientation, they may need refinement controls to transpose.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Always using vertical bars for all categorical comparisons in thumbnails.
- **Why it fails:** Long category labels become hard to read, slowing gallery scanning [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** Truncated or overlapping category labels across many thumbnails.
- **The Test:** Reduce the chart to thumbnail size; if labels become unreadable, switch orientation.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Default to horizontal bars for categorical comparisons.
- **Best Fix:** Provide a transpose-axes refinement control in an expanded view so users can switch orientation when needed [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
