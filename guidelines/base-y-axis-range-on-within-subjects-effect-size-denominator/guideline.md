---
id: base-y-axis-range-on-within-subjects-effect-size-denominator
title: Base the Y-Axis Range on the Within-Subjects Effect-Size Denominator
bibliography: references.bib
description: For within-subject designs, set the y-axis range using the denominator
  of the within-subject effect size so the visual scale matches the effect-size metric.
labels:
- chart:bar
- chart:line
- task:judge-effect-size
- visual:scale
- impact:calibration
- data:repeated-measures
- audience:novice
- domain:within-subjects
- source:wittGraphConstruction2019
---

## The Rule <!-- role: advice -->

For within-subject graphs, set the y-axis range as a function of the denominator used for the within-subject standardized effect size (e.g., Cohen’s d_z), using an SD-based span analogous to ~1–2 denominator units (aim ~1.5) [@wittGraphConstruction2019].

## The Logic <!-- role: reason -->

If effect size interpretation depends on a specific standardization (the denominator), the visual scaling should match that standardization so that “looks big/small” aligns with “is big/small” in the metric readers use [@wittGraphConstruction2019].

- **The Principle:** Metric-consistent scaling for visual–conceptual alignment
- **The Evidence:** The paper argues the SD-based axis rule generalizes to within-subject designs by tying the axis to the within-subject denominator rather than the raw SD [@wittGraphConstruction2019].

## Where to Apply <!-- role: context -->

- **User Goal:** Judging the magnitude of within-subject effects (e.g., pre/post, repeated conditions).
- **Data Type:** Paired/repeated measures where standardized effects use a within-subject denominator (e.g., d_z) [@wittGraphConstruction2019].
- **Audience:** Readers relying on the figure to infer effect magnitude categories [@wittGraphConstruction2019].

## When to Break It <!-- role: exceptions -->

- **Scenario:** Mixed designs (between- and within-subject factors) where it is unclear which effect you intend to emphasize.
- **Reason:** You must choose which denominator best matches the effect you want visually emphasized [@wittGraphConstruction2019].
- **Scenario:** The denominator-based scaling would exclude key plotted elements (e.g., uncertainty intervals) or create nonsensical bounds.
- **Reason:** Axes must contain displayed data/uncertainty and remain meaningful [@wittGraphConstruction2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** More computation/decision-making (you must select and compute the relevant denominator).
- **The Risk:** If you pick the “wrong” denominator for the story, you may visually emphasize a different effect than intended in a mixed design [@wittGraphConstruction2019].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Using the raw-score SD for within-subject plots even though the reported effect size is within-subject standardized.
- **Why it fails:** The visual scale no longer matches the metric used to interpret effect size [@wittGraphConstruction2019].
- **The Wrong Fix:** Copying a between-subject axis rule without adjusting for within-subject standardization.
- **Why it fails:** It can miscalibrate “how big it looks” relative to the within-subject effect-size definition [@wittGraphConstruction2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Within-subject effects look disproportionately large/small relative to how they are described with within-subject standardized effects.
- **The Test:** Verify that the y-axis span equals roughly 1–2 units of the within-subject effect-size denominator (target ~1.5) [@wittGraphConstruction2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Recompute y-limits around the grand mean using ±0.75 × (within-subject denominator).
- **Best Fix:** Standardize your plotting code to compute the intended within-subject denominator and set y-limits from it, documenting the choice for mixed designs [@wittGraphConstruction2019].
