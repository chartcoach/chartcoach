---
id: treat-small-effect-size-fields-as-high-false-positive-risk
title: Treat Small-Effect-Size Fields as High False-Positive Risk
bibliography: references.bib
description: Assume lower credibility for significant results when true effects are
  expected to be small.
labels:
- task:evaluate
- impact:trust
- audience:expert
- custom:effect-size
---

## The Rule <!-- role: advice -->

When the plausible true effects are small, assume that statistically significant findings are less likely to be true unless supported by strong evidence.

## The Logic <!-- role: reason -->

The paper links smaller effect sizes to lower power (for a given sample size) and thus lower PPV; fields targeting tiny relative risks are expected to have more false positives and nonreplication.

- **The Principle:** Small effects reduce signal-to-noise, lowering PPV under typical designs
- **The Evidence:** [@ioannidisWhyMostPublished2005]

## Where to Apply <!-- role: context -->

- **User Goal:** Interpret claims in areas with modest expected effects (e.g., many complex-risk-factor domains)
- **Data Type:** Association/effect estimates near null
- **Audience:** Researchers and readers of observational or molecular-epidemiology-style findings

## When to Break It <!-- role: exceptions -->

- **Scenario:** Very large, low-bias studies explicitly designed for detecting small effects
- **Reason:** Adequate power can partially offset the problem, though bias still matters. [@ioannidisWhyMostPublished2005]

## The Price <!-- role: costs -->

- **The Sacrifice:** More skepticism and higher evidentiary bar
- **The Risk:** True but small effects may be discounted prematurely. [@ioannidisWhyMostPublished2005]

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Interpreting “barely significant” small effects as definitive discoveries
- **Why it fails:** Low PPV is expected in small-effect regimes without strong priors and high power. [@ioannidisWhyMostPublished2005]

## How to Check <!-- role: check -->

- **Visual Sign:** Strong conclusions from small effect estimates with borderline p-values
- **The Test:** Ask whether the design was realistically powered for the reported effect size

## How to Fix <!-- role: fix -->

- **Quick Fix:** Tone down claims; highlight uncertainty and need for replication
- **Best Fix:** Require stronger design (larger studies, better standardization) and interpret through PPV considering low effect sizes. [@ioannidisWhyMostPublished2005]
