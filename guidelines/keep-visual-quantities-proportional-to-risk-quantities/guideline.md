---
id: keep-visual-quantities-proportional-to-risk-quantities
title: Make Visual Encodings Proportional to Risk Values
bibliography: references.bib
description: "Ensure the graphic\u2019s visual elements represent risk magnitudes\
  \ proportionally, especially part-to-whole."
labels:
- chart:icon-array
- task:estimate
- visual:area
- impact:accuracy
- data:proportion
- audience:general-public
- domain:risk-communication
---

## The Rule <!-- role: advice -->

Design risk graphics so the visible amount (height/area/count) is proportional to the underlying probability, including the numerator and denominator relationship.

## The Logic <!-- role: reason -->

When visuals preserve proportionality, they better support accurate magnitude judgments and comparisons; selective emphasis can shift perceived risk and choices.

- **The Principle:** Proportional encoding and foreground/background salience
- **The Evidence:** [@lipkusNumericVerbalVisual2007]

## Where to Apply <!-- role: context -->

- **User Goal:** Judge how large a risk is, or compare two risks
- **Data Type:** Probabilities shown visually (bars, stacked bars, icon arrays)
- **Audience:** Public/patients interpreting benefits vs harms

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your explicit goal is persuasion via emphasizing those affected (foreground) rather than precision.
- **Reason:** Foreground-only emphasis can increase risk-avoidant behavior but may reduce numeric accuracy. [@lipkusNumericVerbalVisual2007]

## The Price <!-- role: costs -->

- **The Sacrifice:** More visual complexity (showing both affected and unaffected).
- **The Risk:** If not labeled clearly, viewers may misread what the background represents.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing only the affected group (numerator) without showing the population at risk (denominator).
- **Why it fails:** Inflates perceived magnitude and can bias decisions. [@lipkusNumericVerbalVisual2007]

## How to Check <!-- role: check -->

- **Visual Sign:** A chart depicts “cases” but not “out of how many.”
- **The Test:** Ask “Can the viewer see both affected and total-at-risk in the graphic?”

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add the denominator visibly (e.g., stacked bars showing affected + unaffected).
- **Best Fix:** Use a display that simultaneously encodes numerator and denominator (stacked bar or full icon array) with explicit “out of N” labeling. [@lipkusNumericVerbalVisual2007]
