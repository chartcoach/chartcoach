---
id: prefer-matlab-or-r-style-scatterplots-for-accurate-outlier-detection
title: Prefer MATLAB- or R-Style Scatterplot Defaults for Accurate Outlier Detection
bibliography: references.bib
description: If outlier-finding accuracy matters most, prefer common fixed scatterplot
  defaults (MATLAB/R) over the tested optimized design.
labels:
- chart:scatter
- task:find-anomalies
- visual:position
- impact:accuracy
- data:quantitative
- audience:novice
- source:literature-collation
- complexity:basic
---

## The Rule <!-- role: advice -->

When users need to find outliers accurately in a scatterplot, prefer MATLAB- or R-generated scatterplot defaults over the tested algorithm-generated optimized design.

## The Logic <!-- role: reason -->

Some defaults can yield higher correctness on outlier-finding tasks even if they are slower.

- **The Principle:** Task performance differs across preset design choices even when the visual encoding stays the same (PX/PY scatterplot); pick the preset aligned to the metric you care about.
- **The Evidence:** For the *find-anomalies* task accuracy, MATLAB (E-2) and R (E-3) ranked above the algorithm-generated scatterplot (E-1), and both were significantly more accurate than E-1 in the reported pairwise significance results [@micallefPerceptualOptimizationVisual2017]. This ranking is captured in the collation for recommendation purposes [@zengReviewCollationGraphical2023].

## Where to Apply <!-- role: context -->

- **User Goal:** Correctly identifying which points are outliers/anomalies (accuracy-first).
- **Data Type:** Two quantitative variables displayed as a scatterplot (positionX/positionY, linear scales).
- **Audience:** Analysts or decision-makers where false positives/negatives are costly.

## When to Break It <!-- role: exceptions -->

- **Scenario:** Speed is more important than correctness for initial triage or rapid screening.
- **Reason:** The algorithm-generated design (E-1) was significantly faster than MATLAB/R and the prior-study design for *find-anomalies* time [@micallefPerceptualOptimizationVisual2017], as collated in [@zengReviewCollationGraphical2023].

## The Price <!-- role: costs -->

- **The Sacrifice:** You may increase time-on-task compared to an optimized preset.
- **The Risk:** Slower detection can hurt throughput or user experience in exploratory workflows.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Picking the fastest-looking preset and assuming accuracy will follow.
- **Why it fails:** The reported results show a speed–accuracy tradeoff for *find-anomalies*: MATLAB/R were more accurate while the optimized design was faster [@micallefPerceptualOptimizationVisual2017; @zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Users miss obvious outliers or disagree frequently on which points are anomalous.
- **The Test:** Run a small accuracy-focused validation with known outliers; if correctness drops relative to MATLAB/R-style defaults, switch away from an optimized-for-speed preset (consistent with the ranked outcomes) [@micallefPerceptualOptimizationVisual2017; @zengReviewCollationGraphical2023].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Use MATLAB- or R-style default scatterplot settings for your outlier workflow instead of an optimized preset.
- **Best Fix:** Offer a metric-driven toggle: “Outlier accuracy” defaults to MATLAB/R-style settings, while “Outlier speed” defaults to the optimized preset, reflecting the distinct rankings in [@micallefPerceptualOptimizationVisual2017] and structured in [@zengReviewCollationGraphical2023].
