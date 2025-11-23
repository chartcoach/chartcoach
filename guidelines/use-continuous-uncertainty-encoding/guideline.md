---
id: use-continuous-uncertainty-encoding
title: Encode Uncertainty Continuously Rather Than Discretely
bibliography: references.bib
description: Use gradients or tapered shapes to represent uncertainty, avoiding the
  binary 'all-or-nothing' interpretation of error bars.
labels:
- chart:violin
- chart:gradient-plot
- visual:transparency
- visual:width
- task:risk-assessment
- impact:nuance
- audience:general
---

## The Rule <!-- role: advice -->
Use continuous visual encodings—such as gradient plots (varying transparency) or violin plots (varying width)—to represent probability distributions, rather than discrete "whiskers" or error bars.

## The Logic <!-- role: reason -->
Standard error bars create a binary interpretation: values are either "inside" the margin of error (and thus perceived as likely or safe) or "outside" (and perceived as impossible or irrelevant).
*   **The Principle:** Visual Continuity vs. Binary Categorization.
*   **The Evidence:** Continuous encodings (gradient and violin plots) allow viewers to make more nuanced judgments about outcome likelihood. In experiments, these encodings resulted in viewer confidence levels that better correlated with actual statistical power (p-values) compared to the "all-or-nothing" interpretation of bar charts [@correll_error_2014].

## Where to Apply <!-- role: context -->
*   **User Goal:** Tasks requiring users to assess risk, likelihood of specific outcomes, or "willingness to critique" a prediction.
*   **Data Type:** Probabilistic predictions, forecast models, or uncertain polling data.
*   **Audience:** General audiences, who are capable of reading these "complex" plots with high accuracy despite lack of training [@correll_error_2014].

## When to Break It <!-- role: exceptions -->
*   **Scenario:** High-Precision Reading of Specific Intervals.
*   **Reason:** If the user specifically needs to read the exact boundary of a 95% confidence interval, a gradient plot makes this edge "fuzzy" and difficult to pinpoint [@correll_error_2014].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Precision at the edges. Gradient plots deliberately introduce "beneficial difficulty" by making precise readings of uncertain boundaries harder.
*   **The Risk:** Technical limitations. Reproducing transparency and gradients can be difficult in certain print media or monotone displays [@correll_error_2014].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Box plots.
*   **Why it fails:** While better than bars, box plots still use discrete whiskers that encourage binary thinking (inside vs. outside the whisker) [@correll_error_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the representation of error end abruptly at a sharp line?
*   **The Test:** If you removed the axes, does the chart imply that a value 1 pixel outside the error bar is impossible?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** If using error bars, add a glyph or annotation that indicates the distribution continues beyond the whiskers.
*   **Best Fix:** Adopt Gradient Plots (using alpha transparency to fade out) or Violin Plots (tapering width) to visually demonstrate the decaying probability of outlier values [@correll_error_2014].
