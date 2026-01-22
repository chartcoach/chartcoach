---
id: use-small-multiple-choropleths-over-proportional-symbol-maps-for-clustering-in-geospatial-propagation
title: Use small-multiple choropleth maps over a proportional-symbol map (single map
  with glyphs) for cluster tasks in propagation data
bibliography: references.bib
description: For clustering judgments in geo-temporal propagation, small-multiple
  maps can outperform a single glyph-based map in accuracy and time.
labels:
- chart:map
- task:cluster
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

## Prefer small-multiple maps for cluster judgments in propagation <!-- role: advice -->

Use small-multiple choropleth maps instead of a single map with per-region glyphs when users must identify clusters in geo-temporal propagation patterns.

## Why small multiples can help clustering here <!-- role: reason -->

Clustering judgments can benefit from seeing each time step as a full spatial field, making spatial groupings easier to spot at each step without decoding many separate per-region glyphs.

**Mechanism:** A set of time-sliced maps can support direct spatial cluster perception per time step, while a per-region glyph layout can disperse the relevant evidence across many small glyphs.

**Evidence:** For cluster tasks, small-multiple maps (E-1) ranked higher than the proportional-symbol map (E-2) on both accuracy and time, with a significant time advantage reported for E-1 over E-2. [@pena-arayaComparisonGeographicalPropagation2020; @zengReviewCollationGraphical2023]

**Notes:** The extracted evidence does not report a significant accuracy difference for clustering, only a directional ranking.

## When this guideline applies (cluster) <!-- role: context -->

- **User Goal:** Detect clusters (spatial groupings) in propagation intensity over time.
- **Task:** Cluster.
- **Data:** Geo-temporal propagation values per region across ordered time steps.
- **Chart Setting:** Comparing a grid of time-sliced choropleth maps versus a single map with per-region glyphs.
- **Audience:** Analysts/experts inspecting propagation structure.
- **Success Criterion:** Faster cluster identification without reducing accuracy.

## When not to follow it (cluster) <!-- role: exceptions -->

**Break it when:** Your cluster task is defined in a way that requires within-region temporal pattern inspection more than across-region spatial grouping. **Why:** The evidence only covers the specific cluster task setup in the study; different clustering definitions may rely on different visual cues.

## Tradeoffs of small multiples for clustering <!-- role: costs -->

**Sacrifice:** Individual maps become smaller as time steps increase, which can reduce legibility of fine geographic detail. **Risk:** Clusters may be missed if the small panels make boundaries and color differences hard to see. **Mitigation:** Keep time-step count per view manageable for the available screen size.

## Common mistakes for clustering propagation data <!-- role: mistakes -->

**Mistake:** Using a single glyph-per-region map for clustering because it “shows everything at once.” **Why it fails:** The cluster evidence ranks the glyph-based approach worse on both accuracy and time, suggesting “everything at once” can still be harder to integrate for clustering.

## Quick tests for clustering views <!-- role: check -->

**Failure Sign:** Users scan many glyphs but cannot confidently point to clustered regions at specific times.\
**Quick Check:** Ask users to mark clustered regions for a few time steps; if they struggle more on the glyph map than small multiples, switch.\
**Stronger Test:** Compare completion time for cluster questions between designs using the same datasets and prompts.

## What to do instead if small multiples become too dense <!-- role: fix -->

- Reduce the number of time steps shown simultaneously in small multiples and paginate or segment the timeline.
- Use a single-map glyph design only as a secondary view for within-region temporal inspection, not as the primary clustering view.
- Increase geographic generalization (e.g., simplify boundaries) to improve readability in smaller panels.
- Provide interactions that help users quickly align the same time step across the view if you split the small multiples into multiple pages.
