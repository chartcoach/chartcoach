---
id: use-perceptual-distance-ciede2000-for-categorical-separation
title: Use CIEDE2000 Perceptual Distance to Separate Categorical Colors
bibliography: references.bib
description: Prefer CIEDE2000 over simple Euclidean LAB distance when optimizing categorical
  color discriminability.
labels:
- chart:categorical
- task:distinguish
- visual:color
- impact:accuracy
- data:categorical
- audience:expert
- complexity:advanced
---

## The Rule <!-- role: advice -->

When measuring or optimizing how different categorical colors look, use CIEDE2000 (ΔE00) rather than Euclidean distance in CIELAB (ΔE76).

## The Logic <!-- role: reason -->

Euclidean distance in CIELAB is limited by imperfect perceptual uniformity—equal numeric distances can have different perceptual consequences depending on region—while CIEDE2000 adds corrections (lightness, chroma, hue, and rotation) that improve perceptual uniformity for difference judgments [@gramazioColorgoricalCreatingDiscriminable2017a].

- **The Principle:** Perceptual uniformity in color-difference metrics
- **The Evidence:** [@gramazioColorgoricalCreatingDiscriminable2017a]

## Where to Apply <!-- role: context -->

- **User Goal:** Reduce confusions between categories (faster and more accurate identification)
- **Data Type:** Categorical palettes (3+ categories)
- **Audience:** Designers or engineers implementing palette selection/scoring

## When to Break It <!-- role: exceptions -->

- **Scenario:** You are reproducing legacy results that specifically used ΔE76 and need strict comparability.
- **Reason:** Changing the metric changes scores and may change chosen palettes, harming reproducibility [@gramazioColorgoricalCreatingDiscriminable2017a].

## The Price <!-- role: costs -->

- **The Sacrifice:** More computation than ΔE76.
- **The Risk:** If you treat ΔE00 as the only constraint, you may still miss name-based confusions (e.g., colors that look distinct but share common names) [@gramazioColorgoricalCreatingDiscriminable2017a].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** “Maximize LAB distance” with ΔE76 and assume it guarantees discriminability.
- **Why it fails:** ΔE76 can mis-estimate perceptual differences in parts of the space; perceived separation may be smaller than the numeric distance suggests [@gramazioColorgoricalCreatingDiscriminable2017a].

## How to Check <!-- role: check -->

- **Visual Sign:** Some color pairs that score “far apart” still look closer than others with similar numeric distance.
- **The Test:** Compare ΔE76 and ΔE00 rankings for your candidate colors; large rank reversals indicate regions where ΔE76 is misleading [@gramazioColorgoricalCreatingDiscriminable2017a].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace ΔE76 with ΔE00 in your scoring function.
- **Best Fix:** Combine ΔE00 with a second discriminability signal like Name Difference when building categorical palettes [@gramazioColorgoricalCreatingDiscriminable2017a].
