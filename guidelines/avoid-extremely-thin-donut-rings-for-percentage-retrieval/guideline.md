---
id: avoid-extremely-thin-donut-rings-for-percentage-retrieval
title: Avoid extremely thin donut rings when readers must retrieve a percentage value
bibliography: references.bib
description: Very thin donut rings were less accurate than thicker donut/pie variants
  for reading percentages.
labels:
- chart:donut
- task:retrieve-value
- visual:angle
- visual:area
- impact:accuracy
- data:quantitative
- audience:general
- parameter:inner-radius
---

## Keep donut rings thick enough for percent readout accuracy <!-- role: advice -->

Avoid donut designs that reduce the ring to an extremely thin outline when the viewer must estimate or report the percentage value.

## Extremely thin rings reduce usable cues for estimating proportion <!-- role: reason -->

As the donut becomes an outline, the filled area cue collapses and the remaining cue behaves more like a pure arc-length depiction, which showed worse accuracy than standard pie/donut wedges.

**Mechanism:** Thinning the mark removes or weakens redundant cues (notably filled area), increasing estimation error for a single percent readout.

**Evidence:** In an accuracy ranking over inner-radius variants for percentage retrieval, the very thin ring (inner radius near the outer radius; recorded as the arc-length-like condition) ranked worst among the tested radii, and was significantly worse than at least some thicker variants. [@skauArcsAnglesAreas2016; @zengReviewCollationGraphical2023]

**Notes:** The evidence here is specific to varying the donut inner radius while holding the part-to-whole task constant.

## Where this applies: donut inner-radius choices for part-to-whole readout <!-- role: context -->

- **User Goal:** Retrieve a percentage value from a donut-like mark.
- **Task:** Retrieve value.
- **Data:** One quantitative portion highlighted against the remainder.
- **Chart Setting:** Static donut chart where inner radius is a design parameter.
- **Audience:** General audiences.
- **Success Criterion:** Lower estimation error for the percent value.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The donut is purely decorative and the percentage is provided as text, so the ring is not used for estimation. **Why:** The risk (lower readout accuracy) is irrelevant if the value is not read from the shape.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Thicker rings reduce available whitespace in the center for labels. **Risk:** Designers may over-correct by making rings so thick they resemble solid pies and lose desired styling. **Mitigation:** Treat ring thickness as a readability parameter and validate with a quick viewer check.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Collapsing a donut into a near-outline ring while still expecting reliable percentage estimation. **Why it fails:** The thinnest tested donut variant produced the worst accuracy ranking for percent retrieval compared to thicker variants. [@skauArcsAnglesAreas2016; @zengReviewCollationGraphical2023]

## Quick tests <!-- role: check -->

**Failure Sign:** Small differences in percentage produce indistinguishable-looking ring segments to casual viewers. **Quick Check:** Print or screenshot the donut at its intended size and ask someone to estimate the highlighted percent; if guesses drift widely, the ring is too thin. **Stronger Test:** Compare absolute error between the current thin-ring design and a thicker ring on the same values.

## What to do instead <!-- role: fix -->

- Increase the donut ring thickness so the highlighted segment is a visibly filled wedge rather than a near-outline.
- If the center label is the reason for thinning, keep the ring moderately thick and move secondary annotations outside the ring.
- If minimalism is required, switch from an extremely thin donut to a standard donut or pie for the percent-readout view.
