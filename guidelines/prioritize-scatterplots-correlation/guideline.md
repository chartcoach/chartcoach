---
id: prioritize-scatterplots-correlation
title: Prioritize Scatterplots for Depicting Correlation
bibliography: references.bib
description: Scatterplots provide the highest perceptual precision for judging correlation
  among common visualization types.
labels:
- chart:scatterplot
- task:correlation
- visual:position
- impact:precision
- data:quantitative
- audience:general
---

## The Rule <!-- role: advice -->
When the primary task is judging or comparing correlation between two variables, use a scatterplot.

## The Logic <!-- role: reason -->
Research applying Weber's Law to visualization demonstrates that scatterplots consistently outperform other chart types (such as parallel coordinates, stacked charts, and line charts) in perceptual precision.
*   **The Principle:** **Weber's Law of Correlation Perception.** The human ability to discriminate differences in correlation follows a linear relationship (Weber's Law). Scatterplots have the lowest Just-Noticeable Differences (JNDs) and the highest correlation coefficients in these perceptual models, making them the most effective standard [@harrison_ranking_2014].
*   **The Evidence:** In comparative experiments, scatterplots showed symmetric high performance for both positively and negatively correlated data, serving as the baseline against which all other visualizations were ranked [@harrison_ranking_2014].

## Where to Apply <!-- role: context -->
This advice applies broadly to statistical data exploration and communication.
*   **User Goal:** Accurately perceiving the strength of the relationship between two variables ($r$).
*   **Data Type:** Bivariate quantitative data.
*   **Audience:** Users who need to assess the tightness of a relationship without being misled by visual artifacts.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** Dealing specifically with **negatively** correlated data in a multivariate context.
*   **Reason:** Parallel coordinates plots performed just as well as scatterplots for detecting negative correlations (though they failed at positive ones) [@harrison_ranking_2014].

## The Price <!-- role: costs -->
*   **The Sacrifice:** Space efficiency when visualizing more than two variables (requires a scatterplot matrix).
*   **The Risk:** Overplotting if the dataset is extremely dense, though the study controlled for standard density ($n=100$).

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using line charts or radar charts to "connect" the data points to show a relationship.
*   **Why it fails:** These charts introduce visual noise (e.g., "spikiness") that increases the perceptual error (JND) compared to the clean bounding box perception of a scatterplot [@harrison_ranking_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using lines, areas, or stacked bars to show how two variables move together?
*   **The Test:** If you replace the visualization with a scatterplot, does the relationship ($r$ value) become immediately more obvious?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the chart type to a scatterplot.
*   **Best Fix:** If visualizing multiple variables, use a scatterplot matrix (SPLOM) rather than a standard parallel coordinates plot, unless the correlations are known to be negative.
