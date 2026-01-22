---
id: connected-scatterplot-avoid-high-complexity-shapes-in-static-presentation
title: Avoid using connected scatterplots with extremely complex paths in static presentation
bibliography: references.bib
description: Reserve connected scatterplots for low-complexity paths that can be read
  and narrated without overload.
labels:
- chart:scatter
- task:understand
- visual:complexity
- impact:clarity
- data:temporal
- audience:novice
- custom:connected-scatterplot
---

## Use connected scatterplots only when the resulting path is low-complexity for the intended audience <!-- role: advice -->

If the connected path creates many crossings, loops, or visually dense segments, choose a different representation for static communication. Prefer connected scatterplots when the relationship produces a small number of salient features that can be annotated.

## Complex connected paths become hard to read and can trigger confusion <!-- role: reason -->

A connected scatterplot encodes time as a continuous path whose shape carries meaning, but this same feature can produce visual complexity that overwhelms interpretation. When the path has salient but hard-to-parse features (such as loops), viewers may report uncertainty about how to read them.

**Mechanism:** Lower visual complexity reduces the need to track and disambiguate path segments and their temporal order, supporting accurate narrative comprehension.

**Evidence:** Extremely complex shapes were identified as a limitation for connected scatterplots in presentation, and viewers reported confusion about “loop-the-loop” features during qualitative interpretation tasks [@harozConnectedScatterplotPresenting2016].

**Notes:** Loops can be engaging and meaningful, but they can also be a focal point of misunderstanding for naive viewers.

## Situations where complexity control is critical <!-- role: context -->

- **User Goal:** Understand a story about how two variables relate over time.
- **Task:** Identify phases, turning points, or time shifts.
- **Data:** Paired time series that generate many loops, self-crossings, or dense point clusters.
- **Chart Setting:** Static print/web images, especially those viewed quickly or as thumbnails.
- **Audience:** General readers unfamiliar with connected scatterplots.
- **Success Criterion:** Viewers can explain the main phases without expressing confusion about how to read the path.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The analysis goal is specifically to explore complex trajectory structure (rather than to communicate a simple message) and the audience is trained for that task. **Why:** The added complexity is part of the analytic value.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose the ability to show time-shift patterns compactly in one view. **Risk:** Switching away can reduce novelty and engagement. **Mitigation:** Preserve narrative by using annotations or by presenting multiple simpler views.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Publishing a connected scatterplot because the shape looks interesting, even if it is hard to explain. **Why it fails:** Viewers can fixate on confusing features like loops and fail to extract the intended message [@harozConnectedScatterplotPresenting2016].
- **Mistake:** Treating self-crossings as inherently meaningful without supporting cues. **Why it fails:** While crossings have a defined meaning in connected scatterplots, they still add visual and cognitive load for naive readers [@harozConnectedScatterplotPresenting2016].

## Quick tests for excessive complexity <!-- role: check -->

**Failure Sign:** Readers say they “don’t know what’s going on” in parts of the path, especially around loops and crossings. **Quick Check:** Count the number of loops/crossings and estimate whether a short caption could explain the key ones. **Stronger Test:** Ask naive viewers to summarize the chart in one sentence; flag high variance or uncertainty.

## What to do instead <!-- role: fix -->

- Switch to a dual-axis line chart if the primary story is about each series over time.
- Split the timeline into separate connected scatterplots for distinct phases if the full history is too complex.
- Use targeted annotations that explain a small number of salient features and de-emphasize the rest.
