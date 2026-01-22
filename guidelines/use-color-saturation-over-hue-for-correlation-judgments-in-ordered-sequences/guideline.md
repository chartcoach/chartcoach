---
id: use-color-saturation-over-hue-for-correlation-judgments-in-ordered-sequences
title: Use color saturation instead of color hue for correlation judgments in ordered
  sequences
bibliography: references.bib
description: For correlation judgments over an ordered sequence, encode magnitude
  with color saturation rather than color hue to improve accuracy.
labels:
- chart:strip
- task:correlate
- visual:color
- visual:color-saturation
- visual:color-hue
- impact:accuracy
- data:quantitative
- complexity:advanced
---

## Use saturation, not hue, to show magnitude for correlation in sequences <!-- role: advice -->

Use color saturation (light-to-dark) rather than color hue (different colors) to encode quantitative magnitude when people must judge correlation in an ordered sequence of marks.

## Why saturation supports correlation judgments better than hue here <!-- role: reason -->

This rule works because a monotonic light-to-dark scale provides a more consistently orderable visual progression than a multi-hue progression, making it easier to perceive whether values rise or fall along an ordered axis.

**Mechanism:** A single ordered visual cue (saturation) supports estimating the direction and consistency of change across the sequence, while hue is less reliably perceived as ordered and can disrupt pattern judgment.

**Evidence:** In correlation tasks on ordered 1D sequences, the saturation-encoded design outperformed the hue-encoded design in accuracy, with a statistically significant difference reported in the study’s pairwise results [@chungHowOrderedIt2016; @zengReviewCollationGraphical2023].

**Notes:** This guideline is about accuracy; time rankings for correlation differ across encodings in the same evidence set.

## When to apply saturation over hue for correlation in sequences <!-- role: context -->

- **User Goal:** Judge whether values follow an ordered pattern consistent with correlation across a sequence.
- **Task:** Correlate.
- **Data:** Quantitative values arranged along an ordinal sequence (e.g., ordered samples).
- **Chart Setting:** Static 1D sequence/strip of marks with an explicit left-to-right order (position on X is ordinal).
- **Audience:** General audiences on standard displays.
- **Success Criterion:** Higher correctness/accuracy for correlation judgment.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The task is not a correlation judgment over an ordered sequence (for example, the viewer is primarily doing min/max identification or speed is the only priority). **Why:** The evidence only establishes the accuracy advantage for the correlate task, and other tasks/metrics may favor different encodings.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may reduce categorical distinctiveness because saturation is a single ordered scale. **Risk:** If your audience expects different colors to indicate different groups, switching to saturation can be misread as a quantitative gradient. **Mitigation:** Ensure the legend and labeling make it explicit that saturation represents magnitude.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Encoding quantitative order with multiple hues and expecting viewers to read it as an ordered scale. **Why it fails:** Hue can be perceived as less ordered for correlation judgments in sequences, reducing accuracy.

## Quick tests <!-- role: check -->

**Failure Sign:** Viewers disagree on whether the sequence shows a consistent increase/decrease when only the color encoding changes.\
**Quick Check:** Ask a colleague to judge “does it increase overall?” using the hue version versus the saturation version without a legend.\
**Stronger Test:** Run a small A/B task test measuring correlation-judgment accuracy for hue vs saturation encodings.

## What to do instead <!-- role: fix -->

- Encode magnitude with color saturation (light-to-dark) rather than color hue (different hues).
- If hue must be used, move the correlation judgment onto a different ordered channel within the same design space (e.g., change the encoding choice rather than the task).
- Reduce the need for color-based ordering by simplifying the sequence (fewer marks) so correlation judgment depends less on subtle color ordering.
