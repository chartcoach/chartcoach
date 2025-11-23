---
id: verify-glyph-coverage
title: Verify font support for all required glyphs
bibliography: references.bib
description: Ensure the chosen font natively supports all symbols, currencies, and
  languages.
labels:
- visual:typography
- impact:integrity
- data:text
- visual:localization
---

## The Rule <!-- role: advice -->

Before finalizing a font choice, confirm it includes all necessary characters (glyphs), including currency symbols, math symbols, and language-specific accents. Do not rely on software to auto-generate missing glyphs.

## The Logic <!-- role: reason -->

Not all fonts contain every character. Cheap or limited fonts may miss specific currency signs ($ € £ ¥), math symbols (+ ÷ × =), or superscripts (¹ ² ³). Good type designers draw superscripts specifically to be legible; relying on software to simply "shrink" a number for a footnote creates poor legibility.

*   **The Principle:** Glyph Completeness and Design Integrity
*   **The Evidence:** [@muth_fonts_2022] warns that superscripts like `²` need to be drawn by hand to be legible, not just size-reduced.

## Where to Apply <!-- role: context -->

*   **User Goal:** Accurate reading of units, formulas, and names.
*   **Data Type:** International data, financial data, scientific notation.

## When to Break It <!-- role: exceptions -->

*   **Scenario:** None.
*   **Reason:** Missing glyphs (appearing as "tofu" boxes or wrong fonts) always degrade the visualization.

## The Price <!-- role: costs -->

*   **The Sacrifice:** You may have to discard a stylistically perfect font if it lacks technical coverage.

## Common Mistakes <!-- role: mistakes -->

*   **The Wrong Fix:** Letting the OS swap in a different font for the missing character.
*   **Why it fails:** It looks mismatched and unprofessional.
*   **The Wrong Fix:** Using a standard "2" and reducing its font size for a squared symbol (m²).
*   **Why it fails:** The stroke width becomes too thin compared to the rest of the text [@muth_fonts_2022].

## How to Check <!-- role: check -->

*   **Visual Sign:** Do math symbols or footnotes look thinner or different in style than the letters?
*   **The Test:** Create a "test sheet" containing all potential symbols (e.g., %, †, ‡, ü, ß, é) to ensure they render correctly in the chosen font.

## How to Fix <!-- role: fix -->

*   **Quick Fix:** Switch to a robust "Pro" or standard web font (like Noto Sans or Source Sans) known for wide glyph coverage.
*   **Best Fix:** Check the character map of the font before starting the design.
