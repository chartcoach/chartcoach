---
id: do-not-equate-monotonicity-with-intrinsic-order-in-color
title: Do Not Equate Monotonicity with Intrinsic Order in Color
bibliography: references.bib
description: Monotonic change in hue or saturation does not guarantee intrinsic perceptual
  order.
labels:
- chart:general
- task:interpret-order
- visual:color
- impact:correctness
- data:ordinal
- audience:general
- source:theory
---

## The Rule <!-- role: advice -->

Do not treat monotonic change in a single color attribute (hue or saturation) as proof that the colormap is intrinsically ordered.

## The Logic <!-- role: reason -->

The paper explicitly proves that monotonicity in one attribute (hue, saturation, or luminance) is **not sufficient** to guarantee local or global **intrinsic** order, providing theoretical counterexamples [@bujackOrderingPerceptionsPerceptual2018]. The collation paper frames such findings as critical for turning perception knowledge into enforceable recommendation rules rather than informal assumptions [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Making viewers correctly perceive the ordering of values from the marks themselves.
- **Data Type:** Ordered values encoded via color (especially **color-hue** or **color-saturation** ramps).
- **Audience:** Any audience; especially relevant when viewers may not consult a legend.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your requirement is strictly legend-based order (not intrinsic order).
- **Reason:** The paper shows strict monotonicity is sufficient for legend-based order under its formalization, which is a different target than intrinsic order [@bujackOrderingPerceptionsPerceptual2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need additional checks or alternative encodings instead of relying on a simple monotonicity heuristic.
- **The Risk:** Adding constraints (e.g., requiring intrinsic order) can reduce the space of permissible palettes in automated recommendation.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using “monotonic in hue” or “monotonic in saturation” as the sole automated criterion for “ordered colormap.”
- **Why it fails:** The paper’s theoretical results show monotonicity can still violate intrinsic order (triangle-distance difference condition) [@bujackOrderingPerceptionsPerceptual2018], motivating richer rule representations as discussed in [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** The palette “looks like it goes up then down” in perceived strength, or creates ambiguous midpoints.
- **The Test:** Pick three well-spaced samples from the map; if observers cannot reliably identify the middle sample by appearance alone, treat intrinsic order as unverified per the paper’s intrinsic-order framing [@bujackOrderingPerceptionsPerceptual2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Clarify that the legend defines order (make legend-based reading the intended interaction).
- **Best Fix:** Replace the assumption “monotonicity ⇒ intrinsic order” with a more explicit design constraint in your recommendation/validation pipeline, consistent with the knowledge-to-constraints goal described in [@zengReviewCollationGraphical2023].
