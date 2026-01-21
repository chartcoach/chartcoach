---
id: use-small-multiples-to-avoid-spaghetti-lines
title: Use Small Multiples When Many Lines Overlap
bibliography: references.bib
description: Split a multi-line time series into small multiples to avoid unreadable
  spaghetti charts.
labels:
- chart:small-multiples
- task:compare
- visual:position
- impact:clarity
- data:temporal
- audience:mainstream
- complexity:intermediate
- source:datawrapper
---

## The Rule <!-- role: advice -->

When a multi-line time series becomes cluttered, split it into small multiples so each category gets its own panel.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Separation-by-layout reduces occlusion and helps the eye track one series at a time while still enabling comparison across panels.
- **The Evidence:** The post recommends a “multiple lines” chart with each line in its own panel when lots of categories overlap, describing it as small multiples [@muth_chart_types_guide_2025].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Comparing many categories’ trends over time without losing track of lines.
- **Data Type:** High-category time series where lines overlap heavily.
- **Audience:** Mainstream/general readers [@muth_chart_types_guide_2025].

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** You must emphasize direct interactions or crossings between categories in one shared frame.
- **Reason:** Small multiples separate lines into different panels, making direct intersections less salient (the post positions them as a fix for overlap, not for emphasizing crossings) [@muth_chart_types_guide_2025].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Uses more space than one combined chart.
- **The Risk:** Readers may compare panels less precisely if scales or layouts aren’t consistent (small multiples require careful standardization) [@muth_chart_types_guide_2025].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Keeping one crowded chart and relying on many colors/legend entries to compensate.
- **Why it fails:** Color and legends don’t solve occlusion; the lines are still hard to trace [@muth_chart_types_guide_2025].

## How to Check <!-- role: check -->

- **Visual Sign:** Lines overlap so much that individual series can’t be followed.
- **The Test:** Try to trace three randomly chosen categories end-to-end; if you repeatedly lose the line, you need separation (small multiples) [@muth_chart_types_guide_2025].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Split the chart into a grid of panels (one line per panel).
- **Best Fix:** Use small multiples with a consistent time axis and scale across panels to preserve comparability [@muth_chart_types_guide_2025].
