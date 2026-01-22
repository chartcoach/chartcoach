---
id: use-cartograms-when-you-want-area-to-explicitly-encode-a-data-variable
title: Use cartograms when you want area to explicitly encode a data variable
bibliography: references.bib
description: Distort geographic regions so their displayed area represents a chosen
  variable, making size comparisons direct.
labels:
- chart:cartogram
- task:compare
- visual:area
- impact:emphasis
- data:geospatial
- audience:general
- complexity:intermediate
---

## Distort geography only to make area represent the intended quantity <!-- role: advice -->

Use a cartogram when you want geographic region area to directly encode a data variable rather than represent land area.

## Area encoding becomes explicit rather than accidental <!-- role: reason -->

Standard maps already vary in region size, which can bias attention; cartograms deliberately make area the encoding, aligning perception of size with the intended data.

**Mechanism:** By resizing regions to match values, viewers can compare magnitudes through area judgments tied to data rather than to geography.

**Evidence:** Cartograms distort the shape of geographic regions so that area directly encodes a data variable; a Dorling cartogram represents regions with sized circles placed to resemble geographic configuration, enabling area and color to encode different variables [@heerTourVisualizationZoo2010].

**Notes:** Dorling cartograms trade geographic fidelity for clearer size comparison.

## Context: Totals or burdens by region <!-- role: context -->

- **User Goal:** Compare regional magnitudes where “how much” is central.
- **Task:** Identify which regions contribute most to a total and compare relative burdens.
- **Data:** Region-level totals or other variables suited to area encoding; optionally a second variable for color.
- **Chart Setting:** Static or interactive map-like display where approximate geography is acceptable.
- **Audience:** General audiences if the distortion is clearly signposted.
- **Success Criterion:** Viewers correctly identify largest contributors without being misled by land area.

## Exceptions: When geographic shape and location must be precise <!-- role: exceptions -->

**Break it when:** Users need accurate geographic shapes or exact spatial relationships. **Why:** Cartograms knowingly distort geography to encode data [@heerTourVisualizationZoo2010].

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Geographic fidelity and immediate recognizability of some regions. **Risk:** Viewers may misinterpret distances and adjacency as literal. **Mitigation:** Add labels and a reference map or interaction to connect distorted regions to real geography.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Using a cartogram without making the distortion goal explicit. **Why it fails:** Viewers can assume the map is geographically faithful and draw incorrect spatial conclusions [@heerTourVisualizationZoo2010].

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Viewers comment on “where things are” rather than “how much” each region represents. **Quick Check:** Ask what the size of a region means; if they answer in land-area terms, the encoding is not clear. **Stronger Test:** Compare whether viewers can correctly pick the top contributors faster than with a standard map.

## Fix: What to do instead <!-- role: fix -->

- Use a choropleth with normalized values when geographic fidelity matters.
- Use a graduated symbol map to show totals without distorting geography.
- Provide a linked reference map that highlights the selected cartogram region in true geography.
- Add clear labeling that region size encodes the chosen variable.
