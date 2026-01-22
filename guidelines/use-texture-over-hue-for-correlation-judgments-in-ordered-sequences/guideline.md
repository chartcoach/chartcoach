---
id: use-texture-over-hue-for-correlation-judgments-in-ordered-sequences
title: Use texture instead of color hue for correlation judgments in ordered sequences
bibliography: references.bib
description: For correlation judgments over an ordered sequence, encode magnitude
  with texture rather than color hue to improve accuracy.
labels:
- chart:strip
- task:correlate
- visual:texture
- visual:color-hue
- impact:accuracy
- data:quantitative
- complexity:advanced
---

## Use texture, not hue, to show magnitude for correlation in sequences <!-- role: advice -->

Use texture rather than color hue to encode quantitative magnitude when people must judge correlation in an ordered sequence of marks.

## Why texture can beat hue for correlation judgments here <!-- role: reason -->

This rule works because texture levels can form a more perceivably ordered progression than hue differences, which supports assessing whether values change consistently along an ordered axis.

**Mechanism:** An ordered texture progression can preserve the visual impression of “more vs less” across adjacent marks, enabling more reliable pattern judgment than hue steps.

**Evidence:** In correlation tasks on ordered 1D sequences, the texture-encoded design was more accurate than the hue-encoded design, and the pairwise significance list indicates a statistically significant advantage of texture over hue for accuracy [@chungHowOrderedIt2016; @zengReviewCollationGraphical2023].

**Notes:** This guideline does not claim texture is best overall for every task; it is scoped to correlate accuracy in this setting.

## When to apply texture over hue for correlation in sequences <!-- role: context -->

- **User Goal:** Determine whether the sequence shows a correlated pattern across ordered samples.
- **Task:** Correlate.
- **Data:** Quantitative values placed along an ordinal X sequence.
- **Chart Setting:** Static sequence/strip of marks; ordering is conveyed by positionX (ordinal).
- **Audience:** General audiences using standard screens.
- **Success Criterion:** Higher accuracy for correlation judgments.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The display environment or rendering constraints make texture hard to see (e.g., low resolution or heavy compression). **Why:** The mechanism depends on reliably discriminating texture steps, and the evidence assumes visible discriminability.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Texture encodings can increase visual noise compared to color. **Risk:** Dense textures can interfere with reading adjacent marks, especially as mark size shrinks. **Mitigation:** Ensure textures remain clearly distinguishable at the intended mark size.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using hue steps to imply quantitative order in a correlation-reading task. **Why it fails:** Hue performed worst for correlation accuracy among the tested channels in this evidence set.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers hesitate or disagree about whether the sequence is mostly increasing/decreasing.\
**Quick Check:** Show both versions briefly and ask which makes the trend clearer without allowing legend reading.\
**Stronger Test:** Measure correlation-judgment accuracy across a small set of stimuli with texture vs hue.

## What to do instead <!-- role: fix -->

- Replace hue with a texture progression when the goal is correlation judgment over an ordered sequence.
- Increase mark size or spacing so texture differences remain discriminable.
- Switch away from color-based ordering entirely by using an alternative ordered encoding within your allowed design space.
