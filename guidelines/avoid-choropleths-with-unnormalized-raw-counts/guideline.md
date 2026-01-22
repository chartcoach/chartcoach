---
id: avoid-choropleths-with-unnormalized-raw-counts
title: Avoid choropleths with unnormalized raw counts
bibliography: references.bib
description: Use normalized rates for choropleth maps to prevent area and population
  effects from misleading interpretation.
labels:
- chart:choropleth
- task:compare
- visual:color
- impact:interpretability
- data:geospatial
- audience:general
- complexity:foundational
---

## Use normalized values rather than raw counts in choropleths <!-- role: advice -->

When using a choropleth map, encode normalized values (rates or densities) rather than raw counts.

## Choropleths can mislead when area and aggregation distort meaning <!-- role: reason -->

Choropleths shade regions, so viewers may conflate the mapped value with the size or prominence of the geographic area; raw counts further confound interpretation when regions differ in population or baseline.

**Mechanism:** Color shading is interpreted in the context of region shapes and sizes, so unnormalized totals can appear to indicate “more” simply because a region is large or populous.

**Evidence:** A common error in choropleths is encoding raw values (such as population) rather than normalized values to produce a density map, and perception of shading can be affected by the underlying area of the region [@heerTourVisualizationZoo2010].

**Notes:** This does not eliminate all perception issues; it prevents a major semantic error.

## Context: Region-based aggregates on maps <!-- role: context -->

- **User Goal:** Compare a metric across geographic regions.
- **Task:** Identify high/low regions and spatial patterns.
- **Data:** Values aggregated by region (states, counties, countries) with heterogeneous population/area.
- **Chart Setting:** Static or interactive map intended for rapid scanning.
- **Audience:** General audiences prone to interpreting shaded regions as “more important.”
- **Success Criterion:** Viewers interpret color as the intended rate/percentage rather than a proxy for size.

## Exceptions: When totals are explicitly the message <!-- role: exceptions -->

**Break it when:** The intended question is explicitly about raw totals per region. **Why:** Normalization would change the meaning of the communicated quantity [@heerTourVisualizationZoo2010].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Normalized values can hide where the largest absolute number of cases/people are. **Risk:** Viewers may assume a rate map implies total burden. **Mitigation:** Provide separate totals via annotation or a coordinated view.

## Mistakes: Common failure modes <!-- role: mistakes -->

- **Mistake:** Coloring regions by total population or total cases and labeling it as prevalence. **Why it fails:** Raw totals do not measure density and misrepresent “how common” something is [@heerTourVisualizationZoo2010].
- **Mistake:** Ignoring that region area influences perceived magnitude. **Why it fails:** Larger regions can dominate attention independent of the encoded value [@heerTourVisualizationZoo2010].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Large-area regions are consistently described as “worst” even when their rates are moderate. **Quick Check:** Compare your map’s top-5 regions to a ranked table of the intended metric; mismatches suggest semantic or perceptual confounding. **Stronger Test:** Ask viewers to explain whether the map shows “total” or “rate”; uncertainty indicates inadequate labeling.

## Fix: What to do instead <!-- role: fix -->

- Convert raw counts to rates or densities before mapping.
- Add a companion view that shows raw totals separately if they matter.
- Use a graduated symbol map when you need to show totals without area confounding.
- Use a cartogram when you want region area to encode a chosen variable explicitly.
