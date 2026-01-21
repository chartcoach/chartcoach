---
id: use-color-to-separate-groups-for-mean-comparisons-in-scatterplots
title: Use Color to Separate Groups for Mean Comparisons
bibliography: references.bib
description: When viewers must compare average values across groups in a scatterplot,
  distinguish groups with color rather than shape for higher accuracy.
labels:
- chart:scatter
- task:compare
- task:summarize
- visual:color
- visual:shape
- impact:accuracy
- data:multiclass
- audience:general
---

## The Rule <!-- role: advice -->

Use color (e.g., orange vs. purple) to distinguish groups when you want people to compare group means in a scatterplot; do not rely on shape alone.

## The Logic <!-- role: reason -->

- **The Principle:** Feature choice changes ensemble-summary accuracy.
- **The Evidence:** In studies of multiclass scatterplots, mean-position comparisons were more accurate when groups were distinguished by color than by shape, as surveyed in [@szafirFourTypesEnsemble2016a].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare average (mean) position/value between two or more groups.
- **Data Type:** Dense point clouds with multiple classes in a scatterplot.
- **Audience:** Analysts or general readers making quick summary judgments.

## When to Break It <!-- role: exceptions -->

- **Scenario:** When color cannot reliably encode categories in your context (e.g., printing constraints or intentionally minimizing class salience).
- **Reason:** The rule’s benefit depends on the viewer being able to use color to select and summarize classes [@szafirFourTypesEnsemble2016a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Consumes a powerful channel (color) that you might need for another variable.
- **The Risk:** Too many colored classes can create visual complexity, making selection and interpretation harder even if mean comparison remains feasible [@szafirFourTypesEnsemble2016a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Switching to many different shapes for classes and assuming it will support accurate mean comparisons.
- **Why it fails:** Shape-based separation was less accurate than color-based separation for mean judgments in the surveyed visualization results [@szafirFourTypesEnsemble2016a].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers hesitate or disagree widely about which group is “higher on average.”
- **The Test:** Ask someone to answer “Which group’s average y is higher?” in 1–2 seconds; if accuracy drops with shape-coded classes, you likely violated the rule [@szafirFourTypesEnsemble2016a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Recode class membership from shape to color.
- **Best Fix:** Use color for class plus keep shapes minimal/uniform so other encodings don’t interfere with the summary task [@szafirFourTypesEnsemble2016a].
