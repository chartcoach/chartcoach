---
id: use-parallel-coordinates-for-outlier-and-cluster-detection
title: Treat Parallel Coordinates as Equal to Scatterplots for Clustering
bibliography: references.bib
description: Parallel Coordinates are as effective as Scatterplots for identifying
  clusters and outliers in multivariate data.
labels:
- chart:parallel-coordinates
- chart:scatterplot
- task:cluster
- task:find-anomalies
- data:multivariate
---

## The Rule <!-- role: advice -->
Do not restrict cluster analysis or outlier detection solely to Scatterplots; utilize Parallel Coordinates Plots (PCP) as a highly effective alternative, especially for high-dimensional data.

## The Logic <!-- role: reason -->
While Scatterplots are the traditional choice for clustering, evidence indicates that Parallel Coordinates perform just as well. The review by [@zeng_review_2023] of the study by [@kanjanabose_multi-task_2015] indicates that for tasks like `cluster` and `find-anomalies` (outlier detection), PCP and Scatterplots (SP) consistently rank in the top tier together, with no statistically significant performance difference in many cases, and both significantly outperforming Data Tables.

*   **The Principle:** Pattern Recognition (Proximity vs. Line Density).
*   **The Evidence:** [@kanjanabose_multi-task_2015]; [@zeng_review_2023]

## Where to Apply <!-- role: context -->
*   **User Goal:** Grouping similar items or finding items that do not fit the pattern.
*   **Data Type:** Multivariate data (more than 2 dimensions) where a single 2D scatterplot cannot show all attributes at once.
*   **Audience:** Analysts exploring dataset structure.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The audience is completely unfamiliar with Parallel Coordinates.
*   **Reason:** While performance is theoretically equal, the learning curve for PCP is steeper. If immediate intelligibility for a lay audience is required, Scatterplots are safer.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Space efficiency (horizontally). PCPs often require significant horizontal width to display multiple axes clearly.
*   **The Risk:** Axis ordering bias. In PCPs, clusters are most visible between adjacent axes; improper axis ordering can hide relationships.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using a Scatterplot Matrix (SPLOM) for high-dimensional clustering without considering PCP.
*   **Why it fails:** SPLOMs break the data into many small views, whereas PCP allows viewing the "profile" of a cluster across all dimensions simultaneously.

## How to Check <!-- role: check -->
*   **Visual Sign:** Are you using a 2D scatterplot to represent 4+ dimensions (using color, size, shape)?
*   **The Test:** Check if users can distinguish clusters based on the 4th or 5th dimension. If not, test a Parallel Coordinates Plot.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Use color encoding in the Scatterplot to denote high-dimensional clusters.
*   **Best Fix:** Implement a Parallel Coordinates Plot to allow users to see the full profile of the outliers or clusters across all dimensions.
