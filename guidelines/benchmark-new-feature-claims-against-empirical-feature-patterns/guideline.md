---
id: benchmark-new-feature-claims-against-empirical-feature-patterns
title: Benchmark New 'Basic Feature' Claims Against Empirical Feature Patterns
bibliography: references.bib
description: Evaluate candidate basic features by comparing their slope and slope-ratio
  patterns to established feature searches, not to idealized zero-slope predictions.
labels:
- chart:scatter
- task:evaluate
- visual:position
- impact:validity
- data:experimental
- audience:expert
- domain:visual-search
---

## The Rule <!-- role: advice -->

When proposing a new basic feature, compare its slope and slope-ratio pattern to empirical distributions from established feature searches—not to an ideal of near-zero slopes and equal present/absent slopes.

## The Logic <!-- role: reason -->

Observed feature searches do not match the theoretical ideal of unlimited-capacity parallel processing (near-zero slopes and similar present/absent slopes). Empirical benchmarks are therefore a more valid target for comparison than an invalid ideal.

- **The Principle:** Model/feature validation should use realistic empirical baselines, not unattainable theoretical extremes.
- **The Evidence:** The paper argues that “real feature searches” differ systematically from predictions of idealized unlimited-capacity parallel search and suggests using benchmark patterns (including slope ratios) for diagnostics [@wolfeWhatCan11998].

## Where to Apply <!-- role: context -->

- **User Goal:** Deciding whether X behaves like a basic feature in visual search.
- **Data Type:** Candidate-feature search tasks with measured present/absent slopes and ratios.
- **Audience:** Vision/attention researchers developing stimuli or theoretical claims.

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are explicitly testing a specific formal model that predicts an idealized baseline and you treat mismatch as evidence against the model, not against the feature.
- **Reason:** The guideline targets feature classification practice; model falsification can still use theoretical ideals if that is the stated aim [@wolfeWhatCan11998].

## The Price <!-- role: costs -->

- **The Sacrifice:** Requires access to benchmark distributions and more nuanced statistical comparison.
- **The Risk:** Benchmarks may depend on the mix of tasks/labs; comparisons should be framed as empirical similarity, not absolute proof.

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Claiming “it’s a basic feature because slopes are ~0 and ratios ~1.”
- **Why it fails:** The paper shows that actual feature searches have systematic structure (including slope ratios) that departs from that ideal [@wolfeWhatCan11998].

## How to Check <!-- role: check -->

- **Visual Sign:** A feature claim justified mainly by closeness to zero slope or by assuming present≈absent slopes.
- **The Test:** Compare both slope and ratio to established feature-search distributions; if you didn’t, the rule is broken.

## How to Fix <!-- role: fix -->

- **Quick Fix:** Add empirical comparisons to known feature tasks (both slopes and ratios).
- **Best Fix:** Treat feature-ness as similarity to a benchmark pattern (including absent/present relationship), as suggested by the paper’s diagnostic framing [@wolfeWhatCan11998].
