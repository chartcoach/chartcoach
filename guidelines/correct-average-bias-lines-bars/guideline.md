---
id: correct-average-bias-lines-bars
title: Annotate Averages in Line and Bar Charts
bibliography: references.bib
description: Users systematically misjudge averages in lines and bars; explicit annotation
  is required to correct this.
labels:
- chart:bar
- chart:line
- task:aggregate
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
---

## The Rule <!-- role: advice -->
Explicitly mark or label the average value on line and bar charts rather than relying on users to visually estimate the mean.

## The Logic <!-- role: reason -->
Human visual processing is prone to systematic directional biases when estimating averages from standard charts.
*   **The Principle:** Systematic Bias. Users consistently **underestimate** the average position of a line graph (perceiving it lower than it is) and **overestimate** the average height of a set of bars (perceiving it higher than it is).
*   **The Evidence:** Experiments by Xiong et al. [@xiong_biased_2020] confirmed that line positions are underestimated while bar positions are overestimated. This finding is collated by Zeng et al. [@zeng_review_2023] as a key example of systematic bias in graphical perception tasks involving aggregation.

## Where to Apply <!-- role: context -->
This applies to static visualizations where the user needs to derive a summary statistic from the visual shape.
*   **User Goal:** Estimating the mean or central tendency of a dataset ("Aggregate" task).
*   **Data Type:** Quantitative data series displayed as lines or bars.
*   **Chart Type:** Simple line charts or bar charts.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The user is performing a specific value retrieval task (reading a single point) rather than a summary task.
*   **Reason:** The bias specifically affects the perception of the *average* position, not necessarily the lookup of individual data points [@xiong_biased_2020].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Adding a reference line or text annotation increases the ink ratio and may add slight visual clutter.
*   **The Risk:** Without the annotation, users will walk away with an incorrect mental model of the data's magnitude (believing line data is lower and bar data is higher than reality).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Relying solely on gridlines.
*   **Why it fails:** Even with reference gridlines, the cognitive process of averaging the visual mass is subject to the biases described by Xiong et al. [@xiong_biased_2020].

## How to Check <!-- role: check -->
*   **Visual Sign:** A line or bar chart intended for summary analysis lacking a specific indicator for the mean.
*   **The Test:** Ask a user to point to where they think the average value is. Compare their guess to the actual calculated mean.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a text label stating the average value in the title or caption.
*   **Best Fix:** Plot a reference line (e.g., a dashed rule) across the chart at the exact mean value to override the perceptual bias.
