---
id: szafir-2018-transparent-aggregation
title: Show Distributions Alongside Summary Statistics
bibliography: references.bib
description: Avoid within-the-bar bias and hidden patterns by visualizing distributions
  (e.g., violin plots) rather than just means.
labels:
- chart:bar
- chart:violin
- data:statistical
- impact:transparency
- bias:within-the-bar
---

## The Rule <!-- role: advice -->
Visualize data distributions or individual points rather than relying solely on summary statistics (like mean bars with error whiskers).

## The Logic <!-- role: reason -->
Summary statistics can hide critical variations (e.g., Anscombe's Quartet: identical statistics, vastly different patterns). Additionally, using bar charts for statistics causes "within-the-bar bias," where users incorrectly assume values inside the bar are more likely than those outside it.
*   **The Principle:** Ensemble Coding & Within-the-Bar Bias.
*   **The Evidence:** [@szafir_good_2018] highlights that our brains are optimized to estimate properties of a distribution (ensemble coding) from visual groups, which is prevented when the data is hidden behind a summary bar.

## Where to Apply <!-- role: context -->
*   **User Goal:** Understanding the reliability, spread, or nature of a dataset.
*   **Data Type:** Large collections of data points where aggregation is usually applied.
*   **Audience:** Scientific or analytical audiences who need to assess validity.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Explicit Aggregation Tasks.
*   **Reason:** When the aggregate statistic *is* the only data point that matters for the decision, and the underlying distribution is irrelevant or standard [@szafir_good_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visual complexity increases. Summary bars are cleaner and simpler than violin plots or strip plots.
*   **The Risk:** "Hairballs" or clutter if the dataset is massive and every point is plotted without filtering or sampling.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Adding error bars to a bar chart.
*   **Why it fails:** This does not solve the "within-the-bar bias" and often obscures the shape (e.g., bimodal vs. normal) of the distribution.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using a solid shape (bar) to represent a range of probabilities?
*   **The Test:** If you removed the bar and plotted the points, would the conclusion change? (e.g., is the data actually bimodal?)

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Overlay the raw data points on top of the bar/summary.
*   **Best Fix:** Use a **Violin Plot** (shows density/shape) or **Gradient Plot** to transparently communicate the distribution [@szafir_good_2018].
