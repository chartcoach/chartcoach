---
id: use-small-multiple-maps-for-clustering-in-geopropagation
title: Use Small-Multiple Maps for Clustering Tasks
bibliography: references.bib
description: Small-multiple maps ranked above a proportional-symbol map for clustering
  accuracy and time in the collated study outcomes.
labels:
- chart:small-multiples
- task:cluster
- visual:row
- visual:column
- visual:color-saturation
- impact:accuracy
- impact:speed
- data:geospatial
- data:temporal
- audience:expert
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Use small-multiple maps rather than a proportional-symbol map for clustering tasks.

## The Logic <!-- role: reason -->

Juxtaposed map panels can make it easier to compare spatial patterns across time steps in support of cluster detection.

- **The Principle:** Support cluster detection via side-by-side temporal comparison.
- **The Evidence:** In the collated results from [@pena-arayaComparisonGeographicalPropagation2020], small-multiple maps (E-1) rank above proportional-symbol map (E-2) for cluster accuracy and for cluster time (with a recorded significant pair for time). This extraction is documented in [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Detecting clusters in geo-temporal propagation patterns.
- **Data Type:** Regional values across time steps (mapped with sequential color).
- **Audience:** Expert analysts.

## When to Break It <!-- role: exceptions -->

- **Scenario:** If your system cannot allocate enough screen space for readable small multiples.
- **Reason:** This evidence compares specific designs under a fixed display setup; if small multiples become too small to read, the expected advantage may not hold.

## The Price <!-- role: costs -->

- **The Sacrifice:** Uses more screen real estate to show many panels.
- **The Risk:** If panels are forced too small, users may struggle to read regions even if the technique is otherwise well-suited.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Packing too many small multiples without preserving legibility.
- **Why it fails:** The method relies on users being able to visually compare panels; illegible panels undermine clustering.

## How to Check <!-- role: check -->

- **Visual Sign:** Users zoom browser/page or lean in repeatedly to identify regions across panels.
- **The Test:** Ask users to do a cluster trial; if they report difficulty reading individual panels, panel size is likely too small for this rule to work.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of panels shown at once (e.g., paginate or show a subset of time steps).
- **Best Fix:** Keep small multiples for clustering but redesign layout to maintain readable region shapes while preserving side-by-side comparison.
