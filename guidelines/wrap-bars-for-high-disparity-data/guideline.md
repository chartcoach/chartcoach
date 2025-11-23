---
id: wrap-bars-for-high-disparity-data
title: Wrap Bars for High-Disparity Data
bibliography: references.bib
description: Use wrapped bar charts to improve identification of small values in datasets
  with outliers.
labels:
- chart:bar
- chart:wrapped-bar
- task:identify
- task:find-extremum
- data:categorical
- data:quantitative
- data:low-entropy
- impact:accuracy
---

## The Rule <!-- role: advice -->
Wrap disproportionately large bars onto new lines (creating a "wrapped bar chart") when visualizing categorical data containing extreme outliers or low entropy distributions.

## The Logic <!-- role: reason -->
Standard bar charts often fail when a single value is significantly larger than the rest; the scale compresses the smaller bars, making them difficult to read or compare. Research collated by Zeng and Battle [@zeng_review_2023] indicates that "wrapped" bars—where the largest bar wraps around to start again from the axis—significantly outperform standard bars in accuracy for identification tasks. Specifically, Karduni et al. [@karduni_du_2020] found that for datasets with **low normalized entropy (0.45–0.60)** (i.e., high disparity between values), participants were more accurate in identifying the smallest and largest values using wrapped designs compared to standard linear scaling.

## Where to Apply <!-- role: context -->
*   **User Goal:** Precisely identifying or comparing the smallest values in a dataset that also contains massive outliers (finding extremums).
*   **Data Type:** Quantitative data with **low entropy** (high concentration/disparity), such as "Power Law" or "Long Tail" distributions where one or two categories dwarf the others.
*   **Audience:** Users who need to read exact values from the tail of a distribution without using logarithmic scales.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The dataset has **high entropy** (0.9–1.0), meaning the values are relatively uniform or evenly distributed.
*   **Reason:** The experimental results in [@karduni_du_2020] show that the accuracy advantage of wrapping diminishes or disappears when the data is evenly spread. In these cases, the visual complexity of wrapping offers no utility.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Time.
*   **The Risk:** Users take significantly longer to process wrapped charts. The experimental rankings show that standard bar charts are consistently faster to read than wrapped versions [@karduni_du_2020].

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a "broken axis" or "scale break" to shorten the tall bar.
*   **Why it fails:** This distorts the visual encoding of length, making it impossible to visually compare the large value to the small value accurately. Wrapping preserves the linear scale, maintaining the integrity of the data ratio.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the chart contain a "flatline" of small bars that are barely visible because one large bar is stretching the axis?
*   **The Test:** Calculate the normalized entropy of the dataset. If it is between 0.45 and 0.60, the data is a candidate for wrapping.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** If technical implementation of wrapping is too difficult, separate the outliers into a distinct chart or use a "Zoom" interaction.
*   **Best Fix:** Implement a Du Bois Wrapped Bar Chart, allowing the largest bar to wrap within the chart area, thereby expanding the scale for the smaller values.
