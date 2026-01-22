---
id: use-line-charts-for-continuous-time-trends
title: Use a line chart to show continuous developments over time
bibliography: references.bib
description: Use line charts as the default for showing how a value changes over months
  or years.
labels:
- chart:line
- task:trend
- visual:position
- impact:clarity
- data:temporal
- audience:mainstream
- complexity:foundational
---

## Use line charts for continuous time series <!-- role: advice -->

Use a line chart when you need to show how one or more values change across many time points. Prefer it as the default for monthly or yearly developments.

## Why line charts fit time-change judgments <!-- role: reason -->

Lines encode time on a continuous axis and make direction and slope visually salient, which aligns with how readers scan for increases, decreases, and turning points.

**Mechanism:** Connecting points into a line emphasizes continuity and supports quick detection of overall trend and local changes.

**Evidence:** For mainstream audiences, the line chart is presented as an intuitive and usually solid choice for showing how numbers change over time [@muth_chart_types_guide_2025].

**Notes:** This guideline addresses chart-type fit, not how to label, scale, or annotate a time axis.

## Situations where a line chart applies <!-- role: context -->

- **User Goal:** Communicate how something evolved over months/years.
- **Task:** Identify trend direction, compare trajectories, notice peaks/dips.
- **Data:** Temporal data with many ordered time points per series.
- **Chart Setting:** Editorial, reporting, monitoring, and explanatory contexts.
- **Audience:** General readers accustomed to common chart forms.
- **Success Criterion:** Readers can describe the trajectory correctly (up/down/flat, accelerations, notable changes).

## When not to use a line chart <!-- role: exceptions -->

**Break it when:** You only have a few time points and want discrete comparisons rather than a continuous story. **Why:** A column chart can be a better fit for a small number of time points [@muth_chart_types_guide_2025].

## Tradeoffs of line charts <!-- role: costs -->

**Sacrifice:** With many categories, multiple lines can become visually cluttered. **Risk:** Overlapping lines can hide patterns and confuse comparisons. **Mitigation:** Treat multi-series density as a constraint that may require an alternate layout.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Plotting too many categories as overlapping lines in one panel. **Why it fails:** The chart turns into a “spaghetti” of crossings that is hard to follow [@muth_chart_types_guide_2025].

## Quick tests <!-- role: check -->

**Failure Sign:** You cannot trace a single category from start to end without losing it. **Quick Check:** Count how many lines overlap heavily; if you frequently need a legend lookup, it’s likely too dense. **Stronger Test:** Ask a reader to point to the highest category at a given date; if they hesitate, the chart is too cluttered.

## What to do instead <!-- role: fix -->

- Use small multiples (multiple-line panels) so each line has its own space.
- Use a slope chart if only the first and last time points matter.
- Use an arrow plot when you need a more compact summary of change across many categories.
- Reduce the number of series shown at once by focusing on key categories.
