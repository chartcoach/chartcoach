---
id: use-choropleth-maps-for-single-party-regional-shares-and-small-multiples-for-multiple-parties
title: "Use a choropleth map for one party\u2019s regional share, and use small multiples\
  \ to compare multiple parties"
bibliography: references.bib
description: Maps can show where support is concentrated, but each choropleth should
  represent one variable; use multiple maps for multiple parties.
labels:
- chart:map
- task:locate
- visual:color
- impact:clarity
- data:geospatial
- audience:general
- domain:elections
- tool:datawrapper
---

## Map one party’s vote share per choropleth, and use multiple maps for comparisons <!-- role: advice -->

Use a choropleth map to show the regional distribution of a single party’s vote share, and place multiple choropleths side by side when you need to compare patterns across parties.

## Why “one variable per choropleth” keeps maps interpretable <!-- role: reason -->

Choropleths rely on color to encode a single quantitative variable per region; trying to encode multiple parties at once makes it hard to decode values and invites confusion between categories and quantities. Small multiples keep each map readable while still allowing pattern comparison through repeated structure.

**Mechanism:** Repetition of the same geography with consistent encodings enables pattern-matching across maps without overloading a single map with competing signals.

**Evidence:** The post notes that each district in a choropleth can only show the vote share of one party at a time and recommends placing a few maps next to each other to show multiple parties and reveal patterns [@muth_german_election_2021].

**Notes:** This guideline concerns the structure of mapped comparisons, not which color scale to use.

## When this applies to election geography <!-- role: context -->

- **User Goal:** See where a party is strong/weak and how patterns differ across parties.
- **Task:** Locate hotspots, compare regional patterns, and scan for geographic clustering.
- **Data:** District-level vote shares by party.
- **Chart Setting:** Results recap, regional explainer, interactive hover tooltips optional.
- **Audience:** Readers who recognize geography but may not know district names.
- **Success Criterion:** Readers can identify regional strongholds without misreading what the colors represent.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your goal is to show only the winning party (a categorical outcome) per district rather than a vote share. **Why:** A single categorical winner map can be clearer for “who won where” than multiple share maps [@muth_german_election_2021].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Multiple maps take more space and may require careful alignment and labeling. **Risk:** Readers may compare color intensities across maps if scales differ. **Mitigation:** Keep legends and scaling consistent across the small multiples when the comparison is the point [@muth_german_election_2021].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Trying to show vote shares for multiple parties in one choropleth. **Why it fails:** A single color encoding cannot simultaneously represent multiple quantitative variables without ambiguity [@muth_german_election_2021].

## Quick tests <!-- role: check -->

**Failure Sign:** A reader asks “Which party does this color represent?” or “Is darker always more of the same party?” **Quick Check:** Verify that each map title names exactly one party (or exactly one mapped variable) [@muth_german_election_2021]. **Stronger Test:** Ask a colleague to find the top region for two different parties; if they can’t do it quickly, split into small multiples.

## What to do instead <!-- role: fix -->

- Create separate choropleths for each party you want to compare and align them as small multiples [@muth_german_election_2021].
- If you need a single-map summary, map only the winning party per district as a categorical choropleth [@muth_german_election_2021].
- Use tooltips to provide exact values while keeping the map focused on pattern, not precision [@muth_german_election_2021].
- Add brief callouts for notable regions to guide attention when the pattern is subtle [@muth_german_election_2021].
