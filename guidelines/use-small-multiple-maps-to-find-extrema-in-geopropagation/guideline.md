---
id: use-small-multiple-maps-to-find-extrema-in-geopropagation
title: Use Small-Multiple Maps to Find Extrema
bibliography: references.bib
description: Small-multiple maps ranked above a proportional-symbol map for find-extremum
  accuracy, with a significant pair reported, in the collated outcomes.
labels:
- chart:small-multiples
- task:find-extremum
- visual:row
- visual:column
- visual:color-saturation
- impact:accuracy
- data:geospatial
- data:temporal
- audience:expert
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use small-multiple maps rather than a proportional-symbol map when users need to find extrema.

## The Logic <!-- role: reason -->

Small multiples allow scanning across time steps to spot maximum/minimum conditions, supporting more accurate extremum identification.

- **The Principle:** Improve extremum detection by enabling rapid comparison across multiple time slices.
- **The Evidence:** The collated results show small-multiple maps (E-1) rank above proportional-symbol map (E-2) for find-extremum accuracy, with a reported significant pair (E-1 > E-2), in [@pena-arayaComparisonGeographicalPropagation2020] as recorded by [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Identifying extreme values/events in geo-temporal propagation.
- **Data Type:** Map regions over time (time steps presented as small multiples).
- **Audience:** Expert/analytic users.

## When to Break It <!-- role: exceptions -->

- **Scenario:** If speed is the only metric that matters for extrema tasks.
- **Reason:** The collated time ranking does not show a clear advantage with reported significance for small multiples on find-extremum time (no significant pairs recorded for time).

## The Price <!-- role: costs -->

- **The Sacrifice:** More space and potentially more visual complexity from many panels.
- **The Risk:** Overcrowded panel grids can reduce readability and slow scanning.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to small multiples but not giving users clear temporal indexing (e.g., unlabeled panels).
- **Why it fails:** Extrema search depends on reliably scanning across time steps; unclear time-step identification increases cognitive load.

## How to Check <!-- role: check -->

- **Visual Sign:** Users correctly find the extremum but struggle to specify *when* it occurs due to unclear panel/time-step cues.
- **The Test:** Ask users to report both the extremum location and corresponding time step; if time-step confusion occurs, temporal cues are insufficient.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add clearer time-step labels/indices to each small multiple.
- **Best Fix:** Keep small multiples for extremum accuracy and improve layout/labeling so users can scan and attribute extrema to the correct time step reliably.
