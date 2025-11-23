---
id: visualize-outcome-uncertainty
title: Visualize Outcome Uncertainty Instead of Inferential Uncertainty
bibliography: references.bib
description: Show variation in individual outcomes (e.g., Prediction Intervals) rather
  than uncertainty in the mean (e.g., Confidence Intervals) to prevent overestimation
  of treatment effects.
labels:
- chart:error-bars
- task:estimate-effect-size
- visual:range
- impact:accuracy
- data:statistical
- audience:lay-people
- metric:cohens-d
---

## The Rule <!-- role: advice -->
When communicating the practical effectiveness of a treatment or intervention to lay audiences, display **Outcome Uncertainty** (e.g., 95% Prediction Intervals or Standard Deviation) rather than **Inferential Uncertainty** (e.g., 95% Confidence Intervals or Standard Error).

## The Logic <!-- role: reason -->
Readers often confuse the precision of the mean estimate with the variability of the data itself.
*   **The Principle:** **The Deterministic Fallacy (or confusion of sampling vs. population distributions).** When readers see tight error bars representing the mean (Standard Error/CIs), they incorrectly assume the groups are distinct and the effect size is large.
*   **The Evidence:** Experiments in [@hofman_how_2020] demonstrated that participants willing to pay significantly more for a treatment and overestimated the "probability of superiority" (winning a contest) when shown 95% Confidence Intervals compared to 95% Prediction Intervals, even when the underlying effect size was identical.

## Where to Apply <!-- role: context -->
This advice applies when the reader cares about the likelihood of a specific individual benefit rather than the statistical significance of a population difference.
*   **User Goal:** Individual decision making (e.g., "Should I take this drug?", "Will I win this game?").
*   **Data Type:** Experimental comparisons with overlapping distributions.
*   **Audience:** Non-statisticians, policy makers, or general public consumers of science.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The primary goal is Null Hypothesis Significance Testing (NHST).
*   **Reason:** If the specific task is to determine if two means are statistically different from one another (rather than how much they overlap), Inferential Uncertainty (Standard Error/CIs) facilitates "inference by eye" better than Outcome Uncertainty [@hofman_how_2020].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual precision regarding the estimate of the mean.
*   **The Risk:** Small but statistically significant effects may look visually unimpressive or "insignificant" because the error bars (representing Standard Deviation) will likely overlap substantialy.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using Standard Error (SE) bars because they are smaller and make the data look "cleaner."
*   **Why it fails:** This visually inflates the perceived effect size, causing readers to believe the treatment is far more effective than it actually is [@hofman_how_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the error bars tiny compared to the total range of the y-axis?
*   **The Test:** Check the calculation. Are the bars $\pm 1.96 \times SE$ (Confidence Interval) or $\pm 1.96 \times SD$ (Prediction Interval)? If the goal is showing individual risk/reward, it should be the latter.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the error bars to represent Standard Deviation ($\sigma$) instead of Standard Error ($\frac{\sigma}{\sqrt{n}}$).
*   **Best Fix:** Explicitly label the interval as a "95% Prediction Interval" or "Range of Likely Outcomes" to distinguish it from a confidence interval of the mean.
