---
id: limit-categorical-palettes-to-seven-or-fewer
title: Keep Categorical Palettes to Seven Colors or Fewer
bibliography: references.bib
description: Avoid using more than seven categorical colors; regroup categories or
  change chart type when you need more.
labels:
- chart:bar
- task:categorize
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:basic
---

## The Rule <!-- role: advice -->

Do not use more than seven distinct colors to encode categories; if you need more, regroup categories or use a different chart type.

## The Logic <!-- role: reason -->

As the number of category colors increases, readers can’t distinguish and remember them easily and must repeatedly consult the key, slowing comprehension [@muth_colors_2018].

- **The Principle:** Reduce cognitive load from color-to-category mapping.
- **The Evidence:** [@muth_colors_2018]

## Where to Apply <!-- role: context -->

- **User Goal:** Identify categories quickly without frequent legend lookups.
- **Data Type:** Categorical series (multiple groups, parties, countries, products, etc.).
- **Audience:** Broad audiences reading quickly.

## When to Break It <!-- role: exceptions -->

- **Scenario:** The visualization is designed for slow, expert analysis where legend-checking is acceptable.
- **Reason:** The “quick read” constraint is relaxed, though Muth still advises reconsidering the design if many colors are required [@muth_colors_2018].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less granular categorization on a single view (you may need to combine groups).
- **The Risk:** Grouping categories can hide meaningful distinctions [@muth_colors_2018].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more and more slightly different hues and hoping the legend will carry the meaning.
- **Why it fails:** Readers lose track and spend more time consulting the key [@muth_colors_2018].

## How to Check <!-- role: check -->

- **Visual Sign:** A long legend and many similarly salient colored marks.
- **The Test:** If readers need to look back and forth between plot and legend repeatedly to identify categories, you’ve exceeded practical color capacity [@muth_colors_2018].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Combine low-importance categories into “Other” or group by higher-level categories.
- **Best Fix:** Switch to a chart type that reduces simultaneous category color encoding (e.g., small multiples or a different structure) [@muth_colors_2018].
