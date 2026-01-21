---
id: present-quantities-in-multiple-formats-to-support-representational-fluency
title: Provide Key Quantities in Multiple Equivalent Formats
bibliography: references.bib
description: Reduce representation effects by presenting the same probability or quantity
  in more than one format (e.g., percent and frequency, text and graphic).
labels:
- task:interpret
- task:compare
- impact:accessibility
- impact:robustness
- data:risk
- audience:general-public
- domain:health
- source:ancker-2007
---

## The Rule <!-- role: advice -->

For important probabilities and quantities, show at least two equivalent representations (e.g., percent and frequency, and/or a graphic plus text).

## The Logic <!-- role: reason -->

People differ in representational fluency; presenting multiple formats can reduce format-driven errors and support users who can’t readily translate between representations.

- **The Principle:** Mitigating representation effects via redundancy
- **The Evidence:** [@anckerRethinkingHealthNumeracy2007]

## Where to Apply <!-- role: context -->

- **User Goal:** Understanding risk magnitude and comparing options accurately
- **Data Type:** Probabilities (percent, proportion, frequency), device readings shown in tables vs meters
- **Audience:** Mixed numeracy populations; users switching between devices or interfaces [@anckerRethinkingHealthNumeracy2007]

## When to Break It <!-- role: exceptions -->

- **Scenario:** A highly constrained interface where duplicating formats would crowd out the primary task.
- **Reason:** Too many parallel formats can increase scanning burden and confusion. [@anckerRethinkingHealthNumeracy2007]

## The Price <!-- role: costs -->

- **The Sacrifice:** Additional screen/print space and design complexity
- **The Risk:** Users may perceive discrepancies if rounding differs across formats [@anckerRethinkingHealthNumeracy2007]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching formats across screens (percent in one place, “1 in N” elsewhere) without showing equivalence.
- **Why it fails:** Users with low representational fluency may treat them as different quantities and make inconsistent choices. [@anckerRethinkingHealthNumeracy2007]

## How to Check <!-- role: check -->

- **Visual Sign:** Users change decisions when the same number is shown as a percent vs a frequency.
- **The Test:** A/B test alternative formats; large decision swings suggest representation dependence. [@anckerRethinkingHealthNumeracy2007]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add the alternate format in parentheses right next to the primary number.
- **Best Fix:** Pair a numeric format with a visual representation that makes the equivalence perceptually obvious. [@anckerRethinkingHealthNumeracy2007]
