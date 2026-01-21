---
id: avoid-bar-charts-with-error-bars-for-inferential-judgments
title: Replace Bar Charts with Error Bars for Inferential Judgments
bibliography: references.bib
description: Use encodings other than bar charts with error bars when viewers must
  reason about mean plus uncertainty.
labels:
- chart:bar
- task:infer
- visual:position
- impact:accuracy
- data:uncertainty
- audience:novice
- source:correll-gleicher-2014
---

## The Rule <!-- role: advice -->

Do not use bar charts with error bars for tasks that require viewers to make inferences from mean and uncertainty; use a different encoding.

## The Logic <!-- role: reason -->

Bar charts with error bars systematically change judgments about uncertain data: they encourage biased likelihood judgments and more confident, larger-effect interpretations than other encodings, producing decisions less aligned with statistical expectations.

- **The Principle:** Encoding drives inference; salient “bar” glyphs induce biased reasoning under uncertainty.
- **The Evidence:** The paper’s crowd experiments show bar charts induce within-the-bar bias in one-sample judgments and inflate confidence/effect-size in two-sample comparisons relative to alternative encodings [@correllErrorBarsConsidered2014].

## Where to Apply <!-- role: context -->

- **User Goal:** Predicting outcomes, judging likelihood, comparing groups while accounting for error/uncertainty.
- **Data Type:** Sample means with margins of error/confidence intervals (e.g., polling, forecasts, financial predictions).
- **Audience:** General audiences or mixed statistical backgrounds.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The task is ratio/height comparison and uncertainty is not part of the decision.
- **Reason:** The paper notes bar charts can be advantageous for some non-uncertainty tasks (e.g., fast ratio comparison), so the inferential benefit may not justify changing encodings [@correllErrorBarsConsidered2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Familiarity—viewers may be less used to non-bar encodings.
- **The Risk:** Alternative encodings may require brief explanation or legend text to clarify what uncertainty means.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Keeping the bar chart and “just adding error bars” without addressing perceptual bias.
- **Why it fails:** The bar glyph itself creates biased interpretations (e.g., containment) even when uncertainty is present [@correllErrorBarsConsidered2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers treat values “inside the bar” as more plausible than equally distant values above the mean.
- **The Test:** Ask a pilot user whether a point equally far above vs. below the mean seems equally likely; if not, the chart is inducing bias [@correllErrorBarsConsidered2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Remove the bar glyph entirely (switch to a symmetric uncertainty depiction).
- **Best Fix:** Use a violin plot or gradient plot (as evaluated) so uncertainty is symmetric and more continuously interpretable [@correllErrorBarsConsidered2014].
