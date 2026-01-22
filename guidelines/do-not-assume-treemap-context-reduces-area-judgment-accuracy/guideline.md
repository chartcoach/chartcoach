---
id: do-not-assume-treemap-context-reduces-area-judgment-accuracy
title: Do not assume treemap context reduces marked-rectangle area judgment accuracy
bibliography: references.bib
description: Additional surrounding rectangles in a treemap did not significantly
  interfere with proportional judgments of marked rectangles.
labels:
- chart:treemap
- task:compare
- visual:area
- impact:clarity
- data:hierarchical
- audience:general
- complexity:intermediate
---

## Treat surrounding treemap rectangles as non-interfering for simple marked-pair area judgments <!-- role: advice -->

When asking viewers to compare two clearly marked rectangles, do not assume that the presence of other treemap rectangles will significantly reduce accuracy. Focus on clear marking and consistent sizing rather than removing context solely to prevent interference.

## Why treemap context may not impair simple pairwise comparisons <!-- role: reason -->

For a task constrained to two marked targets, additional non-target elements may not meaningfully compete for attention or distort the pairwise area estimation process.

**Mechanism:** Strong target marking can localize attention, reducing interference from other marks in the display.

**Evidence:** No significant difference was found between a two-rectangle display and a treemap display for proportional judgments of the same marked rectangles (matched in size and aspect ratio), indicating surrounding rectangles did not measurably impair accuracy in that setup [@heerCrowdsourcingGraphicalPerception2010a].

**Notes:** This evidence pertains to marked pairwise comparison, not to search-heavy tasks like “find the largest leaf.”

## When this applies <!-- role: context -->

- **User Goal:** Compare two known items’ magnitudes in a treemap.
- **Task:** Pairwise proportional judgment between two marked rectangles.
- **Data:** Many rectangles exist, but the compared pair is explicitly highlighted.
- **Chart Setting:** Treemap with clear annotation/marking for the compared items.
- **Audience:** General audiences performing quick judgments.
- **Success Criterion:** Comparable accuracy with or without surrounding rectangles.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The viewer must first locate the items to compare (visual search) rather than being shown the pair. **Why:** Interference can arise from search and selection demands not tested by marked-pair judgments.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Keeping full context may increase overall visual complexity. **Risk:** If marking is weak, attention may diffuse and accuracy may fall even if context itself is not the driver. **Mitigation:** Ensure markings are salient and unambiguous.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Removing most rectangles to “simplify” the display when the real issue is unclear target marking. **Why it fails:** The tested results suggest context alone is not the main accuracy limiter for marked-pair judgments.

## Quick tests <!-- role: check -->

**Failure Sign:** Users misidentify which two rectangles are being compared. **Quick Check:** Ask users to point out the two targets before estimating; if they struggle, fix marking first. **Stronger Test:** Compare proportional-judgment error with and without surrounding rectangles while keeping target rectangles identical.

## What to do instead <!-- role: fix -->

- Increase target marking salience (e.g., outline, label, or highlight) for the compared rectangles.
- Reduce non-target prominence (e.g., lower contrast) while keeping them present for context.
- Provide direct value labels for the compared rectangles if precision is required.
- Use interaction to isolate the compared pair without permanently removing the rest of the treemap.
