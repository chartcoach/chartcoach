---
id: use-area-over-shape-for-find-extremum-accuracy-in-ordered-sequences
title: Use area instead of shape to improve extrema-finding accuracy in an ordered
  sequence
bibliography: references.bib
description: For identifying minima or maxima in an ordered sequence, area encoding
  can be more accurate than shape encoding.
labels:
- chart:strip
- task:find-extremum
- visual:area
- visual:shape
- impact:accuracy
- data:quantitative
- complexity:advanced
---

## Prefer area over shape for finding minima or maxima in sequences <!-- role: advice -->

Use area (varying mark size) rather than shape (varying form) to encode quantitative magnitude when users need to find the minimum or maximum in an ordered sequence.

## Why area can outperform shape for extrema finding here <!-- role: reason -->

This rule works because area variation supports scanning for the largest/smallest mark in a single consistent dimension, while shape variation can require extra interpretation before magnitude comparisons are made.

**Mechanism:** A “bigger vs smaller” cue aligns directly with extremum search, reducing ambiguity when selecting the most extreme mark.

**Evidence:** In find-extremum tasks on ordered sequences, the area-encoded design ranked highest in accuracy and was reported as significantly more accurate than the shape-encoded design in the pairwise significance results [@chungHowOrderedIt2016; @zengReviewCollationGraphical2023].

**Notes:** This evidence is specific to the tested mark/encoding construction (area-circle for area; point marks for shape).

## When to apply area over shape for extrema finding <!-- role: context -->

- **User Goal:** Pick the smallest or largest element in a sequence quickly and correctly.
- **Task:** Find Extremum.
- **Data:** Quantitative values laid out in an ordinal sequence (left-to-right order).
- **Chart Setting:** Static sequence of individual marks where only one channel carries magnitude.
- **Audience:** General audiences.
- **Success Criterion:** Higher accuracy for selecting min/max.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Mark overlap or very dense sequences make size differences hard to see. **Why:** Area comparisons can become unreliable if marks occlude each other or size differences are visually crowded.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Larger marks can consume more space and increase clutter. **Risk:** If area is used for magnitude, it may conflict with using size for emphasizing importance or uncertainty elsewhere. **Mitigation:** Keep the encoding purpose singular within the view and avoid overloading size.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Encoding magnitude with complex shape changes that require counting or interpretation during an extrema search. **Why it fails:** Shape can slow interpretation and reduce extrema-finding accuracy relative to a direct size cue.

## Quick tests <!-- role: check -->

**Failure Sign:** Users misidentify the largest/smallest mark even when they understand the legend.\
**Quick Check:** Squint test: if the largest mark does not visually “pop” immediately, area differences may be too subtle or too cluttered.\
**Stronger Test:** Compare min/max selection accuracy on the same data using area vs shape.

## What to do instead <!-- role: fix -->

- Encode magnitude with area (mark size) for extrema tasks in ordered sequences.
- Increase spacing or reduce the number of marks so size differences remain easy to compare.
- If size cannot vary, switch to another encoding that outperforms hue for extrema finding in this setting (e.g., texture or saturation).
