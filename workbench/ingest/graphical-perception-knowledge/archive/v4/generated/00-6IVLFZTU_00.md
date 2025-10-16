---
id: use-small-multiples-for-spatiotemporal-peaks
title: "Use small-multiple maps to find peaks in spatiotemporal data"

tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:map
  - chart:map.small-multiples
  - task:find-extremum
  - task:compare
  - task:rank
  - data:spatiotemporal
  - medium:interactive
  - medium:screen

sources:
  - type: research
    ref: Peña-Araya, Bezerianos, & Pietriga, 2020
    url: https://doi.org/10.1145/3313831.3376350
    note: "Experiment found small-multiple maps were fastest and most accurate for finding the peak value in a spatiotemporal dataset, outperforming animated maps and maps with glyphs."

examples:
  - type: good
    description: "Small multiples provide a complete overview, allowing a global search across all time-steps at a glance, followed by a local comparison of candidate peaks without relying on memory."
  - type: bad
    description: "An animated map forces the user to remember the location and intensity of previous peaks to make a comparison, increasing cognitive load and leading to slower, less accurate performance."
  - type: bad
    description: "A map with glyphs has very small time-cells, making it difficult to accurately compare subtle color differences to identify the true peak."
---

## Guidance

To help users find the maximum value (peak) of a phenomenon across both space and time, represent the data using small-multiple maps.

## Why

Small-multiple maps are faster and more accurate for this task because they provide a complete, static overview of the entire dataset. This allows users to perform a global visual search to identify potential peaks and then make direct, local comparisons between them without having to rely on working memory (as in an animation) or decipher low-resolution glyphs.

## When it applies

- When the user's task is to identify the location and time of the maximum intensity of a phenomenon, such as the peak of a disease outbreak or the highest level of social media activity.
- When the analysis requires both a broad overview of the entire time-series and detailed comparison between specific points in time and space.

## Exceptions

- If there are too many time-steps to display on the available screen space, the individual maps in a small-multiples layout may become too small to be legible. In such cases, aggregation or an alternative interactive approach may be needed.

## Trade-offs

- **Screen Space:** Small multiples consume significantly more screen real estate than a single animated map or a map with glyphs.
- **Data Density:** Performance may degrade if the number of time-steps is so large that individual maps become unreadably small.

## Signs of Trouble

- **Endless Scrubbing:** With an animated map, users repeatedly play, pause, and scrub the timeline back and forth, trying to remember where and when they saw the "darkest" region.
- **Squinting at Glyphs:** With a glyph map, users struggle to compare colors in the tiny, low-resolution cells, unable to confidently determine which is the true maximum.

## How to Improve

- **Comprehensive Redesign: Switch to Small Multiples.** If you are currently using an animated map or a map with glyphs for peak-finding tasks, switch to a small-multiples layout. Arrange a grid of static maps, one for each time-step, to provide a complete overview and facilitate direct comparison. This is the most effective approach according to the research.