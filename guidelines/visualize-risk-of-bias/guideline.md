---
id: visualize-risk-of-bias
title: Visualize the Risk of Bias in Source Data
bibliography: references.bib
description: Do not just visualize the data values; create a companion visualization
  that summarizes the methodological flaws (risk of bias) of the studies producing
  that data.
labels:
- chart:heatmap
- chart:stacked-bar
- task:assess-quality
- data:meta-analysis
- impact:trust
---

## The Rule <!-- role: advice -->
Accompany statistical summaries with a visual audit of the data's "pedigree." Create a display (such as a color-coded bar chart) that rates the risk of bias for specific categories like selection bias, attrition, blinding, and data reporting.

## The Logic <!-- role: reason -->
*   **The Principle:** Uncertainty Assessment / NUSAP (Numeral Unit Spread Assessment Pedigree).
*   **The Evidence:** [@fischhoff_communicating_2014] highlights that uncertainty arises from poor data quality (e.g., small samples, unblinded trials) just as much as statistical variance. Visualizing these flaws prevents users from placing unwarranted faith in flawed results (Figure 2).

## Where to Apply <!-- role: context -->
*   **User Goal:** Evaluating the strength of evidence in meta-analyses, clinical trials, or policy reviews.
*   **Data Type:** Aggregated study results where methodology varies.
*   **Audience:** Researchers, regulators, or skepticism-prone decision-makers.

## When to Break It <!-- role: exceptions -->
*   **Scenario:** The data source is singular, highly controlled, and the methodology is standard/perfect (rare).
*   **Reason:** If there is no variation in data quality, the chart adds no information.

## The Price <!-- role: costs -->
*   **The Sacrifice:** Space. This requires a secondary chart dedicated solely to metadata/quality.
*   **The Risk:** It requires expert judgment to assess "risk of bias," which can be subjective if not based on a standard protocol like Cochrane’s.

## Common Mistakes <!-- role: mistakes -->
*   **The Wrong Fix:** Discussing data quality only in the footnotes or text methods section.
*   **Why it fails:** Users suffering from "outcome bias" will look at the results chart and ignore the text caveats.

## How to Check <!-- role: check -->
*   **Visual Sign:** Does the dashboard show a precise number (e.g., "20% savings") without visually indicating that the study was unblinded or had high attrition?
*   **The Test:** Can the viewer instantly see if the data comes from high-quality randomized experiments or low-quality observational guesses?

## How to Fix <!-- role: fix -->
*   **Quick Fix:** Add a text label "Low Confidence" or "High Uncertainty" next to the chart.
*   **Best Fix:** Replicate the "Risk of Bias" visualization (Fig 2 in the paper): a stacked bar chart showing the proportion of data sources with High, Low, or Unknown risk of bias across specific methodological criteria.
