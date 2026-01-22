---
id: meet-minimum-text-background-contrast-and-avoid-vibrating-color-pairs
title: Meet minimum contrast ratios for text, and avoid complementary hues as background
  pairs
bibliography: references.bib
description: Ensure readable contrast, especially for small text, and avoid harsh
  complementary or bright background colors.
labels:
- chart:multi
- task:read
- visual:color
- impact:accessibility
- data:various
- audience:general
- complexity:basic
---

## Ensure readable contrast for text and marks against the background <!-- role: advice -->

Keep foreground–background contrast high enough for legibility, especially for small text, and avoid complementary hue pairings or bright background colors that reduce readability.

## Why contrast and hue pairing affect readability <!-- role: reason -->

Low contrast and harsh hue interactions make text and fine marks difficult to perceive, especially in poor lighting or on varied screens, which increases reading effort and errors.

**Mechanism:** Higher luminance contrast supports legibility, while certain hue combinations can create uncomfortable visual vibration that interferes with reading.

**Evidence:** Text needs sufficient contrast to the background, with a contrast ratio of at least 2.5 for big text and at least 4 for small text; complementary hues and bright colors should be avoided for backgrounds, and contrast-checking tools can be used to test compliance [@muth_colors_2018].

**Notes:** Contrast needs increase as text size decreases.

## When this applies to chart styling <!-- role: context -->

- **User Goal:** Read labels, annotations, and legends comfortably.
- **Task:** Decode text and fine visual marks without strain.
- **Data:** Any.
- **Chart Setting:** Screens, mobile, print export, and low-light viewing conditions.
- **Audience:** Broad audiences, including readers with reduced vision or poor display conditions.
- **Success Criterion:** Text and key marks remain readable at a glance.

## When not to follow it <!-- role: exceptions -->

**Break it when:** The chart contains no text and uses only large, thick marks with strong separation. **Why:** Text-specific minimum ratios are less relevant when there is no fine typography to read [@muth_colors_2018].

## Tradeoffs and risks <!-- role: costs -->

**Sacrifice:** High contrast can limit aesthetic options (especially subtle palettes). **Risk:** Over-dark text or heavy contrasts can feel visually harsh. **Mitigation:** Adjust typography and spacing while maintaining the minimum contrast ratios.

## Common failure modes <!-- role: mistakes -->

**Mistake:** Using light grey text on white or very light backgrounds. **Why it fails:** Small text becomes hard to read because contrast is too low [@muth_colors_2018].

## Quick tests <!-- role: check -->

**Failure Sign:** Labels disappear when viewed on a dim screen or from a distance. **Quick Check:** Zoom out to typical reading size and see whether all labels remain legible. **Stronger Test:** Measure contrast ratios for key text and verify they meet the stated minimums.

## What to do instead <!-- role: fix -->

- Increase luminance contrast between text/marks and the background until ratios meet the stated thresholds.
- Avoid using complementary hue pairs or highly saturated colors as backgrounds behind text.
- Use a contrast-checking tool to test ratios and brightness differences before publishing.
- Simplify background treatments (e.g., remove bright fills) when readability is at risk.
