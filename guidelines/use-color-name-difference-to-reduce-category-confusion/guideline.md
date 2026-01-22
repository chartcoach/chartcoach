---
id: use-color-name-difference-to-reduce-category-confusion
title: Use color-name difference to reduce categorical confusion and referencing errors
bibliography: references.bib
description: Favor categorical palettes whose colors differ in their color-name association
  distributions to reduce confusability.
labels:
- chart:categorical
- task:discriminate
- visual:color
- impact:clarity
- data:categorical
- audience:novice
- complexity:advanced
---

## Use Name Difference to separate colors that people might label similarly <!-- role: advice -->

When categories may be referenced or remembered by color names, favor palettes whose colors have high Name Difference, so colors are less likely to be called (and confused as) the same name.

## Why name-based separation improves categorical discrimination <!-- role: reason -->

Colors can be perceptually different yet share overlapping name associations; name-based separation targets confusion driven by language and category labeling rather than purely visual distance.

**Mechanism:** Name Difference compares two colors’ color-name association frequency distributions (using a Hellinger distance), capturing whether observers are likely to map them to different common names.

**Evidence:** Higher Name Difference palette scores were associated with lower discrimination error rates across palette sizes in the behavioral task, and slider weight on Name Difference predicted performance in regressions [@gramazioColorgoricalCreatingDiscriminable2017a]. Name Difference showed strong relationships with other palette scores but still contributed distinct predictive signal, supporting its inclusion as a separate discriminability dimension [@gramazioColorgoricalCreatingDiscriminable2017a].

**Notes:** The paper highlights that a color can be visually distinct but still called “green” or “yellow,” motivating name-based separation.

## When this applies <!-- role: context -->

- **User Goal:** Prevent confusion between categories that users may talk about (“the green one”) or remember by name.
- **Task:** Identify and report category membership from colored marks and legends.
- **Data:** Categorical labels without semantic color mapping requirements.
- **Chart Setting:** Visualizations where users may communicate findings verbally or via annotation.
- **Audience:** Broad audiences with varying color vocabulary.
- **Success Criterion:** Reduced errors attributable to confusable “same-name” colors.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Categories have prescribed semantic colors that must be used even if name overlap exists. **Why:** Name Difference may push you away from required hues.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Maximizing name separability can reduce aesthetic preference. **Risk:** Strongly name-different palettes may increase hue differences that the preference model penalizes. **Mitigation:** Balance Name Difference against a preference objective when acceptance matters.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Using only perceptual distance and ignoring naming overlap. **Why it fails:** Two colors can be distinct in CIELAB yet still be labeled with overlapping names, increasing confusion in practice.
- **Mistake:** Treating Name Difference as a preference metric. **Why it fails:** Name Difference is a discriminability score and was negatively related to preference trends in the experiments.

## Quick tests <!-- role: check -->

**Failure Sign:** Users describe two different legend entries using the same basic color name. **Quick Check:** Ask a small sample of users to name each palette color; flag pairs that share the same dominant name. **Stronger Test:** Run a discrimination task where target/distractor are the lowest-name-difference pair and verify errors drop when Name Difference increases.

## What to do instead <!-- role: fix -->

- Increase emphasis on Name Difference when users will discuss categories by color name.
- Identify the lowest Name Difference pair in a candidate palette and replace one color to increase name separation.
- Combine Name Difference with perceptual distance to avoid creating visually similar but name-distinct pairs.
- Reduce palette size if constraints (brand hues, filters) force many same-name colors.
