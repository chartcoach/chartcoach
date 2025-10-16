---
id: use-glyph-maps-for-arrival-time
title: "Use glyph maps for looking up arrival times in spatiotemporal data"
tags:
  - impact:performance
  - chart:map
  - chart:map.glyphs
  - task:lookup
  - data:spatiotemporal
audience:
  - audience:expert
medium:
  - medium:interactive
evidence:
  strength: medium
  summary: "An experiment by Peña-Araya et al. (2020, n=18) found that a map with temporal glyphs was the most efficient visualization for looking up the arrival time of a phenomenon in a specific geographic region. This technique was significantly faster (by 1.3s to 2.9s) than small-multiple maps and animated maps for this targeted lookup task."
sources:
  - type: research
    ref: Peña-Araya et al., 2020
    url: http://dx.doi.org/10.1145/3313831.3376350
    note: "The study (n=18) showed that for the 'Arrival' task, glyph maps were the fastest method (9.08s), compared to small multiples (10.43s) and animation (11.97s), with no significant difference in error rates."
    role: primary
---
## Guidance
When the user's task is to find out *when* a phenomenon first appeared in a specific, known geographic region, use a map where each region contains a small glyph that encodes its entire time series.

## Why
This task is a targeted lookup: the user knows *where* to look and needs to find the *when*. A glyph map organizes the data by location, placing all temporal information for a single region into one compact, localized glyph. This allows the user to focus their attention on a single glyph and scan its cells to find the first occurrence, without needing to scan across multiple-maps or wait for an animation to play.

### Core Principle
Organize the data to match the structure of the user's question. For a "what happened at this location?" query, a location-centric view (like a glyph map) is more efficient than a time-centric view (like animation or small multiples).

## When it applies
- The primary task is a lookup for a specific location (e.g., "When did the first case appear in County X?").
- The user is familiar with the geography and can easily locate the region of interest.
- The number of time steps is small enough to be legibly represented within a single glyph.

## Exceptions
- When the task is to compare arrival times *between* multiple different regions. This would require the user to visually scan and link cells across different glyphs, which is a difficult task.
- When the user does not know the location they are looking for and must first search the map.
- When the number of time steps is very large, making the cells within each glyph too small to be perceptually distinct.

## Trade-offs
- **Lookup vs. Comparison:** Glyph maps excel at lookup within a location but are poor for comparison between locations or for seeing the overall spatial pattern at a single point in time.
- **Detail vs. Overview:** Glyphs provide a temporal summary at the cost of obscuring the underlying map geography.

## Signs of Trouble
- **"Ping-Pong" Eyes:** The user's eyes are darting back and forth between glyphs, trying to compare the timing of events in different locations.
- **Illegible Glyphs:** The glyphs are too small or the time cells within them are too tiny to be clearly seen.
- **Lost Spatial Patterns:** It's impossible to get a sense of what the entire map looked like at a single moment in time.

## How to Improve
- **Quick Fix: Add Highlighting.** Implement interactivity so that hovering over a time-cell in one glyph highlights the same time-cell in all other glyphs. This can aid in comparison tasks.
- **Moderate Redesign: Link to a Line Chart.** Allow users to click on a region/glyph to open a larger, more detailed line chart showing the time series for just that region.
- **Comprehensive Redesign: Provide Coordinated Views.** Display the glyph map alongside a small-multiples view or an animated map. Clicking a region in one view could highlight it in the others, providing the benefits of each visualization type.