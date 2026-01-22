---
id: set-default-map-extent-by-filtering-to-locations-most-related-to-the-primary-location
title: Set default map extent by filtering to locations most related to the primary
  location
bibliography: references.bib
description: "Choose an initial zoom region that contains only locations strongly\
  \ related to the story\u2019s primary place."
labels:
- chart:map
- task:focus
- visual:position
- impact:relevance
- data:geospatial
- audience:novice
- pipeline:extent
---

## Filter to related locations before computing map extent <!-- role: advice -->

Compute relatedness between each mentioned location and the primary location, keep only high-relatedness locations, and set the map extent to contain that filtered set.

## Why relatedness-filtered extents match story geography <!-- role: reason -->

Articles often mention peripheral places that are not central to the geographic context readers need. Filtering to locations most related to the primary location reduces clutter and yields a default zoom region that better matches the implied geographic scope.

**Mechanism:** Removing weakly connected locations prevents the bounding extent from expanding to include irrelevant distant places.

**Evidence:** The pipeline identifies a primary location from seed locations, computes a combined similarity score using spatial distance, hierarchy distance, and location co-occurrence (PMI), filters locations using a similarity threshold, and sets extent to contain the retained locations and the primary location [@gaoNewsViewsAutomatedPipeline2014].

**Notes:** The method is intended to be extensible; the key idea is combining multiple distance/relatedness signals.

## When relatedness-filtered extent applies <!-- role: context -->

- **User Goal:** Start with a map view that centers on the story’s geographic scope.
- **Task:** Focus attention on the most relevant region without manual navigation.
- **Data:** Multiple extracted locations of varying relevance to the main place.
- **Chart Setting:** Interactive map displayed next to an article.
- **Audience:** Readers who may be unfamiliar with mentioned places.
- **Success Criterion:** Default view includes key places and excludes tangential ones.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The article is explicitly about dispersed geography (e.g., many unrelated locations). **Why:** Filtering to “related” locations can erase the intended breadth of coverage.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Some contextual but distant locations may be excluded from the default view. **Risk:** Poor similarity thresholds can over-zoom or under-zoom. **Mitigation:** Keep excluded locations accessible via interaction (search/list) even if not in the default extent.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Setting extent to the bounding box of all extracted locations. **Why it fails:** A single distant mention can force an overly zoomed-out view that hides meaningful local variation.

## Quick tests <!-- role: check -->

**Failure Sign:** The map opens at an overly zoomed-out level where regional patterns are unreadable. **Quick Check:** Compare the extent with and without filtering and see whether a single far location dominates the bounding box. **Stronger Test:** User-test whether readers can find the primary location and interpret nearby variation without zooming.

## What to do instead <!-- role: fix -->

- Increase the required relatedness threshold when extents are consistently too broad.
- Weight hierarchy distance more when the story is locally framed (e.g., county/city scale).
- Fall back to a reference map zoomed to a single primary location when relatedness is too ambiguous.
