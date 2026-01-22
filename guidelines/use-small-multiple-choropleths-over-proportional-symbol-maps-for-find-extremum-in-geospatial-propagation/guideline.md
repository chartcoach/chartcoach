---
id: use-small-multiple-choropleths-over-proportional-symbol-maps-for-find-extremum-in-geospatial-propagation
title: Use small-multiple choropleth maps over a proportional-symbol map (single map
  with glyphs) for find-extremum tasks in propagation data
bibliography: references.bib
description: For finding extremes in geo-temporal propagation, small-multiple maps
  can yield higher accuracy and competitive speed versus a glyph-based single map.
labels:
- chart:map
- task:find-extremum
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

## Prefer small-multiple maps for finding extremes in propagation <!-- role: advice -->

Use small-multiple choropleth maps rather than a single map with per-region glyphs when users must find an extremum (an extreme high or low) in geo-temporal propagation data.

## Why small multiples can help extremum finding here <!-- role: reason -->

Extremum finding can rely on quickly spotting the strongest color intensity in a spatial field at one or more time steps; time-sliced maps can make those spatial extrema salient without requiring cross-glyph integration.

**Mechanism:** Presenting each time step as a full choropleth supports direct visual search for the most extreme region per time slice.

**Evidence:** For find-extremum, small-multiple maps (E-1) ranked higher than the proportional-symbol map (E-2) on accuracy, with a significant advantage reported for E-1 over E-2. [@pena-arayaComparisonGeographicalPropagation2020; @zengReviewCollationGraphical2023]\
**Evidence:** For find-extremum time, small-multiple maps (E-1) also ranked ahead of the proportional-symbol map (E-2), though no significant pairwise difference was recorded in the extracted result. [@pena-arayaComparisonGeographicalPropagation2020; @zengReviewCollationGraphical2023]

**Notes:** This guideline is specific to the two compared designs (small multiples vs a single glyph-based map) and the find-extremum task framing used.

## When this guideline applies (find-extremum) <!-- role: context -->

- **User Goal:** Identify where (and implicitly when) the maximum or minimum propagation intensity occurs.
- **Task:** Find extremum.
- **Data:** Geo-temporal propagation values per region across ordered time steps.
- **Chart Setting:** Small-multiple choropleth grid vs a single map with per-region glyphs using the same sequential color encoding.
- **Audience:** Analysts/experts performing propagation diagnostics.
- **Success Criterion:** Higher accuracy in locating the extremum; time as a secondary criterion.

## When not to follow it (find-extremum) <!-- role: exceptions -->

**Break it when:** The extremum is defined strictly as a within-region temporal maximum and users only need to inspect one region at a time. **Why:** A per-region glyph may better support localized temporal inspection, which is not what the reported find-extremum evidence isolates.

## Tradeoffs of small multiples for extremum tasks <!-- role: costs -->

**Sacrifice:** Small multiples use more screen space across time steps and reduce per-map size. **Risk:** Very small panels can make subtle color differences harder to discriminate, potentially eroding the accuracy advantage. **Mitigation:** Ensure panels remain large enough for reliable color comparisons on your target display.

## Common mistakes for extremum finding in propagation maps <!-- role: mistakes -->

**Mistake:** Replacing small multiples with a glyph-per-region map to “reduce clutter.” **Why it fails:** The extracted evidence shows lower find-extremum accuracy for the glyph-based approach in this comparison.

## Quick tests for extremum finding <!-- role: check -->

**Failure Sign:** Users misidentify the region/time of the highest intensity or repeatedly change their answer after re-checking.\
**Quick Check:** Run a few find-extremum prompts and count wrong picks; if errors concentrate on the glyph map, prefer small multiples.\
**Stronger Test:** Measure accuracy on find-extremum with representative datasets and keep the design with the lower error rate.

## What to do instead if small multiples are impractical <!-- role: fix -->

- Reduce the number of time steps shown at once and allow switching between subsets of time steps.
- Use the glyph-based single map as a supplementary view for detailed region inspection after an extremum candidate is found.
- Add a mechanism to highlight the currently inspected time step consistently across the view to reduce search friction.
- If you must keep a single-map view, limit the task to localized extrema within a region rather than global extrema across regions and time.
