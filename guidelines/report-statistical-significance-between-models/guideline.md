---
id: report-statistical-significance-between-models
title: Report Statistical Significance for Model Rankings
bibliography: references.bib
description: "Use hypothesis testing (e.g., t-tests at p\u22640.05) to show which\
  \ differences in model scores are meaningful rather than noise."
labels:
- chart:bar
- task:rank
- visual:none
- impact:rigor
- data:spatial
- audience:expert
- analysis:significance
---

## The Rule <!-- role: advice -->

When presenting ranked model results, report **statistical significance** of differences (e.g., pairwise t-tests at p ≤ 0.05) rather than relying on rank order alone.

## The Logic <!-- role: reason -->

Model scores often differ by small margins; significance testing helps distinguish real performance gaps from sampling variability across stimuli.

- **The Principle:** Separating signal from sampling noise in benchmark comparisons
- **The Evidence:** The paper uses t-tests at p ≤ 0.05 to mark significant differences between consecutive models in ranking plots and emphasizes that rankings can vary by metric and dataset [@borjiQuantitativeAnalysisHumanModel2013].

## Where to Apply <!-- role: context -->

- **User Goal:** Making defensible claims that one model outperforms another
- **Data Type:** Per-stimulus scores across many images/frames
- **Audience:** Researchers publishing comparative benchmark results

## When to Break It <!-- role: exceptions -->

- **Scenario:** You have too few stimuli to estimate variance meaningfully.
- **Reason:** With very small N, tests have low power and results can be misleading [@borjiQuantitativeAnalysisHumanModel2013].

## The Price <!-- role: costs -->

- **The Sacrifice:** More computation and more complex reporting.
- **The Risk:** Multiple comparisons can create interpretability issues; readers may over-focus on borderline p-values [@borjiQuantitativeAnalysisHumanModel2013].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Declaring “state of the art” based purely on being #1 by a tiny margin.
- **Why it fails:** The paper shows narrow spreads and metric-dependent rankings; without significance, rank differences may not be meaningful [@borjiQuantitativeAnalysisHumanModel2013].

## How to Check <!-- role: check -->

- **Visual Sign:** Many models cluster tightly with overlapping error bars.
- **The Test:** Compute per-stimulus score distributions and run the planned significance test; confirm whether adjacent ranks differ reliably [@borjiQuantitativeAnalysisHumanModel2013].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add SEM error bars and mark statistically significant adjacent differences.
- **Best Fix:** Predefine the statistical testing protocol for the benchmark and apply it consistently across datasets and metrics [@borjiQuantitativeAnalysisHumanModel2013].
