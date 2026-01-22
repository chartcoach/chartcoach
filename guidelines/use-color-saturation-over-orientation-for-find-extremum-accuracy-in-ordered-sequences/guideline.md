---
id: use-color-saturation-over-orientation-for-find-extremum-accuracy-in-ordered-sequences
title: Use color saturation instead of orientation to improve extrema-finding accuracy
  in an ordered sequence
bibliography: references.bib
description: For finding minima or maxima in an ordered sequence, color saturation
  can yield higher accuracy than orientation encoding.
labels:
- chart:strip
- task:find-extremum
- visual:color-saturation
- visual:orientation
- impact:accuracy
- data:quantitative
- complexity:advanced
---

## Prefer saturation over orientation for finding minima or maxima in sequences <!-- role: advice -->

Use color saturation rather than orientation to encode quantitative magnitude when users must find the minimum or maximum in an ordered sequence of marks.

## Why saturation can beat orientation for extrema finding here <!-- role: reason -->

This rule works because a light-to-dark progression provides a clearer ordered cue for scanning to the extreme, while orientation changes can be harder to map to a consistent “more vs less” judgment during quick searches.

**Mechanism:** Extrema search relies on rapidly identifying the most extreme encoded state; ordered luminance cues can support that search more directly than angle/orientation cues.

**Evidence:** For find-extremum accuracy on ordered sequences, the saturation-encoded design ranked above the orientation-encoded design, and the pairwise results report saturation as significantly more accurate than orientation [@chungHowOrderedIt2016; @zengReviewCollationGraphical2023].

**Notes:** This guideline is scoped to accuracy, not speed.

## When to apply saturation over orientation for extrema finding <!-- role: context -->

- **User Goal:** Correctly identify the minimum or maximum value in a sequence.
- **Task:** Find Extremum.
- **Data:** Quantitative values shown as a 1D ordered sequence.
- **Chart Setting:** Static display where each mark’s magnitude is encoded by a single channel.
- **Audience:** General audiences on standard displays.
- **Success Criterion:** Higher accuracy in min/max selection.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Color encoding is unavailable or unreliable (e.g., grayscale printing or strict color constraints). **Why:** The recommendation depends on using saturation differences as the ordered cue.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Saturation-only encodings can be less expressive when multiple variables also require color. **Risk:** Low-contrast saturation steps can reduce discriminability. **Mitigation:** Ensure the saturation range is visually distinguishable at typical viewing conditions.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using subtle orientation differences and expecting users to quickly detect the most extreme value. **Why it fails:** Orientation performed worse than saturation for extrema accuracy in this task setting.

## Quick tests <!-- role: check -->

**Failure Sign:** Users frequently confuse the smallest/largest oriented mark with a neighboring mark.\
**Quick Check:** Ask users to answer “which is largest?” within two seconds; if many fail, orientation may be too hard to scan.\
**Stronger Test:** A/B test extrema accuracy using saturation vs orientation on the same sequences.

## What to do instead <!-- role: fix -->

- Replace orientation encoding with a saturation scale for magnitude in extrema-finding tasks.
- Increase the perceptual separation between encoding steps (e.g., fewer discrete levels) so saturation differences are easier to scan.
- Add explicit highlights or annotations for the min/max when correct identification is critical.
