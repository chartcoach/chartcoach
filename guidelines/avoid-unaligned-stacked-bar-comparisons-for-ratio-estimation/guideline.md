---
id: avoid-unaligned-stacked-bar-comparisons-for-ratio-estimation
title: Avoid unaligned stacked-bar segments when viewers must compare segment heights
bibliography: references.bib
description: Unaligned comparisons between stacked-bar segments yield higher error
  than aligned comparisons in percent estimation tasks.
labels:
- chart:bar
- task:compare
- visual:position
- impact:accuracy
- data:quantitative
- audience:general
- chart:stacked-bar
---

## Keep compared bar segments aligned to a common baseline <!-- role: advice -->

When viewers need to compare the heights of specific segments, use a configuration where the segments share a common baseline (aligned) rather than requiring unaligned comparisons across stacks. Do not rely on unaligned stacked segments for precise percent judgments.

## Alignment supports more accurate relative judgments than unalignment <!-- role: reason -->

Unaligned comparisons force viewers to judge lengths without a shared baseline, which increases error relative to aligned, position-based comparisons.

**Mechanism:** A common baseline enables positional alignment of endpoints; removing that baseline turns the task into a harder length-comparison problem under clutter.

**Evidence:** Unaligned stacked-bar comparisons produced higher absolute error than aligned stacked-bar comparisons in controlled percent-of-height estimation, with unalignment itself contributing substantially to the total effect. [@talbotFourExperimentsPerception2014; @zengReviewCollationGraphical2023]

**Notes:** Distractors in stacked arrangements further increased error for unaligned comparisons.

## Context: When this applies <!-- role: context -->

- **User Goal:** Compare two values/segments accurately.
- **Task:** Percent/ratio estimation between two marked segments in stacked bars.
- **Data:** Quantitative values represented as segment heights within stacks.
- **Chart Setting:** Stacked bar charts where the compared segments do not share a baseline.
- **Audience:** General audiences, especially under time pressure.
- **Success Criterion:** Lower absolute estimation error.

## Exceptions: When not to follow it <!-- role: exceptions -->

**Break it when:** The primary goal is part-to-whole composition and exact cross-segment comparisons are not required. **Why:** Alignment changes the nature of the composition display and may not match the intended message.

## Costs: Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Enforcing alignment may require changing the chart form or splitting the view, which can cost space. **Risk:** Viewers may lose the compact part-to-whole structure that stacking provides. **Mitigation:** Preserve composition with separate summaries while using aligned views for comparisons.

## Mistakes: Common failure modes <!-- role: mistakes -->

**Mistake:** Using stacked bars and asking viewers to precisely compare interior segments across different stacks. **Why it fails:** Those segments are unaligned, which increases error.

## Check: Quick tests <!-- role: check -->

**Failure Sign:** Users repeatedly misjudge which segment is larger or by how much when segments start at different vertical positions. **Quick Check:** If the compared segments do not begin at the same baseline, treat the comparison as unaligned and high-risk for error. **Stronger Test:** Run a short task test measuring absolute error for aligned vs. unaligned alternatives.

## Fix: What to do instead <!-- role: fix -->

- Replace unaligned stacked comparisons with an aligned bar configuration for the compared values.
- Separate the compared segments into their own aligned bars in a companion view.
- Re-encode the comparison so the endpoints share a baseline within the same local group.
- Provide a focused comparison view that isolates just the segments being compared.
