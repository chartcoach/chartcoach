---
id: prefer-small-multiples-for-spatiotemporal-analysis
title: "Prefer small-multiple maps for general-purpose spatiotemporal analysis"

tags:
  - impact:perceptual
  - impact:cognitive
  - impact:performance
  - chart:map
  - chart:map.small-multiples
  - task:compare
  - task:trend
  - task:find-extremum
  - data:spatiotemporal
  - medium:screen
  - medium:interactive

sources:
  - type: research
    ref: Peña-Araya, Bezerianos, & Pietriga, 2020
    url: https://doi.org/10.1145/3313831.3376350
    note: "The paper's overall conclusion was that 'small-multiple maps perform best overall,' demonstrating a good balance of speed and accuracy across a range of five different spatiotemporal tasks."

examples:
  - type: good
    description: "A dashboard showing the spread of a flu variant using a grid of small maps, one for each week. This allows analysts to spot peaks, assess direction, and see overall scope in a single, static view."
---

## Guidance

For general-purpose analysis of spatiotemporal data, where users may perform a variety of tasks, prefer a small-multiples layout of maps.

## Why

Small-multiple maps performed the best overall in a comparative study, offering a robust balance of speed and accuracy across diverse tasks like finding peaks, determining direction, and assessing scope. They provide a complete static overview, which avoids the memory burden of animation, while maintaining better resolution and avoiding the cognitive fragmentation of glyph-based maps. This makes them a strong default choice.

## When it applies

- When a single visualization must support multiple analytical tasks (e.g., finding peaks, trends, and anomalies).
- When you are designing a general-purpose exploratory tool and are unsure of the user's specific primary task.
- When analytical rigor and the ability to make direct, static comparisons are more important than the narrative flow of an animation.

## Exceptions

- **Targeted Lookup:** If the *only* task is to find the arrival time at a specific location, a map with glyphs is faster.
- **Presentation:** If the primary goal is to present a narrative to a general audience, an animated map may be more engaging and have higher perceived user confidence, even if it's less analytically powerful.
- **Extreme Data Density:** If the number of time-steps is very large (e.g., 100+), the individual maps in a small-multiples view may become too small to be legible on a standard screen, requiring an alternative design.

## Trade-offs

- **Screen Real Estate:** Small multiples are space-intensive. A large number of time-steps can make individual maps very small.
- **Engagement:** For non-expert audiences, a grid of static maps may feel less engaging or more intimidating than a fluid animation.

## Signs of Trouble

- **Illegible Maps:** The individual maps in the grid are so small that geographical details and color variations are impossible to discern.
- **User Disengagement:** A general audience finds the visualization static and overwhelming, failing to grasp the overall story.

## How to Improve

- **Moderate Approach: Add Interactivity.** Enhance a small-multiples view with brushing and linking. Hovering over a region in one map should highlight the same region in all other maps. This helps users track specific locations over time.
- **Comprehensive Approach: Create a Hybrid View.** Combine the strengths of different views. For example, provide a small-multiples layout as the main analytical view, but also offer an animated version on-demand for getting a quick overview of the dynamics.