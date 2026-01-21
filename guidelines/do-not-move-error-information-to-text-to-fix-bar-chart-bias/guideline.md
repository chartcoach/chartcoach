---
id: do-not-move-error-information-to-text-to-fix-bar-chart-bias
title: Do Not Move Error Information to Text as a Bias Fix
bibliography: references.bib
description: Shifting uncertainty or outcomes to text may reduce within-the-bar bias
  but harms accuracy and calibration.
labels:
- chart:bar
- task:infer
- visual:annotation
- impact:accuracy
- data:uncertainty
- audience:novice
- source:correll-gleicher-2014
---

## The Rule <!-- role: advice -->

Do not try to “fix” bar-chart inference problems by moving the outcome and/or margin of error into text while keeping the bar chart.

## The Logic <!-- role: reason -->

Offloading key values to text forces viewers to mentally project numbers back into the chart space, reducing accuracy and producing miscalibrated confidence—even if some bias is reduced.

- **The Principle:** Cognitive projection cost + miscalibration from reduced visual support.
- **The Evidence:** In the paper’s textual one-sample experiment, moving margin-of-error and outcomes to text reduced within-the-bar bias only when both were moved, but it caused large drops in correct strategy adherence and increased (unjustified) confidence [@correllErrorBarsConsidered2014].

## Where to Apply <!-- role: context -->

- **User Goal:** Judging likelihood of a proposed outcome relative to a mean and its uncertainty.
- **Data Type:** Bar charts used with margins of error; designs where designers consider placing MOE in legends/notes.
- **Audience:** General audiences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The chart is purely decorative and no inference is expected from the graphic.
- **Reason:** The harms documented are about inferential task performance; if no inference is intended, the tradeoff may be irrelevant [@correllErrorBarsConsidered2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** If you refuse this approach, you may need to change chart type (organizational and tooling cost).
- **The Risk:** Stakeholders may prefer familiar bars and resist switching.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Showing only means as bars and putting “Margin of Error ±X” in a caption/legend.
- **Why it fails:** Participants became much less accurate at basic inferential reasoning and more confident in wrong judgments under text-only uncertainty [@correllErrorBarsConsidered2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Uncertainty is only in a legend/caption; the plot itself lacks an uncertainty depiction.
- **The Test:** Ask users to answer an outcome-likelihood question; if answers are inconsistent and confidence stays high, text-offloading is failing [@correllErrorBarsConsidered2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Put uncertainty back into the visual encoding, not only text.
- **Best Fix:** Replace the bar chart with a symmetric, continuous uncertainty encoding (gradient or violin) to avoid the underlying bar-induced bias [@correllErrorBarsConsidered2014].
