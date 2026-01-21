---
id: avoid-too-small-marks-for-target-search
title: Increase Mark Size to Avoid Slow Target Search
bibliography: references.bib
description: Very small marks slow down target finding; increasing mark size improves
  search time up to a plateau.
labels:
- chart:scatter
- chart:heatmap
- chart:waffle
- task:find-anomalies
- visual:size
- visual:color-hue
- impact:speed
- data:categorical
- audience:general
---

## The Rule <!-- role: advice -->

Do not use the smallest mark sizes for target-search tasks; increase mark size until performance improvements level off.

## The Logic <!-- role: reason -->

Small marks are harder to visually parse and discriminate during search; enlarging marks reduces search time, but benefits eventually plateau.

- **The Principle:** Mark size affects visual search efficiency with diminishing returns.
- **The Evidence:** Across both grid and scatterplot search experiments, the smallest mark sizes produced the slowest response times, and increasing mark size reduced times until improvements plateaued [@gramazioRelationVisualizationSize2014]. This is represented in the review’s collation as design guidance tied to search performance [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Quickly spot a unique target/anomaly among many marks.
- **Data Type:** Dense mark displays with categorical colors (nominal color-hue) and many items.
- **Audience:** Any audience where speed matters (e.g., rapid scanning).

## When to Break It <!-- role: exceptions -->

- **Scenario:** The primary goal is to preserve high data density (showing many marks) and target search is not the main task.
- **Reason:** Larger marks consume space and can reduce how much can be shown at once; the paper’s evidence is specifically about target search time, not other tasks [@gramazioRelationVisualizationSize2014; @zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** Larger marks reduce maximum achievable density in a fixed area.
- **The Risk:** Overly large marks can obscure nearby marks or create overlap/occlusion in dense plots.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keep tiny marks and rely only on color to make the target “pop.”
- **Why it fails:** Even with the same color encoding, the smallest mark sizes were slowest in measured search time [@gramazioRelationVisualizationSize2014], and the collation treats size as a first-class factor affecting performance [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Marks look like fine noise; individual marks are difficult to separate at a glance.
- **The Test:** Step back (or zoom out) to a typical viewing distance and try to immediately locate the target; if you need to lean in or scan slowly, marks are likely too small.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase mark size one step and retest search time.
- **Best Fix:** Increase mark size and, if space becomes an issue, pair it with either stronger grouping or fewer marks (since both were shown to affect search time) [@gramazioRelationVisualizationSize2014; @zengReviewCollationGraphical2023].
