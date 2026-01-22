---
id: map-rates-not-totals-in-choropleths
title: Map relative rates (not absolute totals) in choropleth maps
bibliography: references.bib
description: Choropleths should encode normalized measures like rates or percentages
  so regions are comparable.
labels:
- chart:choropleth
- task:compare
- visual:color
- impact:honesty
- data:geospatial
- audience:general
- data:quantitative
---

## Encode normalized values in choropleths, such as rates or percentages <!-- role: advice -->

Use choropleth maps for relative measures (rates, shares, percentages) that make regions comparable. Avoid choropleths for raw counts unless the counts have already been normalized appropriately.

## Choropleths imply comparability across unequal regions <!-- role: reason -->

Because choropleths assign colors to geographic regions, viewers naturally compare regions as if the values are directly comparable. Raw totals often reflect population size or area rather than the phenomenon of interest, so mapping totals can mislead by making the map answer a different question than intended.

**Mechanism:** Filled-area color encourages region-to-region comparison; normalization (e.g., per capita) aligns the encoded value with fair comparison across regions.

**Evidence:** Choropleths are described as working best for relative data (e.g., unemployment rate), while mapping absolute numbers (e.g., number of unemployed people) is not useful without context like population size [@muth_choroplethmaps_2018]. For absolute data, a symbol map is presented as a more appropriate alternative, with the caution that it may primarily reveal where most people live [@muth_choroplethmaps_2018].

**Notes:** A choropleth of a derived measure (such as change over time) can still fit this rule if the derived measure remains comparable across regions.

## Situations where this guideline applies <!-- role: context -->

- **User Goal:** Compare intensity or prevalence of a phenomenon across regions.
- **Task:** Identify which regions have higher/lower rates or shares.
- **Data:** Regional values where denominators vary (population, households, land area, registered voters).
- **Chart Setting:** Any choropleth intended for cross-region comparison by color.
- **Audience:** Readers likely to interpret darker/lighter areas as “more/less” in a comparable way.
- **Success Criterion:** Differences reflect the phenomenon, not merely region size or population concentration.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The mapped value is already inherently comparable as an absolute measure for the audience and purpose. **Why:** Normalization could obscure the intended absolute scale of the phenomenon [@muth_choroplethmaps_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Normalized metrics can be less intuitive than counts and may require explanation of the denominator. **Risk:** Poor denominator choice can shift the story to an unintended comparison. **Mitigation:** Make the unit explicit (e.g., “per 100 people”) in the legend/tooltip.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Mapping totals (counts) as a choropleth to imply “where the problem is worst.” **Why it fails:** The map often becomes a proxy for population distribution rather than the phenomenon [@muth_choroplethmaps_2018].
- **Mistake:** Omitting the denominator in labels/legend when mapping a rate. **Why it fails:** Readers cannot interpret what the rate means or compare it appropriately [@muth_choroplethmaps_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** The darkest regions are also the biggest cities or most populous areas regardless of the topic. **Quick Check:** Ask “would a larger population automatically increase this value?”—if yes, you likely need a rate/share. **Stronger Test:** Compare two regions with very different population sizes; if the map’s takeaway flips after converting to per-capita, the choropleth should use the normalized form.

## What to do instead <!-- role: fix -->

- Convert counts to a rate, share, or per-capita measure before mapping.
- Use a symbol map when absolute totals are truly the message you want to communicate.
- Add text, a table, or tooltips to clarify denominators and units for any normalized measure.
- Reframe the question explicitly if the real story is population concentration rather than prevalence.
