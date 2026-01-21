---
id: avoid-overcrowding-in-static-sampling-ensembles
title: Limit Outcome Density in Static Sampling Ensembles
bibliography: references.bib
description: If you use static ensembles, avoid so many samples that the display reads
  like a density field rather than discrete outcomes.
labels:
- chart:line
- chart:uncertainty
- task:infer
- visual:overplotting
- impact:interpretability
- data:temporal
- audience:novice
- uncertainty:sampling
---

## The Rule <!-- role: advice -->

When showing static sampling-oriented uncertainty (e.g., line ensembles), keep the number of outcomes low enough that viewers still perceive discrete samples rather than an undifferentiated density.

## The Logic <!-- role: reason -->

The paper argues that sampling-oriented encodings work by conveying frequency through discrete outcomes; it cautions that showing too many outcomes in one static view can disrupt perception of discreteness, effectively turning the display into a density encoding that is interpreted less consistently than frequency-style displays [@kaleHypotheticalOutcomePlots2019].

- **The Principle:** Discrete frequency representations support experiential probability reasoning.
- **The Evidence:** [@kaleHypotheticalOutcomePlots2019]

## Where to Apply <!-- role: context -->

- **User Goal:** Understand variability and compare candidate explanations (trends/models) using outcome samples.
- **Data Type:** Time series uncertainty shown as multiple possible trajectories.
- **Audience:** Viewers with limited statistical training who benefit from frequency-like displays [@kaleHypotheticalOutcomePlots2019].

## When to Break It <!-- role: exceptions -->

- **Scenario:** Your intent is explicitly to show a smooth distributional shape (a density-style depiction) rather than discrete outcomes.
- **Reason:** The rule targets cases where the design goal is an experiential frequency metaphor; if you want density, discreteness is not required [@kaleHypotheticalOutcomePlots2019].

## The Price <!-- role: costs -->

- **The Sacrifice:** Fewer samples may underrepresent rare patterns or tails.
- **The Risk:** Users may overgeneralize from a small set of drawn outcomes if they assume the shown samples are exhaustive [@kaleHypotheticalOutcomePlots2019].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Increasing the number of ensemble members until the plot becomes a dark band.
- **Why it fails:** It can collapse the intended frequency reading into a density impression, undermining the “outcomes you might see” metaphor emphasized in the paper [@kaleHypotheticalOutcomePlots2019].

## How to Check <!-- role: check -->

- **Visual Sign:** Individual trajectories are no longer distinguishable; the chart reads as a shaded mass.
- **The Test:** Step back (or zoom out) and ask whether you can still pick out individual paths; if not, discreteness has been lost [@kaleHypotheticalOutcomePlots2019].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce the number of displayed outcomes in the ensemble so lines remain individually legible.
- **Best Fix:** Use a HOP instead of a large static ensemble to show many outcomes over time while preserving the sense of discrete samples [@kaleHypotheticalOutcomePlots2019].
