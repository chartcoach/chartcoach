---
id: use-timelines-to-clarify-temporal-sequences
title: Use Timelines or Ordered Sequences for Time-Based Data
bibliography: references.bib
description: Use familiar timelines or ordered sequences to make time-based patterns
  and events easier to interpret.
labels:
- chart:timeline
- task:sequence
- visual:position
- impact:clarity
- data:temporal
- audience:novice
- complexity:low
---

## The Rule <!-- role: advice -->

Use a timeline or a clearly ordered sequence to show time-related data, and avoid mixing multiple timescales in the same view.

## The Logic <!-- role: reason -->

Familiar temporal layouts reduce interpretation effort by mapping “earlier → later” onto a single, consistent spatial order. When time encodings are cluttered or multiple timescales are combined, viewers struggle to trace progression and connect events to patterns; simple timelines and sequences make temporal relationships easier to follow and compare [@koesten_what_2023].

- **The Principle:** Reduce cognitive load with a single, consistent temporal mapping
- **The Evidence:** [@koesten_what_2023]

## Where to Apply <!-- role: context -->

This advice is designed for displays where the primary meaning comes from order, duration, or change over time.

- **User Goal:** Trace what happened when, spot trends, or understand sequences of events
- **Data Type:** Temporal events, intervals, or time series where the order matters
- **Audience:** Broad or mixed audiences, especially non-experts who rely on familiar conventions

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** You need to compare exact magnitudes across many categories at a single point in time
- **Reason:** A bar chart or table may support more accurate value comparison than a timeline.
- **Scenario:** You must show cyclical time (e.g., day-of-week or seasonal patterns) rather than linear progression
- **Reason:** Circular or calendar-based layouts may communicate cycles more directly than a linear timeline.

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Reduced space for showing additional variables (e.g., multiple metrics, uncertainty, annotations)
- **The Risk:** Oversimplifying time may hide important differences in scale (e.g., irregular sampling, gaps, or varying granularity)

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Combining yearly trends and hourly variation in one chart without clear separation
- **Why it fails:** Viewers lose the ability to track a single temporal logic and misread patterns across incompatible scales [@koesten_what_2023].
- **The Wrong Fix:** Adding more marks, colors, or annotations to “explain” a confusing temporal layout
- **Why it fails:** It increases clutter instead of restoring a clear, consistent sequence [@koesten_what_2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The chart shows multiple time granularities (e.g., hours and years) with no distinct panels, or the time order is hard to follow left-to-right/top-to-bottom.
- **The Test:** Ask a viewer to point to “what happens next” at several points; if they hesitate or disagree, the temporal sequence is not clear (often due to clutter or mixed timescales) [@koesten_what_2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Separate timescales into small multiples (one panel per scale) and enforce one clear temporal direction with consistent spacing and labeling.
- **Best Fix:** Switch to a dedicated timeline/sequence design (single timescale, ordered events/intervals, minimal encodings) and move secondary variables to supporting charts or tooltips.
