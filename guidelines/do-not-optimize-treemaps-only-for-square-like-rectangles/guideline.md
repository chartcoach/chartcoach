---
id: do-not-optimize-treemaps-only-for-square-like-rectangles
title: Do not optimize treemaps only for square-like rectangles when supporting area
  comparison
bibliography: references.bib
description: Perfectly square aspect ratios produced worse rectangular area judgment
  accuracy than some non-square ratios.
labels:
- chart:treemap
- task:compare
- visual:area
- impact:accuracy
- data:hierarchical
- audience:general
- complexity:advanced
---

## Avoid treating 1:1 rectangle aspect ratio as the sole perceptual optimum for treemap comparisons <!-- role: advice -->

When treemap reading depends on comparing areas, do not assume that pushing rectangles toward a 1:1 aspect ratio will improve comparison accuracy. Preserve enough variation that rectangles are not uniformly square if your goal is accurate area judgment.

## Why perfect squares can worsen area comparisons <!-- role: reason -->

Viewers may partly rely on 1D side-length comparisons as a proxy for 2D area; when both rectangles are squares, that heuristic can produce larger errors because side lengths provide less discriminating cues for area differences.

**Mechanism:** When rectangles share a square shape, length-based heuristics become ambiguous, increasing proportional area estimation error.

**Evidence:** Rectangular area judgment accuracy varied significantly by aspect ratio, and comparisons involving 1:1 aspect ratios showed the worst performance across both isolated-rectangle and treemap conditions in a crowdsourced study [@heerCrowdsourcingGraphicalPerception2010a].

**Notes:** This finding suggests aspect-ratio objectives in layout algorithms can have perceptual consequences beyond aesthetics.

## When this applies <!-- role: context -->

- **User Goal:** Compare magnitudes encoded by treemap rectangle areas.
- **Task:** Estimate proportional differences between two marked rectangles.
- **Data:** Hierarchical or grouped quantitative data shown as rectangles.
- **Chart Setting:** Treemap or cartogram-like layouts where aspect ratios are controllable by algorithm/design.
- **Audience:** General audiences performing quick visual judgments.
- **Success Criterion:** Lower error in area comparisons between selected items.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your primary objective is not area comparison (e.g., fitting labels or preserving stable layout under updates). **Why:** Other optimization targets may dominate perceptual comparison goals.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Allowing non-square rectangles can increase the presence of thin shapes that are harder to label or tap/click. **Risk:** Overcorrecting away from squares can create extreme aspect ratios that also degrade perception. **Mitigation:** Constrain aspect ratios to a moderate range rather than maximizing squareness.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using “more square is always better” as a blanket rule for treemap readability. **Why it fails:** The tested area-comparison task showed worst accuracy at 1:1 aspect ratio combinations.

## Quick tests <!-- role: check -->

**Failure Sign:** Users hesitate or disagree when comparing similarly square rectangles. **Quick Check:** Identify common comparisons in your treemap and check whether they are frequently between near-squares; if so, test variants. **Stronger Test:** Run a small proportional-judgment test across aspect-ratio regimes and compare log absolute error.

## What to do instead <!-- role: fix -->

- Constrain extreme aspect ratios without trying to force all rectangles to 1:1.
- If area comparison is critical, supplement area with direct labels for key nodes.
- Provide interaction that reveals exact values on hover/click to reduce reliance on area estimation.
- Reduce comparison demand by highlighting the compared rectangles and visually de-emphasizing others.
