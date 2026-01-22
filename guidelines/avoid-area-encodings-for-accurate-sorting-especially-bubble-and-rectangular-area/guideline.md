---
id: avoid-area-encodings-for-accurate-sorting-especially-bubble-and-rectangular-area
title: Avoid area encodings for accurate sorting, especially bubble and rectangular
  area marks
bibliography: references.bib
description: In sort judgments, area-based encodings (circles, rectangles, treemap-like
  blocks) performed worst relative to position, length, and angle.
labels:
- chart:treemap
- chart:bubble
- task:sort
- visual:area
- impact:accuracy
- data:quantitative
- audience:general
- source:graphical-perception
---

## Avoid area marks when the task is sorting values <!-- role: advice -->

Avoid encoding the values to be sorted using area marks (such as bubbles or sized rectangles) when accuracy is important. Use a non-area encoding for sorting whenever you have a choice.

## Why area harms sorting accuracy <!-- role: reason -->

Area judgments are less precise for comparing magnitudes, so sorting decisions based on area require noisier perceptual estimation than alternatives.

**Mechanism:** Viewers must mentally translate a 2D extent into magnitude, which introduces more error than encodings that align values to a 1D reference for comparison.

**Evidence:** In a sort (proportional judgment) task, the area-based designs (including circle area, rectangle area, and a treemap-like rectangle condition) ranked at the bottom of accuracy, and multiple significant pairwise comparisons favored non-area designs over the area-circle condition [@heerCrowdsourcingGraphicalPerception2010]. These performance rankings are preserved as structured, reusable guidance for visualization recommendation [@zengReviewCollationGraphical2023].

**Notes:** This guideline is specifically about sorting/ordering accuracy, not about memorability or aesthetics.

## When this applies to your chart choice <!-- role: context -->

- **User Goal:** Decide which of two values is larger or sort values by magnitude.
- **Task:** Sort.
- **Data:** Quantitative values presented as mark sizes.
- **Chart Setting:** Static displays where users visually compare sizes.
- **Audience:** General audiences.
- **Success Criterion:** Accurate ordering judgments.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The primary goal is to show part-to-whole composition or space-filling layout constraints require area (for example, treemap-like packing). **Why:** The chart form may be required for structural reasons even if it is not optimal for sorting.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Switching away from area may reduce compactness or the ability to show nested containment in a single view. **Risk:** If you keep area for a sorting task, viewers may make systematically less accurate ordering decisions. **Mitigation:** If area is unavoidable, provide numeric labels for the values being compared.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using bubble size or treemap rectangle size to ask users to rank values. **Why it fails:** Area perception is comparatively imprecise for ordering, leading to avoidable accuracy loss.

## Quick tests <!-- role: check -->

**Failure Sign:** People disagree on the ordering of two similarly sized bubbles/blocks. **Quick Check:** If two values are close, ask a colleague to sort them by eye; if they struggle, area is a poor choice. **Stronger Test:** Compare error rates on the same sorting prompt using a position-based alternative.

## What to do instead <!-- role: fix -->

- Use position on a shared axis to encode the values that must be sorted.
- Use length with a common baseline instead of area when you need a compact comparison.
- If you must use area, directly label the marks with the values used for sorting.
- Provide an alternate sortable view (such as a small aligned bar chart) alongside the area-based display.
