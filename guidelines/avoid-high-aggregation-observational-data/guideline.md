---
id: avoid-high-aggregation-observational-data
title: Avoid High Data Aggregation for Observational Data
bibliography: references.bib
description: Limit data aggregation (binning) to prevent viewers from assuming causal
  links in observational datasets.
labels:
- data:aggregation
- impact:bias
- task:analysis
- visual:encoding
---

## The Rule <!-- role: advice -->
Do not aggregate data into a small number of bins (e.g., only two groups) if you wish to avoid implying causality.

## The Logic <!-- role: reason -->
High levels of data aggregation—such as binning a dataset into just two groups (e.g., "High vs. Low")—are strongly associated with higher perceived causality. When data is heavily summarized, it hides the natural variability and overlap between groups, making the relationship appear cleaner and more deterministic than it actually is. Two-bar graphs, in particular, are often associated with controlled experiments (Condition A vs. Condition B), triggering a "schema" of causation in the viewer's mind.
*   **The Principle:** Aggregation Effect
*   **The Evidence:** [@xiong_illusion_2020]

## Where to Apply <!-- role: context -->
This applies when visualizing large datasets where variables are continuous but might be arbitrarily grouped for display.
*   **User Goal:** Preventing misinformation or exaggeration of a relationship's strength.
*   **Data Type:** Continuous variables that are being converted into categorical bins.
*   **Audience:** Lay audiences who may not understand the difference between "correlation" and "causation."

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Controlled Experiments (A/B Tests).
*   **Reason:** If you are presenting the results of a randomized control trial, a highly aggregated 2-bar chart is an appropriate convention to show the causal effect of the treatment.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Simplicity. Increasing the number of bins (e.g., from 2 to 8 or 16) makes the chart more complex and harder to scan quickly.
*   **The Risk:** The "signal" of the correlation might get lost if the data is too granular or noisy.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a 2-bar chart but adding a text disclaimer saying "Correlation is not causation."
*   **Why it fails:** Viewers often ignore text caveats when the visual pattern strongly suggests a simple cause-and-effect story (e.g., "Short bar leads to Tall bar") [@xiong_illusion_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you representing a complex continuous trend with only two or three bars?
*   **The Test:** Count the bins. If there are fewer than 4 bins for a continuous variable, you are maximizing the risk of a causal illusion.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Increase the number of bins (e.g., show data by deciles instead of a binary split).
*   **Best Fix:** Show the distribution of the underlying data using box plots, violin plots, or strip plots instead of simple mean bars.
