---
id: encode-denominator-by-total-icon-count-per-group
title: "Match Icon Array Size to Each Group\u2019s Denominator"
bibliography: references.bib
description: "Make denominators perceptually concrete by using an icon count equal\
  \ to each group\u2019s total."
labels:
- chart:icon-array
- task:estimate
- visual:count
- impact:accuracy
- data:ratio
- audience:general-public
- risk-communication:medical
---

## The Rule <!-- role: advice -->

For each comparison group, use an icon array whose total number of icons equals that group’s denominator (e.g., 100 icons for 100 patients; 500 icons for 500 patients).

## The Logic <!-- role: reason -->

Denominator neglect arises when people fail to incorporate differing totals; representing the total as a countable/visible whole makes it harder to ignore. The studies used arrays with 100 or 500 circles depending on the group size and found improved accuracy when arrays accompanied numbers in unequal-denominator conditions [@garcia-retameroIconArraysHelp2010].

- **The Principle:** Part-to-whole visual grounding of ratios
- **The Evidence:** Accuracy increased substantially when icon arrays reflecting the denominators were provided, particularly when denominators differed [@garcia-retameroIconArraysHelp2010].

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly interpret risk in each group and infer risk reduction.
- **Data Type:** Frequencies such as “x out of N” per group.
- **Audience:** Mixed numeracy audiences, including older adults.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Denominators are very large (e.g., tens of thousands) and an icon-per-person mapping would be infeasible.
- **Reason:** The paper’s tested arrays were 100 or 500; scaling far beyond that may not be practical or legible while preserving the intended mechanism [@garcia-retameroIconArraysHelp2010].

## The Price <!-- role: costs -->

- **The Sacrifice:** Large denominators require large arrays, increasing space and visual complexity.
- **The Risk:** Viewers may abandon counting if the array becomes too dense.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using the same-sized array for both groups when denominators differ (forcing a hidden rescaling).
- **Why it fails:** It undermines the whole point—making denominators visually comparable and salient—thus reintroducing denominator neglect risk [@garcia-retameroIconArraysHelp2010].

## How to Check <!-- role: check -->

- **Visual Sign:** Both groups’ arrays look the same “size” despite different Ns.
- **The Test:** Verify that the total icon count in each group equals the stated denominator (spot-check by design spec).

## How to Fix <!-- role: fix -->

- **Quick Fix:** Regenerate each array so its icon total equals the group’s N.
- **Best Fix:** Use side-by-side arrays that preserve the true denominators, so the viewer can visually register unequal group sizes while also seeing the affected subset [@garcia-retameroIconArraysHelp2010].
