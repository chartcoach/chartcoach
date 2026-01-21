---
id: use-choropleth-maps-for-regional-vote-shares-and-winners
title: Map Regional Vote Patterns With Choropleths
bibliography: references.bib
description: Use choropleth maps to show regional vote shares for a party or the winning
  party/shift by district.
labels:
- chart:map
- task:locate
- visual:color
- impact:clarity
- data:geospatial
- audience:general
- domain:elections
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

Use choropleth maps to show the regional distribution of election results—either a single party’s vote share by district or the winning/most-increased party per district. [@muth_german_election_2021]

## The Logic <!-- role: reason -->

Maps align the data with geographic mental models, making spatial clustering and regional patterns immediately visible when values are tied to districts.

- **The Principle:** Spatial pattern recognition via geographic alignment
- **The Evidence:** [@muth_german_election_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** See where a party is strong/weak or where gains/losses concentrate
- **Data Type:** District-level results (vote share) or district-level categorical outcome (winner / biggest increase)
- **Audience:** General audience interpreting regional political geography [@muth_german_election_2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need to show multiple parties’ vote shares in one view.\
  **Reason:** A choropleth can only encode one party’s share per map at a time. [@muth_german_election_2021]
- **Scenario:** The key comparison is non-spatial (ranking parties nationally).\
  **Reason:** A bar/line chart may communicate national comparisons more directly. [@muth_german_election_2021]

## The Price <!-- role: costs -->

- **The Sacrifice:** Direct precise comparison across many districts
- **The Risk:** Readers may overfocus on area rather than people if districts vary in size (interpretation risk inherent to district maps). [@muth_german_election_2021]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Trying to show several parties’ vote shares in a single choropleth.\
  **Why it fails:** You must choose one variable; forcing multiple shares into one map obscures the message. [@muth_german_election_2021]
- **The Wrong Fix:** Using a map when the story is purely “who is ahead overall.”\
  **Why it fails:** Geography adds complexity without answering the main question. [@muth_german_election_2021]

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers can’t tell what the map encodes (share vs. winner vs. gain).
- **The Test:** If you can’t state the map’s single encoded variable in one short sentence, narrow the encoding and rewrite title/subtitle accordingly. [@muth_german_election_2021]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Limit the map to one clear metric (one party’s share, or a categorical winner/gainer) and clarify in the title. [@muth_german_election_2021]
- **Best Fix:** Use small multiples (several maps side-by-side) to compare multiple parties’ spatial patterns. [@muth_german_election_2021]
