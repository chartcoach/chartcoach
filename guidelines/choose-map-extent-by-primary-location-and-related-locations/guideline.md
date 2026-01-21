---
id: choose-map-extent-by-primary-location-and-related-locations
title: Set Map Extent from Primary and Related Locations
bibliography: references.bib
description: Determine a primary location and include only strongly related locations
  to define the default map extent.
labels:
- chart:map
- task:zoom
- visual:position
- impact:context
- data:geospatial
- audience:general
- domain:news
---

## The Rule <!-- role: advice -->

Identify a primary location from early-mentioned seed locations, score other mentioned locations by relatedness to it, filter to high-relatedness locations, and set the map extent to bound that filtered set.

## The Logic <!-- role: reason -->

A good extent focuses attention on where the story is “about” while retaining enough spatial context for comparison; combining spatial, hierarchical, and co-occurrence relationships supports story-relevant framing.

- **The Principle:** Story-driven geographic framing through location relatedness
- **The Evidence:** [@gaoNewsViewsAutomatedPipeline2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand patterns in the region that matters to the story (not necessarily the whole country)
- **Data Type:** Articles with multiple place mentions across scales (city/county/state)
- **Audience:** General news readers

## When to Break It <!-- role: exceptions -->

- **Scenario:** Articles explicitly about national/global distributions (where zooming in would hide the intended pattern)
- **Reason:** Tight extents can contradict the story’s intended scale [@gaoNewsViewsAutomatedPipeline2014]

## The Price <!-- role: costs -->

- **The Sacrifice:** Some peripheral but contextually meaningful locations may be excluded
- **The Risk:** If the primary location is misidentified, the entire extent becomes wrong [@gaoNewsViewsAutomatedPipeline2014]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Setting extent to include every detected location mention
- **Why it fails:** A single far-away mention can force an unhelpful zoom-out that reduces readability and focus [@gaoNewsViewsAutomatedPipeline2014]

## How to Check <!-- role: check -->

- **Visual Sign:** Map is zoomed out so far that patterns become indistinct, or zoomed in so far that key mentioned places are missing
- **The Test:** Verify the extent encloses the primary location plus only the locations that are meaningfully related (by the system’s relatedness score threshold) [@gaoNewsViewsAutomatedPipeline2014]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase filtering by raising the relatedness threshold so distant weakly-related mentions don’t expand the extent
- **Best Fix:** Combine spatial distance, geo-hierarchy distance, and co-occurrence strength (PMI) into a single relatedness score before extent-setting [@gaoNewsViewsAutomatedPipeline2014]
