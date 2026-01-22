---
id: use-lightness-differences-to-support-print-and-robust-distinction
title: Assign distinct lightness levels to categorical colors when print or grayscale
  robustness matters
bibliography: references.bib
description: Vary lightness across category colors so they remain distinguishable
  in grayscale and as a general signal of separability.
labels:
- chart:generic
- task:distinguish
- visual:color
- impact:accessibility
- data:categorical
- audience:general
- complexity:intermediate
---

## Ensure categorical colors differ in lightness when grayscale or print is in scope <!-- role: advice -->

Give each categorical color a distinct lightness level when your visualization may be printed or viewed without full color fidelity.

## Lightness survives when hue does not <!-- role: reason -->

Hue differences can disappear in grayscale printing or low-fidelity viewing contexts, while lightness differences tend to persist. A palette that separates in lightness provides an additional, robust cue for category distinction.

**Mechanism:** Lightness separation preserves category discriminability when hue information is reduced or removed.

**Evidence:** Having different lightness values helps “get it right in black and white,” which is especially important for print and is also a general indicator that colors will be easier to tell apart for many readers [@muth_good_color_palettes_2024].

**Notes:** Lightness variation complements (rather than replaces) hue distinctness and colorblind robustness.

## Use this when output may be grayscale or low-fidelity <!-- role: context -->

- **User Goal:** Read categories correctly across mediums.
- **Task:** Identify categories from marks when color reproduction varies.
- **Data:** Categorical series with two or more groups.
- **Chart Setting:** Printing, photocopying, PDF export, or environments where color may be muted.
- **Audience:** Readers who may view the chart in grayscale or with limited display quality.
- **Success Criterion:** Categories remain distinguishable even without relying on hue.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Your categories must be visually uniform in tone because lightness encodes a different meaning elsewhere in the design. **Why:** Lightness differences could introduce a competing signal that conflicts with the intended encoding [@muth_good_color_palettes_2024].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Some brand palettes with tight lightness ranges may be harder to use unchanged. **Risk:** Large lightness gaps can make some categories feel more prominent than others. **Mitigation:** Balance lightness separation with the goal of equal visual importance for peer categories [@muth_good_color_palettes_2024].

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using multiple colors with similar lightness because they look harmonious together. **Why it fails:** They can collapse into near-identical grays in print and become hard to distinguish [@muth_good_color_palettes_2024].

## Quick tests <!-- role: check -->

**Failure Sign:** In grayscale, two or more categories become indistinguishable. **Quick Check:** Convert a screenshot to grayscale and verify each category still separates. **Stronger Test:** Print a test page or export a PDF and view it on multiple devices to confirm robust separation [@muth_good_color_palettes_2024].

## What to do instead <!-- role: fix -->

- Adjust colors so each category occupies a distinct lightness band.
- Replace any pair of same-lightness colors with one lighter or darker alternative while maintaining overall distinctness.
- If equal importance is required, keep lightness differences moderate and compensate with hue spacing.
- If print is critical, consider adding non-color cues (labels or patterns) so identification does not depend on color alone [@muth_good_color_palettes_2024].
