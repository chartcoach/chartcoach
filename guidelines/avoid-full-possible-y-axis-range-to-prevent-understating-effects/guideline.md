---
id: avoid-full-possible-y-axis-range-to-prevent-understating-effects
title: Avoid Showing the Full Possible Y-Axis Range by Default
bibliography: references.bib
description: "Do not default to the full possible y-range (e.g., 0\u2013100) when\
  \ communicating effect magnitude, because it biases viewers to judge effects as\
  \ too small."
labels:
- chart:bar
- chart:line
- task:interpret
- visual:scale
- impact:calibration
- impact:clarity
- data:continuous
- audience:novice
- custom:full-range-axis
- source:wittGraphConstruction2019
---

## The Rule <!-- role: advice -->

Do not default to the full possible y-axis range (e.g., 0–100) if your intent is to help readers accurately judge standardized effect magnitude.

## The Logic <!-- role: reason -->

A very wide y-axis compresses differences, making effects look visually small. This drives systematic underestimation (negative bias) and reduces sensitivity to differences among effect magnitudes [@wittGraphConstruction2019].

- **The Principle:** Visual compression from overly broad scaling
- **The Evidence:** Full-range plots produced a strong bias toward “null/small” judgments and lower sensitivity than SD-standardized axes across experiments [@wittGraphConstruction2019].

## Where to Apply <!-- role: context -->

- **User Goal:** Differentiating small vs medium vs large effects.
- **Data Type:** Bounded measures with a large theoretical range relative to observed variance (e.g., percent correct) [@wittGraphConstruction2019].
- **Audience:** Readers making quick, impression-based magnitude judgments [@wittGraphConstruction2019].

## When to Break It <!-- role: exceptions -->

- **Scenario:** The user’s primary question is absolute position in the full possible scale (e.g., “how close to 100 is performance?”).
- **Reason:** Then the full scale provides the needed contextual frame (the paper’s advantage is specifically for effect-size judgment) [@wittGraphConstruction2019].
- **Scenario:** You must keep a fixed scale across multiple charts for direct visual comparability.
- **Reason:** A shared axis can be required for cross-graph comparisons; if used, acknowledge potential underestimation risk [@wittGraphConstruction2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Losing immediate context of the full theoretical range.
- **The Risk:** If you move away from full range without explanation, some readers may misread absolute levels as more extreme than intended [@wittGraphConstruction2019].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** “Always start at 0 / always show 0–100” as a blanket rule.
- **Why it fails:** The paper shows full-range scaling can be misleading in the opposite direction, biasing effects to look too small for magnitude judgment tasks [@wittGraphConstruction2019].
- **The Wrong Fix:** Keeping full range because it feels “honest,” while omitting any SD-based cue for interpreting magnitude.
- **Why it fails:** The impression can still be systematically distorted even when labels are technically correct [@wittGraphConstruction2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Most differences are visually tiny; readers tend to label many effects as “no effect” or “small.”
- **The Test:** Compare y-axis span to the data SD. If the axis covers many SDs (well beyond ~2 SD total) in a standardized-effects context, expect underestimation bias [@wittGraphConstruction2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Switch to a grand mean–centered axis spanning ~1.5 SD total (or 1–2 SD) [@wittGraphConstruction2019].
- **Best Fix:** Define y-limits using SD-based rules for effect-size communication, expanding only for unusually large effects or to include uncertainty elements [@wittGraphConstruction2019].
