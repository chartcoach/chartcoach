---
id: use-area-over-orientation-to-find-extrema-in-1d-sequences
title: Use Area (Size) Instead of Orientation to Find Extrema
bibliography: references.bib
description: For finding minima/maxima in 1D ordered sequences, encoding magnitude
  by area is more accurate than encoding by orientation.
labels:
- chart:glyph
- chart:strip
- task:find-extremum
- visual:area
- visual:orientation
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

When the task is to identify minima/maxima in a 1D sequence, encode the quantitative values with **area/size** rather than **orientation**.

## The Logic <!-- role: reason -->

Area/size provides a stronger cue for magnitude comparison than orientation in this sequence-based extremum task, improving accuracy.

- **The Principle:** Stronger magnitude encodings reduce errors in extremum detection.
- **The Evidence:** Area ranked above orientation for find-extremum accuracy in the extracted results [@chungHowOrderedIt2016], organized as reusable guidance [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Decide which item is smallest/largest in an ordered list/sequence.
- **Data Type:** Quantitative values; ordinal order on X.
- **Audience:** General audiences performing scan-and-pick tasks.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Size variation would cause unacceptable overlap or misalignment in your design.
- **Reason:** The result assumes a readable sequence of size-varying marks as in the evaluated design [@chungHowOrderedIt2016].

## The Price <!-- role: costs -->

- **The Sacrifice:** May reduce cleanliness of the layout (variable mark sizes).
- **The Risk:** Overplotting/occlusion can introduce new errors if spacing is tight.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Encoding magnitude solely via rotated line segments and expecting users to spot the extreme quickly.
- **Why it fails:** Orientation performed worse than size/area for find-extremum accuracy in the extracted ranking [@chungHowOrderedIt2016; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users confuse mid-values with extremes when angle/orientation varies.
- **The Test:** Replace orientation with area encoding and compare error rate on min/max questions.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Swap orientation encoding for size encoding.
- **Best Fix:** Use area/size encoding for the quantitative field in the extremum task scenario (the highest-ranked approach for accuracy in this dataset) [@chungHowOrderedIt2016; @zengReviewCollationGraphical2023].
