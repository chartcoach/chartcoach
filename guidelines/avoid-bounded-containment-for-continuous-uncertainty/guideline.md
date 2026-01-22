---
id: avoid-bounded-containment-for-continuous-uncertainty
title: Avoid bounded containment shapes for continuous uncertainty distributions
bibliography: references.bib
description: Boundaries in uncertainty displays can cause viewers to treat continuous
  uncertainty as categorical containment.
labels:
- chart:map
- task:judge-uncertainty
- visual:boundary
- impact:interpretability
- data:uncertainty
- audience:novice
- bias:containment
---

## Represent uncertainty without hard boundaries when the data are continuous <!-- role: advice -->

When uncertainty is continuous, use a boundary-free representation rather than a crisp enclosed region. If you must show a region, make it clear that it reflects a probabilistic distribution rather than a contained area.

## Boundaries prompt a containment heuristic that distorts judgments <!-- role: reason -->

Enclosed shapes encourage viewers to treat everything inside as meaningfully similar and everything outside as categorically different, even when the underlying variable changes smoothly. This can shift judgments toward “within-the-boundary” reasoning rather than distributional reasoning.

**Mechanism:** Visual boundaries create perceptual grouping and categorical inference, which can override intended probabilistic interpretation.

**Evidence:** For location and geospatial uncertainty, bounded circular overlays increase reliance on a containment heuristic compared to boundary-free uncertainty depictions (e.g., graded fades), changing accuracy judgments and interpretations [@padillaDecisionMakingVisualizations2018]. Boundary salience in hurricane forecast cones is associated with systematic misinterpretations of what the display represents [@padillaDecisionMakingVisualizations2018].

**Notes:** These effects can persist even when viewers are given explanatory keys, indicating the bias can be hard to override.

## Where this applies <!-- role: context -->

- **User Goal:** Interpret uncertainty about where/when an event will occur or where a user is located.
- **Task:** Compare likelihood across locations; decide which locations are at higher risk.
- **Data:** Continuous spatial uncertainty (distributions, ensembles, positional uncertainty).
- **Chart Setting:** Static maps and forecast graphics.
- **Audience:** Public audiences and non-experts; also relevant for experts when time is limited.
- **Success Criterion:** Viewers reason about likelihood gradients rather than “in/out” categories.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The phenomenon is genuinely categorical (e.g., a strict zone definition) and the intended inference is in/out membership. **Why:** A boundary accurately encodes the underlying semantics.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Boundary-free uncertainty can be harder to label precisely and may feel less decisive. **Risk:** Some viewers may struggle to extract exact thresholds without contours. **Mitigation:** Pair boundary-free uncertainty with explicit numeric cues or annotated reference levels.

## Common mistakes <!-- role: mistakes -->

- **Mistake:** Using a single crisp contour to summarize a probability distribution without clarifying what it means. **Why it fails:** Viewers interpret it as a literal extent or category boundary.
- **Mistake:** Making the boundary the most salient element of the display. **Why it fails:** Attention locks to the boundary, reinforcing containment reasoning.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers answer questions using “inside the circle/cone” as the primary reasoning step. **Quick Check:** Ask a viewer whether two points just inside and just outside the boundary are “very different”; if yes, the display is inducing categorical reasoning. **Stronger Test:** Compare decisions made with a bounded versus boundary-free version under short viewing time.

## Fixes <!-- role: fix -->

- Use a graded, boundary-free depiction (e.g., a continuous fade) to communicate uncertainty magnitude.
- If summarizing with regions, show multiple levels (not a single cutoff) and label them as probabilistic.
- Add explicit wording near the graphic that the uncertainty is a distribution, not a physical boundary.
- Provide a complementary depiction (e.g., representative samples/paths) that makes the distributional nature perceptually clear.
