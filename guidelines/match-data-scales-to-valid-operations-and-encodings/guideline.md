---
id: match-data-scales-to-valid-operations-and-encodings
title: Classify Data Scales and Only Use Permissible Operations
bibliography: references.bib
description: "Identify each variable\u2019s data scale (nominal, ordinal, interval,\
  \ ratio) and constrain math and encodings accordingly."
labels:
- data:categorical
- data:quantitative
- task:compare
- impact:correctness
- audience:novice
- source:borner-2019
---

## The Rule <!-- role: advice -->

For every variable you plan to analyze or encode, first classify its data scale (nominal, ordinal, interval, ratio) and only apply operations that are valid for that scale.

## The Logic <!-- role: reason -->

Data scales determine which logical/mathematical operations are meaningful; invalid operations produce misleading summaries and visual mappings.

- **The Principle:** Scales-of-measurement constraints
- **The Evidence:** [@bornerDataVisualizationLiteracy2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Computing summaries (e.g., central tendency), ranking, or comparisons that depend on meaningful arithmetic
- **Data Type:** Mixed tables containing categorical and numeric columns
- **Audience:** Anyone preparing data for visualization or interpreting chart computations

## When to Break It <!-- role: exceptions -->

- **Scenario:** You intentionally convert one scale into another (e.g., binning quantitative into ordinal categories)
- **Reason:** The paper notes scale conversion is possible, but you must treat the transformed variable according to its new scale [@bornerDataVisualizationLiteracy2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less flexibility (you may not be able to compute the statistic you wanted)
- **The Risk:** Slower workflow due to more careful preprocessing and documentation

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Treating ordinal labels as interval numbers and averaging them “because they’re coded 1–5”
- **Why it fails:** It assumes equal distance between levels without justification, violating the framework’s scale logic [@bornerDataVisualizationLiteracy2019].

## How to Check <!-- role: check -->

- **Visual Sign:** A chart implies precise numeric differences between categories that are only ordered.
- **The Test:** For each computed value, ask: “Is this operation permitted for this scale?” (e.g., mean requires interval/ratio) [@bornerDataVisualizationLiteracy2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace invalid statistics with scale-appropriate ones (e.g., median for ordinal; mode for nominal).
- **Best Fix:** Re-express the variable (e.g., collect true interval/ratio measurements, or explicitly bin into ordinal) and document the transformation [@bornerDataVisualizationLiteracy2019].
