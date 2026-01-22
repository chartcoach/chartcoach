---
id: avoid-very-dark-colormap-regions-on-white-backgrounds-for-fine-comparisons
title: Avoid very dark colormap regions on white backgrounds for fine comparisons
bibliography: references.bib
description: Do not rely on near-black portions of colormaps against white backgrounds
  when users must discriminate small value differences.
labels:
- chart:heatmap
- task:compare
- visual:color
- impact:accuracy
- data:quantitative
- audience:general
- complexity:intermediate
---

## Avoid near-black colors against white when users must discriminate small differences <!-- role: advice -->

Avoid using colormap regions with very low luminance (near-black) against a white background when the task requires fine discrimination. If your data meaningfully occupies that region, adjust the design so comparisons do not depend on distinguishing those darkest steps.

## White-background contrast can degrade discrimination in dark regions <!-- role: reason -->

Very dark patches against white can become harder to discriminate than expected from perceptual distance models, creating localized spikes in errors for close-value judgments.

**Mechanism:** High contrast between a white surround and very dark stimuli can reduce effective discriminability among the dark shades, breaking assumptions that equal modeled distances yield equal perceptual differences.

**Evidence:** Error rates spiked in low-luminance regions for greys and for the dark ends of magma (and to a lesser extent plasma), despite those regions not being flagged as unusually problematic by perceptual color space distances alone [@liuSomewhereRainbowEmpirical2018a]. The observed pattern was attributed to the combination of low luminance stimuli and a white background context in the experimental setup [@liuSomewhereRainbowEmpirical2018a].

**Notes:** The same risk may occur in reverse for very light colors on dark backgrounds, but this guideline is scoped to the tested white-background condition.

## Where this problem shows up <!-- role: context -->

- **User Goal:** Compare nearby quantitative values using color.
- **Task:** Similarity judgments among close steps near the low end of the scale.
- **Data:** Continuous quantitative variable with important values near the minimum.
- **Chart Setting:** White (or very light) background with solid colored marks or cells.
- **Audience:** General; heterogeneous viewing conditions.
- **Success Criterion:** Low error rate in the low end of the scale, not just midrange.

## When not to follow this rule <!-- role: exceptions -->

**Break it when:** The darkest region is only used to mark “no data” or rare outliers that are not compared finely. **Why:** The task does not depend on discriminating among multiple near-black steps.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may compress the dynamic range at the low end or reduce the dramatic visual contrast of minima. **Risk:** Adjustments can change the apparent balance of the colormap, affecting interpretability if not communicated. **Mitigation:** Ensure the legend reflects any remapping or truncation clearly.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Assuming a perceptual color space distance (e.g., uniform spacing) guarantees uniform performance at the darkest end. **Why it fails:** The experiments showed substantial dark-end error spikes under a white background even when model distances did not predict them.
- **Mistake:** Using a “nice-looking” dark minimum to increase contrast on white. **Why it fails:** It can make small differences near the minimum much harder to judge.

## Quick tests <!-- role: check -->

**Failure Sign:** Many incorrect choices cluster when the reference is near the minimum of the scale. **Quick Check:** Inspect a few triplets around low reference values (e.g., near 0–15% of the range) and see if “closer” becomes guessy. **Stronger Test:** Run a small pilot focused on low-end reference points and small spans.

## What to do instead <!-- role: fix -->

- Truncate the darkest portion of the colormap so the minimum shown is not near-black.
- Remap the data (e.g., nonlinearly) so more of the palette’s discriminable region is used where comparisons are needed.
- Change the background away from pure white when the design allows.
- Add explicit value labels or interactive readouts for low-end critical comparisons.
