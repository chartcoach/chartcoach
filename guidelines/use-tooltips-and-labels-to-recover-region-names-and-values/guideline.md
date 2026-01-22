---
id: use-tooltips-and-labels-to-recover-region-names-and-values
title: Use tooltips for region names and values, and add labels when geographic familiarity
  is low
bibliography: references.bib
description: Because regions are hard to read directly on a choropleth, tooltips and
  selective labels help viewers identify places and interpret values.
labels:
- chart:choropleth
- task:lookup
- visual:annotation
- impact:clarity
- data:geospatial
- audience:general
- interaction:tooltip
---

## Provide tooltips for names and values, and use labels when readers need orientation <!-- role: advice -->

Use tooltips to show each region’s name and underlying value (and any brief explanatory context) since these details are hard to read on the map itself. Add labels when the audience is unlikely to know the geography being mapped.

## Interaction and annotation compensate for map readability limits <!-- role: reason -->

Choropleths prioritize spatial and color pattern perception, not text legibility, so region identification and exact values can be difficult without assistance. Tooltips let readers retrieve precise information on demand, while labels reduce the burden of geographic knowledge by making key locations explicit.

**Mechanism:** On-demand detail (tooltips) and direct naming (labels) reduce decoding steps and ambiguity in region identification.

**Evidence:** Tooltips are recommended to communicate region names and underlying values and can also convey extra information or reminders; labels become more important the less readers know about the mapped area [@muth_choroplethmaps_2018].

**Notes:** Tooltips help the map function as an overview while still supporting exact lookup.

## Situations where this guideline applies <!-- role: context -->

- **User Goal:** Identify a region and learn its exact value.
- **Task:** Look up details after spotting a pattern.
- **Data:** Region-level values where exact numbers or names matter to interpretation.
- **Chart Setting:** Interactive maps (tooltips) and/or maps for audiences unfamiliar with the geography (labels).
- **Audience:** Mixed familiarity with place names and boundaries; includes readers who need explicit cues.
- **Success Criterion:** Readers can find their region and retrieve its value without confusion.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The map is static and too small to support readable labels without clutter. **Why:** Labels can overwhelm the map and reduce the visibility of the color encoding [@muth_choroplethmaps_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Tooltips require interaction; labels consume space and can clutter. **Risk:** Over-labeling can obscure colors and boundaries. **Mitigation:** Use labels selectively and rely on tooltips for full detail.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Expecting readers to infer region names and exact values purely from color and shape. **Why it fails:** Region text is hard to read on maps and color alone is imprecise for exact values [@muth_choroplethmaps_2018].
- **Mistake:** Labeling too many regions in a dense map. **Why it fails:** Labels compete with the color encoding and make the map harder to scan [@muth_choroplethmaps_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** Users can’t locate a specific region or repeatedly misidentify it. **Quick Check:** Try to find and name five regions without hovering; if that’s hard, add labels or rely on tooltips. **Stronger Test:** Ask a reader to retrieve the value for a specified region; if they can’t do it quickly, the map needs better tooltip/label support.

## What to do instead <!-- role: fix -->

- Enable tooltips that show region name and exact value.
- Add brief tooltip text to remind readers what the measure represents.
- Add labels for key regions or for orientation when the geography is unfamiliar.
- Use a table or text callouts for the handful of regions that matter most when labels would clutter the map.
