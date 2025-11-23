---
id: use-horizon-graphs-density
title: Use Horizon Graphs for High Data Density
bibliography: references.bib
description: Layer and mirror area charts to increase data density without losing
  resolution.
labels:
- chart:horizon
- chart:area
- visual:color
- impact:efficiency
- data:temporal
---

## The Rule <!-- role: advice -->
To compare many time series in a limited space, use horizon graphs. Divide the graph into bands, layer them, and use color intensity to represent magnitude, mirroring negative values into the same region.

## The Logic <!-- role: reason -->
Horizon graphs preserve data resolution while significantly reducing the vertical space required.
*   **The Principle:** Layering and Mirroring
*   **The Evidence:** A horizon graph doubles data density by mirroring negative values and doubles it again by dividing the graph into layered bands. This preserves resolution using only a quarter of the space of a standard area chart. Research shows they are more effective than standard plots when chart sizes are small [@heer_tour_2010].

## Where to Apply <!-- role: context -->
*   **User Goal:** scanning a massive dashboard of time-series data (e.g., stock market tickers).
*   **Data Type:** High-volume time-series data.
*   **Audience:** Expert users (horizon graphs require a learning curve).

## When to Break It <!-- role: exceptions -->
*   **Scenario:** General public or novice audiences.
*   **Reason:** The technique of reading layered color bands is "exotic" and takes time to learn [@heer_tour_2010].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Immediate intuitive understanding is sacrificed for data density.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Shrinking standard line charts until they are flat.
*   **Why it fails:** Flattening a standard chart reduces the resolution of the y-axis, making small fluctuations invisible.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using nested color bands (e.g., light blue to dark blue) to represent increasing height within a compact strip?

## How to Fix <!-- role: fix -->
*   **Best Fix:** Implement the horizon technique: Mirror negatives (colored red) and positives (colored blue), then slice the peaks and layer them to fill the available vertical space [@heer_tour_2010].
