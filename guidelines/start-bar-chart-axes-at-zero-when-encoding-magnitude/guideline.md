---
id: start-bar-chart-axes-at-zero-when-encoding-magnitude
title: Start bar-chart value axes at zero when bar length encodes magnitude
bibliography: references.bib
description: Prevent magnitude exaggeration in bar charts by anchoring the value axis
  at zero.
labels:
- chart:bar
- task:compare
- visual:position
- impact:trust
- data:quantitative
- audience:novice
- distortion:truncated-axis
---

## Zero-baseline bar lengths for magnitude comparisons <!-- role: advice -->

Start the quantitative axis at zero in bar charts whenever viewers are expected to compare amounts by bar length. If you cannot start at zero, avoid using bar length as the primary cue for magnitude.

## Why truncated baselines exaggerate bar-chart messages <!-- role: reason -->

When bar charts encode quantity as length, viewers implicitly treat the baseline as “nothing.” Truncating the axis changes perceived length ratios, which shifts the interpreted “how much bigger” message even when the underlying numbers are correct.

**Mechanism:** A non-zero baseline increases the visual difference between bars relative to their actual numeric difference, biasing “how much” judgments toward exaggeration.

**Evidence:** In a crowdsourced between-subject study, a truncated-axis bar chart produced substantially higher “how much better” ratings than a non-truncated control, with a highly significant difference (one-tailed Mann–Whitney U, p < 0.001) [@pandeyHowDeceptiveAre2015].

**Notes:** This effect was measured at the message level: participants answered a domain-language comparison question rather than a low-level perceptual estimation task.

## When this applies to your bar-chart design <!-- role: context -->

- **User Goal:** Judge the relative size of two or more values (e.g., “how much larger/better”).
- **Task:** Compare magnitudes across categories.
- **Data:** Quantitative values mapped to bar length.
- **Chart Setting:** Static charts in reports, slides, news, advocacy, dashboards.
- **Audience:** Broad/general audiences, including readers with limited chart literacy.
- **Success Criterion:** Viewers’ perceived magnitude differences match numeric differences.

## When not to follow a zero baseline strictly <!-- role: exceptions -->

**Break it when:** The chart’s only purpose is to show small deviations around a meaningful non-zero reference and the baseline is explicitly that reference. **Why:** The viewer’s intended judgment is deviation from a reference, not absolute magnitude, so zero is not the semantic anchor.

## Tradeoffs of enforcing a zero baseline <!-- role: costs -->

**Sacrifice:** You may lose visible detail for small differences when values cluster tightly. **Risk:** Viewers may miss meaningful but small changes if the plot becomes visually flat. **Mitigation:** Consider alternative encodings that do not rely on bar length for fine-grained comparisons.

## Common truncated-axis failure modes <!-- role: mistakes -->

- **Mistake:** Keeping bar charts while zooming the y-axis to “make differences pop.” **Why it fails:** It systematically inflates perceived differences and pushes readers toward exaggerated “how much” interpretations [@pandeyHowDeceptiveAre2015].
- **Mistake:** Assuming that printing data labels cancels the distortion. **Why it fails:** Participants were misled even when numbers were present, indicating the visual cue can dominate message interpretation [@pandeyHowDeceptiveAre2015].

## Quick tests to catch bar-axis truncation deception <!-- role: check -->

**Failure Sign:** Two bars that are numerically close look dramatically different in height. **Quick Check:** Inspect the axis minimum; if it is not zero in a magnitude bar chart, treat it as a potential exaggeration risk. **Stronger Test:** Run a small between-subject comprehension check asking “how much bigger” and compare responses for zero-baseline vs. truncated versions.

## What to do instead of truncating a bar baseline <!-- role: fix -->

- Replace the bar chart with an encoding that supports non-zero baselines without implying an absolute zero length.
- Show change-from-reference explicitly if the intent is deviation rather than magnitude.
- Add an explicit visual cue that the baseline is truncated and ensure the narrative question is about deviation, not absolute size.
- Redesign the comparison so the viewer reads values directly rather than inferring ratios from bar lengths.
