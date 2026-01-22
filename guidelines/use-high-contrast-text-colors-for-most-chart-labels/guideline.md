---
id: use-high-contrast-text-colors-for-most-chart-labels
title: Use high-contrast text colors for most chart labels and annotations
bibliography: references.bib
description: Keep most chart text in black or near-black (or otherwise high-contrast)
  and verify contrast with a checker when needed.
labels:
- chart:generic
- task:read
- visual:color
- impact:accessibility
- data:generic
- audience:general
- scope:text-contrast
---

## Keep most chart text in high-contrast colors <!-- role: advice -->

Use a high-contrast color for most chart and table text, and verify contrast with a contrast checker when selecting lighter grays or colored text.

## Contrast is a primary driver of text legibility <!-- role: reason -->

Even well-chosen fonts become hard to read when contrast is too low, especially at small sizes and in dense chart scaffolding; sufficient contrast keeps attention on the content rather than the effort of decoding.

**Mechanism:** Higher luminance contrast increases character-edge visibility, making letterforms easier to recognize quickly across varied screens and lighting conditions.

**Evidence:** A minimum contrast ratio is emphasized as an accessibility consideration, with guidance to use a contrast checker to ensure compliance [@muth_fonts_2022].

**Notes:** Contrast interacts with size and weight, so low-contrast small text is especially fragile [@muth_fonts_2022].

## Apply to axes, labels, tooltips, notes, and table cells <!-- role: context -->

- **User Goal:** Read all necessary context (labels, units, caveats) without strain.
- **Task:** Scan and interpret text across the visualization.
- **Data:** Any.
- **Chart Setting:** Web, mobile, print exports, and presentations where lighting and display quality vary.
- **Audience:** Broad audiences, including readers with low vision.
- **Success Criterion:** Text remains readable in typical viewing conditions and meets intended accessibility standards.

## Lower contrast can be acceptable for de-emphasized, non-essential text <!-- role: exceptions -->

**Break it when:** The text is intentionally secondary (e.g., subtle helper labels) and you have confirmed it remains readable at the smallest viewing size. **Why:** Not all text needs the same emphasis, but it still must remain legible [@muth_fonts_2022].

## High contrast can reduce the ability to create soft hierarchy <!-- role: costs -->

**Sacrifice:** Using near-black for most text limits how much hierarchy you can achieve with color alone. **Risk:** Too much equally high-contrast text can feel busy. **Mitigation:** Use size, spacing, and selective bolding to create hierarchy while keeping legibility intact [@muth_fonts_2022].

## Don’t rely on faint gray as a default text color <!-- role: mistakes -->

**Mistake:** Making most labels light gray to appear “minimal.” **Why it fails:** Low contrast undermines readability, especially for small text and in imperfect viewing conditions [@muth_fonts_2022].

## Test contrast on realistic backgrounds and exports <!-- role: check -->

**Failure Sign:** Labels fade into the background or disappear when the chart is scaled down. **Quick Check:** Run your text and background colors through a contrast checker. **Stronger Test:** Export the chart (PNG/PDF) and view it on a different screen to confirm text remains clearly readable [@muth_fonts_2022].

## Increase contrast or reduce text demand <!-- role: fix -->

- Darken text colors for axes, labels, and notes to restore contrast.
- Increase font size or weight for any text that must remain low-contrast for hierarchy reasons.
- Reduce the amount of secondary text so the remaining text can stay high-contrast without clutter.
- Adjust background or gridline colors so text maintains contrast without needing extreme styling [@muth_fonts_2022].
