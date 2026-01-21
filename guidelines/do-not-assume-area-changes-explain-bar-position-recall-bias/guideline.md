---
id: do-not-assume-area-changes-explain-bar-position-recall-bias
title: Treat Bar Aspect Ratio as the Primary Driver of Position Recall Bias, Not Area
bibliography: references.bib
description: Changing bar area alone does not explain the direction of bar-top recall
  biases; aspect ratio does.
labels:
- chart:bar
- task:diagnose-bias
- visual:position
- impact:validity
- data:quantitative
- audience:practitioner
- analysis:design-review
---

## The Rule <!-- role: advice -->

When auditing or debugging biased bar-height recall, prioritize controlling bar aspect ratio; do not rely on manipulating bar area as the main mitigation.

## The Logic <!-- role: reason -->

Across conditions where aspect ratio varied but area was controlled, the bias direction flipped systematically (wide → overestimate; tall → underestimate). When the authors introduced a condition with variable area (by fixing width), the same directional bias pattern persisted, and area was not a significant predictor of signed error—implicating aspect ratio as the key factor. [@cejaTruthSquareAspect2021a]

- **The Principle:** Incidental shape (aspect ratio) drives categorical-prototype bias more than mark area in this task
- **The Evidence:** [@cejaTruthSquareAspect2021a]

## Where to Apply <!-- role: context -->

- **User Goal:** Ensure faithful recall/comparison of encoded values
- **Data Type:** Bars where area and aspect ratio can change due to responsive sizing, styling, or layout templates
- **Audience:** Visualization designers/reviewers performing QA on chart systems

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your specific task is area judgment (not position/height judgment).
- **Reason:** This paper tests biases in recalling *position encodings*; it does not claim area never matters for other judgments. [@cejaTruthSquareAspect2021a]

## The Price <!-- role: costs -->

- **The Sacrifice:** Fixing aspect ratio may constrain responsive design and theming choices more than fixing area would.
- **The Risk:** Over-focusing on area tweaks can waste iteration cycles without reducing the bias.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** “Normalize area” (or equalize area across bars) while letting bars become very wide or very tall.
- **Why it fails:** The paper finds the bias pattern remains tied to aspect ratio even when area differs. [@cejaTruthSquareAspect2021a]

## How to Check <!-- role: check -->

- **Visual Sign:** After an “area fix,” bars still look much wider or taller across conditions, and users still misremember heights directionally.
- **The Test:** Hold aspect ratio constant in a prototype and see whether the directional over/underestimation risk is reduced; if you only changed area, you likely did not address the driver. [@cejaTruthSquareAspect2021a]

## How to Fix <!-- role: fix -->

- **Quick Fix:** Standardize bar widths (or chart geometry) so aspect ratios don’t swing dramatically between views.
- **Best Fix:** Redesign templates/components so mark aspect ratio is a controlled parameter across the system, especially for cross-view comparisons. [@cejaTruthSquareAspect2021a]
