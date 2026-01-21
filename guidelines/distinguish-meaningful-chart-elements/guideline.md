---
id: distinguish-meaningful-chart-elements
title: Separate Meaningful Chart Elements So They Are Distinguishable
bibliography: references.bib
description: "Ensure primary marks and all text remain visually separable\u2014never\
  \ obscured or merged\u2014so users can reliably distinguish chart elements."
labels:
- chart:general
- task:read
- visual:separation
- impact:accessibility
- data:general
- audience:general
- source:chartability
---

## The Rule <!-- role: advice -->

Ensure meaningful chart elements are visually distinguishable: do not let primary marks or any text be obscured or overlapped, and add at least 1px of white space between adjacent elements that touch (e.g., stacked bars, pie slices) when separability is required to understand the chart [@elavskyHowAccessibleMy2022].

## The Logic <!-- role: reason -->

Distinguishability is about whether users can perceptually separate foreground elements from each other and from their background; if elements visually merge or are hidden, users cannot reliably identify what is present or compare parts of the chart, even if colors are technically different [@w3c_understanding_distinguishable]. This is treated as a broader perceptual requirement than contrast alone, and is operationalized in Chartability as ensuring marks and text remain separable and unobscured [@elavskyHowAccessibleMy2022; @observablehq_contrast_and].

## Where to Apply <!-- role: context -->

This advice applies when the chart’s message depends on users being able to tell adjacent or overlapping elements apart.

- **User Goal:** Identify which mark is which, and interpret parts without confusion (e.g., separating segments in stacked bars or pie slices) [@elavskyHowAccessibleMy2022].
- **Data Type:** Any chart where marks are adjacent, touching, or potentially overlapping (e.g., stacked charts, pies, dense plots with overlapping marks) [@observablehq_contrast_and].
- **Audience:** Anyone relying on visual perception to parse the chart, including users who need stronger separability cues to identify elements [@w3c_understanding_distinguishable; @elavskyHowAccessibleMy2022].

## When to Break It <!-- role: exceptions -->

- **Scenario:** Marks touch or overlap, but discriminability/separability is not required to understand the chart’s purpose (e.g., the touching does not affect interpretation).
- **Reason:** This guideline is only a failure when separability is required for understanding, as specified in Chartability [@elavskyHowAccessibleMy2022].

## The Price <!-- role: costs -->

- **The Sacrifice:** Adding white space or preventing overlap can reduce the amount of information shown in the same area.
- **The Risk:** If spacing is added without care, the chart may look less compact and may require more room for the same data [@elavskyHowAccessibleMy2022].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Assuming contrast alone solves separability, while leaving adjacent elements touching or leaving text overlapped by marks.
- **Why it fails:** Users may still perceive merged shapes or obscured labels, so elements remain indistinguishable despite “passing” a contrast check [@w3c_understanding_distinguishable; @elavskyHowAccessibleMy2022].
- **The Wrong Fix:** Allowing labels or annotations to sit on top of marks such that either the text or the mark is partially hidden.
- **Why it fails:** Chartability flags any text being obscured or overlapped as a failure [@elavskyHowAccessibleMy2022].

## How to Check <!-- role: check -->

- **Visual Sign:** Adjacent segments (e.g., pie slices or stacked bars) visually merge with no separating gap, or any text overlaps with marks/other text so parts are hidden.
- **The Test:** Inspect the visualization for touching boundaries and overlaps; confirm there is at least 1px white space between adjacent elements that touch, and confirm no text is obscured by any other element [@elavskyHowAccessibleMy2022].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add at least 1px of white space between adjacent touching elements and remove any text overlaps by repositioning labels so they are unobscured [@elavskyHowAccessibleMy2022].
- **Best Fix:** Redesign the mark styling so elements remain separable under typical viewing (e.g., introduce spacing specifically to prevent touching/merging and ensure all text remains unobstructed), using distinguishability-focused techniques as demonstrated for chart elements that must be separated to be readable [@observablehq_contrast_and; @w3c_understanding_distinguishable; @elavskyHowAccessibleMy2022].
