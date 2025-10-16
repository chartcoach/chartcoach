---
id: use-small-multiples-for-propagation
title: "Use small multiples for analyzing spatio-temporal propagation"

impact:
  - perceptual
  - cognitive
  - performance
tags:
  - small-multiples
  - animated-map
  - glyph-map
  - choropleth-map
  - spatio-temporal-analysis
  - propagation
  - comparison

sources:
  - type: research
    ref: Peña-Araya, Bezerianos, & Pietriga, 2020
    url: https://doi.org/10.1145/3313831.3376350
    note: "Compares small multiples, animated maps, and glyph maps for five tasks related to analyzing geographical propagation patterns (e.g., disease spread)."

examples:
  - type: good
    description: "Small-multiple maps are a strong default choice, performing best overall for tasks like finding propagation peaks and assessing overall scope. They provide a good balance of speed and accuracy."
  - type: good
    description: "Animated maps are the fastest technique for determining the direction of propagation, though they can lead to lower accuracy. Users also report high confidence when using them."
  - type: good
    description: "A map with glyphs is the most efficient technique for finding the arrival time of a phenomenon at a specific, known location."
---

## Guidance

For visualizing how a phenomenon spreads across a map over time, start with **small-multiple maps**. This technique generally offers the best overall performance for a variety of analytical tasks.

## Why

Small-multiple maps display the entire time series at once as a grid of snapshots. This allows you to see the big picture and make comparisons across any two points in time without having to remember previous states. This "overview at a glance" reduces cognitive load compared to an animation, which requires you to recall what you just saw, and it's easier to read than the tiny, compact time cells found in a map with glyphs.

## When it applies

- When visualizing how a phenomenon (like a disease, meme, or weather pattern) spreads across geographical regions over a moderate number of time steps (e.g., 20-50).
- When your analysis involves a mix of tasks, such as finding the peak intensity, determining the overall geographic scope, and identifying spatial jumps.
- When creating a static visualization (for a report or presentation) that needs to be comprehensive and self-contained.

## Exceptions

While small multiples are a strong default, other techniques are superior for specific, narrowly-defined tasks:

- **To determine propagation *direction*:** Use an **animated map**. The sequential playback of frames creates a perception of motion that makes the direction of spread easier and faster to see.
- **To find the *arrival time* at one specific location:** Use a **map with glyphs**. This allows a viewer to focus their attention on a single region's glyph and quickly scan its cells to find when the phenomenon first appeared.

## Trade-offs

- **Screen Space:** Small multiples consume a lot of screen space. As you add more time steps, each individual map must shrink, potentially becoming too small to read.
- **Sense of Flow:** Small multiples break a continuous process into discrete snapshots, which can cause you to lose the sense of fluid movement that an animation provides.
- **User Preference vs. Performance:** Viewers often report higher confidence in their judgments when using animated maps, even when their performance (speed and accuracy) is worse. Choosing small multiples for better performance might conflict with your audience's subjective preference for animation.

## Evaluate

- [ ] Viewers have trouble comparing the first and last time steps because they have to rely on memory.
- [ ] It's difficult to get a quick overview of the entire temporal sequence.
- [ ] The primary task is to understand the direction of spread, but the visualization feels like a series of disconnected images rather than a flow.

## Repair

1.  **Enhance with interaction.** If using small multiples, implement "brushing and linking," where hovering over a region in one map highlights that same region across all other maps. If using an animation, provide a slider that allows users to "scrub" back and forth through time.
2.  **Choose the best technique for the primary task.** If the most important question is "Which way is it spreading?", prioritize an animated map. If it's "When did it get to this city?", a glyph map may be best. For all other general exploration, stick with small multiples.
3.  **Allow users to switch views.** If technically feasible, provide controls to let the user toggle between a small-multiple view (for overview) and an animated view (for flow), giving them the best of both worlds.
