---
id: avoid-extremely-tall-thin-bars-when-precision-matters
title: Avoid Extremely Tall, Thin Bars When Precision Matters
bibliography: references.bib
description: Tall-aspect-ratio bars produce larger and more variable errors in recalling
  bar-top positions.
labels:
- chart:bar
- task:read-value
- visual:position
- impact:precision
- data:quantitative
- audience:general
- risk:high-variance
---

## The Rule <!-- role: advice -->

Do not use very tall, thin bars in situations that require precise height recall; redesign to reduce tall aspect ratios.

## The Logic <!-- role: reason -->

In the experiments, tall-aspect-ratio bars were not only underestimated; they also showed much larger absolute error and variability than wide or square bars, indicating poorer precision for reproducing the encoded position under memory. [@cejaTruthSquareAspect2021a]

- **The Principle:** Certain mark shapes degrade position recall precision and increase variance
- **The Evidence:** [@cejaTruthSquareAspect2021a]

## Where to Apply <!-- role: context -->

- **User Goal:** Accurately reproduce/remember a value (audits, checks, “what was that value?”)
- **Data Type:** Sparse bar charts or interactions where a single mark is queried
- **Audience:** Any audience, especially when decisions depend on small differences

## When to Break It <!-- role: exceptions -->

- **Scenario:** The interaction lets users align/trace against a simultaneously visible reference bar (no memory gap).
- **Reason:** The paper shows the characteristic underestimation pattern is mainly present under memory-based reproduction; with the stimulus visible, the pattern changes. [@cejaTruthSquareAspect2021a]

## The Price <!-- role: costs -->

- **The Sacrifice:** May require wider charts, fewer categories per view, or different layout constraints.
- **The Risk:** Making bars wider to avoid “thinness” can reduce the number of categories visible at once.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Shrinking bar width to fit more categories while claiming “users read the top anyway.”
- **Why it fails:** Tall/thin bars were the least accurate and most variable in recalled position. [@cejaTruthSquareAspect2021a]

## How to Check <!-- role: check -->

- **Visual Sign:** Bars appear needle-like compared to the chart’s height.
- **The Test:** Identify whether your design systematically creates tall, thin marks (e.g., many categories squeezed into a narrow panel). [@cejaTruthSquareAspect2021a]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Increase available horizontal space or reduce the number of categories shown so bars can be thicker.
- **Best Fix:** Rework the layout so queried bars are closer to square aspect ratios, reducing both bias and variability. [@cejaTruthSquareAspect2021a]
