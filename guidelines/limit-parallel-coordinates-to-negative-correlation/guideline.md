---
id: limit-parallel-coordinates-to-negative-correlation
title: Restrict Parallel Coordinates to Negative Correlation Tasks
bibliography: references.bib
description: Avoid parallel coordinates for positive correlations due to poor perceptual
  precision; reserve them for negative correlations.
labels:
- chart:parallel-coordinates
- task:correlate
- visual:angle
- impact:precision
- data:multivariate
---

## The Rule <!-- role: advice -->
Only use Parallel Coordinates for correlation tasks if you are specifically looking for *negative* correlations. Avoid them for identifying or comparing *positive* correlations.

## The Logic <!-- role: reason -->
Parallel coordinates exhibit "asymmetric performance" based on the direction of the correlation. Research reviewed in [@zeng_review_2023] highlights that while scatterplots handle both directions well, parallel coordinates fail at positive correlations. The experimental data from [@harrison_ranking_2014] indicates that for negative correlations (where lines cross), parallel coordinates can rank as highly as scatterplots (e.g., Design E-32 ranked #1 for low correlation tasks). However, for positive correlations (where lines are parallel), the "Just Noticeable Difference" increases, making it much harder for users to detect the strength of the relationship.

## Where to Apply <!-- role: context -->
*   **User Goal:** Identifying inverse relationships (negative correlation) in multivariate data.
*   **Data Type:** Multivariate quantitative data where axes can be re-ordered.
*   **Audience:** Analysts looking for specific inverse patterns.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** You are using Parallel Coordinates for tasks other than correlation, such as cluster identification or value retrieval.
*   **Reason:** This guideline is specific to the *correlate* task.

## The Price <!-- role: costs -->
*   **The Sacrifice:** You lose the ability to uniformly assess relationships across all variable pairs.
*   **The Risk:** Users will significantly underestimate or misinterpret positive correlations between adjacent axes.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Keeping a fixed axis order in a Parallel Coordinate plot without allowing users to flip or reorder axes.
*   **Why it fails:** Adjacent axes with positive correlation will result in a "tunnel" pattern that is perceptually difficult to quantify compared to the "bowtie" pattern of negative correlation [@harrison_ranking_2014].

## How to Check <!-- role: check -->
*   **Visual Sign:** Do you have adjacent axes with parallel lines (positive correlation) that you expect users to compare?
*   **The Test:** Check if the lines between axes mostly run parallel (bad for correlation judgment) or cross over (good for correlation judgment).

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Allow users to invert axis scales to turn positive correlations (parallel lines) into visual negative correlations (crossing lines).
*   **Best Fix:** Supplement the view with a scatterplot matrix (SPLOM) for precise correlation estimation.
