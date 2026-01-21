---
id: limit-mark-count-when-colors-are-random-for-target-search
title: Reduce the Number of Marks When Colors Are Random
bibliography: references.bib
description: For target-finding tasks, increasing mark count slows search time in
  randomly colored displays.
labels:
- chart:heatmap
- chart:waffle
- chart:scatter
- task:find-anomalies
- visual:color-hue
- impact:speed
- data:categorical
- audience:general
- design:density
---

## The Rule <!-- role: advice -->

If your color categories are randomly intermingled (not spatially grouped), keep mark counts low for target-finding tasks.

## The Logic <!-- role: reason -->

With random color placement, users’ search time increases as the number of marks increases, indicating increasingly costly search as displays get denser.

- **The Principle:** Higher set size increases search time when visual structure is ungrouped.
- **The Evidence:** In randomly colored grids, time worsened as set size rose (e.g., 36 → 196 marks ranked from fastest to slowest: E-1, E-2, E-3, E-4, E-5; with significant slowdowns for larger set sizes) [@gramazioRelationVisualizationSize2014]. This relationship is explicitly captured in the collation dataset for recommendation purposes [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Find a distinct target/anomaly quickly.
- **Data Type:** Many marks with nominal color-hue encoding; random (unstructured) color layout.
- **Audience:** Any audience performing rapid search.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your colors are spatially grouped.
- **Reason:** When colors are grouped, set size had little effect on search time in the tested grid setting [@gramazioRelationVisualizationSize2014], so reducing marks may be less critical for speed (though other goals may still apply) [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer marks may mean less detail (less complete display of all items).
- **The Risk:** Over-reduction can hide rare items or reduce the chance of spotting specific targets.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keep the same dense, random display and expect users to “just zoom” mentally.
- **Why it fails:** The measured time ranking shows systematic slowdowns as mark count increases under random layouts [@gramazioRelationVisualizationSize2014], and the collation encodes this as a performance-linked factor [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Dense, randomly colored marks fill the space with no clear regions.
- **The Test:** Duplicate the view at two densities (e.g., a smaller subset vs full set) and time a quick “find the target color” attempt; if the dense one is consistently slower, you’re hitting the set-size penalty.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Filter down to fewer marks for the current search task (e.g., subset, paginate, or show a representative slice).
- **Best Fix:** Combine mark reduction with layout restructuring so categories form spatial groups (eliminating the random-layout penalty) [@gramazioRelationVisualizationSize2014; @zengReviewCollationGraphical2023].
