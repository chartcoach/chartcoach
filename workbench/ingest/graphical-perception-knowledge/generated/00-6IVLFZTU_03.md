---
id: use-small-multiples-for-spatiotemporal-peaks
title: "Use small-multiple maps to find peak values in spatiotemporal data"
tags:
  - impact:perceptual
  - impact:performance
  - chart:map
  - chart:map.small-multiples
  - task:find-extremum
  - data:spatiotemporal
audience:
  - audience:expert
medium:
  - medium:interactive
evidence:
  strength: medium
  summary: "In a controlled experiment comparing spatiotemporal visualizations (Peña-Araya et al., 2020; n=18), small-multiple maps were the fastest and most accurate technique for finding the region and time of a peak value. They outperformed animated maps and glyph maps for this specific task, which involves both a global search and local comparisons."
sources:
  - type: research
    ref: Peña-Araya et al., 2020
    url: http://dx.doi.org/10.1145/3313831.3376350
    note: "The study (n=18) found that for the 'Peaks' task, small multiples were significantly faster than both animation (by 12.1s) and glyph maps. Animation was the slowest method."
    role: primary
---
## Guidance
When the task is to identify the maximum value (the "peak") across both space and time in a geographic dataset, a small-multiples display of maps is the most effective visualization strategy.

## Why
The "find peak" task requires two steps: a broad search across the entire time series to locate candidate peaks, followed by a precise comparison of those candidates. Small-multiple maps support both steps well. They provide a complete, static overview, allowing for a quick global scan. They also enable side-by-side comparison of different time steps without relying on memory, which is a major limitation of animated maps.

### Core Principle
Provide a static overview for global search tasks. Forcing users to rely on memory or sequential playback for comparison increases cognitive load and error rates.

## When it applies
- You are visualizing data that changes over time across geographic regions (e.g., disease outbreaks, election result shifts, climate data).
- The user's primary goal is to find the "hottest" spot and when it occurred.
- The number of time steps is moderate (e.g., up to ~40), allowing each small map to remain legible.

## Exceptions
- When the number of time steps is very large, the individual maps in a small-multiples layout may become too small to read. In such cases, an interactive animated map might be necessary, despite its drawbacks.
- If the task is simply to find the peak in a single, pre-specified region, a glyph map or a simple line chart for that region would be more efficient.

## Trade-offs
- **Screen Real Estate:** Small multiples consume a large amount of screen space. This can be a challenge on smaller displays.
- **Detail:** The individual maps are necessarily small, which can obscure fine-grained geographic details within each time-step.

## Signs of Trouble
- **Scrubbing Back and Forth:** With an animated map, users are repeatedly scrubbing the timeline slider back and forth, trying to remember and compare the intensity of colors from different moments in time.
- **Tiny, Illegible Glyphs:** With a glyph map, the individual time-cells within each glyph are too small to accurately compare colors.
- **Lost Context:** The user can find a peak in one time-step but has difficulty comparing it to peaks in other, non-adjacent time-steps.

## How to Improve
- **Quick Fix: Add Highlighting to an Animated Map.** If you must use animation, provide an interactive feature that lets users "bookmark" or highlight candidate peaks so they can easily jump between them for comparison.
- **Moderate Redesign: Switch to Small Multiples.** Change the visualization from an animation or glyph map to a small-multiples layout. Ensure the maps are laid out in a logical order (e.g., left-to-right, top-to-bottom).
- **Comprehensive Redesign: Implement Coordinated Brushing.** In your small-multiples view, implement brushing and linking. When a user hovers over a region in one map, that same region should be highlighted in all other maps, facilitating comparison of a single region's journey through time.