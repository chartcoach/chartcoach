---
id: visualize-uncertainty-discrete-recall
title: Use Discrete Outcomes for Distribution Recall
bibliography: references.bib
description: Represent probability distributions as sets of discrete outcomes to improve
  user memory of the shape.
labels:
- chart:dot-plot
- chart:histogram
- task:recall
- visual:shape
- impact:retention
- audience:novice
---

## The Rule <!-- role: advice -->
When visualizing sampling distributions or uncertainty for non-experts, represent the probability as a set of discrete outcomes (e.g., a stack of balls or distinct points) rather than a continuous probability density curve.

## The Logic <!-- role: reason -->
Discrete-outcome visualizations improve a user's ability to recall the sampling distribution later. By breaking the abstract concept of probability into a concrete set of countable objects (frequency format), the visualization reduces the distribution to a shape constructed from a small number of elements. This makes the "shape" easier to encode in memory than an abstract curve [@hullman_imagining_2018].

*   **The Principle:** Shape Memory via Simplification.
*   **The Evidence:** In a controlled study, participants who viewed discrete visualizations (specifically with 20 outcomes) were better at graphically reproducing the distribution later compared to those who viewed continuous density plots [@hullman_imagining_2018].

## Where to Apply <!-- role: context -->
*   **User Goal:** When the primary goal is for the audience to remember the specific uncertainty profile (shape and location) of a reported effect after they have looked away.
*   **Data Type:** Univariate probability distributions (e.g., sampling distributions of an experimental effect).
*   **Audience:** Non-statisticians or lay audiences who may struggle to interpret or recall abstract probability density functions.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user needs to make precise probability estimates or predictions about *new* scenarios (transfer tasks).
*   **Reason:** The study found that while discrete plots helped recall, they actually led to *worse* accuracy when users had to estimate uncertainty for a *new* experiment in a different domain, possibly because users misunderstood the weight of individual outcomes [@hullman_imagining_2018].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Precision. Discrete plots with small numbers of outcomes (e.g., 20) cannot convey the same granular detail as a high-resolution density plot.
*   **The Risk:** Users might misinterpret the meaning of individual "balls" or "dots" if the total number is not intuitive (e.g., thinking one dot represents a specific person rather than a probability weight).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using too many discrete points (e.g., 100+).
*   **Why it fails:** The paper suggests that limiting the number of outcomes (e.g., to 20) may facilitate the "memorability via shape" effect, whereas too many points effectively blur back into a continuous mass [@hullman_imagining_2018].

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart look like a smooth curve (continuous) or a countable stack of objects (discrete)?
*   **The Test:** Ask a user to view the chart, hide it, and then draw what they saw. Discrete formats should yield more accurate drawings of the distribution's location and spread.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Bin the data and use a standard histogram.
*   **Best Fix:** Use a "quantile dotplot" or "icon array" style visualization where the distribution is built from a set of ~20 to 50 distinct, countable circles or icons.
