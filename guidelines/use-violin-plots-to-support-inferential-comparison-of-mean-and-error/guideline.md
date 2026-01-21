---
id: use-violin-plots-to-support-inferential-comparison-of-mean-and-error
title: Use Violin Plots to Encode Uncertainty with Width
bibliography: references.bib
description: Show uncertainty around a mean using a symmetric violin shape so viewers
  can compare plausibility across values.
labels:
- chart:violin
- task:compare
- visual:width
- impact:calibration
- data:uncertainty
- audience:novice
- source:correll-gleicher-2014
---

## The Rule <!-- role: advice -->

For inferential tasks with mean and uncertainty, use a symmetric violin plot centered on the mean (width encodes plausibility), and mark the mean explicitly.

## The Logic <!-- role: reason -->

A violin plot provides continuous information about how plausibility changes as you move away from the mean, supports comparisons beyond a single interval boundary, and avoids within-the-bar containment bias by being symmetric.

- **The Principle:** Symmetric, continuous uncertainty depiction supports graded inference.
- **The Evidence:** The paper’s experiments show symmetric alternatives (including violin plots) mitigate within-the-bar bias and improve alignment with expected inferential strategies compared to bar charts with error bars [@correllErrorBarsConsidered2014].

## Where to Apply <!-- role: context -->

- **User Goal:** Comparing uncertain group means and reasoning about how likely different outcomes are at different distances.
- **Data Type:** Means with uncertainty modeled as a distribution (the paper uses t-based inference).
- **Audience:** General audiences, including those without deep statistical training.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You cannot risk confusion between “distribution of the data” and “distribution used for inference,” and you cannot add clarifying labeling.
- **Reason:** The paper highlights that common distribution plots can be misread as showing the raw data distribution rather than an inferential distribution [@correllErrorBarsConsidered2014].

## The Price <!-- role: costs -->

- **The Sacrifice:** Space and unfamiliarity compared to bars; may require a short explanation.
- **The Risk:** Viewers may interpret the violin as showing sample data distribution rather than uncertainty about the mean if not clearly framed.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding internal boxplot glyphs or extra marks without clarifying what distribution is being shown.
- **Why it fails:** It can increase confusion about whether the shape refers to observed data vs inferential uncertainty [@correllErrorBarsConsidered2014].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers ask “is this the distribution of observed values?” or treat width as sample size rather than uncertainty.
- **The Test:** Ask a pilot user what the width means; if they can’t articulate it as uncertainty/plausibility around the mean, revise labeling [@correllErrorBarsConsidered2014].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add explicit annotation that the shape represents uncertainty around the mean (and add a clear mean line).
- **Best Fix:** Use the paper’s adapted violin approach for inferential tasks (no interior glyphs; centered on mean; width encodes plausibility) [@correllErrorBarsConsidered2014].
