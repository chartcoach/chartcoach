---
id: clamp-lightness-range-to-keep-colors-visible-on-white-or-black-backgrounds
title: Clamp palette lightness to keep categorical colors visible on white and black
  backgrounds
bibliography: references.bib
description: Restrict categorical palette lightness to a midrange so colors remain
  visible against common light and dark backgrounds.
labels:
- chart:categorical
- task:choose
- visual:color
- impact:accessibility
- data:categorical
- audience:novice
- complexity:basic
---

## Keep categorical palette lightness in a midrange for background visibility <!-- role: advice -->

Clamp categorical palette colors to a midrange of lightness so they remain visible on both white and black backgrounds.

## Why lightness clamping protects legibility across backgrounds <!-- role: reason -->

Extremely light colors disappear on white backgrounds and extremely dark colors disappear on black backgrounds; constraining lightness avoids these failures without needing background-specific tuning.

**Mechanism:** By excluding very high and very low lightness values, you reduce the risk that color chips and marks collapse into the background luminance.

**Evidence:** The palette construction enforces a lightness clamp (L\* between 25 and 85 in CIELAB) to ensure visibility on black (L\*≈0) and white (L\*≈100) backgrounds as a baseline constraint for visualization use [@gramazioColorgoricalCreatingDiscriminable2017a]. This constraint is part of the model’s minimum assertions intended to support discriminability and practical usability [@gramazioColorgoricalCreatingDiscriminable2017a].

**Notes:** This is a general-purpose constraint and may be relaxed for known fixed backgrounds.

## When this applies <!-- role: context -->

- **User Goal:** Ensure colored marks are visible regardless of background choice.
- **Task:** Use color to encode category identity on charts or maps.
- **Data:** Categorical.
- **Chart Setting:** Visualizations that may be viewed with light or dark themes, or printed/copied.
- **Audience:** General audiences, including those on varied displays.
- **Success Criterion:** No category color becomes indistinguishable from the background.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The background is fixed and you intentionally need very light or very dark accent colors. **Why:** The clamp may exclude deliberate design choices that are safe in a controlled setting.

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** Reduced gamut and fewer available colors, especially for large palettes. **Risk:** Over-clamping can force more hue crowding as palette size increases. **Mitigation:** Reduce palette size or use additional encodings if you run out of distinct colors.

## Common failure modes <!-- role: mistakes -->

- **Mistake:** Including near-white pastels on white backgrounds. **Why it fails:** Marks lose contrast and become hard to see.
- **Mistake:** Including near-black colors on dark backgrounds. **Why it fails:** Marks collapse into the background.

## Quick tests <!-- role: check -->

**Failure Sign:** A category disappears when switching between light and dark themes. **Quick Check:** Preview the palette on both a white and black background and flag any color that becomes hard to see. **Stronger Test:** Render the palette on representative charts (not just swatches) and check visibility of small marks.

## What to do instead <!-- role: fix -->

- Adjust lightness of failing colors toward the midrange while keeping their hue distinct from neighbors.
- Choose a fixed background theme and regenerate the palette with constraints tuned for that background.
- Reduce reliance on very light or very dark colors for category identity; reserve them for non-data elements.
- Use outlines or other mark styling if background constraints cannot be met with color alone.
