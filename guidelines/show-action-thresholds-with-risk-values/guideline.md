---
id: show-action-thresholds-with-risk-values
title: Show the Action Threshold Next to the Risk
bibliography: references.bib
description: Pair risk magnitudes with explicit standards for action so users know
  what the number means.
labels:
- chart:risk-ladder
- task:decide
- visual:position
- impact:decision-support
- data:threshold
- audience:general-public
- domain:risk-communication
---

## The Rule <!-- role: advice -->

When a numeric risk implies a recommended action threshold, display the threshold and the recommended action alongside the risk magnitude.

## The Logic <!-- role: reason -->

Risk numbers alone may not convey what to do; showing an interpretive standard links magnitude to decision-relevant meaning.

- **The Principle:** Mapping risk magnitude to actionable interpretation
- **The Evidence:** [@lipkusNumericVerbalVisual2007]

## Where to Apply <!-- role: context -->

- **User Goal:** Decide whether to act (treat, test, remediate, vaccinate)
- **Data Type:** Risk levels with known cutoffs or guidelines
- **Audience:** Public/patients making practical decisions

## When to Break It <!-- role: exceptions -->

- **Scenario:** No consensus action standard exists or benefits/harms are value-sensitive.
- **Reason:** A single “correct” action could misrepresent preference-sensitive decisions. [@lipkusNumericVerbalVisual2007]

## The Price <!-- role: costs -->

- **The Sacrifice:** More annotation and layout complexity.
- **The Risk:** Users may focus only on “above/below” and ignore how far from the threshold they are.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Labeling only “safe/unsafe” without showing the underlying level.
- **Why it fails:** Hides meaningful variation (e.g., two values both “action needed” but with very different hazard). [@lipkusNumericVerbalVisual2007]

## How to Check <!-- role: check -->

- **Visual Sign:** A risk value is shown but the viewer is left asking “Is that high?”
- **The Test:** Ask users “What would you do next?” If they can’t answer, the threshold/action mapping is missing.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a callout: “At/above X, do Y.”
- **Best Fix:** Use a ladder or scale that marks the threshold visually and includes short action guidance by range. [@lipkusNumericVerbalVisual2007]
