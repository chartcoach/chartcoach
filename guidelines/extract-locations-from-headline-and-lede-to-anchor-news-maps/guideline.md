---
id: extract-locations-from-headline-and-lede-to-anchor-news-maps
title: Extract locations from the headline and first three sentences to anchor the
  map extent
bibliography: references.bib
description: Use early-article location mentions as seeds to determine the primary
  location and drive map framing.
labels:
- chart:map
- task:locate
- visual:position
- impact:relevance
- data:geospatial
- audience:novice
- pipeline:information-extraction
---

## Seed map framing from headline + lede locations <!-- role: advice -->

Extract place names from the article title and first three sentences and treat them as the initial location set used to frame the visualization.

## Why early-location anchoring improves map fit <!-- role: reason -->

Early article text often contains the core “who/what/where,” so locations found there are more likely to represent the story’s geographic anchor than locations mentioned later. Prioritizing these locations supports choosing a primary location and a default map extent that reflects what the article is mainly about.

**Mechanism:** Reducing the candidate location space to the earliest, most central mentions increases the chance that the chosen geographic focus matches reader expectations for the story’s “main place.”

**Evidence:** The pipeline extracts seed locations from the title and first three sentences, counts their occurrences across the article, and uses the most frequent seed as the primary location for setting extent and related-location selection [@gaoNewsViewsAutomatedPipeline2014].

**Notes:** This rule is about anchoring the geographic frame, not about selecting the thematic variable.

## When early-location anchoring applies <!-- role: context -->

- **User Goal:** Understand the geographic context of a news story with minimal effort.
- **Task:** Identify the main place and see surrounding or related places in context.
- **Data:** News article text containing toponyms and/or geographically anchored entities.
- **Chart Setting:** Automated or semi-automated news visualization shown alongside an article.
- **Audience:** General news readers with uneven geographic familiarity.
- **Success Criterion:** The default map region matches the story’s implied “where” without requiring manual zoom/pan.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The article’s early sentences are intentionally generic (e.g., opening with national framing) while the substantive geographic focus appears later. **Why:** Early extraction may select an overly broad or wrong primary location, leading to an unhelpful map extent.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Sensitivity to later-emerging but important locations. **Risk:** The map extent can be too broad (national) or too narrow (single locale) if early text is misleading. **Mitigation:** Validate the early-location choice against whole-article mention frequency before finalizing extent.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Treating all locations mentioned anywhere in the article as equally central. **Why it fails:** It dilutes the geographic anchor and can cause an extent that includes tangential places, reducing relevance.

## Quick tests <!-- role: check -->

**Failure Sign:** The default map opens on a region that feels unrelated to the article’s main place. **Quick Check:** Verify that the chosen primary location is among the most frequently mentioned places in the full article. **Stronger Test:** Human-rate whether the selected primary location matches the story’s main “where” on a sample set.

## What to do instead <!-- role: fix -->

- Count full-article occurrences of candidate seed locations and choose the most frequent as primary.
- Filter candidate locations by their relatedness to the primary location before setting extent.
- Fall back to a reference/locator map when location signals are weak or dispersed.
