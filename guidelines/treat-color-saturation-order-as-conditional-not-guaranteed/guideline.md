---
id: treat-color-saturation-order-as-conditional-not-guaranteed
title: Treat Color Saturation Order as Conditional, Not Guaranteed
bibliography: references.bib
description: Do not assume that increasing saturation automatically yields intrinsic
  perceptual order.
labels:
- chart:general
- task:interpret-order
- visual:color-saturation
- impact:clarity
- data:ordinal
- audience:general
- source:literature-collation
---

## The Rule <!-- role: advice -->

Do not assume that a color-saturation encoding will be intrinsically ordered just because saturation changes monotonically.

## The Logic <!-- role: reason -->

The paper shows that monotonicity in a single attribute (including saturation) is sufficient to imply **legend-based** order under its assumptions, but is **not sufficient** to guarantee **intrinsic** order (local or global) [@bujackOrderingPerceptionsPerceptual2018]. This is precisely the kind of nuance the collation work highlights as necessary to convert graphical perception theory into usable recommendation rules [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Inferring an ordered progression from color appearance alone (without depending on a legend).
- **Data Type:** Ordinal (or otherwise ordered) data mapped to **color saturation**.
- **Audience:** Any audience, especially where legend use is uncertain or minimal.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You only require legend-based order (users will rely on the legend for ordering).
- **Reason:** Under the paper’s framework, strict monotonicity implies local/global legend-based order, which is a different requirement than intrinsic order [@bujackOrderingPerceptionsPerceptual2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may need to invest in stronger legend design or switch encodings, reducing palette freedom.
- **The Risk:** Over-correcting may lead to palettes that are harder to discriminate if you constrain saturation too tightly (tradeoff depends on your broader design, beyond what is specified in the extracted record).

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using a monotonic saturation ramp and assuming it is automatically “ordered” in the intuitive/intrinsic sense.
- **Why it fails:** Theoretical counterexamples show monotonic saturation can still violate intrinsic order conditions [@bujackOrderingPerceptionsPerceptual2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users hesitate or disagree when asked which of two colors corresponds to a larger value without seeing the legend.
- **The Test:** Sample three colors from the scale and ask users to identify the “middle” value by appearance alone; failure indicates intrinsic order is not assured under the paper’s definition [@bujackOrderingPerceptionsPerceptual2018], aligning with the review’s emphasis on actionable validation [@zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Ensure the legend is visible, proximate, and intended as the mechanism for interpreting order (legend-based order assumption) [@bujackOrderingPerceptionsPerceptual2018].
- **Best Fix:** Use a different strategy than “saturation monotonicity ⇒ intrinsic order” when your goal is intrinsic ordering; treat this as a constraint/assumption in recommendation logic as advocated by [@zengReviewCollationGraphical2023].
