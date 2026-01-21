---
id: avoid-minimal-y-axis-range-to-prevent-overstating-effects
title: Avoid Minimal Y-Axis Ranges That Just Fit the Data
bibliography: references.bib
description: Do not set the y-axis to the smallest range that contains the data, because
  it biases viewers to judge effects as larger than they are.
labels:
- chart:bar
- chart:line
- task:interpret
- visual:scale
- impact:honesty
- impact:calibration
- data:continuous
- audience:novice
- custom:axis-minimization
- source:wittGraphConstruction2019
---

## The Rule <!-- role: advice -->

Do not use a “minimal” y-axis range that starts just below the smallest value and ends just above the largest value when the goal is to communicate effect magnitude.

## The Logic <!-- role: reason -->

A minimal y-axis increases the apparent visual difference between conditions, which pushes readers to categorize effects as larger than their true standardized magnitude (positive bias) and can reduce calibrated discrimination among small/medium/large effects [@wittGraphConstruction2019].

- **The Principle:** Visual exaggeration from scale truncation
- **The Evidence:** In the experiments, minimal-range graphs produced a strong bias toward “big” judgments compared to SD-standardized axes [@wittGraphConstruction2019].

## Where to Apply <!-- role: context -->

- **User Goal:** Estimating magnitude categories (none/small/medium/big) from the visual.
- **Data Type:** Two-condition comparisons or simple trends where scale choice strongly changes perceived differences.
- **Audience:** Readers likely to rely on the plot’s “look” rather than numerically decoding values [@wittGraphConstruction2019].

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are explicitly not communicating effect magnitude, and instead need to inspect fine-grained variation within a narrow operational window.
- **Reason:** The paper’s evidence targets magnitude judgments and bias; other analytic goals may justify different scaling [@wittGraphConstruction2019].
- **Scenario:** You must ensure all uncertainty displays (e.g., confidence intervals) are visible.
- **Reason:** Even then, avoid “tight as possible” if the goal is calibrated magnitude communication; prefer SD-based scaling where applicable [@wittGraphConstruction2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Less zoomed-in detail of small within-range fluctuations.
- **The Risk:** Using a wider, SD-based axis may make some subtle differences harder to notice at a glance [@wittGraphConstruction2019].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Accepting software defaults that auto-fit the y-axis to the data.
- **Why it fails:** Auto-fit commonly approximates the minimal-range behavior that increases perceived effect size [@wittGraphConstruction2019].
- **The Wrong Fix:** Adding tiny padding (e.g., ±1 unit) and assuming it solves exaggeration.
- **Why it fails:** Small padding does not address the core problem: the range remains too narrow relative to SD [@wittGraphConstruction2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Small differences visually dominate the plot area; many effects “look big” even when standardized effects are small.
- **The Test:** Express the y-axis span in SD units. If it is substantially below ~1 SD total in a standardized-effects setting, the plot is likely exaggerating [@wittGraphConstruction2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace the minimal y-limits with grand mean ± 0.75 SD (≈1.5 SD total) when SD-based interpretation applies [@wittGraphConstruction2019].
- **Best Fix:** Adopt SD-tied axis rules for standardized-effect fields and document the chosen SD range so it is deliberate rather than auto-fit [@wittGraphConstruction2019].
