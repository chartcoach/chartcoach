---
id: treat-color-hue-order-as-conditional-not-guaranteed
title: Treat Color Hue Order as Conditional, Not Guaranteed
bibliography: references.bib
description: Do not assume that mapping ordered values to hue automatically produces
  a perceptually ordered scale.
labels:
- chart:general
- task:interpret-order
- visual:color-hue
- impact:clarity
- data:ordinal
- audience:general
- source:literature-collation
---

## The Rule <!-- role: advice -->

Do not assume that a color-hue encoding will be perceptually ordered just because the hue changes.

## The Logic <!-- role: reason -->

Hue-based order is not guaranteed as an intrinsic property of a hue cycle; order depends on the kind of “order” you require (e.g., intrinsic vs legend-based, local vs global). The paper formally shows that hue maps generally do not satisfy global intrinsic order, even if they are monotonic in hue [@bujackOrderingPerceptionsPerceptual2018]. This guideline is included as part of the collated graphical perception knowledge intended to translate such findings into actionable recommendation constraints [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Reading an ordered progression (e.g., low→high) from color alone, without relying on a legend.
- **Data Type:** Ordinal (or any ordered) data mapped to **color hue**.
- **Audience:** Any audience that may try to infer order directly from the colored marks.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The viewer will explicitly use a legend to read values and ordering.
- **Reason:** The paper distinguishes legend-based order from intrinsic order; assumptions and guarantees differ by order definition [@bujackOrderingPerceptionsPerceptual2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may rule out some visually diverse palettes that change mostly by hue.
- **The Risk:** If you avoid hue for order, you may need alternative encodings or additional scaffolding (e.g., clearer legends), potentially increasing design complexity.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Choosing any “rainbow-like” or strongly hue-varying palette and calling it “ordered” because hue progresses.
- **Why it fails:** Monotonic change in an attribute does not necessarily imply intrinsic order; the paper provides counterexamples and formal results demonstrating this mismatch [@bujackOrderingPerceptionsPerceptual2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers can plausibly disagree on the ordering of colors when looking at the marks alone.
- **The Test:** Show the colored marks briefly without a legend and ask users to sort a few sampled colors by “increasing value”; disagreement suggests the hue mapping is not intrinsically ordered (order type per [@bujackOrderingPerceptionsPerceptual2018]; collation motivation in [@zengReviewCollationGraphical2023]).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add/strengthen the legend and ensure the legend is the primary mechanism for reading order (since the guarantees differ for legend-based order) [@bujackOrderingPerceptionsPerceptual2018].
- **Best Fix:** Replace hue-as-order with a different encoding strategy rather than expecting hue alone to carry ordered meaning (the need to translate such theory into recommendation constraints is emphasized in [@zengReviewCollationGraphical2023]).
