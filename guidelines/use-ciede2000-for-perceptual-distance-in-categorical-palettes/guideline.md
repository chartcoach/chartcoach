---
id: use-ciede2000-for-perceptual-distance-in-categorical-palettes
title: Use CIEDE2000 perceptual distance to separate categorical colors
bibliography: references.bib
description: Measure and promote perceptual separability between categorical colors
  using the CIEDE2000 color-difference formula.
labels:
- chart:categorical
- task:discriminate
- visual:color
- impact:clarity
- data:categorical
- audience:expert
- complexity:advanced
---

## Use CIEDE2000 (DE00) to quantify perceptual separation <!-- role: advice -->

When you need categorical colors to be perceptually distinct, measure separation using the CIEDE2000 color-difference formula and favor palettes with larger minimum pairwise distance.

## Why DE00 supports perceptual discriminability <!-- role: reason -->

A perceptual distance metric provides a numeric proxy for how different two colors will look; using a more perceptually uniform metric makes that proxy more reliable across regions of color space.

**Mechanism:** CIEDE2000 computes differences with corrections for lightness, chroma, and hue (and a hue rotation term), improving uniformity compared to Euclidean distance in CIELAB; maximizing the minimum pairwise distance targets the most confusable pair in the palette.

**Evidence:** The tool uses CIEDE2000 as its perceptual distance score, and higher perceptual-distance palette scores were associated with lower discrimination error rates (better performance) in the behavioral task across palette sizes [@gramazioColorgoricalCreatingDiscriminable2017a]. Perceptual-distance scores were negatively related to preference, illustrating the discriminability–preference tradeoff that requires deliberate balancing [@gramazioColorgoricalCreatingDiscriminable2017a].

**Notes:** The paper operationalizes palette quality by the minimum pairwise score, reflecting a “weakest link” assumption.

## When this applies to categorical color choice <!-- role: context -->

- **User Goal:** Reduce confusion between colored categories.
- **Task:** Identify categories by color in a legend-to-mark mapping.
- **Data:** Categorical, with at least 3 categories and potentially up to 8.
- **Chart Setting:** Small marks or dense displays where confusions are likely (e.g., maps).
- **Audience:** General audiences where fast, accurate identification matters.
- **Success Criterion:** Fewer identification errors for the most similar color pair.

## When not to follow DE00 prioritization <!-- role: exceptions -->

**Break it when:** The primary goal is maximizing subjective liking of the combination and small discriminability losses are acceptable. **Why:** Increasing perceptual distance can reduce preference ratings in the reported experiments.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Strong separation can push colors toward combinations that viewers rate as less preferable. **Risk:** Overemphasizing distance can lead to palettes that feel incohesive. **Mitigation:** Combine distance with at least one preference-oriented objective when aesthetics matter.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Treating average pairwise distance as sufficient. **Why it fails:** A palette can still fail if one pair is too similar; the minimum pair dominates confusions.
- **Mistake:** Maximizing distance without checking preference. **Why it fails:** The experiments show preference can decrease as perceptual distance increases.

## Quick tests <!-- role: check -->

**Failure Sign:** Two categories are repeatedly confused even though most other pairs look distinct. **Quick Check:** Identify the most similar-looking pair and verify it is not the minimum-distance pair you are accepting. **Stronger Test:** Use an error-based discrimination task on representative stimuli and verify errors drop as minimum DE00 increases.

## What to do instead <!-- role: fix -->

- Optimize for the minimum pairwise DE00 in the palette rather than a mean distance.
- Combine DE00 with a preference model when appearance matters, instead of using distance alone.
- Reduce palette size (fewer categories) if minimum distances become too small at the required cardinality.
- Apply additional constraints (e.g., hue range filters) only after verifying they do not collapse minimum distances.
