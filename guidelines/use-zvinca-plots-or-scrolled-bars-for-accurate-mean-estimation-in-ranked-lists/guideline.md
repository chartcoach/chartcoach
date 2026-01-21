---
id: use-zvinca-plots-or-scrolled-bars-for-accurate-mean-estimation-in-ranked-lists
title: Use Zvinca Plots or Scrolled Barcharts for Accurate Mean Estimation in Ranked
  Lists
bibliography: references.bib
description: For estimating the average (mean) of all items in a ranked list, Zvinca
  plots and scrolled barcharts are the most accurate options among the tested designs.
labels:
- chart:bar
- chart:point
- task:aggregate
- visual:position
- visual:length
- impact:accuracy
- data:quantitative
- audience:general
- domain:ranked-list
---

## The Rule <!-- role: advice -->

For mean/average estimation across all items in a ranked list, use a Zvinca plot or a scrolled barchart—not packed bars.

## The Logic <!-- role: reason -->

In the extracted aggregate (mean) accuracy ranking, scrolled barchart (E-1) and Zvinca plot (E-6) are tied for best accuracy, both significantly outperforming wrapped bars (E-3), piled bars (E-5), treemap (E-2), and packed bars (E-4).

- **The Principle:** Support global estimation by presenting values in a way that enables more reliable aggregate judgment.
- **The Evidence:** Aggregate accuracy ranking puts (E-1, E-6) first; significance pairs include E-1 and E-6 beating E-3/E-5/E-2/E-4 [@mylavarapuRankedListVisualizationGraphical2019]. The collation work records and operationalizes these rankings for recommendation systems [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimate the average value of the full ranked list (global distribution summary).
- **Data Type:** Many-item ranked list of quantitative values.
- **Audience:** General audiences.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Users must also be fast, and accuracy can be slightly lower.
- **Reason:** While Zvinca (E-6) is fastest for the aggregate task, scrolled barchart (E-1) is slowest for time on aggregate; choosing scrolled barchart may be inappropriate in speed-critical contexts [@mylavarapuRankedListVisualizationGraphical2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** If you choose scrolled barchart for accuracy, you pay a large time cost for the aggregate task.
- **The Risk:** If you choose Zvinca, you may lose accuracy on other tasks (e.g., comparison) relative to length-based designs, per the extracted accuracy ranks.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using packed bars for “dense overview” and expecting it to help with mean estimation.
- **Why it fails:** Packed barchart (E-4) is ranked worst for aggregate accuracy and is significantly worse than the top group [@mylavarapuRankedListVisualizationGraphical2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Users’ mean estimates are widely off (large normalized absolute error).
- **The Test:** Give repeated mean-estimation prompts and compare error distributions across candidate designs.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace packed bars with Zvinca plots for mean-estimation views.
- **Best Fix:** Provide Zvinca as the default for mean estimation (fast and accurate in this study), and reserve scrolled barchart only when users accept slower interaction for accuracy [@mylavarapuRankedListVisualizationGraphical2019; @zengReviewCollationGraphical2023].
