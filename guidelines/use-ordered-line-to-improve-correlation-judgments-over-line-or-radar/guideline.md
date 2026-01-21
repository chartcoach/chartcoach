---
id: use-ordered-line-to-improve-correlation-judgments-over-line-or-radar
title: Use Ordered Line Charts to Improve Correlation Judgments
bibliography: references.bib
description: When using line-based encodings, sorting by x (ordered line) improves
  correlation discrimination relative to unsorted line or radar for positive correlations.
labels:
- chart:line
- chart:ordered-line
- chart:radar
- task:judge-correlation
- impact:accuracy
- data:bivariate
- audience:designer
- encoding:order
---

## The Rule <!-- role: advice -->

If you must show correlation with a line-based chart, sort the x-axis by the x variable (use an ordered line chart) instead of an unsorted line or radar chart.

## The Logic <!-- role: reason -->

Adding an explicit order (sorting) changes the visual structure and can make correlation-related patterns easier to discriminate. In the study, ordered line charts significantly outperformed both standard line charts and radar charts for positive correlations in JND-based discrimination tasks.

- **The Principle:** Ordering as a design factor that alters discrimination thresholds
- **The Evidence:** For positive correlation, ordered line outperformed line and radar (both p < 0.001), and radar outperformed line (p = 0.0017) [@harrisonRankingVisualizationsCorrelation2014a].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare correlation strengths using line-like representations.
- **Data Type:** Two quantitative variables represented as lines with an imposed x-order.
- **Audience:** Designers using line-based charts due to tool constraints or stylistic consistency.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The x-axis order has semantic meaning you cannot reorder (e.g., you cannot sort because the sequence itself is the message).
- **Reason:** The “ordered line” advantage depends on sorting by x; if order cannot change, you cannot apply this rule as tested [@harrisonRankingVisualizationsCorrelation2014a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Sorting may remove meaningful original sequencing and can change what the chart communicates beyond correlation.
- **The Risk:** Users may misinterpret the sorted order as a meaningful sequence if not clearly indicated [@harrisonRankingVisualizationsCorrelation2014a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching from line to radar hoping radial form alone will solve correlation readability.
- **Why it fails:** Radar was better than line in the study, but ordered line was best among these; skipping ordering leaves performance on the table [@harrisonRankingVisualizationsCorrelation2014a].

## How to Check <!-- role: check -->

- **Visual Sign:** In an unsorted line chart, the plot looks “noisy” and users rely on vague impressions rather than consistent discrimination.
- **The Test:** Compare JND/Weber-model predictions for line-positive vs ordered-line-positive; if ordered line is lower in your r-range, the unsorted line choice violates the rule [@harrisonRankingVisualizationsCorrelation2014a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Sort the x-axis by the x variable to create an ordered line view for correlation judgment.
- **Best Fix:** If correlation judgment is the core task, replace the line-based view with a scatterplot (lower JND overall in the study) or validate alternatives with Weber/JND modeling [@harrisonRankingVisualizationsCorrelation2014a].
