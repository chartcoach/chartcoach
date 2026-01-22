---
id: use-smallest-geographic-units-when-detail-reveals-patterns
title: Use the smallest geographic units available when finer detail reveals regional
  patterns
bibliography: references.bib
description: Smaller administrative units can reveal local variation and clearer spatial
  patterns than coarse aggregations.
labels:
- chart:choropleth
- task:discover
- visual:granularity
- impact:insight
- data:geospatial
- audience:general
- complexity:intermediate
---

## Prefer finer regional units to show more detailed spatial variation <!-- role: advice -->

Choose the smallest geographic units you can reliably map and explain, so readers can see more refined patterns. Use larger units only when the aggregation is itself the meaningful story.

## Coarse aggregation can hide local structure <!-- role: reason -->

When data is aggregated into large regions, local variation gets averaged away and true clusters or contrasts may disappear. Smaller units preserve spatial texture, making it easier to spot patterns that are geographically specific.

**Mechanism:** Finer geographic granularity increases the number of comparable regions and reduces averaging, which surfaces localized highs/lows.

**Evidence:** Using smaller units (e.g., counties instead of states, NUTS2 regions instead of countries) is recommended to provide a more refined picture and allow readers to spot more regional patterns [@muth_choroplethmaps_2018]. An exception is noted where larger units can be more informative when the system outcome is determined at that unit level (e.g., winner-takes-all in U.S. presidential elections) [@muth_choroplethmaps_2018].

**Notes:** This is a design choice about the meaningful unit of interpretation, not just “more detail is always better.”

## Situations where this guideline applies <!-- role: context -->

- **User Goal:** Find where within a larger region values differ or cluster.
- **Task:** Detect within-state/within-country variation and localized anomalies.
- **Data:** Values available (or can be computed) at multiple administrative levels.
- **Chart Setting:** Static or interactive maps where extra regions remain readable with tooltips/labels.
- **Audience:** Readers who can handle more regions, or who have interaction support to look up values.
- **Success Criterion:** The map reveals patterns that would be hidden with coarser boundaries.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The relevant outcome is determined at a higher aggregation level (e.g., winner-takes-all results by state). **Why:** Showing smaller units can distract from the unit that actually decides the result [@muth_choroplethmaps_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Smaller units increase visual complexity and may require more interaction (tooltips) to read. **Risk:** Very small regions can become illegible or visually noisy. **Mitigation:** Use tooltips and selective labeling to support comprehension.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Mapping only large units by default even when small-unit data exists. **Why it fails:** Aggregation can hide important regional patterns and oversimplify the geography [@muth_choroplethmaps_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** Large regions look uniform despite known local differences. **Quick Check:** If smaller-unit data is available, preview both; if the fine-grain version reveals distinct clusters, keep it. **Stronger Test:** Ask a domain reader to locate a known hotspot; if it can’t be seen at the coarse level, the unit is too large.

## What to do instead <!-- role: fix -->

- Switch the map to smaller administrative units when available (e.g., counties instead of states).
- Add tooltips so the increased number of regions does not require on-map labels everywhere.
- Use selective labels for key places when geography is unfamiliar.
- Keep the larger-unit map only when the aggregated unit is the decision-relevant unit.
