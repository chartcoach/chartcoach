---
id: use-colorgorical-for-categorical-color-hue-palettes
title: Generate Categorical Color-Hue Palettes with Colorgorical
bibliography: references.bib
description: Use Colorgorical to create categorical color palettes for nominal data
  encoded with color hue.
labels:
- chart:general
- task:aggregate
- visual:color
- visual:color-hue
- impact:clarity
- impact:preference
- data:categorical
- audience:practitioner
- source:graphical-perception-collation
---

## The Rule <!-- role: advice -->

Generate your categorical palette using Colorgorical when encoding nominal categories with color hue.

## The Logic <!-- role: reason -->

Colorgorical is a purpose-built method/tool for creating categorical palettes intended to balance two objectives: (1) categorical discriminability and (2) aesthetic preference, by scoring candidate colors and iteratively constructing a palette.

- **The Principle:** Model-driven categorical palette construction (balancing discriminability and preference)
- **The Evidence:** The guideline is derived from the structured collation of this paper in the graphical perception knowledge base [@zengReviewCollationGraphical2023], which records Colorgorical as a nominal → color-hue design; the original work introduces and evaluates Colorgorical for generating discriminable and preferable categorical palettes [@gramazioColorgoricalCreatingDiscriminable2017].

## Where to Apply <!-- role: context -->

This advice is designed for specific moments.

- **User Goal:** Aggregating over categories where categories must remain distinguishable
- **Data Type:** Nominal (categorical) data encoded via color hue
- **Audience:** Visualization designers/developers selecting a categorical palette

## When to Break It <!-- role: exceptions -->

List the specific scenarios where you should ignore this rule.

- **Scenario:** You are not encoding nominal categories with color hue.
- **Reason:** This guideline only covers the nominal → color-hue encoding recorded in the collated structured knowledge [@zengReviewCollationGraphical2023] and does not support other encodings.

## The Price <!-- role: costs -->

Be honest about the downsides.

- **The Sacrifice:** You commit to a specific palette-generation approach rather than hand-picking colors.
- **The Risk:** If your system/tooling cannot consume Colorgorical palettes, you may need integration work.

## Common Mistakes <!-- role: mistakes -->

Describe the common anti-patterns or "lazy fixes" people use that don't actually solve the problem.

- **The Wrong Fix:** Treating Colorgorical as a general rule for all color encodings (e.g., ordinal/quantitative scales) without evidence.
- **Why it fails:** The collated structured record only specifies nominal data encoded with color hue (and does not provide broader results in this extracted entry) [@zengReviewCollationGraphical2023].

## How to Check <!-- role: check -->

- **Visual Sign:** Your categorical palette was selected ad hoc with no documented method, despite relying on color hue to separate categories.
- **The Test:** Verify whether your palette selection step is reproducible (i.e., can you regenerate the same palette given the same requirements?) and whether you used a categorical palette generator consistent with the Colorgorical approach [@gramazioColorgoricalCreatingDiscriminable2017].

## How to Fix <!-- role: fix -->

- **Quick Fix:** Replace your current categorical palette with a palette produced by Colorgorical.
- **Best Fix:** Integrate Colorgorical (or its palette outputs) into your visualization recommendation pipeline for nominal → color-hue designs, as suggested by the notion of ingesting collated perception knowledge into recommendation logic [@zengReviewCollationGraphical2023], using the palette-generation method from [@gramazioColorgoricalCreatingDiscriminable2017].
