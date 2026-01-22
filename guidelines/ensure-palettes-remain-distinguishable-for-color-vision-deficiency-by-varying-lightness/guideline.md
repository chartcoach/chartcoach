---
id: ensure-palettes-remain-distinguishable-for-color-vision-deficiency-by-varying-lightness
title: Ensure palettes remain distinguishable for color vision deficiency by varying
  lightness
bibliography: references.bib
description: Use lightness differences and testing tools so color-deficient readers
  can still distinguish marks.
labels:
- chart:multi
- task:distinguish
- visual:color
- impact:accessibility
- data:various
- audience:general
- complexity:basic
---

## Make color encodings robust to color vision deficiency <!-- role: advice -->

Use palettes with clear lightness differences and verify with a colorblindness check that the colors remain distinguishable.

## Why lightness supports accessibility across vision types <!-- role: reason -->

Color vision deficiency can collapse hue distinctions, but lightness differences often remain perceivable, preserving separability and meaning for more readers.

**Mechanism:** Encoding differences in lightness as well as hue reduces reliance on a single channel that some viewers cannot perceive reliably.

**Evidence:** Using different lightnesses in gradients and palettes helps readers with color vision deficiency distinguish colors, and online tools or automated checks can be used to validate distinguishability across different types of color blindness [@muth_colors_2018].

**Notes:** There are multiple types of color blindness, so a single “safe” assumption is insufficient without checking.

## When this applies to audience accessibility <!-- role: context -->

- **User Goal:** Distinguish categories or value levels regardless of color perception.
- **Task:** Decode color-encoded differences accurately.
- **Data:** Any chart where color carries meaning.
- **Chart Setting:** Public-facing communication where audience vision variation is expected.
- **Audience:** Mixed audiences, including readers with color vision deficiency.
- **Success Criterion:** Color-deficient readers can still differentiate the encoded groups or levels.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Color is not used to encode any information (only decoration). **Why:** Distinguishability of color-encoded meaning is irrelevant when color encodes nothing [@muth_colors_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Some aesthetically pleasing hue-only palettes may be unusable. **Risk:** Overreliance on lightness can reduce the number of distinct categories you can encode. **Mitigation:** Reduce category count or add redundant cues like labeling.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Choosing category colors that differ mainly by hue while having similar lightness. **Why it fails:** Color-deficient readers may not be able to distinguish them [@muth_colors_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** Multiple categories collapse into the same-looking color under a colorblind simulation. **Quick Check:** Run a colorblindness check and confirm each encoded group remains distinct. **Stronger Test:** Also check the chart in grayscale to verify that lightness still separates key encodings.

## What to do instead <!-- role: fix -->

- Adjust the palette so categories or steps differ in lightness, not only hue.
- Reduce the number of color-encoded categories when separability is not achievable.
- Add direct labels or other non-color cues where confusion remains.
- Validate the final palette with an online tool or built-in colorblind check.
