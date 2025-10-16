---
id: use-glyphs-for-arrival-time-lookup
title: "Use a map with temporal glyphs to find when a phenomenon reaches a specific location"

tags:
  - impact:performance
  - chart:map
  - chart:map.glyphs
  - data:spatiotemporal
  - task:lookup
  - medium:interactive
  - medium:static

evidence:
  strength: medium
  summary: "For the task of looking up the arrival time of a phenomenon at a single geographic location, a 2020 study found that maps with temporal glyphs were significantly faster than animated maps or small-multiple maps."

sources:
  - type: research
    ref: "Peña-Araya, Bezerianos, & Pietriga, 2020"
    url: https://doi.org/10.1145/3313831.3376350
    note: "In the 'Arrival' task, the glyph map visualization was fastest, outperforming small-multiples and animation."
    role: primary

---

## Guidance

To support quick lookups of an event's arrival time at a *specific* geographic region, use a map where each region contains a small glyph that encodes the entire time series for that location (e.g., a mini-calendar or a grid of colored cells).

## Why

This design co-locates all temporal data for a single spatial entity. Finding the arrival time at a target location becomes a highly efficient, two-step visual search task: 1) find the target region on the map, and 2) scan its local glyph for the first sign of the event (e.g., the first colored cell). This is much faster than waiting for an animation to reach the right moment or scanning across many different maps in a small-multiple layout.

### Core Principle

Minimize the visual travel distance for comparisons. By placing all temporal information for a location *at that location*, the task is transformed into a simple, local lookup.

## When it applies

- When the primary user task is to look up a specific temporal value (like a start time, end time, or peak time) for a specific, known location.
- When you have a moderate number of time steps that can be legibly encoded within a small glyph.

## Exceptions

- **When the task requires comparing patterns *across* different regions.** The advantage of a glyph map disappears when the user has to compare the glyph of one region to the glyph of another, spatially distant region.
- **When the task is to understand the overall spatial pattern at a single point in time.** In this case, a simple choropleth map (like one frame of an animation or one view in a small-multiple set) is far more effective.
- **When the task is to judge and compare magnitudes.** The small size of the cells or marks within a glyph makes it perceptually difficult to compare values precisely (e.g., to find the absolute highest peak across all regions).

## Trade-offs

- **Clutter:** Maps with glyphs can become visually cluttered, especially if geographic regions are small and densely packed. The glyphs themselves can obscure the underlying map geography.
- **Poor for Comparison:** This design optimizes for *lookup at a location*, but it is poor for *comparison across locations* or *overview of a time slice*.
- **Scalability:** The legibility of the glyphs degrades as the number of time steps increases, as each cell within the glyph must become smaller.

## Signs of Trouble

- **Zig-Zagging Eyes:** A user's gaze has to jump back and forth between two different glyphs on opposite sides of the map to try and compare them.
- **"Which is Darker?":** Users struggle to compare the color of a tiny cell in one glyph to another tiny cell in a different glyph.
- **Can't See the Forest for the Trees:** The user can see the detailed history of every single region but has no clear picture of the overall spatial pattern at any given moment.

## How to Improve

- **Quick approach: Use Interaction to Help.** Add a hover interaction that enlarges a glyph or shows a tooltip with the detailed time-series chart for that region. Also, allow users to click a time-step in one glyph to highlight the same time-step in all other glyphs.
- **Moderate approach: Offer a "Small-Multiple" View of Glyphs.** Instead of placing glyphs on a map, arrange them in a grid, which can make it easier to compare them directly (though it sacrifices geographic context).
- **Comprehensive approach: Use as Part of a Coordinated View.** Pair the glyph map with a choropleth map. Clicking a region on the glyph map could show its detailed history, while clicking a time on a timeline could update the choropleth map to show the spatial pattern at that moment.