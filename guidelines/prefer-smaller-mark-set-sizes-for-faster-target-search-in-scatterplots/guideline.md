---
id: prefer-smaller-mark-set-sizes-for-faster-target-search-in-scatterplots
title: Prefer smaller mark set sizes for faster target search in scatterplots
bibliography: references.bib
description: In scatterplot-like displays, fewer plotted points yield faster target
  search times than more points.
labels:
- chart:scatter
- task:find-anomalies
- visual:position
- visual:color
- impact:speed
- data:categorical
- audience:practitioner
- complexity:basic
---

## Use fewer points in scatterplots to speed target search <!-- role: advice -->

Use fewer plotted points when the goal is to find a single target quickly in a scatterplot-like view. If you increase point count, plan for slower target search.

## Why fewer points speed target search in scatterplots <!-- role: reason -->

As the number of points increases, viewers must discriminate and scan more items, which increases time to locate a specific target.

**Mechanism:** Higher point density increases the search space and the number of potential distractors, raising response time.

**Evidence:** For scatterplot-like designs using position (x/y) plus color hue, the 196-point design was faster than the 484-point design for the recorded target-search task, with a statistically significant difference reported (ANOVA, threshold 0.001) [@gramazioRelationVisualizationSize2014; @zengReviewCollationGraphical2023]. The extracted ranking for time was 196 points faster than 484 points [@gramazioRelationVisualizationSize2014; @zengReviewCollationGraphical2023].

**Notes:** This guideline is about response time (speed), not accuracy.

## When this applies: target search in scatterplots <!-- role: context -->

- **User Goal:** Quickly locate a single target point.
- **Task:** Find anomalies (target detection / locating an odd item).
- **Data:** Points in 2D; nominal categories encoded by color hue; point set size is high (hundreds of marks).
- **Chart Setting:** Static scatterplot-like view using positionX/positionY plus color hue.
- **Audience:** Any; especially time-constrained viewers.
- **Success Criterion:** Faster completion time.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The analysis requires seeing the full point cloud at once to preserve context. **Why:** Reducing points can remove necessary context even if it improves speed.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Lower point counts can reduce completeness of what is shown. **Risk:** Viewers may miss patterns that only appear at full density. **Mitigation:** Align density reductions with the specific target-search goal rather than general exploration.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Increasing point count while keeping the same display space and expecting search time not to change. **Why it fails:** The recorded results show slower time at higher set size.

## Quick tests <!-- role: check -->

**Failure Sign:** Finding a single target point becomes noticeably slower as point count increases. **Quick Check:** Time a few representative searches at two point-count levels (e.g., hundreds vs. more hundreds) and compare median time. **Stronger Test:** Run a small benchmark study and compare completion-time distributions.

## What to do instead <!-- role: fix -->

- Filter to a smaller subset of points before asking users to locate a target.
- Partition the points into multiple smaller views (small multiples) so each view has fewer points.
- Provide a staged workflow where users narrow candidates first, then do target search on a reduced set.
- Offer an alternate view that lists candidates in a reduced set for confirmation after the initial search.
