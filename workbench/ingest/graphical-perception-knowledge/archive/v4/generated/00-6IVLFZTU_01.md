---
id: use-map-glyphs-for-spatiotemporal-lookup
title: "Use maps with glyphs for fast arrival time lookups"

tags:
  - impact:performance
  - impact:perceptual
  - chart:map
  - chart:map.glyphs
  - task:lookup
  - data:spatiotemporal
  - medium:interactive
  - medium:screen

sources:
  - type: research
    ref: Peña-Araya, Bezerianos, & Pietriga, 2020
    url: https://doi.org/10.1145/3313831.3376350
    note: "The study found that a map with glyphs was the fastest technique for the 'Arrival' task, which involved finding the time a phenomenon reached a specific, known location."

examples:
  - type: good
    description: "On a map with glyphs, finding the arrival time for a specific region requires only a quick scan within a single, localized glyph, making it very efficient."
  - type: bad
    description: "Using small multiples for this task forces the user to scan across many different maps to find the one where the target region first appears, which is slower."
  - type: bad
    description: "Using an animation for this task is the slowest method, as the user must wait for the animation to play until the target region appears."
---

## Guidance

When the primary task is to find out *when* a phenomenon first appeared at a *specific* geographical location, use a map with glyphs where each glyph visualizes the time series for its location.

## Why

This technique is fastest because it co-locates all temporal data for a single spatial region. The task is transformed from a search across many maps (small multiples) or a waiting game (animation) into a simple, highly efficient visual lookup within a single, designated glyph on the map.

## When it applies

- The task is a targeted lookup: "When did X happen at location Y?"
- The user knows the specific location they are interested in.
- Speed of lookup for this specific task is the highest priority.

## Exceptions

- This technique is not suitable for most other spatiotemporal analysis tasks, such as determining propagation direction, identifying spatial jumps, or finding overall peaks. Its optimization for lookup comes at a high cost to other analytical capabilities.

## Trade-offs

- **Task Specificity:** This method is highly optimized for single-location temporal lookup but performs poorly for tasks requiring comparisons across different regions or across consecutive time steps.
- **Cognitive Load for Other Tasks:** Using this visualization for tasks other than lookup can be cognitively demanding because the temporal information is spatially fragmented across the glyphs.

## Signs of Trouble

- **Poor Global Understanding:** Users can easily find the arrival time at one location but cannot describe the overall pattern, direction, or speed of the propagation across the entire map.
- **Difficulty with Comparisons:** Users struggle to answer questions like "Did the phenomenon spread from east to west?" or "Did it jump over any regions?"

## How to Improve

- **Quick Fix: Add Highlighting.** If using a glyph map, ensure robust interactivity that allows a user to hover over a time-cell in one glyph and see the corresponding time-cell highlighted in all other glyphs to aid comparison.
- **Moderate Redesign: Use a More General-Purpose View.** If analysis involves more than just arrival-time lookup, switch to a small-multiples layout. It offers a better balance for a wider range of spatiotemporal tasks.