---
id: prefer-small-multiples-for-peak-finding
title: "Prefer small-multiple maps for identifying peak values in spatiotemporal data"

tags:
  - impact:performance
  - impact:perceptual
  - impact:cognitive
  - chart:map
  - chart:map.small-multiples
  - data:spatiotemporal
  - task:compare
  - task:rank
  - task:find-extremum
  - medium:interactive
  - medium:static

evidence:
  strength: medium
  summary: "A 2020 study showed that small-multiple maps were both faster and more accurate than animated maps or maps with glyphs for the task of identifying the time and place of a peak value in a geographical propagation."

sources:
  - type: research
    ref: "Peña-Araya, Bezerianos, & Pietriga, 2020"
    url: https://doi.org/10.1145/3313831.3376350
    note: "For the 'Peaks' task, small-multiples were fastest and had lower error rates than the other two conditions."
    role: primary

---

## Guidance

When the task is to find the maximum value (the "peak") of a phenomenon across both space and time, small-multiple maps are the most effective visualization strategy.

## Why

Finding a peak is a two-stage process: a broad, global search across the entire dataset to identify candidate moments, followed by focused, local comparisons to confirm the true maximum. Small-multiple maps support this process perfectly. They provide a complete static overview, allowing for a rapid visual scan తిన identify the darkest-colored regions across all time frames. Once candidates are spotted, they can be easily and accurately compared because they are juxtaposed in space.

### Core Principle

Effective visualizations support the structure of the task. Peak-finding requires both overview (global search) and detail (local comparison), and small-multiples provide both simultaneously.

## When it applies

- When a key analytical task is to find an extremum (minimum or maximum) in spatiotemporal data.
- When you need to compare values across multiple, non-consecutive points in time.
- When both speed and accuracy are important for the task.

## Exceptions

- If the number of time steps is so large that the individual maps become too small to discern subtle differences in color or value, the effectiveness of this approach will decrease. In such cases, interactive filtering or aggregation may be needed first.
- If the peak is so obvious that it can be easily spotted in an animation, the engagement of animation might be preferred for presentation, but it will still likely be slower.

## Trade-offs

- **Screen Real Estate:** This is the most space-intensive of the common techniques.
- **Engagement:** While effective, it may be perceived as less engaging or dynamic than an animated map, which could be a factor when presenting to a general audience.
- **Detail:** The size of each individual map is necessarily smaller than a full-screen animated map, which can reduce the visibility of small geographic regions.

## Signs of Trouble

- **Animation Overload:** You are trying to find a peak by watching an animation, forcing you to hold candidate values in your working memory and hope a larger one doesn't appear later.
- **Glyph Squinting:** You are trying to find the darkest cell by scanning across dozens of tiny, separate glyphs, making comparisons difficult and unreliable.
- **"Did I Miss It?":** With animation, there is a constant fear that the peak moment flashed by too quickly to notice or register.

## How to Improve

- **Quick approach: Implement Brushing.** If using small multiples, ensure that hovering a region in one map highlights it in all maps. This helps you track a single region's values over time to see if it ever peaks.
- **Moderate approach: Add a Summary Visualization.** Accompany the small multiples with a simple line chart that shows the global peak value over time. This can help the user quickly narrow down which time frames to inspect more closely in the maps.
- **Comprehensive approach: Create a "Peak-Finding" Mode.** Design an interactive mode that automatically highlights the top N candidate regions across all time-steps, drawing the user's attention తిన the most likely areas and reducing the visual search workload.