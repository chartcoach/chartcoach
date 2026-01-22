---
id: verify-palettes-for-colorblind-distinguishability-and-text-contrast
title: Check palettes for color-vision deficiency distinguishability and sufficient
  text contrast
bibliography: references.bib
description: Validate that colors remain distinguishable for color-vision deficiencies
  and that text on color meets contrast needs.
labels:
- chart:multi
- task:validate
- visual:color
- impact:accessibility
- data:multi
- audience:general
- custom:colorblindness
---

## Validate colors with color-vision deficiency simulation and contrast checks <!-- role: advice -->

Simulate color-vision deficiencies to confirm categories remain distinguishable, and check text-on-color contrast before publishing.

## Why accessibility checks prevent invisible differences <!-- role: reason -->

Some color pairs collapse into similar tones under common forms of color-vision deficiency, and insufficient contrast makes labels unreadable; both failures block comprehension even when the data is correct.

**Mechanism:** Human perception of hue differences varies by viewer, and text legibility depends strongly on luminance contrast between foreground and background.

**Evidence:** Palette testing tools and simulators can reveal when chosen colors are not distinguishable for colorblind readers, and contrast checkers can flag text/background pairs that are not readable at typical sizes [@muth_colorguide_2018].

**Notes:** These checks apply to both categorical palettes and gradients, and they should be done on the final rendered chart colors.

## When this applies in practice <!-- role: context -->

- **User Goal:** Ensure all readers can decode the visualization.
- **Task:** Distinguish categories; read labels placed on colored areas.
- **Data:** Any data encoded with color; heightened risk with multiple categories or subtle gradients.
- **Chart Setting:** Charts, maps, and tables; especially when labels sit on filled shapes.
- **Audience:** Broad public audience, including readers with color-vision deficiencies or low-contrast sensitivity.
- **Success Criterion:** Categories remain separable under simulation, and text remains readable without zooming.

## When not to follow it <!-- role: exceptions -->

**Break it when:** Color is purely decorative and carries no information, and no text is placed on colored areas. **Why:** The chart’s decoding does not depend on color distinctions or color-based legibility.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** You may need to abandon a preferred palette for a more robust one. **Risk:** Overcorrecting can lead to overly conservative palettes with reduced expressive range. **Mitigation:** Use other channels (labels, position, shape) to share the encoding burden.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Assuming “different in the legend” means “distinguishable for everyone.” **Why it fails:** Some viewers will perceive those colors as similar or identical.
- **Mistake:** Placing text on saturated fills without checking contrast. **Why it fails:** Labels become unreadable even if the color encoding works.

## Quick tests <!-- role: check -->

**Failure Sign:** Under color-vision deficiency simulation, multiple categories look the same, or labels blend into their backgrounds. **Quick Check:** Run a colorblindness simulator view and a contrast checker on any text-on-color combination. **Stronger Test:** Print the chart in grayscale and view it at small size; verify the key distinctions and labels still hold.

## What to do instead <!-- role: fix -->

- Replace confusing color pairs with more separable hues or with clearer lightness differences.
- Add direct labels or patterns/borders so categories do not rely on color alone.
- Change label placement or switch label color/background to increase contrast.
- Reduce the number of categories shown at once or split into multiple views when colors cannot remain distinct.
