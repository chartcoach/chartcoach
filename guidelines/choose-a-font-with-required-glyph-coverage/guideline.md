---
id: choose-a-font-with-required-glyph-coverage
title: Choose a font that contains every symbol and language character your visualization
  needs
bibliography: references.bib
description: Confirm your typeface includes all required glyphs (diacritics, currencies,
  math symbols, footnote marks) before committing to it.
labels:
- chart:generic
- task:communicate
- visual:typography
- impact:correctness
- data:multilingual
- audience:general
- scope:glyphs
---

## Verify glyph coverage before finalizing the typeface <!-- role: advice -->

Choose a font only after confirming it includes all symbols and special characters your chart or table will display, and that those glyphs look appropriate at your intended size.

## Missing or poor glyphs break meaning and credibility <!-- role: reason -->

Charts frequently include currency signs, math operators, diacritics, superscripts, and reference marks; if these glyphs are missing or poorly drawn, the visualization can display incorrect placeholders or degrade legibility in precisely the characters that carry meaning.

**Mechanism:** Complete, well-designed glyph sets prevent rendering fallbacks and ensure critical symbols (like %, currency, or superscripts) remain legible and stylistically consistent with surrounding text.

**Evidence:** Required glyphs are highlighted as a practical selection constraint because not all fonts include special characters, and quality matters (for example, superscripts are not just scaled-down numerals) [@muth_fonts_2022].

**Notes:** This is especially important when using inexpensive or niche typefaces where coverage is less predictable [@muth_fonts_2022].

## Use when your labels include non-ASCII text or specialized notation <!-- role: context -->

- **User Goal:** Read labels and values correctly without confusion.
- **Task:** Interpret units, currencies, footnotes, and multilingual names.
- **Data:** International place/person names; currencies; percentages; equations; annotated notes.
- **Chart Setting:** Any chart/table that includes symbols in axes, tooltips, headers, or notes.
- **Audience:** Multilingual or international audiences; readers who rely on precise notation.
- **Success Criterion:** No tofu boxes/placeholder glyphs, no unexpected substitutions, and symbols remain clear at small sizes.

## You can skip exhaustive checking only for tightly controlled ASCII-only content <!-- role: exceptions -->

**Break it when:** You are certain the visualization will only use a restricted ASCII subset (A–Z, basic punctuation) across all outputs. **Why:** The risk of missing glyphs is minimal in a strictly constrained character set [@muth_fonts_2022].

## More coverage can limit stylistic choices <!-- role: costs -->

**Sacrifice:** Fonts with broad coverage may offer fewer distinctive stylistic traits or fewer weights than boutique options. **Risk:** Late discovery of missing glyphs forces a last-minute font change and can disrupt layout. **Mitigation:** Test glyphs early using real draft text, including currencies, diacritics, and footnote symbols [@muth_fonts_2022].

## Don’t assume common symbols exist or look good <!-- role: mistakes -->

- **Mistake:** Selecting a font based on how letters look, then discovering missing €/%/¹ or broken diacritics after design is finalized. **Why it fails:** The visualization can render incorrect characters or visually inconsistent substitutes that undermine clarity and trust [@muth_fonts_2022].

## Test with a “worst-case” string <!-- role: check -->

**Failure Sign:** Placeholder boxes appear, or symbols look oddly styled compared with surrounding text. **Quick Check:** Paste a stress-test line into your chart labels (e.g., “München ¹²³ — € £ ¥ % × ÷ ±”) and verify rendering. **Stronger Test:** Export in every intended format (web, PNG, PDF) and confirm the same glyphs render identically [@muth_fonts_2022].

## Swap fonts or isolate the problematic characters <!-- role: fix -->

- Replace the font with one that includes the needed glyph set.
- Adjust typography so specialized symbols appear only where the chosen font supports them (for example, in notes rather than axis ticks).
- If your tooling allows, use a font fallback stack that preserves symbol correctness.
- Simplify notation (for example, avoid superscripts) if the required glyphs cannot be rendered reliably [@muth_fonts_2022].
