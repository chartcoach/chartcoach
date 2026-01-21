---
id: reduce-cognitive-effort-by-doing-the-math-for-users
title: Do Required Risk Calculations for the User
bibliography: references.bib
description: "Precompute totals and end-state risks so users don\u2019t have to combine\
  \ or convert probabilities themselves."
labels:
- task:calculate
- task:decide
- impact:accuracy
- impact:accessibility
- data:risk
- audience:novice
- domain:health
- source:ancker-2007
---

## The Rule <!-- role: advice -->

If the decision requires adding, converting, or combining risks, provide the computed results rather than making users do the arithmetic.

## The Logic <!-- role: reason -->

Offloading computation reduces cognitive effort and improves accuracy in risk tradeoffs, especially for users with weaker probability skills.

- **The Principle:** Cognitive offloading to improve numerical decision-making
- **The Evidence:** [@anckerRethinkingHealthNumeracy2007]

## Where to Apply <!-- role: context -->

- **User Goal:** Comparing options with multiple outcomes (benefits and harms) or interpreting compounded risks
- **Data Type:** Multiple probabilities, baseline + modified risks, multi-outcome tradeoffs
- **Audience:** General public and patients, particularly those prone to probability conversion errors [@anckerRethinkingHealthNumeracy2007]

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users must learn the computation as part of training (e.g., clinician education or skills-building).
- **Reason:** Hiding the computation may impede learning and auditability. [@anckerRethinkingHealthNumeracy2007]

## The Price <!-- role: costs -->

- **The Sacrifice:** Less transparency about how the number was derived
- **The Risk:** Users may over-trust a computed summary if assumptions are not visible [@anckerRethinkingHealthNumeracy2007]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Presenting component probabilities and expecting users to sum/convert mentally.
- **Why it fails:** Many users struggle to manipulate percentages/proportions and to translate between formats. [@anckerRethinkingHealthNumeracy2007]

## How to Check <!-- role: check -->

- **Visual Sign:** Users ask “so what’s my total risk?” or give totals that don’t match the provided components.
- **The Test:** Ask users to compute the total from what you show; if many can’t, you’re demanding unnecessary computation. [@anckerRethinkingHealthNumeracy2007]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a “Total / Overall” line with the computed number.
- **Best Fix:** Restructure the display so the computed end-state is primary, with components as optional drill-down. [@anckerRethinkingHealthNumeracy2007]
