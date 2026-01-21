---
id: use-grouped-columns-for-subcategory-comparisons-not-totals
title: Use Grouped Columns to Compare Subcategories, Not Totals
bibliography: references.bib
description: Choose grouped columns when the goal is comparing subcategory values
  within each group, not comparing totals across groups.
labels:
- chart:grouped-column
- task:compare
- visual:position
- impact:clarity
- data:categorical
- audience:mainstream
- source:datawrapper
---

## The Rule <!-- role: advice -->

Use grouped column charts when you want readers to compare subcategories within each group; do not use them when the key comparison is totals.

## The Logic <!-- role: reason -->

Explain the principle at work here. Connect the rule to human perception or clear communication.

- **The Principle:** Grouping supports within-group comparison of like bars, but makes summing totals mentally effortful.
- **The Evidence:** The post says grouped column charts make comparing subcategories easier, and warns not to use them if you want readers to compare totals [@muth_chart_types_guide_2025].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Comparing two or three values within each category (subcategories).
- **Data Type:** Categorical groups with a small number of subcategories per group.
- **Audience:** Mainstream/general readers [@muth_chart_types_guide_2025].

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** The story is about totals and composition together.
- **Reason:** The post points to stacked bars/columns (or other share-focused options) when totals or part-to-whole structure matter [@muth_chart_types_guide_2025].

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** Totals become implicit; readers must mentally add bars.
- **The Risk:** With many groups, horizontal crowding can reduce label readability [@muth_chart_types_guide_2025].

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Using grouped columns and expecting readers to compare overall heights across groups.
- **Why it fails:** There is no single total bar per group; totals are not directly encoded [@muth_chart_types_guide_2025].

## How to Check <!-- role: check -->

- **Visual Sign:** The viewer must “add up” multiple bars per group to answer the headline.
- **The Test:** If your key sentence contains “total” or “overall,” grouped columns are likely mismatched [@muth_chart_types_guide_2025].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add an explicit total series elsewhere (e.g., separate chart) if totals are essential.
- **Best Fix:** Switch to stacked columns (to show totals + composition) or a different structure that directly encodes totals, depending on the message [@muth_chart_types_guide_2025].
