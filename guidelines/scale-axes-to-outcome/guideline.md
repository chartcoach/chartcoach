---
id: scale-axes-to-outcome
title: Scale Y-Axes to Include Outcome Variability
bibliography: references.bib
description: If using Confidence Intervals, expand the axis range to match the range
  of individual outcomes to reduce bias.
labels:
- chart:error-bars
- task:compare
- visual:scale
- impact:bias-mitigation
- data:quantitative
- audience:expert
---

## The Rule <!-- role: advice -->
If you must visualize Inferential Uncertainty (e.g., 95% Confidence Intervals), **rescale the y-axis** to accommodate the full range of likely individual outcomes (the 95% Prediction Interval range), rather than zooming in tightly on the means.

## The Logic <!-- role: reason -->
Tight axes that frame only the means and their standard errors visually emphasize the distance between the groups, exaggerating the perceived effect size.
*   **The Principle:** **Visual Framing / Anchoring.** By displaying the full range of potential data points (even if the points aren't shown), the visual distance between means appears smaller relative to the total variance.
*   **The Evidence:** [@hofman_how_2020] found that "rescaling the axis reduces error" in willingness-to-pay and probability judgments compared to standard zoomed-in Confidence Interval plots, although it was not as effective as showing the Prediction Intervals directly.

## Where to Apply <!-- role: context -->
*   **User Goal:** Comparing means while retaining some context of the underlying data spread.
*   **Data Type:** Group comparisons (bar charts or dot plots with error bars).
*   **Audience:** Situations where statistical conventions require CIs (e.g., academic publishing) but you want to mitigate lay interpretation errors.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Detecting minute differences in means is the sole purpose.
*   **Reason:** If the variance is known to be irrelevant and the user is strictly looking for a shift in the mean (e.g., manufacturing quality control of a precise part), zooming in is appropriate.

## The Price <!-- role: costs -->
*   **The Sacrifice:** The error bars for the Confidence Interval will appear very small, potentially making it harder to read exact upper/lower bounds of the CI.
*   **The Risk:** Users may miss that a difference is statistically significant because the visual separation looks negligible on the zoomed-out scale.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a "break" in the axis to show detail at the top.
*   **Why it fails:** This distorts the ratio of signal (difference) to noise (variance).

## How to Check <!-- role: check -->
*   **Visual Sign:** Do the error bars take up a significant portion of the vertical space? (If they are CIs, they usually shouldn't if the axis shows the full data range).
*   **The Test:** Calculate the 95% Prediction Interval (approx $\pm 2SD$). Does the Y-axis cover this range?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Manually set the Y-axis `min` and `max` to standard deviation boundaries rather than letting the software auto-scale to the error bars.
*   **Best Fix:** Add a visual indicator (like a light grey background box or a second set of error bars) that explicitly marks the outcome range, forcing the axis to accommodate it [@hofman_how_2020].
