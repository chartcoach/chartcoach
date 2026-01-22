---
id: avoid-color-hue-for-find-extremum-in-ordered-sequences
title: Avoid color hue when users must find extrema in an ordered sequence
bibliography: references.bib
description: For finding minima or maxima in an ordered sequence, color hue yields
  lower accuracy than several alternative channels.
labels:
- chart:strip
- task:find-extremum
- visual:color-hue
- impact:accuracy
- data:quantitative
- complexity:advanced
---

## Do not use hue to encode magnitude for finding minima or maxima in sequences <!-- role: advice -->

Avoid using color hue to encode quantitative magnitude when the task is to find the minimum or maximum in an ordered sequence of marks.

## Why hue hurts extrema finding here <!-- role: reason -->

This rule works because hue differences do not reliably convey a single ordered “more-to-less” scale, which makes it harder to identify the most extreme value by visual scanning.

**Mechanism:** If the encoding does not strongly impose perceptual order, viewers must perform extra interpretation before they can confidently pick the smallest or largest element.

**Evidence:** For find-extremum accuracy on ordered sequences, the hue-encoded design ranked last among the tested encodings, and multiple other encodings (area, shape, texture, saturation, and orientation) showed statistically significant accuracy advantages over hue in the reported pairwise comparisons [@chungHowOrderedIt2016; @zengReviewCollationGraphical2023].

**Notes:** This guideline is about accuracy, not completion time.

## When this applies <!-- role: context -->

- **User Goal:** Identify the smallest or largest value in a displayed sequence.
- **Task:** Find Extremum.
- **Data:** Quantitative values arranged along an ordinal sequence (positionX encodes order).
- **Chart Setting:** Static, single-sequence display of marks (a 1D ordered strip).
- **Audience:** General audiences on standard displays.
- **Success Criterion:** Correctly selecting the true minimum or maximum.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Hue is encoding categories (not ordered magnitude) and the extrema task is performed on another channel. **Why:** The evidence concerns hue used as a quantitative/ordered encoding, not categorical labeling.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may lose the ability to use hue to separate groups if hue is reserved for categorization. **Risk:** Replacing hue without updating legends can confuse users about what the colors mean. **Mitigation:** Keep legends consistent with the encoding change and verify users interpret the mapping correctly.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a rainbow-like progression of hues and assuming “red means high, blue means low” will be read consistently. **Why it fails:** Hue performed poorly for accurate extrema identification in this task setting.

## Quick tests <!-- role: check -->

**Failure Sign:** People correctly describe the sequence order but miss the true minimum/maximum.\
**Quick Check:** Ask three people to point to the smallest and largest mark without reading the legend; if answers vary, hue is likely failing.\
**Stronger Test:** Time-box a small pilot task and compare extrema accuracy for hue vs a more orderable channel.

## What to do instead <!-- role: fix -->

- Encode magnitude with an alternative channel that performed better for find-extremum accuracy in this setting (e.g., area, texture, shape, or saturation).
- Add redundant cues so extrema can be identified without relying on hue as the only ordered signal.
- Reduce reliance on subtle encoding differences by directly annotating the min and max when identification accuracy is critical.
