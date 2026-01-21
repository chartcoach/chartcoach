---
id: use-glyphs-to-reuse-shapes-by-position-when-encoding-many-variables
title: Use Glyphs to Encode Multiple Variables Without More Colors
bibliography: references.bib
description: When you need to encode many variables, use structured glyphs that reuse
  shapes in fixed positions instead of adding more colors.
labels:
- chart:scatter
- task:encode
- visual:shape
- visual:position
- impact:accessibility
- data:multivariate
- audience:expert
- complexity:advanced
- source:datawrapper
---

## The Rule <!-- role: advice -->

When encoding multiple variables per data point, use glyphs made of repeated shapes placed in consistent positions so meaning does not depend on color.

## The Logic <!-- role: reason -->

Fixed positional structure makes repeated shapes distinguishable by where they appear, enabling multi-variable encoding without requiring many hues; however, glyphs demand slower, more attentive reading [@muth_colorblindness_2020].

- **The Principle:** Structured composition (position + form) enables reusable marks
- **The Evidence:** The post explains glyphs as markers made of multiple elements whose meaning is readable because the shapes appear in consistent positions, and cautions that glyphs are “a slow read” not suitable for quick-glance overviews [@muth_colorblindness_2020].

## Where to Apply <!-- role: context -->

- **User Goal:** Compare multiple attributes per entity (beyond what color alone can support)
- **Data Type:** Multivariate point-based data (each row/entity has several measures)
- **Audience:** Analytical readers willing to spend time decoding marks [@muth_colorblindness_2020]

## When to Break It <!-- role: exceptions -->

- **Scenario:** You need instant “at a glance” comprehension for a general audience
- **Reason:** Glyphs increase cognitive load and slow reading [@muth_colorblindness_2020].

## The Price <!-- role: costs -->

- **The Sacrifice:** Speed and simplicity
- **The Risk:** Readers may misdecode glyph components without strong explanatory labeling [@muth_colorblindness_2020].

## Common Mistakes <!-- role: mistakes -->

- **The Wrong Fix:** Adding more colors to encode more variables instead of structuring marks
- **Why it fails:** Many colors become hard to separate, especially for colorblind readers; glyph structure avoids that dependence [@muth_colorblindness_2020].

## How to Check <!-- role: check -->

- **Visual Sign:** Viewers need the legend constantly and still struggle to interpret points
- **The Test:** Hide color (grayscale) and verify you can still decode each variable from the glyph’s components and positions [@muth_colorblindness_2020].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Reduce glyph complexity to fewer components and make positions unambiguous
- **Best Fix:** Pair glyphs with direct annotation and/or split variables into separate, simpler views if quick comprehension is required [@muth_colorblindness_2020].
