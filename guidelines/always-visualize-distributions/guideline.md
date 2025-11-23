---
id: always-visualize-distributions
title: Visualize Data Distributions Before Relying on Summary Statistics
bibliography: references.bib
description: Summary statistics can hide vastly different data shapes; always plot
  the raw data.
labels:
- chart:scatter
- task:explore
- impact:accuracy
- data:statistical
- audience:analyst
---

## The Rule <!-- role: advice -->
Always generate a scatter plot or visual distribution of your data before drawing conclusions from summary statistics alone. Do not assume that identical mean, standard deviation, and correlation imply identical data structure.

## The Logic <!-- role: reason -->
Summary statistics are descriptive reductions, not unique fingerprints. Through a technique called simulated annealing, it is computationally easy to generate vastly different graphical shapes (such as a star, a circle, or a dinosaur) that share identical summary statistics to two decimal places. As demonstrated by the "Datasaurus Dozen," relying solely on numerical summaries can lead to missing obvious patterns or outliers.
*   **The Principle:** Statistical Equivalence vs. Graphical Distinction
*   **The Evidence:** [@matejka_same_2017]

## Where to Apply <!-- role: context -->
*   **User Goal:** Exploratory Data Analysis (EDA) or validating statistical models.
*   **Data Type:** Continuous quantitative variables (x, y) typically summarized by mean and standard deviation.
*   **Audience:** Data scientists, analysts, and researchers interpreting new datasets.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** extremely large datasets (Big Data).
*   **Reason:** Plotting raw scatter points for millions of rows causes overplotting, rendering the chart useless. In these cases, use density plots, heatmaps, or hexbins instead of raw scatter plots.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Visualizing raw data requires more screen space and processing power than a simple table of summary numbers.
*   **The Risk:** The visualization may look "messy" or unstructured if the data is truly random, potentially tempting the viewer to find patterns where none exist (apophenia).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Calculating more advanced statistics (like kurtosis) without plotting.
*   **Why it fails:** While helpful, even advanced metrics can be mimicked or shared by visually distinct datasets. As the paper notes, "numerical calculations are exact, but graphs are rough," yet looking at the data is necessary to confirm the calculations apply effectively [@matejka_same_2017].

## How to Check <!-- role: check -->
*   **Visual Sign:** You have a table of means and standard deviations in your report, but no accompanying chart showing the spread of points.
*   **The Test:** If you swapped your data for a picture of a dinosaur with the same stats, would your current analysis detect the difference?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Generate a standard scatter plot alongside your statistical table.
*   **Best Fix:** Use a "small multiples" display to show the distribution of several variables simultaneously to ensure no structural anomalies exist (like the "X" shape or outliers shown in the paper).
