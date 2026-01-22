---
id: use-entity-linking-to-assign-geographic-footprints-to-mentioned-entities
title: Use entity linking to attach coordinates to mentioned entities with geographic
  footprints
bibliography: references.bib
description: Resolve place mentions to knowledge-base entities so each extracted location
  can be mapped to coordinates.
labels:
- chart:map
- task:identify
- visual:position
- impact:robustness
- data:text
- audience:novice
- pipeline:entity-linking
---

## Link extracted entities to a geographic footprint <!-- role: advice -->

Use an entity-linking step that maps detected place/entity mentions in the article text to knowledge-base entities that provide coordinates.

## Why entity linking stabilizes location tagging for maps <!-- role: reason -->

News text contains ambiguous names (e.g., multiple cities with the same name) and non-place entities that can be mistaken for places. Linking mentions to a structured entity (such as a Wikipedia-backed entry) provides a consistent identifier and coordinates for mapping.

**Mechanism:** Entity linking disambiguates surface strings into canonical entities and enables a reliable coordinate lookup, which supports downstream extent setting and annotation placement.

**Evidence:** The pipeline uses a Wikifier system to identify entities and link them to their Wikipedia pages, then uses recorded geographic coordinates as the entity’s geographic footprint [@gaoNewsViewsAutomatedPipeline2014].

**Notes:** The guideline concerns turning text mentions into map-ready coordinates, not choosing what data to visualize.

## When entity-linking applies <!-- role: context -->

- **User Goal:** See places discussed in the story on a map without manual geocoding.
- **Task:** Convert place mentions to coordinates for map display.
- **Data:** Unstructured article text mentioning U.S. states, counties, cities, regions, or geolocated organizations.
- **Chart Setting:** Automated map generation with georeferenced marks.
- **Audience:** Readers who expect place names in the article to be findable on the map.
- **Success Criterion:** High precision in mapping mentions to the correct geographic location.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The visualization does not require precise geographic placement (e.g., only needs country-level grouping). **Why:** Full entity-linking overhead may be unnecessary for coarse aggregation.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Additional computation and dependency on external knowledge-base coverage. **Risk:** Entity-linking errors can propagate into wrong extents and misleading annotations. **Mitigation:** Apply post-filters for obvious misclassifications (e.g., person vs place).

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using raw string matching to a gazetteer without disambiguation. **Why it fails:** Ambiguous names can map to incorrect coordinates, reducing trust in the map.

## Quick tests <!-- role: check -->

**Failure Sign:** The map highlights a plausible but wrong location for an article mention (same-name confusion). **Quick Check:** Sample ambiguous place names and verify linked coordinates match the article’s intended region. **Stronger Test:** Measure precision/recall of tagged locations against human coding on a random article set.

## What to do instead <!-- role: fix -->

- Add a disambiguation stage that outputs multiple candidates and select using context.
- Combine two taggers and filter conflicts where one labels an entity as a person and the other as a location.
- Default to a simple reference map if confident linking cannot be achieved.
