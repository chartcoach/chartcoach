---
id: prefer-continuous-uncertainty-encodings-over-binary-interval-only-displays
title: Encode Uncertainty Continuously, Not as a Binary Interval
bibliography: references.bib
description: "Show uncertainty as a continuous field/shape so viewers can reason beyond\
  \ \u201Cinside vs outside the error bar.\u201D"
labels:
- chart:interval
- task:compare
- visual:transparency
- impact:calibration
- data:uncertainty
- audience:novice
- source:correll-gleicher-2014
---

## The Rule <!-- role: advice -->

Avoid uncertainty displays that imply a hard cutoff (only “in” or “out” of an interval); use encodings that communicate gradations of plausibility across values.

## The Logic <!-- role: reason -->

Binary interval presentations encourage all-or-nothing reasoning and can inflate perceived effect size and confidence in comparisons. Continuous encodings provide information about outcomes beyond the margin-of-error boundary and encourage more appropriate doubt.

- **The Principle:** Binary thresholding promotes overconfident inference under uncertainty.
- **The Evidence:** In two-sample judgments, bar charts produced significantly larger predicted effects and higher confidence than alternative encodings; the paper attributes this partly to binary “within/outside” interpretations [@correllErrorBarsConsidered2014].

## Where to Apply <!-- role: context -->

- **User Goal:** Comparing groups and judging both direction and strength of differences under uncertainty.
- **Data Type:** Two or more means with margins of error; inferential comparison (e.g., “who will win?” plus “how close?”).
- **Audience:** General audiences and mixed-expertise settings.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You must communicate only a single, fixed decision threshold (e.g., a specific confidence interval cutoff) and nothing else.
- **Reason:** If the sole purpose is a binary decision rule, a binary depiction may match the communication goal—even though it limits inference flexibility [@correllErrorBarsConsidered2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Continuous encodings can be less directly “readable” as a single interval and may require more space.
- **The Risk:** Viewers may misinterpret the continuous shape as the raw data distribution if labeling is unclear.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding significance asterisks to a bar+error-bar chart as a substitute for richer uncertainty depiction.
- **Why it fails:** It still enforces an all-or-nothing interpretation and prevents viewers from applying different standards of proof [@correllErrorBarsConsidered2014].

## How to Check <!-- role: check -->

- **Visual Sign:** The graphic only shows an interval boundary with no information about relative plausibility across values.
- **The Test:** Ask: “Can a viewer distinguish ‘somewhat unlikely’ from ‘extremely unlikely’ outcomes without additional text?” If not, it’s binary [@correllErrorBarsConsidered2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add a continuous uncertainty encoding around the mean (while keeping a clear mean mark).
- **Best Fix:** Use gradient plots (transparency decay beyond the CI) or violin plots (width as density) as evaluated [@correllErrorBarsConsidered2014].
