---
id: do-not-assume-perceptual-uniformity-metrics-predict-user-accuracy
title: Validate Colormaps with User Tasks, Not Just Color-Space Distance
bibliography: references.bib
description: Perceptual color-space distances (LAB/UCS) and color naming measures
  poorly predict overall user accuracy on quantitative comparison tasks.
labels:
- chart:heatmap
- task:evaluate
- visual:color
- impact:reliability
- data:quantitative
- audience:designer
- method:user-testing
---

## The Rule <!-- role: advice -->

Do not rely on LAB/UCS distance (or color naming) metrics alone to select a quantitative colormap; validate with task-relevant checks.

## The Logic <!-- role: reason -->

- **The Principle:** Color difference models are imperfect proxies for task performance, especially under contextual factors (background, legends) and multi-stimulus comparisons.
- **The Evidence:** The paper’s mixed-effects models using LAB, CAM02-UCS, and color naming differences explained little variance in observed error (about 10% R² for their additive UCS+Name model) and did not reliably rank colormap performance [@liuSomewhereRainbowEmpirical2018a].

## Where to Apply <!-- role: context -->

- **User Goal:** Choosing or generating colormaps expected to support accurate quantitative reading.
- **Data Type:** Any scalar-to-color mapping where accuracy matters.
- **Audience:** Visualization designers and tool builders using automated palette selection.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You only need a rough pre-filter before manual review.
- **Reason:** The paper shows these metrics correlate somewhat with performance, but weakly; they can guide but not decide [@liuSomewhereRainbowEmpirical2018a].

## The Price <!-- role: costs -->

- **The Sacrifice:** Extra time and effort to run validations (even lightweight ones).
- **The Risk:** Small internal tests may not perfectly match your real users or contexts.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Declaring a colormap “good” solely because it is derived from a perceptually-uniform space.
- **Why it fails:** Even UCS-based maps showed context-specific failures (e.g., dark-region degradation), and distance-based models poorly predicted accuracy overall [@liuSomewhereRainbowEmpirical2018a].

## How to Check <!-- role: check -->

- **Visual Sign:** A palette looks “smooth” in a legend but still yields user confusion in specific regions (e.g., dark end, midpoint crossings).
- **The Test:** Run quick triplet judgments internally at multiple reference points and spans relevant to your use case; look for spikes in error concentrated in specific ranges [@liuSomewhereRainbowEmpirical2018a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add targeted spot-checks focused on known failure regions (dark end on white; midpoint for diverging).
- **Best Fix:** Evaluate candidate colormaps using the same type of judgment task your visualization demands (e.g., relative similarity), and iterate based on observed failures [@liuSomewhereRainbowEmpirical2018a].
