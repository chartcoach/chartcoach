---
id: align-visuals-with-insight-needs
title: Align Visual Encodings with Insight Needs
bibliography: references.bib
description: Select specific combinations of graphic variables based on whether the
  user needs to identify outliers, trends, or clusters.
labels:
- task:identify-outliers
- task:identify-trends
- task:cluster
- visual:color
- visual:position
---

## The Rule <!-- role: advice -->
Tailor your choice of graphic variables (position, size, color) to the specific "insight need" (outlier, trend, or cluster) you want to highlight. Do not use a "one size fits all" encoding strategy.

## The Logic <!-- role: reason -->
Different visual features support different perceptual tasks. Empirical research allows us to order graphic variables by effectiveness for specific visual queries.
*   **The Principle:** Task-Based Effectiveness.
*   **The Evidence:** [@borner_data_2019] references Szafir et al., showing that specific combinations (like position + size + color) support different insight needs. For example, highlighting outliers requires different emphasis than revealing clustering.

## Where to Apply <!-- role: context -->
*   **User Goal:** Analyzing data for specific patterns (e.g., "Where are the anomalies?" vs. "What is the general direction?").
*   **Data Type:** Multidimensional data (e.g., scatterplots with size/color coding).
*   **Audience:** Analysts performing exploratory data analysis.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** General overview dashboards.
*   **Reason:** If the user's intent is unknown, you may need a balanced encoding that doesn't bias toward one specific pattern (like outliers) at the expense of others (like general trends).

## The Price <!-- role: costs -->
*   **The Sacrifice:** You may need to create multiple versions of a chart or add interactive controls to change encodings based on the task.
*   **The Risk:** Optimizing for one task (e.g., outlier detection) might obscure another (e.g., density/clustering) if the variable choices conflict.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Using the same scatterplot encoding for all analysis tasks.
*   **Why it fails:** A design optimized for reading exact values (position) might not be sufficiently salient for spotting a single outlier if color/luminance isn't used effectively [@borner_data_2019].

## How to Check <!-- role: check -->
*   **Visual Sign:** The chart looks "flat" or uniform.
*   **The Test:** Ask the question: "Can I spot the [outlier/trend/cluster] in less than 2 seconds?" If not, the encoding priority is likely mismatched to the task.

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Change the color scheme (e.g., diverging color) to highlight the specific pattern of interest.
*   **Best Fix:** Redesign the mapping of data columns to visual channels (x, y, size, color) based on the specific insight need defined in the stakeholder phase (Table 1 in [@borner_data_2019]).
