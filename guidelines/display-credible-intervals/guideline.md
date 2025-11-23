---
id: display-credible-intervals
title: Display Credible Intervals Over Confidence Intervals
bibliography: references.bib
description: Expand uncertainty bounds to include methodological weaknesses and expert
  judgment, not just statistical sampling error.
labels:
- chart:error-bars
- chart:box-plot
- task:estimation
- data:statistical
- impact:accuracy
---

## The Rule <!-- role: advice -->
When plotting error bars or uncertainty ranges, present "credible intervals" that incorporate assessments of internal validity, external validity, and the strength of the basic science—do not rely solely on standard statistical confidence intervals derived from the data's variance.

## The Logic <!-- role: reason -->
*   **The Principle:** Total Uncertainty Assessment.
*   **The Evidence:** [@fischhoff_communicating_2014] notes that standard confidence intervals only capture observed variability. "Credible intervals" are wider when scientists question the underlying science or methods, and narrower when strong theory discounts anomalous observations. This provides a more honest picture of what is actually known (Table 2, Step vi).

## Where to Apply <!-- role: context -->
*   **User Goal:** Making high-stakes decisions where "surprises" (outcomes outside the predicted range) are costly.
*   **Data Type:** Forecasts or estimates derived from imperfect models or studies (e.g., climate sensitivity, drug efficacy).
*   **Audience:** Decision-makers who need to know the true range of likely outcomes, not just the statistical artifacts.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Reporting raw experimental results to other scientists for pure replication purposes.
*   **Reason:** In pure scientific discourse, separating the raw statistical error from the "subjective" expert assessment may be preferred for transparency.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Perceived precision. Credible intervals are often wider than confidence intervals, which can make the science look "weaker" or less certain.
*   **The Risk:** Scientists may be reluctant to express these intervals because they fear being evaluated unfairly if the outcome falls outside a narrow range.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using standard 95% Confidence Intervals ($1.96 \times SE$).
*   **Why it fails:** It ignores systematic biases (e.g., population bias, scenario bias) that are often larger than sampling error.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are the error bars symmetric and calculated purely by formula?
*   **The Test:** Does the range include the possibility of methodological failure (e.g., the model is wrong), or just data noise?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Widen the error bars visually and label them "Estimated Uncertainty" rather than "Statistical Error."
*   **Best Fix:** Follow the protocol in Table 2 of the paper: Elicit expert judgments on validity and pedigree, and plot the resulting credible interval that bounds the true value with X% certainty.
