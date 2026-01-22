---
id: prefer-smaller-mark-set-sizes-for-faster-target-search-in-grids
title: Prefer smaller mark set sizes for faster target search in colored grids
bibliography: references.bib
description: In colored grid displays, smaller numbers of marks yield faster target
  search times than larger numbers of marks.
labels:
- chart:heatmap
- task:find-anomalies
- visual:position
- visual:color
- impact:speed
- data:categorical
- audience:practitioner
- complexity:basic
---

## Use fewer marks in colored grids to speed target search <!-- role: advice -->

Use fewer marks (lower set size) when you need faster target search in colored grid-like displays. If you must show more marks, expect slower search.

## Why fewer marks speed target search in grids <!-- role: reason -->

Increasing the number of visual items increases the amount of visual material a viewer must scan, which tends to slow time-to-find for a specific target in a dense display.

**Mechanism:** More marks increase visual scanning demands, which increases response time for locating a target.

**Evidence:** In grid-style designs using position (x/y) plus color hue, a 36-mark design was faster than 100/144/196-mark designs, and a 64-mark design was faster than 144/196-mark designs for the recorded target-search task, with statistically significant pairwise differences reported (ANOVA, threshold 0.001) [@gramazioRelationVisualizationSize2014; @zengReviewCollationGraphical2023]. The recorded ranking for time was monotonic from 36 to 196 marks (36 fastest → 196 slowest) [@gramazioRelationVisualizationSize2014; @zengReviewCollationGraphical2023].

**Notes:** This guideline is about response time (speed), not accuracy.

## When this applies: target search in colored grids <!-- role: context -->

- **User Goal:** Quickly locate a single target item in a grid-like view.
- **Task:** Find anomalies (target detection / locating an odd item).
- **Data:** Many marks; marks positioned on a 2D plane; categories encoded by color hue (nominal).
- **Chart Setting:** Static grid-like display with rectangular marks (cell-like) using positionX/positionY plus color hue.
- **Audience:** Any; especially time-constrained viewers.
- **Success Criterion:** Faster completion time.

## When not to follow it <!-- role: exceptions -->

**Break it when:** You cannot reduce the number of marks without losing required data coverage for the user’s decision. **Why:** The display must include all items even if search becomes slower.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may show less information at once if you reduce set size. **Risk:** Over-reducing marks can hide items the viewer needs to verify. **Mitigation:** Treat speed as the optimization target only when time-to-find is the priority.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Increasing mark count to “show everything” while expecting target search time to stay the same. **Why it fails:** The measured time increases as set size increases in the ranked results.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers report that the view feels slower to scan as you add marks. **Quick Check:** Compare time-to-find on a small internal trial between a low set size and a high set size version. **Stronger Test:** Run an A/B timing test with representative users and measure median completion time.

## What to do instead <!-- role: fix -->

- Reduce the number of marks shown at once by filtering to the subset relevant to the target search.
- Split the display into multiple smaller panels so each panel has fewer marks to scan.
- Provide multiple views at different densities so users can choose the faster-to-scan option for target search.
- Replace the single dense grid view with a workflow that lets users iteratively narrow candidates before searching.
