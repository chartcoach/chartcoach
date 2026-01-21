---
id: use-entity-linking-to-anchor-places-to-coordinates
title: Link Mentioned Places to Canonical Geo-Entities
bibliography: references.bib
description: Resolve place mentions to canonical entities with coordinates before
  generating reference or thematic maps.
labels:
- chart:map
- task:disambiguate
- visual:position
- impact:accuracy
- data:text
- audience:general
- domain:news
---

## The Rule <!-- role: advice -->

Disambiguate and link place names in the article to canonical geo-entities that have recorded coordinates, and use those coordinates as map anchors.

## The Logic <!-- role: reason -->

Maps require a geographic footprint; entity linking turns ambiguous text mentions into stable identifiers with coordinates, enabling consistent extent-setting and annotation placement.

- **The Principle:** Canonical grounding of toponyms for geovisualization
- **The Evidence:** [@gaoNewsViewsAutomatedPipeline2014]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand where the story happens and how places relate spatially
- **Data Type:** Articles with toponyms (cities, counties, states, regions, organizations with locations)
- **Audience:** General news readers

## When to Break It <!-- role: exceptions -->

- **Scenario:** Stories with intentionally vague geography or non-geographic “locations” (e.g., metaphorical places)
- **Reason:** Forcing coordinate grounding can introduce misleading specificity [@gaoNewsViewsAutomatedPipeline2014]

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional processing complexity for disambiguation
- **The Risk:** Wrong entity resolution for ambiguous names leads to incorrect map anchors [@gaoNewsViewsAutomatedPipeline2014]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating every capitalized phrase as a place and geocoding it
- **Why it fails:** It increases false positives and can anchor the map to irrelevant or incorrect entities [@gaoNewsViewsAutomatedPipeline2014]

## How to Check <!-- role: check -->

- **Visual Sign:** Map zooms to an implausible region (e.g., wrong state/country) for an otherwise clear story
- **The Test:** Spot-check ambiguous place names and confirm linked coordinates match the article’s context [@gaoNewsViewsAutomatedPipeline2014]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a disambiguation filter using a second tagger to remove mismatched entity types (e.g., filter entities flagged as persons)
- **Best Fix:** Maintain a geo-entity mapping table (IDs across sources) so links resolve consistently across datasets and articles [@gaoNewsViewsAutomatedPipeline2014]
