---
id: use-small-multiples-for-spatiotemporal-correlation
title: Juxtapose Maps to Show Spatio-Temporal Correlation
bibliography: references.bib
description: Use small multiples rather than single maps with embedded charts when
  users need to identify correlations over space and time.
labels:
- chart:small-multiples
- chart:map
- task:correlate
- visual:layout
- impact:efficiency
- data:spatio-temporal
- audience:analyst
---

## The Rule <!-- role: advice -->
Visualize spatio-temporal correlations by juxtaposing multiple map views (small multiples) for each time step, rather than embedding complex time-series glyphs onto a single map.

## The Logic <!-- role: reason -->
When users need to identify how two variables correlate over both space and time, separating time steps into distinct, juxtaposed maps significantly improves performance.
*   **The Evidence:** In a review of graphical perception knowledge [@zeng_review_2023], experimental results from Peña-Araya et al. [@pena-araya_comparison_2020] demonstrated that small multiple designs (using either proportional symbols or cartograms) significantly outperformed single maps containing embedded bar charts (E-3) for correlation tasks.
*   **The Principle:** **Visual Search Efficiency.** Small multiples allow the eye to scan for spatial patterns across a sequence (space-centric comparison), whereas a single map with embedded bar charts forces the user to decode complex glyphs at every individual location (time-centric decoding) to build a mental model of the correlation.

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying correlation between variables that change over time and geography.
*   **Data Type:** Multivariate spatio-temporal data (e.g., two quantitative variables across multiple regions and years).
*   **Audience:** Analysts or general users looking for broad trends and relationships rather than precise point values.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Analyzing a specific location in isolation.
*   **Reason:** If the task is purely to read the value evolution of a *single* specific region without comparing it to neighbors, a glyph (like a bar chart) located on that region might be faster than scanning across multiple map frames [@pena-araya_comparison_2020].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Screen real estate. Small multiples require enough space to display multiple maps legibly.
*   **The Risk:** If the maps are too small, individual geographic features become illegible, hindering the spatial component of the analysis.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Placing a mini-bar chart or line chart on top of every state or country on a single map.
*   **Why it fails:** This creates visual clutter and high cognitive load, as users must perform a "retrieval" task at every location before they can compare them [@zeng_review_2023].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does your map look like a "porcupine" of bars or lines sticking out of regions?
*   **The Test:** Ask a user to identify if the variables generally rise or fall together across the northern region. If they have to read every individual chart to answer, the design has failed.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Remove the embedded charts and use color encoding (choropleth) with a time slider (though animation has its own drawbacks).
*   **Best Fix:** Split the time steps into a grid of static small multiple maps, ensuring the visual encoding (scale and size) is consistent across all frames.
