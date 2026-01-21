---
id: align-with-existing-schemas
title: "Match Visual Encodings to Users\u2019 Learned Graphic Conventions"
bibliography: references.bib
description: Use familiar conventions so viewers do not need extra mental transformations
  to interpret the display.
labels:
- chart:general
- task:interpret
- visual:convention
- impact:speed
- data:general
- audience:novice
- mechanism:type-2
- concept:cognitive-fit
---

## The Rule <!-- role: advice -->

Use standard, widely learned graphical conventions unless you have a strong, tested reason not to.

## The Logic <!-- role: reason -->

When a visualization violates users’ graph schemas, viewers must perform corrective mental transformations using working memory (Type 2). The review emphasizes that mismatches between a visualization and learned schema increase effort and can increase errors and time [@padillaDecisionMakingVisualizations2018].

## Where to Apply <!-- role: context -->

- **User Goal:** Accurate comprehension and decision making, especially under time pressure
- **Data Type:** Any chart/map that relies on conventions (axes direction, symbol meaning, uncertainty marks)
- **Audience:** Mixed audiences, especially non-experts

## When to Break It <!-- role: exceptions -->

- **Scenario:** Expert-only tools where users are trained on a nonstandard but superior encoding
- **Reason:** Training can create or strengthen the needed schema, reducing transformation cost over time [@padillaDecisionMakingVisualizations2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Potentially less novel or “clever” encodings
- **The Risk:** Standard conventions may be suboptimal for niche tasks, even if easier to interpret [@padillaDecisionMakingVisualizations2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Introducing a new convention and assuming a legend will solve it
- **Why it fails:** Viewers may still default to their existing schema and misinterpret despite keys or legends [@padillaDecisionMakingVisualizations2018].

## How to Check <!-- role: check -->

- **Visual Sign:** Users consistently invert, swap, or reinterpret variables (e.g., reversing an axis mentally).
- **The Test:** Ask users to explain what each axis/mark means without prompting; mismatched explanations indicate schema conflict [@padillaDecisionMakingVisualizations2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Revert to standard conventions for axes, ordering, and symbol semantics.
- **Best Fix:** If you must be nonstandard, add training that explicitly teaches the convention and test comprehension under realistic time constraints [@padillaDecisionMakingVisualizations2018].
