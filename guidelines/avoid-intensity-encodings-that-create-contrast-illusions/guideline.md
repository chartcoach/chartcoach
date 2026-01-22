---
id: avoid-intensity-encodings-that-create-contrast-illusions
title: Avoid intensity encodings where background contrast can bias perceived values
bibliography: references.bib
description: Prevent luminance-contrast illusions by not relying on perceived brightness
  when backgrounds vary.
labels:
- chart:map
- task:compare
- visual:color
- impact:accuracy
- data:spatial
- audience:novice
- risk:illusion
---

## Don’t rely on perceived brightness when backgrounds differ <!-- role: advice -->

Avoid designs where the same intensity value appears on different background intensities and must be compared by eye. If intensity is used, ensure comparisons are not confounded by varying backgrounds.

## Contrast illusions distort intensity judgments <!-- role: reason -->

Brightness perception is influenced by surrounding context, so identical intensities can look different when placed on light versus dark backgrounds. This leads to systematic misreading when intensity is meant to encode data values.

**Mechanism:** The visual system uses local contrast to infer illumination and object brightness, which can miscalibrate perceived intensity in artificial displays.

**Evidence:** Identical gray values can appear different against different backgrounds, which can systematically bias interpretation when intensity is used to encode data [@zacksDesigningGraphsDecisionMakers2020].

**Notes:** This risk is especially relevant when encoding multiple variables in the same spatial region.

## Apply when intensity is a primary quantitative cue <!-- role: context -->

- **User Goal:** Compare magnitudes across regions or items using lightness/darkness.
- **Task:** Determine which region/item is darker (higher/lower) and by how much.
- **Data:** Spatial or overlaid layers where backgrounds vary substantially.
- **Chart Setting:** Maps, layered heatmaps, overlays on images.
- **Audience:** Any audience, especially when decisions depend on small intensity differences.
- **Success Criterion:** Perceived intensity matches the encoded values across contexts.

## When intensity is only decorative or redundant <!-- role: exceptions -->

**Break it when:** Intensity is not used for comparison and the quantitative message is carried by another channel. **Why:** The illusion is less consequential if brightness is not part of the decision.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Avoiding intensity can reduce the ability to show dense spatial patterns in a compact space. **Risk:** Overcorrecting can remove useful “big picture” cues. **Mitigation:** Keep intensity as a secondary cue and avoid requiring fine-grained intensity comparisons.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Overlaying intensity-coded marks on heterogeneous map backgrounds and expecting accurate comparisons. **Why it fails:** Luminance contrast changes perceived brightness independent of the encoded value [@zacksDesigningGraphsDecisionMakers2020].
- **Mistake:** Encoding two variables with intensity in the same region. **Why it fails:** Context effects and interference make decoding ambiguous and biased [@zacksDesigningGraphsDecisionMakers2020].

## Quick tests <!-- role: check -->

**Failure Sign:** Two identical values look different depending on where they sit. **Quick Check:** Copy the same mark to multiple backgrounds in the figure; if it appears to change, comparisons will be biased. **Stronger Test:** Ask users to rank a few equal-valued marks placed on different backgrounds; errors indicate contrast bias.

## What to do instead <!-- role: fix -->

- Encode the key quantitative variable with position or length instead of intensity.
- Place intensity-coded marks on a uniform, controlled background.
- Separate layers so the intensity-coded layer is not visually blended with a varying background.
- Add direct numeric labels for the few values that must be read accurately.
