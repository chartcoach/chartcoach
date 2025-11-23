---
id: communicate-statistical-uncertainty-clearly
title: Communicate Statistical Uncertainty with Visuals and Text
bibliography: references.bib
description: Ensure statistical confidence intervals use clear visual conventions
  and textual explanations to minimize cognitive load.
labels:
- impact:clarity
- impact:accessibility
- data:statistical
- visual:annotation
- task:interpret
- audience:general
---

## The Rule <!-- role: advice -->

If statistical confidence intervals or uncertainty data exist in your dataset, you must display them using clear, ambiguous visual conventions and accompany them with a textual explanation.

## The Logic <!-- role: reason -->

Presenting data without ambiguity is essential to minimizing cognitive load and ensuring the visualization is understandable [@elavsky_how_2022]. Research indicates that using established visual conventions—such as error bars, violin plots, or gradient shading—alongside textual explanations significantly helps viewers understand the nature of the uncertainty. This combination allows users to make better decisions compared to visualizations that lack these specific cues [@fernandes_uncertainty_displays_2018].

## Where to Apply <!-- role: context -->

This advice applies to any data-driven interface where the data is probabilistic or contains margins of error.
*   **User Goal:** Evaluating risk, reliability, or probability ranges to make a decision.
*   **Data Type:** Quantitative data possessing confidence intervals, standard errors, or probability distributions.
*   **Audience:** Users who need to distinguish between precise values and estimates.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** Highly complex ethical or cognitive contexts where standard visualizations are insufficient or misleading.
*   **Reason:** There are contexts where the "best" way to communicate uncertainty is not yet settled, and standard methods might introduce ethical risks or fail to meet specific cognitive accessibility needs [@elavsky_how_2022].

## The Price <!-- role: costs -->

*   **The Sacrifice:** Screen real estate. Including both visual markers (like error bars or shading) and explanatory text takes up more space than a simple mean line.
*   **The Risk:** If the textual explanation is too technical, it may fail to clarify the visual for non-expert audiences.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Displaying error bars without a label or legend entry defining them.
*   **Why it fails:** Visuals alone are often ambiguous (e.g., is it a standard deviation or a 95% confidence interval?); without text, the user cannot be certain what is being shown [@elavsky_how_2022].

## How to Check <!-- role: check -->

*   **Visual Sign:** Look for charts that imply precision (single lines or points) where the underlying data is uncertain. Conversely, look for error bars that lack labels.
*   **The Test:** If you remove the chart title, does the interface explicitly tell you what the shaded region or whisker represents?

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Add a caption or legend explicitly stating what the visual element represents (e.g., "Error bars represent the 95% confidence interval").
*   **Best Fix:** Use advanced uncertainty displays like quantile dotplots or cumulative distribution functions (CDFs) combined with natural language descriptions to improve decision-making accuracy [@fernandes_uncertainty_displays_2018].
