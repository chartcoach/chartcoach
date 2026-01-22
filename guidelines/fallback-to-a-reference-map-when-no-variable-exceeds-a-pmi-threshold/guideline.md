---
id: fallback-to-a-reference-map-when-no-variable-exceeds-a-pmi-threshold
title: Fallback to a reference map when no variable exceeds a PMI threshold
bibliography: references.bib
description: Use a locator map when topical variable matching is weak so the visualization
  still supports geographic context.
labels:
- chart:map
- task:locate
- visual:position
- impact:graceful-degradation
- data:geospatial
- audience:novice
- pipeline:fallback
---

## Use a locator map when thematic relevance is too weak <!-- role: advice -->

If no candidate variable achieves a sufficiently high PMI match to the article text, generate a reference (locator) map zoomed to mentioned locations instead of forcing a thematic map.

## Why a reference fallback prevents irrelevant thematic maps <!-- role: reason -->

When the system cannot confidently infer a relevant variable, a thematic map risks showing unrelated data and undermining trust. A reference map still provides value by helping readers place mentioned locations in geographic context.

**Mechanism:** Switching to a lower-commitment visualization reduces semantic mismatch while preserving a useful geographic affordance.

**Evidence:** The pipeline creates a reference map when no PMI score surpasses a threshold (set to 2.5 in the implementation) and zooms to locations mentioned in the article with place markers [@gaoNewsViewsAutomatedPipeline2014].

**Notes:** This is a decision rule at the map-type selection stage.

## When the fallback applies <!-- role: context -->

- **User Goal:** Get geographic context for a story even without a clear thematic variable.
- **Task:** Locate and contextualize mentioned places.
- **Data:** Article mentions locations but topic-to-variable alignment is weak.
- **Chart Setting:** Automated news visualization adjacent to article text.
- **Audience:** General readers; low tolerance for off-topic data graphics.
- **Success Criterion:** The visualization remains relevant and non-misleading.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The article explicitly states a measurable variable and geography level even if PMI is low. **Why:** Thematic mapping may still be appropriate using explicit cues not captured by PMI.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Loss of quantitative comparison when a thematic map would have been acceptable. **Risk:** Overuse of reference maps can reduce the perceived value of the system. **Mitigation:** Tune the PMI threshold and consider additional topic signals before triggering fallback.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Always generating a thematic map regardless of variable-match confidence. **Why it fails:** Irrelevant thematic encodings are salient and can decrease usefulness and trust.

## Quick tests <!-- role: check -->

**Failure Sign:** Users ask “why is this data shown?” when reading the map. **Quick Check:** Check whether the best PMI score is below the configured threshold. **Stronger Test:** Compare user relevance ratings for forced thematic maps versus reference fallbacks on low-PMI articles.

## What to do instead <!-- role: fix -->

- Display a locator map framed to the extracted locations with simple markers.
- Reduce the map’s thematic commitments by removing legends and choropleth encoding when in fallback mode.
- Provide navigation from the reference map to related articles or deeper views only when confidence increases.
