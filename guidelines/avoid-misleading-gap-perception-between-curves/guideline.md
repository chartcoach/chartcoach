---
id: avoid-misleading-gap-perception-between-curves
title: "Do Not Rely on Perceived \u2018Gap\u2019 Between Lines for Differences"
bibliography: references.bib
description: Avoid designs where viewers infer differences from the apparent thickness
  of the space between curves.
labels:
- chart:line
- task:compare
- visual:position
- impact:accuracy
- data:temporal
- audience:novice
- complexity:intermediate
---

## The Rule <!-- role: advice -->

When showing differences between two series, do not rely on the viewer judging the “thickness” of the space between lines; make the difference explicit.

## The Logic <!-- role: reason -->

- **The Principle:** The visual system can misperceive the space between curves as an object with varying thickness, biasing difference judgments.
- **The Evidence:** Parallel curves can appear non-parallel, making equal vertical separations look larger in one region than another [@zacksDesigningGraphsDecisionMakers2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Comparing two trends or estimating their difference across x (often time).
- **Data Type:** Two series plotted as lines with vertical offset.
- **Audience:** Decision-makers who might act on perceived changes in “distance.”

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is to compare each line to a baseline independently, not to each other.
- **Reason:** The misleading cue is specifically about inferring inter-line differences from the intervening space [@zacksDesigningGraphsDecisionMakers2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional marks (difference band/series) may add visual elements.
- **The Risk:** Over-emphasis of differences if the added encoding is too salient.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding a translucent fill between lines and assuming it clarifies the difference.
- **Why it fails:** It can intensify the “object thickness” interpretation rather than correct it [@zacksDesigningGraphsDecisionMakers2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers report bigger differences where the lines “look farther apart,” even when the vertical difference is constant.
- **The Test:** Add equal-length vertical reference ticks at multiple x positions; if perceived differences disagree, the design is misleading.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a third series representing the difference (delta) directly.
- **Best Fix:** Re-encode the comparison as explicit deltas (a difference plot) so the comparison becomes a single perceptual read rather than an inferred gap [@zacksDesigningGraphsDecisionMakers2020].
