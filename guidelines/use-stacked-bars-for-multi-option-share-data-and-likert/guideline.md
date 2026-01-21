---
id: use-stacked-bars-for-multi-option-share-data-and-likert
title: Use Stacked Bar Charts for Multi-Option Shares (Including Likert Scales)
bibliography: references.bib
description: Stacked bars are a space-efficient way to show share breakdowns across
  multiple categories, especially survey/Likert results.
labels:
- chart:stacked-bar
- task:show-composition
- visual:length
- impact:space-efficiency
- data:proportional
- audience:mainstream
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use stacked bar charts to show share breakdowns across many categories, especially for survey results with multiple response options (e.g., Likert scales).

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Stacking keeps each category on one line while encoding composition, making the display compact for many categories.
- **The Evidence:** The post recommends stacked bar charts for survey results with multiple response options and Likert scales, noting they’re “nicely space-efficient” [@muth_chart_types_guide_2025].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Comparing distributions of responses across many items (e.g., parties, products, questions).
- **Data Type:** Proportions that sum to 100% per category, multiple response levels.
- **Audience:** Mainstream/general readers [@muth_chart_types_guide_2025].

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** You need to show how these proportions change over time using discrete time points.
- **Reason:** The post highlights stacked column charts as especially good for intuitively showing proportions over several time points [@muth_chart_types_guide_2025].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Precise comparison of internal segments across different bars can be harder than comparing aligned bars.
- **The Risk:** Small segments can be difficult to see or label, especially with many response levels [@muth_chart_types_guide_2025].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Switching to multiple pies/donuts/waffles for each category to “show shares.”
- **Why it fails:** Many small circular charts make cross-category comparisons difficult and can use more space; the post positions stacked bars as a strong, efficient alternative [@muth_chart_types_guide_2025].

## How to Check <!-- role: check -->

- **Visual Sign:** You’re tempted to create a grid of many small share charts to cover all categories.
- **The Test:** If you have many categories and each must show a 100% breakdown, prototype a stacked bar; if it reduces clutter while retaining the message, prefer it [@muth_chart_types_guide_2025].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace repeated pies/donuts with a single stacked bar chart.
- **Best Fix:** Use stacked bars as the default for many-category share breakdowns; switch to stacked columns if the key comparison is over time points [@muth_chart_types_guide_2025].
