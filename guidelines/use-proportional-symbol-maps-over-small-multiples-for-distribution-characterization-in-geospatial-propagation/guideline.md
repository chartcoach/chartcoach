---
id: use-proportional-symbol-maps-over-small-multiples-for-distribution-characterization-in-geospatial-propagation
title: Use a proportional-symbol map (single map with glyphs) over small-multiple
  choropleths for characterize-distribution tasks in propagation data
bibliography: references.bib
description: For characterize-distribution judgments in geo-temporal propagation,
  a single map with region glyphs can improve accuracy compared to small-multiple
  maps.
labels:
- chart:map
- task:characterize-distribution
- visual:color
- visual:position
- impact:accuracy
- data:temporal
- data:geospatial
- audience:expert
- domain:propagation
- comparison:small-multiples-vs-glyph-map
---

## Prefer a proportional-symbol map for distribution characterization in propagation <!-- role: advice -->

Use a single map with per-region glyphs (a proportional-symbol map design) rather than small-multiple choropleth maps when users must characterize the distribution of propagation over time.

## Why glyphs can support distribution characterization <!-- role: reason -->

Distribution characterization can depend on perceiving patterns across regions without losing geographic context; a single-map view avoids shrinking each time slice into many small panels.

**Mechanism:** Keeping the geography fixed while showing per-region temporal variation can make it easier to assess overall distribution patterns without repeatedly relocating regions across panels.

**Evidence:** In characterize-distribution, the proportional-symbol map (E-2) ranked higher than small-multiple maps (E-1) on accuracy. [@pena-arayaComparisonGeographicalPropagation2020; @zengReviewCollationGraphical2023]\
**Evidence:** In characterize-distribution, small-multiple maps (E-1) ranked higher than the proportional-symbol map (E-2) on time, with a significant difference reported for E-1 over E-2. [@pena-arayaComparisonGeographicalPropagation2020; @zengReviewCollationGraphical2023]

**Notes:** This is an accuracy–time tradeoff: the design that ranks higher on accuracy ranks lower on time for this task.

## When this guideline applies (characterize-distribution) <!-- role: context -->

- **User Goal:** Describe the overall distributional pattern of propagation values across regions over time.
- **Task:** Characterize distribution.
- **Data:** Geo-temporal propagation values per region across ordered time steps.
- **Chart Setting:** Static comparison between small-multiple choropleth panels versus a single map with per-region glyphs.
- **Audience:** Analysts/experts working with propagation patterns.
- **Success Criterion:** Higher distribution-characterization accuracy (even if slower).

## When not to follow it (distribution characterization) <!-- role: exceptions -->

**Break it when:** You need fastest possible completion time for characterize-distribution. **Why:** Small multiples ranked better on time for this task, with evidence of a significant advantage.

## Tradeoffs of choosing accuracy over speed <!-- role: costs -->

**Sacrifice:** Users may take longer to answer distribution questions with the glyph-based single map. **Risk:** In time-sensitive workflows, the slower design can reduce throughput even if answers are more correct. **Mitigation:** Decide explicitly whether accuracy or speed is the priority metric for this task.

## Common mistakes for distribution tasks in propagation maps <!-- role: mistakes -->

**Mistake:** Optimizing only for accuracy without checking time cost on distribution tasks. **Why it fails:** The evidence shows the more accurate design can be slower for the same task.

## Quick tests for distribution characterization <!-- role: check -->

**Failure Sign:** Users provide correct answers but report the task feels slow or tedious, or you see long dwell times.\
**Quick Check:** Time a few characterize-distribution trials; if the glyph map consistently slows users, reconsider.\
**Stronger Test:** Measure both accuracy and completion time on the same characterize-distribution prompts and pick the design that matches your metric priority.

## What to do instead if you must prioritize speed <!-- role: fix -->

- Use small-multiple maps when characterize-distribution must be answered quickly.
- Provide a “speed mode” that defaults to small multiples and an “accuracy mode” that switches to the glyph map for careful review.
- Shorten the number of time panels shown at once when using small multiples to reduce scanning overhead.
- Gate the slower glyph map behind a user action (“inspect distribution in detail”) to preserve speed for routine checks.
