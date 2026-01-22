---
id: cluster-visually-similar-encodings-and-show-only-the-top-exemplar-in-the-main-gallery
title: Cluster visually similar encodings and show only the top exemplar in the main
  gallery
bibliography: references.bib
description: Avoid exhaustive enumeration by grouping near-duplicate charts and presenting
  one best representative by default.
labels:
- chart:gallery
- task:browse
- visual:layout
- impact:scannability
- data:tabular
- audience:novice
- system:recommendation
---

## Collapse near-duplicate chart designs into clusters and display a single representative <!-- role: advice -->

Group encodings that are visually similar (for example, simple axis swaps or alternative retinal channels) and show only the highest-ranked chart per cluster in the default gallery.

## Clustering preserves diversity while controlling combinatorial explosion <!-- role: reason -->

Enumerating all encoding permutations produces too many charts to scan, many of which differ only slightly. Clustering removes redundant designs, allowing the gallery to emphasize differences that matter while still preserving access to alternatives when needed.

**Mechanism:** Reducing redundancy increases the effective information density of the gallery without increasing cognitive load.

**Evidence:** The recommendation engine groups encoding candidates into channel-based clusters and recommends only the most effective view per cluster to avoid exhaustive enumeration in the main gallery, while enabling drill-down to see alternatives [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

**Notes:** Clustering is complementary to ranking; it prevents many similar high-scoring variants from crowding out others.

## When the generator can produce many variants for the same variable set <!-- role: context -->

- **User Goal:** Scan a manageable number of recommended charts.
- **Task:** Browsing and comparing many candidate views.
- **Data:** Variable sets that admit multiple valid encodings and mark types.
- **Chart Setting:** Multi-view gallery with limited screen space per chart.
- **Audience:** Users who want quick variety without being overwhelmed.
- **Success Criterion:** The gallery shows clearly distinct views rather than many trivial variants.

## When not to hide encoding variants behind clustering <!-- role: exceptions -->

**Break it when:** The user is explicitly exploring encoding alternatives for the same data (for example, after selecting an “expand” action). **Why:** At that point, the redundant variants are the point of the task [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Tradeoffs of clustering similar encodings <!-- role: costs -->

**Sacrifice:** Some potentially preferred encodings are not immediately visible. **Risk:** Users may assume the shown exemplar is the only available design. **Mitigation:** Provide a clear interaction to reveal the cluster’s alternatives (for example, an expanded gallery) [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Common clustering mistakes <!-- role: mistakes -->

**Mistake:** Treating axis swaps and minor retinal changes as fully distinct recommendations in the main gallery. **Why it fails:** The gallery becomes repetitive and harder to scan quickly [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## Quick checks for redundancy control <!-- role: check -->

**Failure Sign:** Many adjacent recommendations differ only by transposition or swapping color/shape. **Quick Check:** For each data table (variable set + transformations), count how many charts appear in the main gallery; it should be one. **Stronger Test:** Measure how many unique data tables are represented in the first N gallery slots; clustering should increase this count [@wongsuphasawatVoyagerExploratoryAnalysis2016a].

## What to do if users still want more design choice upfront <!-- role: fix -->

- Add a per-view “expand” affordance that reveals alternative encodings for the same data.
- Provide a sidebar of thumbnails in expanded mode to browse clustered alternatives quickly.
- Keep the main gallery exemplar-only, but allow users to pin or bookmark an alternative encoding once discovered [@wongsuphasawatVoyagerExploratoryAnalysis2016a].
