---
id: cluster-visually-similar-encodings-and-show-one-exemplar-in-the-main-gallery
title: Cluster Similar Encodings and Show One Exemplar
bibliography: references.bib
description: Prevent exhaustive enumeration by grouping near-duplicate designs and
  surfacing only the top-ranked representative.
labels:
- chart:gallery
- task:explore
- visual:encoding
- impact:scannability
- data:multivariate
- audience:analyst
- system:recommendation
---

## The Rule <!-- role: advice -->

Cluster encoding variants that are visually similar, and show only the highest-ranked exemplar per cluster in the main gallery.

## The Logic <!-- role: reason -->

A recommendation space explodes combinatorially across permutations of channels and mark types. Voyager’s Compass clusters similar encodings (e.g., swaps of x/y, color vs shape variants) to avoid flooding the gallery and to keep browsing cognitively manageable [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

- **The Principle:** Managing combinatorial explosion via clustering and pruning
- **The Evidence:** [@wongsuphasawatVoyagerExploratoryAnalysis2016a]

## Where to Apply <!-- role: context -->

- **User Goal:** Scan many meaningful alternatives quickly
- **Data Type:** Same underlying data table admits multiple reasonable encodings
- **Audience:** Analysts browsing thumbnails

## When to Break It <!-- role: exceptions -->

- **Scenario:** The goal is explicitly to compare alternative encodings (a “design gallery” task).
- **Reason:** Then you want design variation front-and-center rather than collapsed.

## The Price <!-- role: costs -->

- **The Sacrifice:** Users may not realize an omitted variant exists unless they drill down.
- **The Risk:** A suboptimal exemplar could hide a better niche encoding if the ranking is imperfect.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing every permutation of mark types and channel assignments.
- **Why it fails:** It overwhelms users and violates Voyager’s preference for fine-tuning over exhaustive enumeration [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** The gallery contains many near-duplicates that differ only by swapped axes or minor retinal channels.
- **The Test:** If removing every other view doesn’t reduce informational content, you need clustering.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Define channel groups (position, facets, detail, retinal measures) and cluster by these similarities; keep only the top-ranked per cluster.
- **Best Fix:** Provide an “expanded” drill-down that reveals the full set of clustered alternatives for the selected data table [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
