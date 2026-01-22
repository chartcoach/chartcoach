---
id: use-spectrum-color-to-encode-geographic-intensity-on-area-maps-with-a-legend
title: Use a spectrum encoding for geographic intensity on area maps, and include
  a spectrum legend
bibliography: references.bib
description: Encode mortality intensity across geographic areas with a spectral color
  scale and a visible legend for interpretation.
labels:
- chart:map
- task:locate
- task:compare
- visual:color
- impact:readability
- data:geospatial
- audience:novice
- complexity:intermediate
- domain:health
---

## Encode geographic variation with spectrum color on an area-based map <!-- role: advice -->

When the goal is to explore how mortality varies across geographic regions, use an area-based map and encode intensity with a spectrum of color saturation, supported by a spectrum legend.

## Why spectrum-on-area supports geographic variability judgments <!-- role: reason -->

A geographic substrate allows spatial reasoning, and a spectral encoding makes relative intensity differences across regions immediately perceivable, especially for scanning variability across the globe.

**Mechanism:** Spatial layout leverages users’ ability to reason by location, while saturation variation creates a monotonic cue for magnitude across areas.

**Evidence:** For geographic exploration, geographic entities were organized by spatial attributes using an area-based map, and mortality variability was encoded with a spectrum via color saturation with an accompanying legend to support interpretation [@olaSimpleChartsDesign2016].

**Notes:** This approach complements non-spatial representations used for geography in other perspectives (e.g., demography/chronology).

## When this applies in health data visualization <!-- role: context -->

- **User Goal:** Assess global or regional variation and spot hotspots.
- **Task:** Geographic scanning and comparison of intensity.
- **Data:** Regional aggregates (countries or country clusters) with a quantitative measure (e.g., mortality rate).
- **Chart Setting:** Interactive geographic view linked to other facets (causes/risks).
- **Audience:** Mixed audiences, including users who think spatially.
- **Success Criterion:** Users can identify high/low regions and compare broad patterns quickly.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Users need precise numeric comparisons among many similarly valued regions. **Why:** A spectrum-on-area map prioritizes pattern recognition over exact value reading [@olaSimpleChartsDesign2016].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Numerical precision compared to tabular or aligned coordinate views. **Risk:** Users may over-interpret small color differences as meaningful. **Mitigation:** Provide the legend and enable on-demand value readout through interaction.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Showing a map without an explicit spectrum legend. **Why it fails:** Users cannot reliably interpret what saturation differences mean in terms of magnitude [@olaSimpleChartsDesign2016].

## Quick tests <!-- role: check -->

**Failure Sign:** Users ask “what does this shade mean?” **Quick Check:** Hide labels and ask users to identify the top three regions; if they cannot, the spectrum encoding or legend is insufficient. **Stronger Test:** Validate that users can correctly classify regions into legend bins using only the map and legend.

## What to do instead <!-- role: fix -->

- Add a spectrum legend with labeled bins that matches the map’s saturation steps.
- Link the map to a complementary comparative view (e.g., a matrix of countries × causes) for more precise comparisons.
- Aggregate to meaningful geographic clusters when country-level density is overwhelming.
- Provide interaction for tooltips or selection-driven detail to retrieve exact values.
