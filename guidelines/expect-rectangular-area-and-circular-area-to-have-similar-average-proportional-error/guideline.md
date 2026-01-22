---
id: expect-rectangular-area-and-circular-area-to-have-similar-average-proportional-error
title: Treat rectangular and circular area encodings as similarly accurate on average
  for proportional judgments
bibliography: references.bib
description: Rectangular area judgments matched circular area judgments on average
  in proportional estimation tasks.
labels:
- chart:treemap
- task:estimate
- visual:area
- impact:accuracy
- data:quantitative
- audience:general
- complexity:intermediate
---

## Expect similar average accuracy for rectangular and circular area comparisons <!-- role: advice -->

If you must encode quantitative values by area, expect rectangular and circular marks to yield similar average proportional-judgment accuracy. Choose between them based on layout needs rather than expecting one to be inherently more accurate.

## Why shape family (rectangle vs circle) is not the main driver on average <!-- role: reason -->

For proportional estimation by area, error is dominated by the general difficulty of mapping 2D area to number rather than by whether the mark boundary is circular or rectangular.

**Mechanism:** Both circles and rectangles require viewers to infer area magnitude, which is a noisier perceptual channel for quantitative decoding than position.

**Evidence:** In crowdsourced proportional-judgment experiments, rectangular area judgments (including isolated rectangles and treemap rectangles) matched circular area judgments on average, using the same log absolute error metric and comparable task format [@heerCrowdsourcingGraphicalPerception2010a].

**Notes:** Aspect ratio effects can still meaningfully change accuracy within rectangular encodings.

## When this applies <!-- role: context -->

- **User Goal:** Estimate one value as a percentage of another using area marks.
- **Task:** Proportional judgment between two highlighted areas.
- **Data:** Quantitative values displayed as bubbles/circles or rectangles (including treemap/cartogram-like marks).
- **Chart Setting:** Choosing a mark shape within an area-based design.
- **Audience:** General audiences; unknown devices/displays.
- **Success Criterion:** Comparable average estimation accuracy between shape choices.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your task depends on comparing lengths or positions rather than areas. **Why:** This guideline is specific to proportional judgments using area as the encoding.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Area-based encodings generally trade accuracy for compactness or part-to-whole layout benefits. **Risk:** Assuming “similar” means “good enough” can lead to avoidable misreads for precise comparisons. **Mitigation:** Provide labels for key values or enable interaction to reveal exact numbers.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Switching from circles to rectangles (or vice versa) expecting a large accuracy gain for proportional comparisons. **Why it fails:** Average proportional-judgment accuracy did not materially differ between the two in the tested conditions.

## Quick tests <!-- role: check -->

**Failure Sign:** Readers disagree widely on percentage estimates from area marks. **Quick Check:** Ask a few users to estimate the same ratio from both shapes; if errors are similar, prioritize layout constraints. **Stronger Test:** Run a small proportional-judgment evaluation using log absolute error to compare design variants.

## What to do instead <!-- role: fix -->

- Use position on a common scale when accurate proportional decoding is required.
- If area is required, label the most important marks and ratios directly.
- Reduce the number of comparisons the viewer must make from area alone by highlighting only a few marks at once.
- Consider adding reference cues (e.g., bounding boxes or guides) to support estimation when exact reading matters.
