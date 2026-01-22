---
id: use-proportional-symbol-maps-over-small-multiples-for-range-estimation-in-geospatial-propagation
title: Use a proportional-symbol map (single map with glyphs) over small-multiple
  choropleths for determine-range tasks in propagation data
bibliography: references.bib
description: For determine-range judgments in geo-temporal propagation, a single map
  with region glyphs can outperform small-multiple maps on accuracy and/or time.
labels:
- chart:map
- task:determine-range
- visual:color
- visual:position
- impact:accuracy
- impact:speed
- data:temporal
- data:geospatial
- audience:expert
- domain:propagation
- comparison:small-multiples-vs-glyph-map
---

## Prefer a proportional-symbol map for determine-range in propagation <!-- role: advice -->

Use a single map with per-region glyphs (a proportional-symbol map design) instead of small-multiple choropleth maps when users must determine the range of a propagation pattern over time.

## Why the glyph-based single map can help range judgments <!-- role: reason -->

Range judgments can benefit when viewers can keep spatial context stable while inspecting temporal variation per region, rather than repeatedly re-locating regions across many small panels.

**Mechanism:** A stable single-map layout supports faster, less error-prone scanning for minima/maxima across regions and time when the alternative reduces each frame’s resolution via many small maps.

**Evidence:** For one determine-range task instance, the proportional-symbol map (E-2) ranked better than small-multiple maps (E-1) on both accuracy and time. [@pena-arayaComparisonGeographicalPropagation2020; @zengReviewCollationGraphical2023]\
**Evidence:** For a second determine-range task instance, accuracy ranked small multiples (E-1) above the proportional-symbol map (E-2), but time ranked the proportional-symbol map (E-2) above small multiples (E-1). [@pena-arayaComparisonGeographicalPropagation2020; @zengReviewCollationGraphical2023]

**Notes:** The extracted evidence is directional ranking; only some pairwise differences were marked significant for time in the determine-range tasks.

## When this guideline applies (determine-range) <!-- role: context -->

- **User Goal:** Judge how widely values vary (span from low to high) in a geo-temporal propagation setting.
- **Task:** Determine range.
- **Data:** Geo-temporal propagation values per region across ordered time steps.
- **Chart Setting:** Static comparison between a small-multiple choropleth grid versus a single map with per-region glyphs; typical desktop display.
- **Audience:** Analysts/experts working with propagation patterns.
- **Success Criterion:** Higher accuracy and/or lower completion time for range judgments.

## When not to follow it (range) <!-- role: exceptions -->

**Break it when:** You must optimize specifically for accuracy in the determine-range scenario represented by the second determine-range result where small multiples ranked higher. **Why:** The available evidence includes a determine-range accuracy ranking that favors small multiples over the proportional-symbol map.

## Tradeoffs of using a glyph-based single map <!-- role: costs -->

**Sacrifice:** You may add visual complexity by introducing per-region glyphs on top of geography. **Risk:** Users may become slower or less accurate if the glyph map’s structure makes the relevant range cues harder to isolate than scanning multiple frames. **Mitigation:** Validate with a task-matched pilot using the same determine-range prompt you expect in deployment.

## Common mistakes for range-oriented propagation views <!-- role: mistakes -->

**Mistake:** Assuming one map strategy will dominate for all versions of “determine range.” **Why it fails:** The evidence includes mixed rankings across two determine-range instances, suggesting task wording or setup can flip which design is best.

## Quick tests for this choice (range) <!-- role: check -->

**Failure Sign:** People hesitate while searching for extremes or frequently re-check earlier views to confirm the span.\
**Quick Check:** Ask a few users to answer a determine-range question and note whether they can complete it without repeatedly switching attention across many panels.\
**Stronger Test:** Run a small A/B test comparing time and accuracy between the two designs using your exact determine-range prompt.

## What to do instead if the glyph map underperforms for range <!-- role: fix -->

- Use small-multiple maps when your determine-range question format matches the scenario where small multiples ranked higher on accuracy.
- Offer both representations and let the analyst switch when they notice errors or delays on range judgments.
- Reduce the number of panels (time steps shown at once) if small multiples are required but become hard to scan.
- Add a focused interaction that helps users keep the same region identifiable across views when small multiples are used.
