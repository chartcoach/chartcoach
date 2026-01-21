---
id: use-small-multiple-maps-to-compare-party-spatial-patterns
title: Compare Multiple Parties With Small Multiple Maps
bibliography: references.bib
description: "Because a choropleth shows only one party\u2019s vote share at a time,\
  \ use side-by-side maps to compare spatial distributions."
labels:
- chart:map
- task:compare
- visual:layout
- impact:clarity
- data:geospatial
- audience:general
- domain:elections
- source:datawrapper-blog
---

## The Rule <!-- role: advice -->

When you need to compare vote-share patterns of multiple parties, place multiple choropleth maps next to each other instead of trying to combine parties into a single map. [@muth_german_election_2021]

## The Logic <!-- role: reason -->

A single choropleth can encode only one continuous variable per region. Small multiples preserve geographic consistency while enabling side-by-side comparison of patterns.

- **The Principle:** Small multiples for multi-variable comparison
- **The Evidence:** [@muth_german_election_2021]

## Where to Apply <!-- role: context -->

- **User Goal:** Compare where different parties are strong/weak regionally
- **Data Type:** District-level vote shares for multiple parties
- **Audience:** Readers looking for geographic contrasts, especially for smaller parties where patterns stand out [@muth_german_election_2021]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You only need to compare two parties directly in one view.\
  **Reason:** A dedicated two-party comparison map may be more compact than multiple panels. [@muth_german_election_2021]
- **Scenario:** Space is extremely constrained (mobile-only card).\
  **Reason:** Multiple maps may become too small to read. [@muth_german_election_2021]

## The Price <!-- role: costs -->

- **The Sacrifice:** Screen/print space
- **The Risk:** Too many panels can overwhelm; viewers may not know what to compare unless titles and scales are consistent. [@muth_german_election_2021]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching party layers in a single map without showing them simultaneously.\
  **Why it fails:** Readers can’t compare patterns reliably from memory. [@muth_german_election_2021]
- **The Wrong Fix:** Using inconsistent color scales across the maps.\
  **Why it fails:** Side-by-side comparisons become invalid or misleading. [@muth_german_election_2021]

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers ask “Are these maps using the same scale?” or comparisons feel ambiguous.
- **The Test:** Verify that each panel uses consistent boundaries and comparable scaling; if not, the small-multiple comparison breaks. [@muth_german_election_2021]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce to the few parties needed for the story and keep map sizes readable. [@muth_german_election_2021]
- **Best Fix:** Standardize titles, legends/scales, and layout across panels so differences reflect data, not design changes. [@muth_german_election_2021]
