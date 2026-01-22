---
id: use-diverging-palettes-only-when-values-deviate-from-a-meaningful-baseline
title: Use a diverging palette only when values deviate from a meaningful baseline
bibliography: references.bib
description: Apply diverging color gradients to signed data around a reference point,
  with a neutral center.
labels:
- chart:choropleth
- task:compare
- visual:color
- impact:clarity
- data:quantitative
- audience:general
- complexity:intermediate
---

## Use diverging gradients to show direction away from a reference value <!-- role: advice -->

Use a diverging color gradient when the key message is how values differ from a baseline, with clearly distinguishable hues on each side and a neutral light grey center.

## Why diverging palettes communicate direction and deviation <!-- role: reason -->

Diverging palettes encode two directions from a midpoint, letting readers see both magnitude and which side of the baseline a value falls on.

**Mechanism:** A neutral center marks the baseline, while two distinct hue directions reduce ambiguity about “above vs below” the reference.

**Evidence:** Diverging palettes are appropriate to emphasize how a variable diverts from a baseline (such as a national average), should use clearly distinguishable hues on both sides, and should ideally use a light grey center rather than white [@muth_colors_2018].

**Notes:** The baseline must be meaningful to the story, not arbitrary.

## When this applies to baseline-centered data <!-- role: context -->

- **User Goal:** See which items are above vs below a reference and by how much.
- **Task:** Judge direction and magnitude relative to a baseline.
- **Data:** Quantitative values centered on a reference point (e.g., difference from average).
- **Chart Setting:** Maps or charts using a continuous color scale with a midpoint.
- **Audience:** Readers needing quick directional interpretation.
- **Success Criterion:** The baseline is visually identifiable and both sides are clearly distinct.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The data have no meaningful baseline and are purely magnitude-based. **Why:** A diverging palette would imply a midpoint meaning that the data do not support [@muth_colors_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Diverging palettes can make midrange values look less prominent. **Risk:** A poor center color (e.g., white) can blend with the background and hide near-baseline values. **Mitigation:** Use a light grey center that remains visible on the page background.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using a diverging palette for values that do not represent deviation from a baseline. **Why it fails:** The palette suggests positive/negative meaning where none exists [@muth_colors_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** Readers ask what the midpoint color represents. **Quick Check:** State the baseline in one phrase and verify it matches the palette midpoint. **Stronger Test:** Hide the legend title and see if the baseline is still inferable from the annotation and center color.

## What to do instead <!-- role: fix -->

- Switch to a sequential light-to-dark palette when you are encoding magnitude only.
- Add explicit annotation of the baseline and ensure the center color is light grey.
- Choose two clearly distinguishable hues for the two sides of the divergence.
- Re-express the data as deviations from a meaningful baseline if deviation is the true analytic focus.
